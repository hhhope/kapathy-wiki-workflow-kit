const EXPERIMENTS={
 network:{title:'神经元前向传播',intro:'输入x=2，ReLU(wx+b)。改变权重，观察线性值和激活值。这里只演示一个神经元。',label:'权重 w',min:-1,max:1,step:.1,value:.5,run:w=>{const z=2*w-.2,y=Math.max(0,z);return{formula:`z=2×${w.toFixed(1)}−0.2=${z.toFixed(2)}；ŷ=max(0,z)=${y.toFixed(2)}`,result:`目标y=1，平方损失=${((y-1)**2).toFixed(4)}`,explain:'负半轴ReLU输出为0；零点的导数由具体实现选取。多层网络用链式法则传播梯度。'}}},
 loss:{title:'交叉熵与困惑度',intro:'只改变正确token的预测概率p，其他分布细节暂不展开。使用自然对数。',label:'正确token概率 p',min:.01,max:.99,step:.01,value:.5,run:p=>({formula:`L=−ln(${p.toFixed(2)})=${(-Math.log(p)).toFixed(4)}`,result:`单位置困惑度 exp(L)=${(1/p).toFixed(3)}`,explain:'正确答案被赋予的概率越低，惩罚越大；这不是对回答事实性的直接评审。'})},
 adam:{title:'Adam首步与SGD首步',intro:'固定η=0.1，β₁=0.9，β₂=0.999，m₀=v₀=0。改变首个梯度，显示偏差修正。ε=10⁻⁸。',label:'梯度 g₁',min:-5,max:5,step:.5,value:2,run:g=>{let m=.1*g,v=.001*g*g,upd=-.1*g/(Math.abs(g)+1e-8);return{formula:`m₁=${m.toFixed(4)}，v₁=${v.toFixed(4)}；m̂₁=${g.toFixed(2)}，v̂₁=${(g*g).toFixed(2)}`,result:`Adam Δθ=${upd.toFixed(4)}；SGD Δθ=${(-.1*g).toFixed(4)}`,explain:'首步非零梯度经缩放后幅度近似η。后续更新依赖整段历史，不能从首步推断整条轨迹。'}}},
 cosine:{title:'向量方向与余弦相似度',intro:'固定u=[1,0]；v是二维单位向量。改变v与横轴的夹角。',label:'夹角 θ（度）',min:0,max:180,step:5,value:45,run:a=>{let c=Math.cos(a*Math.PI/180),s=Math.sin(a*Math.PI/180);return{formula:`v=[${c.toFixed(3)}, ${s.toFixed(3)}]；cos(u,v)=${c.toFixed(3)}`,result:`当前余弦相似度=${c.toFixed(3)}（参考：0°为1，90°为0，180°为−1）`,explain:'这是几何关系。模型中相似性有没有语义价值，取决于向量如何训练；降到二维也会损失信息。'}}},
 attention:{title:'一次注意力加权',intro:'固定缩放后的分数[s,1,0]，value=[10,20,30]。改变第一个分数，观察权重与加权输出。此例不含mask。',label:'第一个匹配分数 s',min:-2,max:5,step:.25,value:2,run:s=>{const z=[s,1,0],m=Math.max(...z),e=z.map(x=>Math.exp(x-m)),sum=e.reduce((a,b)=>a+b),w=e.map(x=>x/sum),y=w.reduce((a,b,i)=>a+b*[10,20,30][i],0);return{formula:`softmax=[${w.map(x=>x.toFixed(3)).join(', ')}]`,result:`输出=Σ权重×value=${y.toFixed(3)}`,bars:w,explain:'注意力输出是信息聚合，不是挑一个最可信的事实。提高第一项分数使输出更靠近value=10。'}}},
 bayes:{title:'先验、似然与后验',intro:'固定P(E|H)=0.8、P(E|非H)=0.1，改变先验P(H)。这是一道抽象概率题，不用于诊断现实人物。',label:'先验 P(H)',min:.01,max:.99,step:.01,value:.2,run:p=>{const post=.8*p/(.8*p+.1*(1-p));return{formula:`P(H|E)=0.8×${p.toFixed(2)}/[0.8×${p.toFixed(2)}+0.1×${(1-p).toFixed(2)}]`,result:`后验=${(post*100).toFixed(2)}%`,explain:'同一份证据在不同先验下可以得到不同后验；似然也应有证据支持，不是任意填一个数。'}}},
 reward:{title:'真实正确与迎合的代理目标',intro:'A真实但不认同，得分特征[1,0]；B错误但认同，特征[0,1]。R=α×真实+(1−α)×认同。',label:'真实性权重 α',min:0,max:1,step:.05,value:.7,run:a=>({formula:`R(A)=${a.toFixed(2)}；R(B)=${(1-a).toFixed(2)}`,result:a>.5?'代理目标选择A':a<.5?'代理目标选择B':'两者并列',explain:'目标定义改变偏好的行为。这只是二维线性示意，不是真实奖励模型，也不能证明所有迎合都来自这一机制。'})},
 dropout:{title:'Dropout的期望保持',intro:'激活值6，保留概率q。inverted dropout保留时除以q，丢弃时为0。',label:'保留概率 q',min:.1,max:1,step:.05,value:.75,run:q=>({formula:`保留时输出6/q=${(6/q).toFixed(3)}；丢弃时输出0`,result:`本次保留时=${(6/q).toFixed(3)}，丢弃时=0；平均输出=6`,explain:'期望保持不等于单次结果不变；非线性后整个网络输出也不一定保持完全相同的期望。'})},
 convolution:{title:'一个卷积窗口',intro:'输入[1,2,3,4]，核[1,k]，步长1，不填充。按深度学习常见互相关约定，不反转卷积核。',label:'核的第二个权重 k',min:-2,max:2,step:.25,value:-1,run:k=>({formula:`[1+2k, 2+3k, 3+4k]`,result:`输出=[${[1+2*k,2+3*k,3+4*k].map(x=>x.toFixed(2)).join(', ')}]`,explain:'同一核在不同窗口复用参数。这个例子展示局部运算，不代表单个核就会自动识别语义。'})},
 early:{title:'早停与恢复最佳权重',intro:'固定验证损失[0.9,0.7,0.65,0.68,0.70,0.72]，越小越好。改变patience，超过数据末尾则表示尚未触发停止。',label:'允许连续不改善轮数',min:1,max:4,step:1,value:2,run:p=>{let vals=[.9,.7,.65,.68,.70,.72],best=Infinity,bestAt=0,bad=0,stop=null;for(let i=0;i<vals.length;i++){if(vals[i]<best){best=vals[i];bestAt=i+1;bad=0}else bad++;if(bad>=p){stop=i+1;break}}return{formula:`最佳检查点：第${bestAt}轮，验证损失${best}`,result:stop?`第${stop}轮后停止，并恢复第${bestAt}轮权重`:'给定6轮以内尚未触发早停',explain:'停止点和最佳检查点不同。实际实现还可能包含min_delta、评估间隔等规则，需事先约定。'}}}
};

