class Sidebar {
    constructor() {
        /** @type {NodeListOf<HTMLElement>|Array} */
        this.dragTargets = [];
        /** @type {NodeListOf<HTMLElement>|Array} */
        this.dragItems = [];
        /** @type {NodeListOf<HTMLElement>|Array} */
        this.collectionToggles = [];
        /** @type {string[]} */
        this.openedCollections = [];

        // store these here because event.dataTransfer data is not available in all drag and drop events
        /** @type {string|null} */
        this.draggedItemId = null;
        /** @type {string|null} */
        this.draggedItemType = null;

        // store these for a later removal after the hx-swap="morph". Otherwise, event listeners will be duplicated.
        /** @type {Map<HTMLElement, (event: Event) => void>} */
        this.boundDropFunctions = new Map();
        /** @type {Map<HTMLElement, (event: Event) => void>} */
        this.boundDragEndFunctions = new Map();
        /** @type {Map<HTMLElement, (event: Event) => void>} */
        this.boundDragStartFunctions = new Map();
        /** @type {Map<HTMLElement, (event: Event) => void>} */
        this.boundCollectionToggleFunctions = new Map();
    }

    setup() {
        this.dragTargets = document.querySelectorAll('[sidebar-target]');
        this.dragItems = document.querySelectorAll('[sidebar-item]');
        this.collectionToggles = document.querySelectorAll('[sidebar-collection-toggle]');

        this.removeOldEventListeners();
        this.addEventListeners();
    }

    addEventListeners() {
        this.dragTargets.forEach(target => {
            target.addEventListener('dragover', this.dragOver.bind(this));
            target.addEventListener('dragleave', this.dragLeave);

            const boundDrop = (event) => this.drop(event, target);
            this.boundDropFunctions.set(target, boundDrop);
            target.addEventListener('drop', boundDrop);
        });

        this.dragItems.forEach(message => {
            const boundDragEnd = (event) => this.dragEnd(event, message);
            this.boundDragEndFunctions.set(message, boundDragEnd);
            message.addEventListener('dragend', boundDragEnd);
            const boundDragStart = (event) => this.dragStart(event, message);
            this.boundDragStartFunctions.set(message, boundDragStart);
            message.addEventListener('dragstart', boundDragStart);
        });

        this.collectionToggles.forEach(toggle => {
            const boundCollectionToggle = (event) => this.toggleCollectionVisibility(event, toggle);
            this.boundCollectionToggleFunctions.set(toggle, boundCollectionToggle);
            toggle.addEventListener('click', boundCollectionToggle);
        });
    }

    removeOldEventListeners() {
        // remove previous event listeners because of the hx-swap="morph"
        this.dragTargets.forEach(target => {
            target.removeEventListener('drop', this.boundDropFunctions.get(target));
            target.removeEventListener('dragover', this.dragOver);
            target.removeEventListener('dragleave', this.dragLeave);
        });

        this.dragItems.forEach(target => {
            target.removeEventListener('dragend', this.boundDragEndFunctions.get(target));
            target.removeEventListener('dragstart', this.boundDragStartFunctions.get(target));
        });

        this.collectionToggles.forEach(toggle => {
            toggle.removeEventListener('click', this.boundCollectionToggleFunctions.get(toggle));
        });
    }

    /**
     * @param {Event} event
     * @param {HTMLElement} target
     */
    drop(event, target) {
        event.preventDefault();
        event.stopPropagation();

        if (Sidebar.isCollectionToCollectionDrag(event, this.draggedItemType)) {
            return;
        }

        const parentId = target.getAttribute('sidebar-parent');
        const prevItemWeight = target.getAttribute('sidebar-weight');

        switch (this.draggedItemType) {
            case 'collection':
                this.moveCollection(this.draggedItemId, prevItemWeight);
                break;
            case 'message':
                this.moveMessage(this.draggedItemId, parentId, prevItemWeight);
                break;
        }
    }

