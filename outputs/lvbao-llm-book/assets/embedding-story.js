(() => {
  const host = document.querySelector('#embedding-story');
  if (!host) return;

  const people = [
    {name: '你', id: 17, music: 8, film: 8},
    {name: '小周', id: 18, music: 2, film: 3},
    {name: '小林', id: 900, music: 7, film: 9},
  ];
  const x = score => 45 + score * 24;
  const y = score => 255 - score * 22;
  const distance = person => Math.hypot(person.music - 8, person.film - 8);

  host.innerHTML = `
    <div class="diagram-toolbar"><span class="diagram-kicker">INTERACTIVE ATLAS / ID 与向量</span></div>
    <h2>号码挨得近，兴趣也更像吗？</h2>
    <p>你是 17 号，想找人一起听歌看电影。先凭号码猜一猜。</p>
    <div class="example-controls">
      <button type="button" data-guess="18" aria-pressed="false">猜 18 号 · 小周</button>
      <button type="button" data-guess="900" aria-pressed="false">猜 900 号 · 小林</button>
      <button type="button" data-guess="unknown" aria-pressed="false">号码看不出来</button>
    </div>
    <button type="button" class="embedding-reveal" aria-expanded="false" aria-controls="embedding-plane">揭晓兴趣图</button>
    <div id="embedding-plane" hidden>
      <svg viewBox="0 0 320 290" role="img" aria-label="横轴音乐，纵轴电影。你在8、8，小周在2、3，小林在7、9；小林距你最近。">
        <path d="M45 24V255H292" stroke="#8a9abe" stroke-width="2" fill="none"/>
        ${[0, 2, 4, 6, 8, 10].map(n => `<text x="${x(n)}" y="273" text-anchor="middle">${n}</text><text x="38" y="${y(n)+4}" text-anchor="end">${n}</text>`).join('')}
        <text x="45" y="17">电影</text><text x="285" y="287">音乐</text>
        <path d="M${x(2)} ${y(3)}L${x(8)} ${y(8)}" stroke="#798bad" stroke-dasharray="5 4" fill="none"/>
        <path class="embedding-near" d="M${x(7)} ${y(9)}L${x(8)} ${y(8)}" stroke="#c8adff" stroke-width="3" fill="none"/>
        ${people.map(({name,music,film}, i) => `<circle cx="${x(music)}" cy="${y(film)}" r="6" fill="${i===2?'#c8adff':'#82d8ec'}"/><text x="${x(music)+9}" y="${y(film)+(i===2?-5:5)}">${name}</text>`).join('')}
      </svg>
      <p>小林在两个兴趣维度都只差 1，距离约 ${distance(people[2]).toFixed(2)}；小周距离约 ${distance(people[1]).toFixed(2)}。号码差值不参与这次比较。</p>
      <details><summary>接回模型：编号怎样查到一排数？</summary><p>教学词表把 token「书」编号为 7。模型拿 7 去嵌入表查这一行，得到示意向量 [1,0]。改编号时也要移动对应的表行；向量的值由模型学习，通常不能直接读成「音乐」或「电影」。</p><a href="#token-demo">继续操作 token 查表 →</a></details>
    </div>
    <p class="embedding-feedback" aria-live="polite"></p>
    <button type="button" class="embedding-reset">重置</button>`;

  const graph = host.querySelector('#embedding-plane');
  const feedback = host.querySelector('.embedding-feedback');
  const reveal = host.querySelector('.embedding-reveal');
  const options = [...host.querySelectorAll('[data-guess]')];
  let guess;
  options.forEach(option => option.onclick = () => {
    guess = option.dataset.guess;
    options.forEach(button => button.setAttribute('aria-pressed', String(button === option)));
    if (!graph.hidden) showFeedback();
  });
  function showFeedback() {
    feedback.textContent = guess === 'unknown'
      ? '你的判断正确：只看号码无法比较兴趣。'
      : guess ? '你猜了 ' + guess + ' 号。兴趣图上，900 号离你最近。' : '兴趣图上，900 号离你最近。';
  }
  reveal.onclick = () => {
    graph.hidden = false;
    reveal.setAttribute('aria-expanded', 'true');
    showFeedback();
  };
  host.querySelector('.embedding-reset').onclick = () => {
    graph.hidden = true;
    guess = undefined;
    reveal.setAttribute('aria-expanded', 'false');
    options.forEach(button => button.setAttribute('aria-pressed', 'false'));
    feedback.textContent = '';
    reveal.focus();
  };
})();
