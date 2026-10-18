const mobileMenu = document.querySelector('.mobile-nav');
mobileMenu?.addEventListener('click', event => {
  if (event.target.closest('a')) mobileMenu.open = false;
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && mobileMenu?.open) {
    mobileMenu.open = false;
    mobileMenu.querySelector('summary').focus();
  }
});
function revealPolicy() {
  // Keep links from the 2068 homepage useful after the redesign.
  const legacy = {democracy:'freedom', rights:'freedom', media:'freedom', opportunity:'learning', science:'learning', health:'care', housing:'homes', economy:'work', environment:'climate'};
  const id = location.hash.slice(1);
  if (!id) return;
  const target = document.getElementById(id);
  if (target?.classList.contains('policy')) {
    target.querySelector('details').open = true;
    requestAnimationFrame(() => target.scrollIntoView({block:'start', behavior:'instant'}));
  } else if (document.querySelector('.photo-grid') && (legacy[id] || id === 'world')) {
    location.replace('./plan/#' + (legacy[id] || id));
  } else if (document.querySelector('.photo-grid') && ['plan','manifesto','vision'].includes(id)) {
    location.replace('./' + (id === 'vision' ? 'vision' : 'plan') + '/');
  }
}
window.addEventListener('hashchange', revealPolicy);
revealPolicy();
document.getElementById('share')?.addEventListener('click', async () => {
  const status = document.getElementById('share-status');
  const url = new URL('./', location.href).href;
  try {
    if (navigator.share) {
      await navigator.share({title:'NPP 2072 — A freer, fairer Caprica', text:'Freedom to be yourself. A fair chance to thrive.', url});
      status.textContent = 'Thank you for sharing.';
    } else if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(url);
      status.textContent = 'Website link copied. Ready to share.';
    } else {
      status.textContent = 'Copy this address to share: ' + url;
    }
  } catch (error) {
    if (error.name !== 'AbortError') status.textContent = 'Copy this address to share: ' + url;
  }
});
