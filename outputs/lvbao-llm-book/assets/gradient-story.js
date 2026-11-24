(() => {
  const host = document.querySelector('[data-gradient-lesson]');
  if (!host) return;
  const local = host.dataset.gradientLesson === '9';
  const loss = w => (2 * w - 12) ** 2;
  const slope = w => 4 * (2 * w - 12);
  const initial = 5;
  const options = local ? [4.99, 5, 5.01] : [0.05, 0.125, 0.5];

  host.innerHTML = `
    <div class="diagram-toolbar"><span class="diagram-kicker">INTERACTIVE ATLAS / ${local ? '局部梯度' : '更新路径'}</span></div>
    <h2>${local ? '把单价调高一点，误差会变小吗？' : '方向相同，迈多远才合适？'}</h2>
    <p>买两杯饮料，实际付了 12 元。模型暂估每杯 5 元，预测总价为 10 元。预测差了 2 元，平方损失为 4。</p>
    <p>${local ? '先猜单价往哪边调会减损，再试 5 元左右的三个点。' : '先猜哪一步会跨过最低点，再比较三个步长。每次都从 5 元开始。'}</p>
    <div class="example-controls" aria-label="${local ? '选择试探单价' : '选择学习率'}">
      ${options.map((value,i) => `<button type="button" data-step="${i}" aria-pressed="false">${local ? value.toFixed(2) + ' 元' : '学习率 ' + value}</button>`).join('')}
      <button type="button" class="gradient-reset">重置</button>
    </div>
    <div class="gradient-plot"></div>
    <div class="example-result" aria-live="polite"></div>
    <details class="gradient-math"><summary>核对公式</summary><p>损失 L(w)=(2w−12)²。对单价求导：L′(w)=4(2w−12)。w=5 时 L′(w)=−8，因此在该点稍往右，损失会下降。更新公式 w新 = w旧 − 学习率 × L′(w旧)。</p></details>
    ${local ? '' : '<details class="gradient-terrain"><summary>换一张有两个低点的地形</summary><p>先猜：两个起点的坡度都指向右边，最后会到同一个低点吗？</p><div class="example-controls"><button type="button" data-terrain="left" aria-pressed="false">从左侧出发</button><button type="button" data-terrain="right" aria-pressed="false">从中间出发</button></div><div class="terrain-plot"></div><p class="terrain-result" aria-live="polite"></p></details>'}`;

  const plot = host.querySelector('.gradient-plot');
  const result = host.querySelector('.example-result');
  const controls = [...host.querySelectorAll('[data-step]')];

  function draw(container, f, limits, from, to, axis, trajectory = [from, to]) {
    const [x0, x1, y0, y1] = limits;
    const px = x => 44 + (x - x0) * 330 / (x1 - x0);
    const py = y => 170 - (y - y0) * 143 / (y1 - y0);
    const point = x => px(x) + ' ' + py(f(x));
    const curve = Array.from({length: 61}, (_, i) => point(x0 + (x1 - x0) * i / 60)).join(' L');
    const changed = from !== to;
    container.innerHTML = `<svg viewBox="0 0 420 212" role="img" aria-label="${axis}，从 ${from} 比较到 ${to}，损失 ${f(to).toFixed(4)}">
      <path class="gradient-axis" d="M44 22V170H385"/>
      <text x="12" y="20">损失</text><text x="285" y="201">${axis}</text>
      <text x="44" y="188">${x0}</text><text x="365" y="188">${x1}</text>
      <path class="gradient-curve" d="M${curve}"/>
      ${changed ? `<path class="gradient-step-line" pathLength="1" d="M${trajectory.map(point).join(' L')}"/>` : ''}
      <circle class="gradient-origin" cx="${px(from)}" cy="${py(f(from))}" r="5"/>
      ${changed ? `<circle class="gradient-destination" cx="${px(to)}" cy="${py(f(to))}" r="6"/>` : ''}
    </svg>`;
  }

  function render(index) {
    const option = options[index];
    const destination = option === undefined ? initial : local ? option : initial - option * slope(initial);
    controls.forEach((button, i) => button.setAttribute('aria-pressed', String(i === index)));
    draw(plot, loss, local ? [4.98, 5.02, 3.8, 4.2] : [4.6, 9.2, 0, 42], initial, destination, local ? '单价（局部放大）' : '单价');
    result.textContent = option === undefined
      ? '起点：单价 5 元，损失 4。'
      : `单价 ${destination.toFixed(local ? 2 : 1)} 元 · 预测 ${(2 * destination).toFixed(2)} 元 · 损失 ${loss(destination).toFixed(4)}。` +
        (!local && destination > 6 ? '这一步跨过最低点，损失反而增加。' : '');
  }

  controls.forEach((button, i) => button.onclick = () => render(i));
  host.querySelector('.gradient-reset').onclick = () => { render(-1); host.querySelector('.gradient-math').open = false; controls[0].focus(); };
  render(-1);

  const terrain = host.querySelector('.gradient-terrain');
  if (!terrain) return;
  const landscape = x => (x * x - 1) ** 2 + 0.25 * (x ** 3 / 3 - x) + 0.2;
  const terrainSlope = x => (x * x - 1) * (4 * x + 0.25);
  const terrainButtons = [...terrain.querySelectorAll('button')];
  terrainButtons.forEach((button, i) => button.onclick = () => {
    const start = i === 0 ? -1.4 : 0;
    let end = start;
    const trajectory = [start];
    for (let step = 0; step < 60; step++) {
      end -= 0.05 * terrainSlope(end);
      trajectory.push(end);
    }
    terrainButtons.forEach((item, n) => item.setAttribute('aria-pressed', String(n === i)));
    draw(terrain.querySelector('.terrain-plot'), landscape, [-1.5, 1.5, 0, 2], start, end, '参数位置', trajectory);
    terrain.querySelector('.terrain-result').textContent = `起点 ${start}，初始梯度 ${terrainSlope(start).toFixed(3)}，都向右更新。60 步后约到 ${end.toFixed(2)}，损失约 ${landscape(end).toFixed(3)}。`;
  });
  function resetTerrain() {
    terrain.open = false;
    terrainButtons.forEach(button => button.setAttribute('aria-pressed', 'false'));
    terrain.querySelector('.terrain-result').textContent = '';
    draw(terrain.querySelector('.terrain-plot'), landscape, [-1.5, 1.5, 0, 2], -1.4, -1.4, '参数位置');
  }
  host.querySelector('.gradient-reset').addEventListener('click', resetTerrain);
  resetTerrain();
})();
