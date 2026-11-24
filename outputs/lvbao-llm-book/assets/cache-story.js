(() => {
  const host = document.querySelector('#cache-story');
  if (!host) return;

  const prefix = ['小红', '翻开', '一本'];
  host.innerHTML = `
    <div class="diagram-toolbar"><span class="diagram-kicker">INTERACTIVE ATLAS / KV CACHE</span></div>
    <h2>加上「书」，哪三组 K/V 可以直接拿来用？</h2>
    <p>先处理「小红 / 翻开 / 一本」。两边用同一个模型，试着预测接上「书」后要算几组 K/V。</p>
    <div class="example-controls">
      <button type="button" class="cache-append">接上「书」</button>
      <button type="button" class="cache-reset">重置</button>
    </div>
    <div class="cache-comparison"></div>
    <p class="cache-summary" aria-live="polite"></p>
    <p class="meta">仅示意单层的 K/V 计算。教学切分不代表真实分词器。</p>`;
  const comparison = host.querySelector('.cache-comparison');
  const summary = host.querySelector('.cache-summary');
  const append = host.querySelector('.cache-append');
  const reset = host.querySelector('.cache-reset');

  function lane(cached, appended, tokens) {
    const cells = tokens.map((token, i) => {
      const fresh = appended && i === prefix.length;
      const label = fresh ? '新算 K/V' : !appended ? (cached ? '计算并保存 K/V' : '初次计算 K/V') : cached ? '读取旧 K/V' : '重算旧 K/V';
      return `<li class="${fresh ? 'cache-fresh' : appended && cached ? 'cache-reuse' : ''}"><strong>${token}</strong><span>${label}</span></li>`;
    }).join('');
    return `<section><h3>${cached ? '使用缓存' : '不使用缓存'}</h3><ol>${cells}</ol><p>${appended ? (cached ? '新算 1 组 · 读取 3 组' : '计算 4 组') : '初次计算 3 组'}</p></section>`;
  }

  function render(appended) {
    const tokens = appended ? [...prefix, '书'] : prefix;
    comparison.innerHTML = lane(false, appended, tokens) + lane(true, appended, tokens);
    summary.textContent = appended
      ? '两边都根据「小红 / 翻开 / 一本 / 书」计算下一词。新位置的查询仍会读取前文；省掉的是旧三组 K/V 的重复计算。'
      : '两边还在处理相同的三片段前缀；缓存侧会保存这三组 K/V。';
    append.disabled = appended;
  }

  append.onclick = () => { render(true); reset.focus({preventScroll:true}); };
  reset.onclick = () => { render(false); append.focus({preventScroll:true}); };
  render(false);
})();