    /**
     * @param {Event} event
     * @param {HTMLElement} message
     */
    dragEnd(event, message) {
        message.style.opacity = '1';

        this.draggedItemId = null;
        this.draggedItemType = null;
    }

    /**
     * @param {Event} event
     * @param {HTMLElement} message
     */
    dragStart(event, message) {
        message.style.opacity = '.5';
        const dragElement = document.createElement('div');
        event.dataTransfer.setDragImage(dragElement, 0, 0);

        this.draggedItemId = message.getAttribute('sidebar-item');
        this.draggedItemType = message.getAttribute('sidebar-item-type');
    }

    /**
     * @param {Event} event
     */
    dragOver(event) {
        event.preventDefault();
        if (Sidebar.isCollectionToCollectionDrag(event, this.draggedItemType)) {
            return;
        }

        const target = event.target.closest('[sidebar-target]');
        if (target) {
            target.classList.remove('border-opacity-0');
            target.classList.add('border-opacity-100');
        }
    }

    /**
     * @param {Event} event
     */
    dragLeave(event) {
        event.preventDefault();
        const target = event.target.closest('[sidebar-target]');
        if (target) {
            target.classList.remove('border-opacity-100');
            target.classList.add('border-opacity-0');
        }
    }

    /**
     * @param {Event} event
     * @param {HTMLElement} toggle
     */
    toggleCollectionVisibility(event, toggle) {
        event.stopPropagation();
        event.preventDefault();

        const collectionId = toggle.getAttribute('sidebar-collection-toggle');
        const collectionContainer = document.querySelector(`[sidebar-collection-container="${collectionId}"]`);
        collectionContainer.classList.toggle('hidden');
        toggle.classList.toggle('-rotate-90');
        this.openedCollections.includes(collectionId) ? this.openedCollections.splice(this.openedCollections.indexOf(collectionId), 1) : this.openedCollections.push(collectionId);
    }

    /**
     * @param {string} htmlString
     * @returns {string}
     */
    restoreCollectionVisibility(htmlString) {
        const parser = new DOMParser();
        const doc = parser.parseFromString(htmlString, 'text/html');
        this.openedCollections.forEach(collectionId => {
            const collectionContainer = doc.querySelector(`[sidebar-collection-container="${collectionId}"]`);
            const collectionToggle = doc.querySelector(`[sidebar-collection-toggle="${collectionId}"]`);

            collectionContainer.classList.remove('hidden');
            collectionToggle.classList.remove('-rotate-90');
        });
        return doc.body.innerHTML;
    }

    /**
     * @param {string} messageId
     * @param {string} collectionId
     * @param {string} prevItemWeight
     */
    moveMessage(messageId, collectionId, prevItemWeight) {
        prevItemWeight = prevItemWeight === null ? '' : prevItemWeight;
        collectionId = collectionId === null ? '' : collectionId;

        htmx.ajax('POST', `/message/${messageId}/move`, {
            values: {
                collection_id: collectionId,
                prev_item_weight: prevItemWeight
            }
        });
    }

    /**
     * @param {string} collectionId
     * @param {string} prevItemWeight
     */
    moveCollection(collectionId, prevItemWeight) {
        prevItemWeight = prevItemWeight === null ? '' : prevItemWeight;

        htmx.ajax('POST', `/collection/${collectionId}/move`, {
            values: {
                prev_item_weight: prevItemWeight
            }
        });
    }

    /**
     * @param {Event} event
     * @param {string} draggedItemType
     * @returns {boolean}
     */
    static isCollectionToCollectionDrag(event, draggedItemType) {
        return draggedItemType === 'collection' && event.target.closest('[sidebar-parent]') !== null;
    }
}

const sidebar = new Sidebar();

document.body.addEventListener('htmx:beforeSwap', function (evt) {
    if (evt.detail.elt.attributes['sidebar']) {
        // reopen returned collections before the swap
        evt.detail.serverResponse = sidebar.restoreCollectionVisibility(evt.detail.serverResponse);
    }
});
