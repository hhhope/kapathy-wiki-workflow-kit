(() => {
  const host = document.querySelector('#evidence-story');
  if (!host) return;
  const c = reimbursementCase;
  const documents = [
    ['旧制度 · 检索第 1', '限额 ' + c.oldLimit + ' 元。自 ' + c.effectiveDate + ' 起被新版替代。'],
    ['现行制度 · 检索第 2', c.effectiveDate + ' 起生效。' + c.clause + '要求金额不超过 ' + c.currentLimit + ' 元，并有有效凭证。'],
    ['报销单 · 工具记录', '日期 ' + c.expenseDate + '，金额 ' + c.amount + ' 元。凭证状态需要另外查询。'],
  ];
  const findings = [
    ['虚构引用', '这份教学证据里的现行制度没有' + c.inventedClause + '。可核对的依据是' + c.clause + '。', 1],
    ['结论超出证据', '单据金额满足现行条款的限额，但凭证还需要核验。', 2],
  ];
  host.innerHTML = `
    <div class="diagram-toolbar"><span class="diagram-kicker">INTERACTIVE ATLAS / 证据查证</span></div>
    <h2>这笔 680 元差旅能不能报销？</h2>
    <p>先读回答，猜哪一处最需要核验，然后点一下看证据。</p>
    <p class="evidence-claim">按现行制度<button type="button" data-claim="0" aria-pressed="false">第 9 条</button>，680 元<button type="button" data-claim="1" aria-pressed="false">可以直接报销</button>。</p>
    <div class="example-controls evidence-docs" aria-label="打开证据">
      ${documents.map(([name], i) => `<button type="button" data-document="${i}" aria-pressed="false">${name}</button>`).join('')}
    </div>
    <div class="evidence-reading" aria-live="polite">选择回答中的一句或打开一份材料。</div>
    <h3>查询凭证状态</h3>
    <div class="example-controls" aria-label="模拟工具查询">
      <button type="button" data-receipt="verified" aria-pressed="false">查到有效凭证</button>
      <button type="button" data-receipt="missing" aria-pressed="false">查询无结果</button>
    </div>
    <div class="example-result evidence-verdict" aria-live="polite"></div>
    <button type="button" class="evidence-reset">重置</button>
    <p class="meta">虚构教学数据。示意检索负责找规则，工具负责查询单据状态。</p>`;

  const claims = [...host.querySelectorAll('[data-claim]')];
  const sources = [...host.querySelectorAll('[data-document]')];
  const receipts = [...host.querySelectorAll('[data-receipt]')];
  const reading = host.querySelector('.evidence-reading');
  const verdict = host.querySelector('.evidence-verdict');

  function pressed(group, selected) {
    group.forEach(button => button.setAttribute('aria-pressed', String(button === selected)));
  }

  function showEvidence(documentIndex, claimIndex) {
    pressed(sources, sources[documentIndex]);
    pressed(claims, claims[claimIndex]);
    const [title, body] = documents[documentIndex];
    const finding = findings[claimIndex];
    reading.replaceChildren();
    for (const text of [finding?.[0], finding?.[1], title, body].filter(Boolean)) {
      const line = document.createElement('p');
      line.textContent = text;
      reading.append(line);
    }
    reading.classList.remove('evidence-flash');
    void reading.offsetWidth;
    reading.classList.add('evidence-flash');
  }

  function showVerdict(state) {
    const selected = receipts.find(button => button.dataset.receipt === state);
    pressed(receipts, selected);
    const status = state === 'verified' ? '已核验有效' : state === 'missing' ? '查询无结果' : '尚未查询';
    verdict.dataset.receipt = state;
    verdict.textContent = '凭证：' + status + '。680 元符合现行 800 元限额。' +
      (state === 'verified' ? '已满足示例中的金额与凭证两项条件。' : '是否可报销仍需核验凭证。');
  }

  claims.forEach((button, i) => button.onclick = () => showEvidence(findings[i][2], i));
  sources.forEach((button, i) => button.onclick = () => showEvidence(i));
  receipts.forEach(button => button.onclick = () => showVerdict(button.dataset.receipt));
  host.querySelector('.evidence-reset').onclick = () => {
    pressed(claims);
    pressed(sources);
    reading.classList.remove('evidence-flash');
    reading.textContent = '选择回答中的一句或打开一份材料。';
    showVerdict('initial');
    claims[0].focus();
  };
  showVerdict('initial');
})();
