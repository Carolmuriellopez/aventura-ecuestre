document.addEventListener('DOMContentLoaded', function () {
  const banner = document.getElementById('cookieBanner');
  const btnOpenConfig = document.getElementById('btnOpenConfig');
  const configPanel = document.getElementById('configPanel');
  const btnAccept = document.getElementById('btnAccept');
  const btnReject = document.getElementById('btnReject');
  const btnSavePrefs = document.getElementById('btnSavePrefs');
  const analyticsToggle = document.getElementById('analyticsToggle');

  if (!banner) return;

  const COOKIE_NAME = 'cookie_consent';
  const COOKIE_MAX_AGE = 60 * 60 * 24 * 365; // 1 año

  function getConsent() {
    const match = document.cookie.match(new RegExp('(?:^|; )' + COOKIE_NAME + '=([^;]*)'));
    return match ? decodeURIComponent(match[1]) : null;
  }

  function setConsent(value) {
    document.cookie = COOKIE_NAME + '=' + value + '; max-age=' + COOKIE_MAX_AGE + '; path=/; SameSite=Lax; Secure';
  }

  function loadGA4() {
    const GA4_ID = window.GA4_MEASUREMENT_ID;
    if (!GA4_ID || window.__ga4Loaded) return;
    window.__ga4Loaded = true;

    const s = document.createElement('script');
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA4_ID;
    s.async = true;
    document.head.appendChild(s);

    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }
    window.gtag = window.gtag || gtag;

    gtag('js', new Date());
    gtag('config', GA4_ID, { anonymize_ip: true });
  }

  function grantAnalytics() {
    if (typeof window.gtag === 'function') {
      window.gtag('consent', 'update', { analytics_storage: 'granted' });
    }
    loadGA4();
  }

  // Si ya hay una decisión guardada, no mostramos el banner
  if (getConsent() === null) {
    banner.hidden = false;
  }

  btnOpenConfig.addEventListener('click', function () {
    const isOpen = configPanel.classList.toggle('open');
    btnOpenConfig.textContent = isOpen ? 'Ocultar opciones' : 'Personalizar';
  });

  btnAccept.addEventListener('click', function () {
    setConsent('all');
    grantAnalytics();
    banner.hidden = true;
  });

  btnReject.addEventListener('click', function () {
    setConsent('necessary_only');
    banner.hidden = true;
  });

  btnSavePrefs.addEventListener('click', function () {
    if (analyticsToggle.checked) {
      setConsent('custom_yes');
      grantAnalytics();
    } else {
      setConsent('custom_no');
    }
    banner.hidden = true;
  });

  // Permite reabrir el banner desde un enlace del footer, ej:
  // <button onclick="window.reopenCookieBanner()">Configurar cookies</button>
  window.reopenCookieBanner = function () {
    banner.hidden = false;
    const stored = getConsent();
    if (stored === 'custom_yes' && analyticsToggle) {
      analyticsToggle.checked = true;
    }
  };
});