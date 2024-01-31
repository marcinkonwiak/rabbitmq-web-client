class ErrorHandler {

    /**
     * @param {string} str
     * @returns {string}
     */
    humanize(str) {
        if (str === undefined || str === null) {
            return '';
        }
        const frags = str.split('_');
        for (let i = 0; i < frags.length; i++) {
            frags[i] = frags[i].charAt(0).toUpperCase() + frags[i].slice(1);
        }
        return frags.join(' ');
    }

    /**
     * @param {string} serverResponse
     * @returns {void}
     */
    displayErrors(serverResponse) {
        let errors = JSON.parse(serverResponse);
        errors = errors.detail.map(item => [item.loc[1], item.msg]);

        for (const value of errors) {
            Toastify({
                title: "Error",
                text: `${this.humanize(value[0])}: ${value[1]}`,
                duration: 5000,
                gravity: "bottom",
                position: "right",
                stopOnFocus: true,
                style: {
                    "background": "var(--dark-500)",
                    "border-radius": "0.5rem",
                    "color": "var(--light-300)",
                    "text-align": "left",
                    "box-shadow": "none",
                    "width": "20rem",
                    "border-left": "0.5rem solid var(--error-500)",
                }
            }).showToast();
        }
    }
}

const errorHandler = new ErrorHandler();

document.body.addEventListener('htmx:beforeSwap', function (evt) {
    if (evt.detail.xhr.status === 422) {
        evt.detail.isError = false;

        errorHandler.displayErrors(evt.detail.serverResponse);
    }
});
