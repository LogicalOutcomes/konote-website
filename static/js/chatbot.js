// KoNote chatbot widget — bilingual, page-aware, with source attribution
(function () {
  "use strict";

  var lang = document.documentElement.lang || "en";
  var apiUrl = document.body.dataset.chatbotApi;
  if (!apiUrl) return;

  var widget = document.getElementById("chatbot-widget");
  var panel = document.getElementById("chatbot-panel");
  var toggleBtn = document.getElementById("chatbot-toggle");
  var closeBtn = document.getElementById("chatbot-close");
  var form = document.getElementById("chatbot-form");
  var input = document.getElementById("chatbot-input");
  var messages = document.getElementById("chatbot-messages");
  var disclaimer = document.getElementById("chatbot-disclaimer");

  if (!widget || !panel || !toggleBtn || !form || !input || !messages) return;

  var history = [];
  var isOpen = false;

  // Get current page context
  var currentPage = window.location.pathname;
  var currentPageTitle = document.title.split("|")[0].trim();

  function toggle() {
    isOpen = !isOpen;
    panel.hidden = !isOpen;
    toggleBtn.setAttribute("aria-expanded", isOpen);
    if (isOpen) {
      input.focus();
      if (messages.children.length === 0 && disclaimer) {
        disclaimer.hidden = false;
      }
    }
  }

  function addMessage(role, text, sources) {
    var div = document.createElement("div");
    div.className = "chatbot-msg chatbot-msg--" + role;
    div.textContent = text;
    if (role === "assistant") {
      div.setAttribute("aria-live", "polite");
    }
    messages.appendChild(div);

    // Render source links for assistant messages
    if (role === "assistant" && sources && sources.length > 0) {
      var srcDiv = document.createElement("div");
      srcDiv.className = "chatbot-sources";
      var label = lang === "fr" ? "Sources\u00a0: " : "Sources: ";
      srcDiv.appendChild(document.createTextNode(label));
      sources.forEach(function (src, i) {
        if (i > 0) srcDiv.appendChild(document.createTextNode(", "));
        var a = document.createElement("a");
        a.href = src.url;
        a.textContent = src.label;
        a.className = "chatbot-source-link";
        srcDiv.appendChild(a);
      });
      messages.appendChild(srcDiv);
    }

    messages.scrollTop = messages.scrollHeight;
  }

  function setLoading(on) {
    var existing = messages.querySelector(".chatbot-msg--loading");
    if (on && !existing) {
      var div = document.createElement("div");
      div.className = "chatbot-msg chatbot-msg--loading";
      div.setAttribute("aria-live", "polite");
      div.textContent = lang === "fr" ? "R\u00e9flexion en cours\u2026" : "Thinking\u2026";
      messages.appendChild(div);
      messages.scrollTop = messages.scrollHeight;
    } else if (!on && existing) {
      existing.remove();
    }
  }

  function sendMessage(query) {
    addMessage("user", query);
    setLoading(true);

    fetch(apiUrl + "/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        query: query,
        language: lang,
        current_page: currentPage,
        current_page_title: currentPageTitle,
        history: history,
      }),
    })
      .then(function (resp) {
        if (resp.status === 429) {
          setLoading(false);
          addMessage(
            "assistant",
            lang === "fr"
              ? "Trop de demandes. Veuillez r\u00e9essayer dans un moment."
              : "Too many requests. Please try again in a moment."
          );
          return null;
        }
        if (!resp.ok) throw new Error("API error: " + resp.status);
        return resp.json();
      })
      .then(function (data) {
        if (!data) return;
        setLoading(false);
        addMessage("assistant", data.response, data.sources);
        history.push({ role: "user", content: query });
        history.push({ role: "assistant", content: data.response });
        if (history.length > 6) history = history.slice(-6);
      })
      .catch(function () {
        setLoading(false);
        addMessage(
          "assistant",
          lang === "fr"
            ? "D\u00e9sol\u00e9, je n'ai pas pu traiter votre question. Veuillez r\u00e9essayer."
            : "Sorry, I couldn't process your question. Please try again."
        );
      });
  }

  toggleBtn.addEventListener("click", toggle);
  if (closeBtn) closeBtn.addEventListener("click", toggle);

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var query = input.value.trim();
    if (!query) return;
    input.value = "";
    sendMessage(query);
  });

  // Close on Escape
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && isOpen) toggle();
  });
})();
