(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var progress = document.querySelector('.scroll-progress span');
    var backToTop = document.querySelector('.back-to-top');

    function updateScrollUi() {
      var scrollTop = window.scrollY || document.documentElement.scrollTop;
      var scrollable = document.documentElement.scrollHeight - window.innerHeight;
      if (progress) progress.style.width = (scrollable > 0 ? (scrollTop / scrollable) * 100 : 0) + '%';
      if (backToTop) backToTop.classList.toggle('is-visible', scrollTop > 360);
    }

    window.addEventListener('scroll', updateScrollUi, { passive: true });
    window.addEventListener('resize', updateScrollUi);
    updateScrollUi();

    if (backToTop) {
      backToTop.addEventListener('click', function () {
        var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
      });
    }

    var categoryButtons = document.querySelectorAll('.category-toggle');
    categoryButtons.forEach(function (button) {
      button.addEventListener('click', function () {
        var panel = document.getElementById(button.getAttribute('aria-controls'));
        var expanded = button.getAttribute('aria-expanded') === 'true';
        button.setAttribute('aria-expanded', String(!expanded));
        if (panel) panel.hidden = expanded;
      });
    });

    if (window.location.hash) {
      var selectedCategory = document.querySelector(window.location.hash);
      var selectedButton = selectedCategory && selectedCategory.querySelector('.category-toggle');
      if (selectedButton) selectedButton.click();
    }

    var revealItems = document.querySelectorAll('.reveal-item');
    if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      revealItems.forEach(function (item) { item.classList.add('is-revealed'); });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-revealed');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealItems.forEach(function (item) { observer.observe(item); });
  });
})();
