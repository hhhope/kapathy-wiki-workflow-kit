(() => {
  const host = document.querySelector('#context-story');
  if (!host) return;

  const positions = [
    {label: '小红', value: 1, x: 61},
    {label: '书', value: 2, x: 180},
    {label: '其他', value: 4, x: 299},
  ];
  const questions = [
    {label: '她指谁？', target: 0, explanation: '这句里，「她」可以指向小红。'},
    {label: '递了什么？', target: 1, explanation: '句子里被递过去的是「书」。'},
  ];
  host.innerHTML = `
    <div class="diagram-toolbar"><span class="diagram-kicker">INTERACTIVE ATLAS / ATTENTION</span></div>
    <h2>问题变了，应该读哪条线索？</h2>
    <p>小明把书递给小红，因为她要读书。先想一想，再点一个问题。</p>
    <div class="example-controls" aria-label="切换要找的线索">
      ${questions.map(q => `<button type="button" aria-pressed="false">${q.label}</button>`).join('')}
    </div>
    <div class="attention-visual"></div>
    <p class="attention-answer" aria-live="polite">选择一个问题，查看图上哪条线索被突出。</p>
    <details class="attention-calculation" hidden>
      <summary>展开计算：分数怎样变成输出</summary>
      <div class="attention-products"></div>
    </details>
    <p class="meta">问题、分数和 Value 都是教学设定。「其他」合并其余线索；用一维 Value 示意真实模型中的向量加权。注意力权重显示这一步取了哪些信息，不能验证事实。</p>
    <button type="button" class="attention-reset">重置</button>`;

  const control = [...host.querySelectorAll('.example-controls button')];
  const visual = host.querySelector('.attention-visual');
  const answer = host.querySelector('.attention-answer');
  const calculation = host.querySelector('.attention-calculation');
  const products = host.querySelector('.attention-products');

  function render(index) {
    const question = questions[index];
    const exponential = positions.map((_, i) => i === question?.target ? 2 : 1);
    const total = exponential.reduce((sum, value) => sum + value, 0);
    const weights = exponential.map(value => value / total);
    control.forEach((button, i) => button.setAttribute('aria-pressed', String(i === index)));
    visual.innerHTML = `
      <svg viewBox="0 0 360 170" role="img" aria-label="${question ? question.label + ' 重点线索：' + positions[question.target].label : '三个待选线索：小红、书、其他'}">
        <rect class="attention-query" x="110" y="8" width="140" height="40" rx="9"/>
        <text x="180" y="34">${question?.label || '先选一个问题'}</text>
        ${question ? positions.map(({x}, i) => `<path class="attention-edge ${i === question.target ? 'attention-edge-active' : ''}" pathLength="1" d="M180 48 Q180 82 ${x} 109"/>`).join('') : ''}
        ${positions.map(({x,label},i) => `<g><rect class="${i === question?.target ? 'attention-node-active' : 'attention-node'}" x="${x-48}" y="109" width="96" height="43" rx="8"/><text x="${x}" y="136">${label}${question ? ' · ' + weights[i] * 100 + '%' : ''}</text></g>`).join('')}
      </svg>`;
    calculation.hidden = !question;
    if (!question) {
      calculation.open = false;
      answer.textContent = '选择一个问题，查看图上哪条线索被突出。';
      products.replaceChildren();
      return;
    }
    answer.textContent = question.explanation + ' 图上这条线索的权重是 50%。';
    const contributions = positions.map(({value}, i) => value * weights[i]);
    const sum = contributions.reduce((a,b) => a+b,0);
    products.innerHTML = '<p>缩放后分数取指数，再除以总和 4。</p><table><thead><tr><th>线索</th><th>分数</th><th>权重</th><th>Value × 权重</th></tr></thead><tbody>' +
      positions.map(({label,value},i) => `<tr><th scope="row">${label}</th><td>${i === question.target ? 'ln 2' : '0'}</td><td>${weights[i]*100}%</td><td>${value} × ${weights[i]} = ${contributions[i]}</td></tr>`).join('') +
      '</tbody></table><p>加权输出：<strong>' + contributions.join(' + ') + ' = ' + sum + '</strong></p>';
  }
  control.forEach((button, i) => button.onclick = () => render(i));
  host.querySelector('.attention-reset').onclick = () => { render(-1); control[0].focus(); };
  render(-1);
})();
