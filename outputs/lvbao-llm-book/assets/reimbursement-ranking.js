(() => {
  const host = document.querySelector('[data-reimbursement-ranking]');
  if (!host) return;
  const data = reimbursementCase;
  const currentScore = 85;
  host.innerHTML = `
    <label>旧制度相似度 <input type="range" min="0" max="100" value="95"></label>
    <div class="example-bars"></div>
    <p aria-live="polite"></p>
    <button type="button">重置相似度</button>`;
  const slider = host.querySelector('input');
  const chart = host.querySelector('.example-bars');
  const result = host.querySelector('p');

  function render() {
    const oldScore = Number(slider.value);
    const sources = [['旧制度', oldScore, data.oldLimit], ['现行制度', currentScore, data.currentLimit]];
    sources.sort((a, b) => b[1] - a[1]);
    chart.innerHTML = sources.map(([label, score, limit]) =>
      `<div><span>${label}（限额 ${limit} 元）</span><progress aria-label="${label}相似度" max="100" value="${score}"></progress><span>${score}%</span></div>`).join('');
    const rank = oldScore === currentScore ? '两份制度相似度并列' : sources[0][0] + '检索排名第一';
    result.textContent = rank + '。单据日期 ' + data.expenseDate + ' 晚于新版生效日期 ' + data.effectiveDate +
      '，仍应依据现行制度' + data.clause + '，并核验凭证。';
  }

  slider.addEventListener('input', render);
  host.querySelector('button').onclick = () => { slider.value = 95; render(); slider.focus(); };
  render();
})();
