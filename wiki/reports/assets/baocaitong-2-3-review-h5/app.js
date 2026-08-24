(function () {
  "use strict";

  const compareButtons = [...document.querySelectorAll("[data-compare-mode]")];
  const versionPanels = [...document.querySelectorAll("[data-version-panel]")];
  const ownerButtons = [...document.querySelectorAll("[data-owner-filter]")];
  const questionCards = [...document.querySelectorAll("[data-question-owner]")];
  const navLinks = [...document.querySelectorAll(".nav a[href^='#']")];
  const sections = [...document.querySelectorAll("main section[id]")];
  const progress = document.querySelector(".progress");
  let scrollFrame = 0;

  function setCompareMode(mode) {
    compareButtons.forEach((button) => {
      const active = button.dataset.compareMode === mode;
      button.setAttribute("aria-pressed", String(active));
    });
    versionPanels.forEach((panel) => {
      panel.hidden = mode !== "compare" && panel.dataset.versionPanel !== mode;
    });
    document.documentElement.dataset.compareMode = mode;
  }

  function setOwnerFilter(owner) {
    ownerButtons.forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.ownerFilter === owner));
    });
    questionCards.forEach((card) => {
      card.hidden = owner !== "all" && card.dataset.questionOwner !== owner;
    });
  }

  function updateProgress() {
    if (!progress) return;
    const root = document.documentElement;
    const distance = Math.max(1, root.scrollHeight - root.clientHeight);
    progress.style.width = `${Math.min(100, (root.scrollTop / distance) * 100)}%`;
  }

  function activateSection(sectionId) {
    navLinks.forEach((link) => {
      const active = link.getAttribute("href") === `#${sectionId}`;
      link.classList.toggle("active", active);
      if (active) link.setAttribute("aria-current", "location");
      else link.removeAttribute("aria-current");
    });
  }

  function toggleNode(button) {
    const detail = button.querySelector(".node-detail");
    if (!detail) return;
    const expanded = button.getAttribute("aria-expanded") === "true";
    button.setAttribute("aria-expanded", String(!expanded));
    detail.hidden = expanded;
  }

  compareButtons.forEach((button) => {
    button.addEventListener("click", () => setCompareMode(button.dataset.compareMode));
  });
  ownerButtons.forEach((button) => {
    button.addEventListener("click", () => setOwnerFilter(button.dataset.ownerFilter));
  });
  document.querySelectorAll("[data-node-button]").forEach((button) => {
    button.addEventListener("click", () => toggleNode(button));
  });

  window.addEventListener("scroll", () => {
    if (scrollFrame) return;
    scrollFrame = window.requestAnimationFrame(() => {
      updateProgress();
      scrollFrame = 0;
    });
  }, { passive: true });

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (visible) activateSection(visible.target.id);
    }, { rootMargin: "-25% 0px -60% 0px", threshold: [0.05, 0.3, 0.6] });
    sections.forEach((section) => observer.observe(section));
  }

  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape") return;
    document.querySelectorAll("[data-node-button][aria-expanded='true']").forEach((button) => {
      button.setAttribute("aria-expanded", "false");
      const detail = button.querySelector(".node-detail");
      if (detail) detail.hidden = true;
    });
  });

  setCompareMode("compare");
  setOwnerFilter("all");
  updateProgress();
  if (sections[0]) activateSection(sections[0].id);

  window.baocaitongReview = { setCompareMode, setOwnerFilter, updateProgress, activateSection };
})();