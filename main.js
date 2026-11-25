var typed = new Typed("#text", {
    strings: ["Developpeur web", "Programmeur amateur", "Programmeur"],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop: true
});

// Menu responsive
const toggleNavbar = document.querySelector('.toggle_navbar');
const navbar = document.querySelector('.navbar');

if (toggleNavbar && navbar) {
    toggleNavbar.addEventListener('click', () => {
        toggleNavbar.classList.toggle('active');
        navbar.classList.toggle('active');
    });
}

// Smooth scrolling pour les liens de navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const id = this.getAttribute('href');
        const target = id.length > 1 ? document.querySelector(id) : null;
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Bouton retour en haut
const topButton = document.querySelector('.top');
if (topButton) {
    topButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Afficher/cacher le bouton retour en haut selon le scroll
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            topButton.style.display = 'block';
        } else {
            topButton.style.display = 'none';
        }
    });
}

// Lien actif selon la section visible
const navLinks = [...document.querySelectorAll('.navbar a')];
const spy = new IntersectionObserver(entries => {
    entries.forEach(e => {
        if (!e.isIntersecting) return;
        navLinks.forEach(l => l.classList.toggle('active', l.getAttribute('href') === '#' + e.target.id));
    });
}, { rootMargin: '-40% 0px -55% 0px' });
navLinks.forEach(l => {
    const t = document.querySelector(l.getAttribute('href'));
    if (t) spy.observe(t);
    l.addEventListener('click', () => {
        navbar.classList.remove('active');
        toggleNavbar.classList.remove('active');
    });
});

// Thème clair / sombre (choix mémorisé, sinon réglage du système)
const root = document.documentElement;
const themeBtn = document.querySelector('.theme-toggle');
const syncThemeBtn = () => themeBtn && themeBtn.setAttribute('aria-pressed', root.dataset.theme === 'dark');
syncThemeBtn();
if (themeBtn) {
    themeBtn.addEventListener('click', () => {
        root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
        try { localStorage.setItem('theme', root.dataset.theme); } catch (e) {}
        syncThemeBtn();
    });
}
matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
    try { if (localStorage.getItem('theme')) return; } catch (err) {}
    root.dataset.theme = e.matches ? 'dark' : 'light';
    syncThemeBtn();
});

// Ouverture des projets dans le portfolio
const viewer = document.getElementById('viewer');
if (viewer && typeof viewer.showModal === 'function') {
    const frame = document.getElementById('viewer-frame');
    document.querySelectorAll('a[data-viewer]').forEach(a => {
        a.addEventListener('click', e => {
            e.preventDefault();
            document.getElementById('viewer-title').textContent = a.dataset.viewer;
            document.getElementById('viewer-new').href = a.href;
            frame.src = a.href;
            viewer.showModal();
            root.classList.add('no-scroll');
        });
    });
    viewer.querySelector('.viewer-close').addEventListener('click', () => viewer.close());
    viewer.addEventListener('click', e => { if (e.target === viewer) viewer.close(); });
    viewer.addEventListener('close', () => {
        frame.src = 'about:blank';
        root.classList.remove('no-scroll');
    });
}