EXPERIMENTS.temperature={title:'温度与候选token概率',intro:'固定 logits=[2,1,0]，改变T，比较同一个模型输出的采样概率。',label:'温度 T',min:.1,max:2,step:.1,value:1,run:t=>{let e=[2,1,0].map(x=>Math.exp((x-2)/t)),sum=e.reduce((a,b)=>a+b),w=e.map(x=>x/sum);return {formula:'softmax(logits/T)',result:w.map(x=>(100*x).toFixed(1)+'%').join(' / '),bars:w,explain:'温度只改变分布形状，不增加知识或事实可靠性。'}}};
const gradientLab={title:'学习率与梯度更新',intro:'L=(θ−3)²，从θ=0开始，点击按钮逐步更新。',label:'学习率 η',min:.02,max:1.1,step:.02,value:.1};
const labQuestions = {
  network: '把权重调到 0，ReLU 还会输出正数吗？',
  loss: '把正确词的概率从 0.50 调到 0.25，困惑度会变成多少？',
  adam: '把梯度从 2 增到 4，两种优化器的首步幅度都会翻倍吗？',
  cosine: '旋转到 90° 时，余弦相似度是多少？',
  attention: '提高第一项的匹配分数，加权输出会更接近哪个 Value？',
  bayes: '证据的似然保持固定，调低先验时后验会怎么变？',
  reward: '把真实性权重降到 0.5 以下，代理目标会选谁？',
  dropout: '保留概率降到 0.5，保留时输出和平均输出各是多少？',
  convolution: '把核的第二个权重调到 0，三个窗口的输出是什么？',
  early: '把容忍轮数从 2 改成 1，停止轮次和最佳轮次分别怎样变化？',
  temperature: '提高温度后，分数最低的候选会得到更多还是更少的概率？',
  gradient: '学习率为 0.10 时，更新一步后参数会往哪边走？',
  distill: '学生第一类概率调到 0.70 后，KL 散度会变成多少？',
  discount: '把折扣从 0.90 降到 0.50，当前回报会变成多少？',
  ewc: '把保护系数降到 0，最优参数更接近哪个任务？',
  contrastive: '提高困难负例分数，固定正例能分到的概率怎么变？',
  growth: '反面乘数为 0.60 时，平均乘数大于 1。对数增长也为正吗？',
  retrieval: '下调旧规则的相似度，排序与最终引用依据会一起改变吗？',
};

