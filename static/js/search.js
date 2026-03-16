// Pagefind search dialog
(function () {
  var trigger = document.getElementById("search-trigger");
  var dialog = document.getElementById("search-dialog");
  var closeBtn = document.getElementById("search-close");

  if (!trigger || !dialog) return;

  new PagefindUI({ element: "#search", showSubResults: true, showImages: false });

  trigger.addEventListener("click", function () {
    dialog.showModal();
    var input = dialog.querySelector(".pagefind-ui__search-input");
    if (input) input.focus();
  });

  closeBtn.addEventListener("click", function () {
    dialog.close();
  });

  dialog.addEventListener("click", function (e) {
    if (e.target === dialog) dialog.close();
  });

  // Ctrl+K / Cmd+K keyboard shortcut
  document.addEventListener("keydown", function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key === "k") {
      e.preventDefault();
      dialog.showModal();
      var input = dialog.querySelector(".pagefind-ui__search-input");
      if (input) input.focus();
    }
  });
})();
