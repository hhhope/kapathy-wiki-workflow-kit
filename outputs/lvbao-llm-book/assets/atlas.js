(() => {
  const sidebar = document.querySelector('.sidebar');
  const header = document.querySelector('body > header');
  if (sidebar && header) {
    sidebar.id = 'atlas-navigation';
    const menu = document.createElement('button');
    menu.className = 'atlas-menu'; menu.textContent = '目录';
    menu.setAttribute('aria-controls', sidebar.id); menu.setAttribute('aria-expanded', 'false');
    const close = () => { sidebar.classList.remove('atlas-open'); menu.setAttribute('aria-expanded', 'false'); };
    menu.onclick = () => { const open = sidebar.classList.toggle('atlas-open'); menu.setAttribute('aria-expanded', String(open)); };
    header.prepend(menu);
    document.addEventListener('keydown', e => { if(e.key === 'Escape') close(); });
    document.addEventListener('click', e => { if(!sidebar.contains(e.target) && !menu.contains(e.target)) close(); });
    sidebar.querySelectorAll('a').forEach(a => {
      const normalize = p => p.replace(/\.html$/, '').replace(/\/$/, '/index');
      if(normalize(new URL(a.href).pathname) === normalize(location.pathname)) { a.classList.add('active'); a.setAttribute('aria-current','page'); }
    });
  }
  const progress = document.createElement('div'); progress.className = 'atlas-progress'; document.body.append(progress);
  const update = () => { const total = document.documentElement.scrollHeight - innerHeight; progress.style.width = (total > 0 ? scrollY / total * 100 : 0) + '%'; };
  addEventListener('scroll', update, {passive:true}); addEventListener('resize', update); update();
  if(!matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelector('main')?.classList.add('atlas-reveal');
  }
})();

document.querySelectorAll('.atlas-video').forEach(disclosure => {
  const template = disclosure.querySelector('template');
  if (!template) return;

  function syncPlayer() {
    const player = disclosure.querySelector('iframe');
    if (disclosure.open && !player) {
      disclosure.append(template.content.cloneNode(true));
    } else if (!disclosure.open && player) {
      player.remove();
    }
  }

  disclosure.addEventListener('toggle', syncPlayer);
  syncPlayer();
});
