(() => {
  const host = document.querySelector('[data-reimbursement-lesson]');
  if (!host) return;
  const c = reimbursementCase;
  const generalization = host.dataset.reimbursementLesson === '11';
  const models = [[16, 14], [19, 12]];
  const options = generalization ? ['第 5 轮', '第 10 轮'] : ['只看条款号和明确结论', '核对条款和证据'];
  const buttons = options.map((label, i) => `<button type="button" data-option="${i}" aria-pressed="false">${label}</button>`).join('');
  host.innerHTML = `
    <div class="diagram-toolbar"><span class="diagram-kicker">INTERACTIVE ATLAS / ${generalization ? '训练与验证' : '评分规则'}</span></div>
    <h2>${generalization ? '熟题多答对了三道，你会留下这个模型吗？' : '答案不变，为什么换个评分规则排名就反了？'}</h2>
    <p>同一笔 ${c.amount} 元差旅。标准结论是金额符合 ${c.currentLimit} 元限额，凭证仍待核验。</p>
    ${generalization ? '<p>先预测该留哪个检查点。训练题与未见验证题各 20 道，两组始终按同一标准评分。</p>' : `<p>先预测：只看条款号和表态是否明确，哪份会得高分？</p><ol type="A"><li>${c.cautiousAnswer}</li><li>${c.wrongAnswer}</li></ol>`}
    <div class="example-controls">${buttons}</div>
    <div class="example-result" aria-live="polite"><p>先想一想，再选择查看。</p></div>
    ${generalization ? `<details><summary>查看错题</summary><p>熟悉问法：「这笔 ${c.amount} 元能不能报？」未见改写：「我这趟出差花了六百八，票据还没核验，能直接提交吗？」示意中的后期模型能答熟题，却在改写题里漏掉凭证条件。</p></details>` : ''}
    <button type="button" class="training-reset">重置</button>
    <p class="meta">虚构教学数据。<a href="14.html#evidence-story">到第14课核对制度与凭证</a></p>`;
  const controls = [...host.querySelectorAll('[data-option]')];
  const result = host.querySelector('.example-result');

  function row(name, value, maximum) {
    return `<div><span>${name}</span><progress aria-label="${name}" max="${maximum}" value="${value}"></progress><span>${value}/${maximum}</span></div>`;
  }

  function render(index) {
    controls.forEach((button, i) => button.setAttribute('aria-pressed', String(index === i)));
    if (index < 0) {
      result.innerHTML = '<p>先想一想，再选择查看。</p>';
      return;
    }
    if (generalization) {
      const [training, validation] = models[index];
      result.innerHTML = `<div class="example-bars">${row('训练题', training, 20)}${row('验证题', validation, 20)}</div><p>${index ? '多学五轮，训练多对 3 题，验证少对 2 题。按验证结果应选第 5 轮。' : '验证答对 14 题，记下这个检查点，再和第 10 轮比较。'}</p>`;
      return;
    }
    const scores = index === 0 ? [1, 2] : [3, 0];
    const explanation = index === 0
      ? '每项 1 分：含条款号 A、B 都得分；无条件给出结论仅 B 得分。B 排第一。'
      : '每项 1 分：条款存在、金额结论有据、缺凭证时保留结论。A 三项满足，B 三项均不满足。A 排第一。';
    result.innerHTML = `<div class="example-bars">${row('回答 A', scores[0], index ? 3 : 2)}${row('回答 B', scores[1], index ? 3 : 2)}</div><p>${explanation}</p>`;
  }

  controls.forEach((button, i) => button.onclick = () => render(i));
  host.querySelector('.training-reset').onclick = () => {
    render(-1);
    host.querySelector('details')?.removeAttribute('open');
    controls[0].focus();
  };
})();
