/**
 * 文档索引搜索：根据输入过滤导航列表（支持桌面端和移动端抽屉）
 */
document.addEventListener('DOMContentLoaded', function() {
  const searchInputs = document.querySelectorAll('.doc-nav-search-input');
  const navSections = document.querySelectorAll('.doc-nav-section');
  if (!searchInputs.length || !navSections.length) return;

  function filterNav(q) {
    navSections.forEach(function(section) {
      const links = section.querySelectorAll('.doc-nav-list a');
      let visibleCount = 0;
      links.forEach(function(link) {
        const text = link.textContent.toLowerCase();
        const match = !q || text.includes(q);
        const li = link.closest('li');
        if (li) li.style.display = match ? '' : 'none';
        if (match) visibleCount++;
      });
      section.open = !q || visibleCount > 0;
    });
  }

  searchInputs.forEach(function(input) {
    input.addEventListener('input', function() {
      var q = this.value.trim().toLowerCase();
      searchInputs.forEach(function(other) { if (other !== input) other.value = input.value; });
      filterNav(q);
    });
  });
});