const drinkPriceGradient = {
  title: '学习率与饮料估价',
  intro: '沿用主课：买两杯，实付 12 元。从暂估单价 w=5 开始，先猜学习率 0.5 会不会跨过目标，再按「更新一步」。',
  label: '学习率 η', min: 0, max: 0.5, step: 0.025, value: 0.125,
};
const storyAttention = {
  title: '让「书」得到更多注意力',
  intro: '固定小红、书、其他的 Value 为 1、2、4。三项分数起初都是 0，只给「书」增加分数。',
  label: '「书」分数取指数后的值',
  min: 1, max: 4, step: 0.25, value: 2,
  run(multiplier) {
    const weights = [1, multiplier, 1].map(n => n / (multiplier + 2));
    const contributions = weights.map((weight, i) => weight * [1, 2, 4][i]);
    const sum = contributions.reduce((a, b) => a + b, 0);
    return {
      formula: '分数 [0, ln(' + multiplier + '), 0] → 取指数 [1, ' + multiplier + ', 1] → 各自除以 ' + (multiplier + 2),
      result: '加权输出 = ' + sum.toFixed(3),
      bars: weights,
      explain: '当前贡献：' + contributions.map(x => x.toFixed(3)).join(' + ') + '（显示值已舍入）。滑块为 2 时，复现主课「递了什么」的 2.25。',
    };
  },
};

