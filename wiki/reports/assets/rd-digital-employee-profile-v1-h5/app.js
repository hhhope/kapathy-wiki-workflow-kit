"use strict";

function initProgress() {
  const progress = document.querySelector("[data-reading-progress]");
  if (!progress) return;

  const update = () => {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const ratio = scrollable > 0 ? window.scrollY / scrollable : 1;
    const percentage = Math.min(100, Math.max(0, ratio * 100));
    progress.style.width = `${percentage}%`;
  };

  update();
  window.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update);
}

function initChapterNav() {
  const chapters = Array.from(document.querySelectorAll("[data-chapter]"));
  const links = Array.from(document.querySelectorAll("[data-chapter-link]"));
  if (!chapters.length || !links.length) return;

  const linksByChapter = new Map(
    links.map((link) => [link.getAttribute("data-chapter-link"), link]),
  );
  if (chapters.some((chapter) => !linksByChapter.has(chapter.id))) return;

  const setActive = (chapterId) => {
    links.forEach((link) => {
      const active = link.getAttribute("data-chapter-link") === chapterId;
      link.classList.toggle("is-active", active);
      link.setAttribute("aria-current", String(active));
    });
  };

  links.forEach((link) => {
    link.addEventListener("click", () => {
      setActive(link.getAttribute("data-chapter-link"));
    });
  });
  setActive(chapters[0].id);

  if (!("IntersectionObserver" in window)) return;
  const ratios = new Map(chapters.map((chapter) => [chapter.id, 0]));
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => ratios.set(entry.target.id, entry.intersectionRatio));
      const active = [...ratios.entries()].sort((left, right) => right[1] - left[1])[0];
      if (active && active[1] > 0) setActive(active[0]);
    },
    { rootMargin: "-15% 0px -55%", threshold: [0, 0.1, 0.35, 0.65] },
  );
  chapters.forEach((chapter) => observer.observe(chapter));
}

function initReveal() {
  const pages = Array.from(document.querySelectorAll("[data-content-page]"));
  if (!pages.length) return;

  const revealAll = () => pages.forEach((page) => page.classList.add("is-revealed"));
  const reduceMotion = window.matchMedia?.("(prefers-reduced-motion: reduce)").matches;
  if (reduceMotion || !("IntersectionObserver" in window)) {
    revealAll();
    return;
  }

  const revealWithMotion = (page) => {
    page.classList.add("is-revealed");
    if (typeof page.animate !== "function") return;
    try {
      page.animate(
        [
          { opacity: 0.15, transform: "translateY(14px)" },
          { opacity: 1, transform: "translateY(0)" },
        ],
        { duration: 520, easing: "cubic-bezier(.2, .7, .2, 1)" },
      );
    } catch (_error) {
      // The page remains readable when Web Animations is unavailable or rejected.
    }
  };

  try {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          revealWithMotion(entry.target);
          observer.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -8%", threshold: 0.08 },
    );
    pages.forEach((page) => observer.observe(page));
  } catch (_error) {
    revealAll();
  }
}

