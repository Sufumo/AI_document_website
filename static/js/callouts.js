/**
 * Obsidian 风格 callout 块：将 [!NOTE]、[!TIP]、[!WARNING] 转为带图标的提示框
 */
document.addEventListener('DOMContentLoaded', function() {
  const content = document.querySelector('.doc-content');
  if (!content) return;

  const calloutMap = {
    '[!NOTE]': { class: 'callout-note', label: 'Note', icon: '📝' },
    '[!TIP]': { class: 'callout-tip', label: 'Tip', icon: '💡' },
    '[!WARNING]': { class: 'callout-warning', label: 'Warning', icon: '⚠️' }
  };

  content.querySelectorAll('blockquote').forEach(function(blockquote) {
    const firstP = blockquote.querySelector('p');
    if (!firstP) return;

    const text = firstP.textContent.trim();
    const callout = calloutMap[text];
    if (!callout) return;

    blockquote.classList.add('callout', callout.class);
    firstP.outerHTML = '<div class="callout-header">' +
      '<span class="callout-icon">' + callout.icon + '</span>' +
      '<span class="callout-label">' + callout.label + '</span>' +
      '</div>';
  });
});
