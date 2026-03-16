// Pagefind search dialog — bilingual support
(function () {
  "use strict";

  var currentLang = document.documentElement.lang || "en";
  var bundlePath = "/" + currentLang + "/_pagefind/";

  var frTranslations = {
    placeholder: "Rechercher sur le site\u2026",
    zero_results: "Aucun r\u00e9sultat pour [SEARCH_TERM]",
    many_results: "[COUNT] r\u00e9sultats pour [SEARCH_TERM]",
    one_result: "[COUNT] r\u00e9sultat pour [SEARCH_TERM]",
    search_label: "Rechercher sur ce site",
    filters_label: "Filtres",
    load_more: "Charger plus de r\u00e9sultats",
  };

  var searchEl = document.getElementById("search");
  if (!searchEl) return;

  new PagefindUI({
    element: "#search",
    bundlePath: bundlePath,
    showSubResults: true,
    showImages: false,
    translations: currentLang === "fr" ? frTranslations : {},
  });

  // Search dialog open/close
  var trigger = document.getElementById("search-trigger");
  var dialog = document.getElementById("search-dialog");
  var closeBtn = document.getElementById("search-close");

  if (trigger && dialog) {
    trigger.addEventListener("click", function () {
      dialog.showModal();
      var input = dialog.querySelector(".pagefind-ui__search-input");
      if (input) input.focus();
    });
  }

  if (closeBtn && dialog) {
    closeBtn.addEventListener("click", function () {
      dialog.close();
    });
  }

  if (dialog) {
    dialog.addEventListener("click", function (e) {
      if (e.target === dialog) dialog.close();
    });
  }

  // Keyboard shortcut: Ctrl+K / Cmd+K
  document.addEventListener("keydown", function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key === "k") {
      e.preventDefault();
      if (dialog) {
        dialog.showModal();
        var input = dialog.querySelector(".pagefind-ui__search-input");
        if (input) input.focus();
      }
    }
  });
})();