function initSelectablePanel(triggerSelector, triggerAttribute, panelSelector, panelAttribute) {
  const triggers = Array.from(document.querySelectorAll(triggerSelector));
  const panels = Array.from(document.querySelectorAll(panelSelector));
  if (!triggers.length || !panels.length) return;

  const panelsByKey = new Map(
    panels.map((panel) => [panel.getAttribute(panelAttribute), panel]),
  );
  if (triggers.some((trigger) => !panelsByKey.has(trigger.getAttribute(triggerAttribute)))) {
    return;
  }

  const tablist = triggers[0].closest(".horizontal-diagram");
  if (tablist && triggers.every((trigger) => tablist.contains(trigger))) {
    tablist.setAttribute("role", "tablist");
    tablist.setAttribute("aria-orientation", "horizontal");
  }

  const activate = (activeKey, focus = false) => {
    triggers.forEach((trigger) => {
      const selected = trigger.getAttribute(triggerAttribute) === activeKey;
      trigger.classList.toggle("is-active", selected);
      trigger.setAttribute("aria-selected", String(selected));
      trigger.tabIndex = selected ? 0 : -1;
      if (selected && focus) trigger.focus();
    });
    panels.forEach((panel) => {
      panel.hidden = panel.getAttribute(panelAttribute) !== activeKey;
    });
  };

  triggers.forEach((trigger, index) => {
    const key = trigger.getAttribute(triggerAttribute);
    const panel = panelsByKey.get(key);
    const triggerId = trigger.id || `${triggerAttribute.slice(5)}-tab-${key}`;
    trigger.id = triggerId;
    trigger.setAttribute("role", "tab");
    panel.setAttribute("role", "tabpanel");
    panel.setAttribute("aria-labelledby", triggerId);

    trigger.addEventListener("click", () => activate(key));
    trigger.addEventListener("keydown", (event) => {
      let targetIndex = null;
      if (event.key === "ArrowRight" || event.key === "ArrowDown") {
        targetIndex = (index + 1) % triggers.length;
      } else if (event.key === "ArrowLeft" || event.key === "ArrowUp") {
        targetIndex = (index - 1 + triggers.length) % triggers.length;
      } else if (event.key === "Home") {
        targetIndex = 0;
      } else if (event.key === "End") {
        targetIndex = triggers.length - 1;
      }
      if (targetIndex === null) return;
      event.preventDefault();
      activate(triggers[targetIndex].getAttribute(triggerAttribute), true);
    });
  });

  const selected = triggers.find(
    (trigger) => trigger.getAttribute("aria-selected") === "true",
  );
  activate((selected || triggers[0]).getAttribute(triggerAttribute));
}

function initCapabilityPanel() {
  initSelectablePanel(
    ".capability-trigger",
    "data-capability",
    "[data-capability-panel]",
    "data-capability-panel",
  );
}

function initStatePanel() {
  initSelectablePanel(
    ".state-trigger",
    "data-state",
    "[data-state-panel]",
    "data-state-panel",
  );
}

function initLightbox() {
  const dialog = document.querySelector("#onepager-lightbox");
  const triggers = Array.from(document.querySelectorAll("[data-lightbox-open]"));
  const closeButton = dialog?.querySelector("[data-lightbox-close]");
  if (!dialog || !triggers.length || !closeButton) return;

  let lastTrigger = null;

  const finishClose = () => {
    dialog.hidden = true;
    dialog.removeAttribute("open");
    if (lastTrigger?.isConnected) lastTrigger.focus();
    lastTrigger = null;
  };

  const closeDialog = () => {
    if (dialog.hidden) return;
    if (dialog.open && typeof dialog.close === "function") {
      dialog.close();
    } else {
      finishClose();
    }
  };

  triggers.forEach((trigger) => {
    trigger.addEventListener("click", () => {
      lastTrigger = trigger;
      dialog.hidden = false;
      if (typeof dialog.showModal === "function") {
        if (!dialog.open) dialog.showModal();
      } else {
        dialog.setAttribute("open", "");
      }
      closeButton.focus();
    });
  });

  closeButton.addEventListener("click", (event) => {
    event.preventDefault();
    closeDialog();
  });
  dialog.addEventListener("cancel", (event) => {
    event.preventDefault();
    closeDialog();
  });
  dialog.addEventListener("close", finishClose);
  dialog.addEventListener("click", (event) => {
    if (event.target === dialog) closeDialog();
  });
}

function initBackToTop() {
  const controls = Array.from(document.querySelectorAll("[data-back-to-top]"));
  if (!controls.length) return;

  controls.forEach((control) => {
    control.addEventListener("click", (event) => {
      event.preventDefault();
      const reduceMotion = window.matchMedia?.("(prefers-reduced-motion: reduce)").matches;
      window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" });
    });
  });
}

document.addEventListener("DOMContentLoaded", () => {
  [
    initProgress,
    initChapterNav,
    initReveal,
    initCapabilityPanel,
    initStatePanel,
    initLightbox,
    initBackToTop,
  ].forEach((initialize) => {
    try {
      initialize();
    } catch (error) {
      console.warn("Interactive enhancement skipped:", error);
    }
  });
});
