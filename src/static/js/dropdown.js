document.addEventListener('click', (event) => {
    document.querySelectorAll('[dropdown-menu]').forEach((dropdownMenu) => {
        const dropdownMenuId = dropdownMenu.getAttribute('dropdown-menu');
        const dropdownButton = document.querySelector(`[dropdown-button="${dropdownMenuId}"]`);

        if (!dropdownMenu.contains(event.target) && !dropdownButton.contains(event.target)) {
            dropdownMenu.classList.add('hidden');
        }
    });

    const button = event.target.closest('[dropdown-button]');
    if (button) {
        const dropdownMenuId = button.getAttribute('dropdown-button');
        const dropdownMenu = document.querySelector(`[dropdown-menu="${dropdownMenuId}"]`);
        dropdownMenu.classList.toggle('hidden');
    }
});
