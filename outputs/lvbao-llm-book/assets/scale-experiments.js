(() => {
  const root = document.querySelector('#scale-experiments');
  if (!root) return;

  const budgets = [[20, 5], [10, 10], [5, 20]];
  const labels = ['猫', '狗', '车'];
  const supervision = [[100, 0, 0], [70, 20, 10]];
  const completed = [2, 3, 4];
  const bar = (label, value, max, suffix = '') => `
    <div><span>${label}</span><progress aria-label="${label}" value="${value}" max="${max}"></progress><span>${value}${suffix}</span></div>`;

  const experiments = [
    {
      title: '训练预算相同，怎么分给模型和数据？',
      task: '先猜：参数翻倍时，为了保持这笔预算不变，数据量要增还是要减？',
      choices: budgets.map(([n, d]) => `参数 ${n}／数据 ${d}`),
      render(i) {
        const [n, d] = budgets[i];
        return `<div class="example-bars">${bar('参数量 N', n, 20)}${bar('数据量 D', d, 20)}</div><p><strong>${n} × ${d} = ${n * d} 预算单位</strong></p><p>此处用 N×D 近似比较训练计算。三组用掉同样预算；谁学得更好还要看验证损失。</p>`;
      },
    },
    {
      title: '同一张猫图，老师多告诉了学生什么？',
      task: '先猜：只告诉学生正确类别，它还能不能看出狗比车更容易混淆？',
      choices: ['只给正确标签', '给教师分布'],
      render(i) {
        return `<div class="example-bars">${supervision[i].map((p, j) => bar(labels[j], p, 100, '%')).join('')}</div><p>${i ? '教师给狗 20%、车 10%，学生看到了教师怎样区分两个错误候选。' : '只给猫 100%，狗与车都是 0%，没有提供教师对两种错误候选的比较。'}</p>`;
      },
    },
    {
      title: '同一批作答，能力突然出现了吗？',
      task: '三种规模的模型做同一道四步题，依次答对 2、3、4 步。先猜：改成整题全对才得分，分数曲线会怎样？',
      choices: ['按步骤计分', '整题全对才计分'],
      render(i) {
        const scores = completed.map(steps => i ? (steps === 4 ? 100 : 0) : steps * 25);
        return `<div class="scale-step-grid">${completed.map((steps, j) => `<div><span>模型 ${j + 1} · 对 ${steps}/4 步</span><span aria-hidden="true">${Array.from({length:4}, (_, k) => k < steps ? '●' : '○').join(' ')}</span></div>`).join('')}</div><div class="example-bars">${scores.map((score,j) => bar('模型 ' + (j + 1), score, 100, '%')).join('')}</div><p>${i ? '整题指标显示 0、0、100% 的跳变，但作答内容没有变。' : '按步骤计分展示 50%、75%、100% 的渐进变化。'} 这个示例只说明评分方式会改变看到的形状。</p>`;
      },
    },
  ];

  experiments.forEach(({title,task,choices,render}) => {
    const panel = document.createElement('section');
    panel.className = 'course-example';
    panel.innerHTML = `<h2>${title}</h2><p>${task}</p><div class="example-controls"></div><div class="example-result" aria-live="polite"><p>先预测，再选一个条件核对。</p></div>`;
    const controls = panel.querySelector('.example-controls');
    const result = panel.querySelector('.example-result');
    function update(index) {
      buttons.forEach((button,i) => button.setAttribute('aria-pressed', String(i === index)));
      result.innerHTML = index < 0 ? '<p>先预测，再选一个条件核对。</p>' : '<div>' + render(index) + '</div>';
    }
    const buttons = choices.map((label,i) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.textContent = label;
      button.setAttribute('aria-pressed', 'false');
      button.onclick = () => update(i);
      controls.append(button);
      return button;
    });
    const reset = document.createElement('button');
    reset.type = 'button';
    reset.textContent = '重置';
    reset.onclick = () => { update(-1); buttons[0].focus(); };
    controls.append(reset);
    root.append(panel);
  });
})();
