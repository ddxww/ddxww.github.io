(function () {
  var storageKey = 'site-theme';

  function setTheme(theme) {
    var root = document.documentElement;
    var button = document.querySelector('.theme-switch a');
    var icon = button && button.querySelector('i');

    root.setAttribute('data-theme', theme);
    if (!button || !icon) return;

    var isDark = theme === 'dark';
    icon.className = isDark ? 'fa fa-sun-o' : 'fa fa-moon-o';
    button.setAttribute('aria-label', isDark ? '切换浅色模式' : '切换深色模式');
    button.setAttribute('title', isDark ? '切换为浅色背景' : '切换为深色背景');
  }

  document.addEventListener('DOMContentLoaded', function () {
    setTheme(document.documentElement.getAttribute('data-theme') || 'light');

    var button = document.querySelector('.theme-switch a');
    if (!button) return;

    button.addEventListener('click', function (event) {
      event.preventDefault();
      var current = document.documentElement.getAttribute('data-theme');
      var next = current === 'dark' ? 'light' : 'dark';
      localStorage.setItem(storageKey, next);
      setTheme(next);
    });
  });
})();
