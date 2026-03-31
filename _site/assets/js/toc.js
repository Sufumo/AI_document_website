// 自动生成目录并高亮当前阅读位置
document.addEventListener('DOMContentLoaded', function() {
  const content = document.querySelector('.doc-content');
  const toc = document.getElementById('toc');
  if (!content || !toc) return;

  const headings = content.querySelectorAll('h2, h3, h4');
  if (headings.length === 0) return;

  const ul = document.createElement('ul');
  let currentUl = ul;
  let lastLevel = 2;

  headings.forEach((h, i) => {
    const level = parseInt(h.tagName.charAt(1));
    const id = h.id || 'heading-' + i;
    h.id = id;

    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = '#' + id;
    a.textContent = h.textContent.trim();
    li.appendChild(a);

    if (level > lastLevel) {
      const childUl = document.createElement('ul');
      currentUl.lastElementChild.appendChild(childUl);
      currentUl = childUl;
    } else if (level < lastLevel) {
      for (let j = level; j < lastLevel; j++) {
        currentUl = currentUl.parentElement.closest('ul') || ul;
      }
    }
    currentUl.appendChild(li);
    lastLevel = level;
  });

  toc.appendChild(ul);

  // 滚动高亮
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        toc.querySelectorAll('a').forEach(a => {
          a.classList.remove('active');
          if (a.getAttribute('href') === '#' + entry.target.id) {
            a.classList.add('active');
          }
        });
      }
    });
  }, { rootMargin: '-80px 0px -60% 0px' });

  headings.forEach(h => observer.observe(h));
});
