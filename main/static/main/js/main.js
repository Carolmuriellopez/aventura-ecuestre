
const menu = document.getElementById('menu');
const toggle = document.getElementById('menu-toggle');
let isOpen = false;
const isMobile = () => window.innerWidth < 768;


if (menu && toggle) {
    let isOpen = false;
    const isMobile = () => window.innerWidth < 768;

    if (isMobile()) {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'flex';
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

const langToggle = document.getElementById('lang-toggle');
const langMenu = document.getElementById('lang-menu');

if (langToggle && langMenu) {
    const closeLangMenu = () => {
        langMenu.hidden = true;
        langToggle.setAttribute('aria-expanded', 'false');
    };

    langToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        const expanded = langToggle.getAttribute('aria-expanded') === 'true';
        langToggle.setAttribute('aria-expanded', !expanded);
        langMenu.hidden = expanded;
    });

    document.addEventListener('click', (e) => {
        if (!langMenu.hidden && !langMenu.contains(e.target) && e.target !== langToggle) {
            closeLangMenu();
        }
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && !langMenu.hidden) {
            closeLangMenu();
            langToggle.focus();
        }
    });
}

function equalizeSlideHeights(swiper) {
    const slides = Array.from(swiper.slides);
    slides.forEach(s => s.style.height = 'auto');
    const maxH = Math.max(...slides.map(s => s.offsetHeight));
    slides.forEach(s => s.style.height = maxH + 'px');
}

const rutasCarousel = new Swiper('#rutas-carousel', {
    loop: false,
    loopedSlides: 5,
    slidesPerView: 1,
    spaceBetween: 16,
    pagination: {
        el: '#rutas-pagination',
        clickable: true,
    },
    breakpoints: {
        768: { slidesPerView: 2 },
    },
    on: {
        afterInit(swiper) {
            requestAnimationFrame(() => equalizeSlideHeights(swiper));
        },
        resize(swiper) {
            requestAnimationFrame(() => equalizeSlideHeights(swiper));
        },
    },
})

document.fonts.ready.then(() => {
    equalizeSlideHeights(rutasCarousel);
    equalizeSlideHeights(packsCarousel);
});

const packsCarousel = new Swiper('#packs-carousel', {
    loop: false,
    loopedSlides: 2,
    slidesPerView: 1,
    spaceBetween: 16,
    pagination: {
        el: '#packs-pagination',
        clickable: true,
    },
    breakpoints: {
        768: { slidesPerView: 2 },
    },
    on: {
        afterInit(swiper) {
            requestAnimationFrame(() => equalizeSlideHeights(swiper));
        },
        resize(swiper) {
            requestAnimationFrame(() => equalizeSlideHeights(swiper));
        },
    },
})

