/**
 * 右侧目录由 Hugo .TableOfContents 在编译时生成；此处仅做滚动时高亮当前章节。
 */
document.addEventListener('DOMContentLoaded', function() {
  const content = document.querySelector('.doc-content');
  const toc = document.getElementById('TableOfContents');
  if (!content || !toc) return;

  const headings = content.querySelectorAll('h2[id], h3[id], h4[id]');
  if (headings.length === 0) return;

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (!entry.isIntersecting) return;
      var id = entry.target.id;
      toc.querySelectorAll('a').forEach(function(a) {
        a.classList.remove('active');
        if (a.getAttribute('href') === '#' + id) {
          a.classList.add('active');
        }
      });
    });
  }, { rootMargin: '-80px 0px -60% 0px' });

  headings.forEach(function(h) {
    observer.observe(h);
  });
});
