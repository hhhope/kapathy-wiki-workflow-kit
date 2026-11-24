(() => {
  const host = document.querySelector('#generation-story');
  if (!host) return;

  const examples = [
    {prefix: '小红翻开一本', choices: [['书',70],['杂志',20],['笔记本',10]]},
    {prefix: '小红拧开一瓶', choices: [['水',70],['果汁',20],['牛奶',10]]},
  ];
  host.innerHTML = `
    <div class="diagram-toolbar"><span class="diagram-kicker">INTERACTIVE ATLAS / 逐词续写</span></div>
    <div class="generation-board">
      <h2>只换前文，下一词会变吗？</h2>
      <p>先猜「一本」和「一瓶」后面各会接什么，再切换前缀。</p>
      <div class="diagram-tabs" aria-label="切换前缀"></div>
      <div class="generation-prefix" aria-live="polite"></div>
      <p class="generation-instruction">点一个候选，把它接回句尾。</p>
      <div class="generation-candidates"></div>
      <div class="diagram-detail" aria-live="polite"></div>
      <button type="button" class="generation-reset">重置本轮</button>
      <p class="meta">候选、概率与切分均为教学设定。</p>
    </div>`;

  const tabs = host.querySelector('.diagram-tabs');
  const prefix = host.querySelector('.generation-prefix');
  const candidates = host.querySelector('.generation-candidates');
  const detail = host.querySelector('.diagram-detail');
  let current = 0;

  function button(label, action) {
    const control = document.createElement('button');
    control.type = 'button';
    control.textContent = label;
    control.onclick = action;
    return control;
  }

  const switches = examples.map(({prefix: text}, i) => {
    const control = button(text, () => render(i));
    tabs.append(control);
    return control;
  });

  function render(index) {
    current = index;
    const example = examples[index];
    switches.forEach((control, i) => control.setAttribute('aria-pressed', String(i === index)));
    prefix.textContent = example.prefix;
    detail.textContent = '选中的词会成为下一轮输入的一部分。';
    candidates.replaceChildren(...example.choices.map(([word, score]) => {
      const control = button(`${word} · ${score}%`, () => {
        prefix.textContent = example.prefix;
        const appended = document.createElement('strong');
        appended.textContent = word;
        prefix.append(appended);
        for (const candidate of candidates.children) {
          candidate.setAttribute('aria-pressed', String(candidate === control));
        }
        detail.textContent = `下一轮收到「${example.prefix}${word}」，会根据这段更长的前缀重新计算候选。`;
      });
      control.setAttribute('aria-pressed', 'false');
      control.style.setProperty('--score', `${score}%`);
      return control;
    }));
  }

  host.querySelector('.generation-reset').onclick = () => {
    render(current);
    switches[current].focus({preventScroll: true});
  };
  render(0);
})();