function renderLab(el) {
  const key = el.dataset.lab;
  const isStoryAttention = key === 'attention' && el.dataset.attentionExample === 'book';
  const drinkGradient = key === 'gradient' && el.dataset.gradientExample === 'drink';
  const initial = drinkGradient ? 5 : 0;
  const loss = w => drinkGradient ? (2 * w - 12) ** 2 : (w - 3) ** 2;
  const derivative = w => drinkGradient ? 4 * (2 * w - 12) : 2 * (w - 3);
  const experiment = drinkGradient ? drinkPriceGradient : isStoryAttention ? storyAttention : key === 'gradient' ? gradientLab : EXPERIMENTS[key];
  if (!experiment) return;

  let theta = initial;
  let steps = 0;
  el.classList.add('atlas-calculation');
  el.innerHTML = `
    <h3>${experiment.title}</h3>
    <p>${experiment.intro}</p>
    <p class="calculation-prediction"><strong>先预测</strong> ${drinkGradient ? '从 5 元出发，哪种步长会让预测越过目标？' : isStoryAttention ? '提高「书」的分数后，加权输出会更接近哪个 Value？' : labQuestions[key]}</p>
    <label>${experiment.label} <output></output>
      <input type="range" aria-label="${experiment.label}" min="${experiment.min}" max="${experiment.max}" step="${experiment.step}" value="${experiment.value}">
    </label>
    <div class="calculation-actions">
      ${key === 'gradient' ? '<button type="button" class="step">更新一步</button>' : ''}
      <button type="button" class="pin">记录当前结果</button>
      <button type="button" class="reset">重置</button>
    </div>
    <p class="calculation-baseline" aria-live="polite" hidden></p>
    <div class="lab-result" aria-live="polite"></div>`;

  const input = el.querySelector('input');
  const output = el.querySelector('output');
  const baseline = el.querySelector('.calculation-baseline');
  const result = el.querySelector('.lab-result');
  const bookTemperature = key === 'temperature' && el.dataset.temperatureExample === 'book';
  const reimbursementReward = key === 'reward' && el.dataset.rewardExample === 'reimbursement';
  if (reimbursementReward) {
    el.querySelector('h3').textContent = '真实性与明确表态的奖励权重';
    el.querySelector('h3 + p').textContent = 'A 的真实与明确表态得分为 [1,0]，B 为 [0,1]。只调真实性的权重 α，总分按 α×真实＋(1−α)×明确表态计算。明确表态指给出无条件结论。';
  }
  if (bookTemperature) {
    el.querySelector('h3 + p').textContent = '固定前缀「小红翻开一本」。书、杂志、笔记本的分数分别是 2、1、0。只调整温度，观察候选概率。';
  }
  const barLabels = {
    attention: isStoryAttention ? ['小红', '书', '其他'] : ['Value 10', 'Value 20', 'Value 30'],
    contrastive: ['正例', '困难负例', '另一负例'],
    distill: ['学生 · 猫', '学生 · 狗', '学生 · 车'],
  };

  function update() {
    const value = Number(input.value);
    output.textContent = value.toFixed(drinkGradient ? 3 : 2);
    const snapshot = key === 'gradient' ? {
      formula: drinkGradient ? 'w新 = w旧 − η × 4(2w旧 − 12)' : 'θ新 = θ旧 − η × 2(θ旧 − 3)',
      result: drinkGradient ? `第${steps}步：单价 ${theta.toFixed(2)} 元；总价 ${(theta * 2).toFixed(2)} 元；损失 ${loss(theta).toFixed(4)}` : `第${steps}步：θ=${theta.toFixed(4)}；L=${loss(theta).toFixed(4)}`,
      explain: drinkGradient ? '先重置，再比较另一种步长；调滑块本身不会更新参数。' : value >= 1 ? '此例 η≥1 时不收敛。' : '更新后比较参数离 3 的距离。',
    } : experiment.run(value);
    if (reimbursementReward) snapshot.explain = '分数越偏重无条件表态，越容易奖励缺乏证据的回答。这里使用教学评分。';
    const bars = snapshot.bars?.map((fraction, i) => {
      const name = (bookTemperature ? ['书', '杂志', '笔记本'][i] : barLabels[key]?.[i]) || `候选 ${i + 1}`;
      const percent = (fraction * 100).toFixed(1);
      return `<div class="calculation-bar"><span>${name}</span><progress aria-label="${name}" max="100" value="${percent}"></progress><span>${percent}%</span></div>`;
    }).join('') || '';
    result.innerHTML = `<strong class="lab-answer">${snapshot.result}</strong>${bars}<pre>${snapshot.formula}</pre><p class="meta">${snapshot.explain}</p>`;
  }
  input.addEventListener('input', update);
  el.querySelector('.pin').onclick = () => {
    baseline.textContent = `对照 · ${experiment.label} ${output.textContent} · ${result.querySelector('.lab-answer').textContent}`;
    baseline.hidden = false;
  };
  el.querySelector('.reset').onclick = () => {
    input.value = experiment.value;
    theta = initial;
    steps = 0;
    baseline.hidden = true;
    update();
    input.focus({preventScroll: true});
  };
  if (key === 'gradient') {
    el.querySelector('.step').onclick = () => {
      if (Math.abs(theta) > 1e8) return;
      theta -= Number(input.value) * derivative(theta);
      steps++;
      update();
    };
  }
  update();
}
EXPERIMENTS.distill = {
  title: '让学生接近教师的猫、狗、车分布',
  intro: '沿用主课：教师固定为猫 70%、狗 20%、车 10%。只改学生对猫的预测，其余概率按狗:车 = 2:1 分配。',
  label: '学生给「猫」的概率',
  min: 0.1, max: 0.9, step: 0.05, value: 0.6,
  run(cat) {
    const teacher = [0.7, 0.2, 0.1];
    const student = [cat, (1 - cat) * 2 / 3, (1 - cat) / 3];
    const divergence = teacher.reduce((sum, probability, i) =>
      sum + probability * Math.log(probability / student[i]), 0);
    return {
      formula: 'KL(教师 || 学生) = Σ Pᵢ ln(Pᵢ / Qᵢ)',
      result: 'KL = ' + Math.max(0, divergence).toFixed(5),
      bars: student,
      explain: '教师基准：猫 70%、狗 20%、车 10%。学生三项都匹配时，KL 为 0。这里比较的是输出分布。',
    };
  },
};
EXPERIMENTS.discount={"title": "延迟回报与折扣", "intro": "最终奖励10在两次状态转移之后到达。", "label": "折扣 γ", "min": 0, "max": 1, "step": 0.05, "value": 0.9,run:v=>{return {formula:'G=γ²×10',result:'当前折现回报='+(v*v*10).toFixed(3),explain:'步数定义必须与任务一致。折扣不是对人的耐心的测量。'}}};
EXPERIMENTS.ewc={"title": "旧任务与新任务的权衡", "intro": "旧任务最佳w=1，新任务最佳w=−1，L=(w+1)²+λ(w−1)²。", "label": "保护系数 λ", "min": 0, "max": 9, "step": 0.5, "value": 3,run:v=>{let w=(v-1)/(v+1);return {formula:'w*=(λ−1)/(λ+1)',result:'w*='+w.toFixed(3)+'；旧损失='+((w-1)**2).toFixed(3)+'；新损失='+((w+1)**2).toFixed(3),explain:'增加保护可减少旧任务退化，但也可能限制新任务适应。这是EWC思路的简化示意。'}}};
EXPERIMENTS.contrastive={"title": "对比学习中的正例份额", "intro": "正例分数固定2，另一个负例固定0，改变困难负例分数。", "label": "困难负例分数", "min": -2, "max": 4, "step": 0.25, "value": 1,run:v=>{let e=[Math.exp(2),Math.exp(v),1],sum=e.reduce((a,b)=>a+b);return {formula:'P正=exp(2)/(exp(2)+exp(s负)+exp(0))',result:'正例概率='+(e[0]/sum).toFixed(4)+'；损失='+(-Math.log(e[0]/sum)).toFixed(4),bars:e.map(x=>x/sum),explain:'正例没变，负例变强仍会提高损失。假负例与真正困难负例应分开。'}}};
EXPERIMENTS.growth={"title": "算术期望与长期增长", "intro": "公平硬币，正面乘1.5，反面乘m。未加入破产退出线。", "label": "反面乘数 m", "min": 0.2, "max": 1, "step": 0.05, "value": 0.6,run:v=>{return {formula:'E乘数=(1.5+m)/2；E对数增长=(ln1.5+lnm)/2',result:'平均乘数='+((1.5+v)/2).toFixed(3)+'；对数增长='+((Math.log(1.5)+Math.log(v))/2).toFixed(4),explain:'两种均值衡量不同问题；这不是投资建议，也不意味着每条路径有限步必然归零。'}}};
EXPERIMENTS.retrieval={"title": "检索相似度与证据版本", "intro": "A为2024旧规则，B为2026新规则且已明确替代A。改变A相似度，观察排序与应答依据。", "label": "A相似度", "min": 0.1, "max": 1, "step": 0.05, "value": 0.95,run:v=>{return {formula:'B相似度固定0.85；适用性与版本独立检查',result:'相似度第一：'+(v>.85?'A（旧）':'B（新）')+'；有效依据仍为B',explain:'此例假设B明确适用且替代A。真实情况必须核对对象、有效期与替代关系，不能永远选最新文件。'}}};
document.querySelectorAll('[data-lab]').forEach(renderLab);
