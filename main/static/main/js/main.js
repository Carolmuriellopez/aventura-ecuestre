
const menu = document.getElementById('menu');
const toggle = document.getElementById('menu-toggle');
let isOpen = false;
const isMobile = () => window.innerWidth < 768;


if (menu && toggle) {
    let isOpen = false;
    const isMobile = () => window.innerWidth < 768;

    if (isMobile()) {
        menu.style.display = 'none';
    }

    toggle.addEventListener('click', () => {
        const expanded = toggle.getAttribute('aria-expanded') === 'true';
        toggle.setAttribute('aria-expanded', !expanded);
        isOpen = !isOpen;
        menu.style.display = isOpen ? 'flex' : 'none';
    });

    menu.addEventListener('click', (e) => {
        if (e.target === menu) {
            isOpen = false;
            menu.style.display = 'none';
            toggle.setAttribute('aria-expanded', 'false');
        }
    });
}