(function () {
  var article = document.querySelector('article.page-content[data-toc]');
  if (!article) return;

  var headings = article.querySelectorAll('section h2, .container > h2');
  if (headings.length < 3) return;

  // Build TOC list
  var nav = document.createElement('nav');
  nav.className = 'page-toc';
  nav.setAttribute('aria-label', 'On this page');

  var title = document.createElement('p');
  title.className = 'page-toc-title';
  title.textContent = document.documentElement.lang === 'fr' ? 'Sur cette page' : 'On this page';
  nav.appendChild(title);

  var list = document.createElement('ul');

  headings.forEach(function (h, i) {
    // Add id if missing
    if (!h.id) {
      h.id = 'section-' + (i + 1);
    }

    var li = document.createElement('li');
    var a = document.createElement('a');
    a.href = '#' + h.id;
    a.textContent = h.textContent;
    li.appendChild(a);
    list.appendChild(li);
  });

  nav.appendChild(list);

  // Insert after hero, before first section
  var hero = article.querySelector('.hero');
  if (hero && hero.nextElementSibling) {
    article.insertBefore(nav, hero.nextElementSibling);
  } else {
    article.insertBefore(nav, article.firstChild);
  }
})();
