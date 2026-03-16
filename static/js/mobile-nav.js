/**
 * 移动端目录侧滑抽屉
 */
document.addEventListener('DOMContentLoaded', function() {
  var trigger = document.getElementById('mobile-nav-trigger');
  var drawer = document.getElementById('mobile-nav-drawer');
  var overlay = document.getElementById('mobile-nav-overlay');
  var closeBtn = document.getElementById('mobile-nav-close');

  if (!trigger || !drawer || !overlay) return;

  function open() {
    drawer.classList.add('is-open');
    overlay.classList.add('is-open');
    overlay.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function close() {
    drawer.classList.remove('is-open');
    overlay.classList.remove('is-open');
    overlay.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  trigger.addEventListener('click', open);
  closeBtn && closeBtn.addEventListener('click', close);
  overlay.addEventListener('click', close);

  drawer.querySelectorAll('a').forEach(function(link) {
    link.addEventListener('click', close);
  });

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && drawer.classList.contains('is-open')) close();
  });

  window.addEventListener('resize', function() {
    if (window.matchMedia('(min-width: 64.0625rem)').matches && drawer.classList.contains('is-open')) {
      close();
    }
  });
});
