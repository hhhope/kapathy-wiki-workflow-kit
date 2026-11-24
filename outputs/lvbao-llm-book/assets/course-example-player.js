(() => {
  const host = document.querySelector('[data-course-example]');
  if (!host) return;
  const lesson = Number(host.dataset.courseExample);
  const [question, prediction, states] = courseExamples[lesson - 1];
  // Labels and values follow the calculations in course-examples.js.
  const distributions = {
    4: [1, 2].map(t => temperatureDistribution(t).map(item => [item.name, Number(item.probability.toFixed(1))])),
    5: [[['今天',25],['天气',50],['很',25]]],
    12: [[['猫',100],['狗',0],['车',0]], [['猫',70],['狗',20],['车',10]]],
  };

  function drawStructure(index) {
    const visual = element('div', '');
    visual.className = 'example-structure';
    if (lesson === 2) {
      const tokens = [['今天', 7], ['天气', 12], ['很', 5]];
      if (index === 1) [tokens[0], tokens[1]] = [tokens[1], tokens[0]];
      tokens.forEach(([token, id], position) => {
        const cell = element('div', '');
        cell.className = 'example-tile';
        cell.append(element('small', '位置 ' + (position + 1)), element('strong', token), element('span', '查嵌入表第 ' + id + ' 行'));
        visual.append(cell);
      });
    }
    if (lesson === 3) {
      const rule = interestRules[index];
      const ranked = [...interestCandidates].sort((a, b) => interestScore(b, rule) - interestScore(a, rule));
      ranked.forEach((person, i) => {
        const score = interestScore(person, rule);
        const cell = tile(i === 0 ? '本轮领先' : '本轮第二', person.name + ' · ' + score + ' 分');
        const meter = element('progress', '');
        meter.max = 10;
        meter.value = score;
        meter.setAttribute('aria-label', person.name + '的匹配分');
        cell.append(meter, element('span', person.scores.map((v, dimension) =>
          (dimension ? '电影 ' : '音乐 ') + v + ' × ' + rule.weights[dimension]).join(' ＋ ')));
        if (i === 0) cell.classList.add('example-tile-new');
        visual.append(cell);
      });
    }
    if (lesson === 5) {
      const tokens = ['今天', '天气', '很'];
      [0.25, 0.5, 0.25].forEach((weight, i) => {
        const value = [1, 2, 4][i];
        visual.append(tile(tokens[i] + ' · Value ' + value, weight + ' × ' + value + ' = ' + weight * value));
      });
    }
    if (lesson === 6) {
      if (index === 0) {
        visual.append(tile('人物线索 · 小红', '[2]'), tile('物品线索 · 书', '[3]'), tile('并排保留两路线索', '[2, 3]'));
      } else {
        visual.append(tile('人物通道的贡献', '2 × 1 = 2'), tile('物品通道的贡献', '3 × 2 = 6'), tile('合成输出', '2 + 6 = 8'));
      }
    }
    if (lesson === 7) {
      const widths = index === 0 ? [4, 4] : [4, 8, 4];
      const labels = index === 0 ? ['输入', '注意力输出'] : ['输入', 'FFN 中间层', '投影后'];
      widths.forEach((width, i) => {
        const tile = element('div', '');
        tile.className = 'example-tile';
        const matrix = element('div', '');
        matrix.className = 'example-matrix';
        matrix.style.setProperty('--columns', width);
        matrix.setAttribute('aria-hidden', 'true');
        for (let cell = 0; cell < 3 * width; cell++) matrix.append(element('i', ''));
        tile.append(element('small', labels[i]), matrix, element('span', '3 个位置 × ' + width + ' 维'));
        visual.append(tile);
      });
    }
    if (lesson === 8) {
      const tokens = index === 0 ? ['今天', '天气', '很'] : ['今天', '天气', '很', '好'];
      tokens.forEach((token, i) => {
        const tile = element('div', '');
        tile.className = 'example-tile';
        if (i === 3) tile.classList.add('example-tile-new');
        tile.append(element('strong', token), element('span', index === 0 ? '保存 K/V' : i === 3 ? '新算 K/V' : '复用 K/V'));
        visual.append(tile);
      });
    }
    if ([9, 10, 11].includes(lesson)) {
      return drawTraining(index);
    }
    if (lesson === 13) {
      const examples = index === 0
        ? [['示范摘要', '周五 15:00 在 302 室开项目会。']]
        : [['更受偏好', '周五 15:00 在 302 室开项目会。'], ['较不受偏好', '周五 15:00 开项目会。']];
      examples.forEach(([label, text]) => visual.append(tile(label, text)));
    }
    if (lesson === 14) {
      const notices = [['旧草稿', '周三截止'], ['当前公告', '周五截止']];
      notices.forEach(([label, text], i) => {
        const card = tile(label, text);
        if (i === index) card.classList.add('example-tile-new');
        visual.append(card);
      });
      visual.append(element('p', index === 0 ? '当前查看：旧草稿，不能作为最终引用。' : '引用当前公告，回答「周五截止」。'));
    }
    return visual;
  }

  function tile(label, text) {
    const card = element('div', '');
    card.className = 'example-tile';
    card.append(element('small', label), element('strong', text));
    return card;
  }

  function drawTraining(index) {
    const chart = element('div', '');
    chart.className = 'example-bars';
    const rows = lesson === 11
      ? [['训练损失', index ? 0.15 : 0.30], ['验证损失', index ? 0.55 : 0.40]]
      : [['目标总价', 12], ['更新前预测', 10], ...(lesson === 10 || index ? [['更新后预测', lesson === 10 && index ? 18 : 12]] : [])];
    const limit = lesson === 11 ? 1 : 20;
    for (const [label, value] of rows) {
      const row = element('div', '');
      const bar = element('progress', '');
      bar.max = limit;
      bar.value = value;
      bar.setAttribute('aria-label', label);
      row.append(element('span', label), bar, element('span', lesson === 11 ? value.toFixed(2) : value + ' 元'));
      chart.append(row);
    }
    return chart;
  }

  function drawValue(value, index) {
    if ([2, 3, 6, 7, 8, 9, 10, 11, 13, 14].includes(lesson) || (lesson === 5 && index === 1)) {
      const visual = element('div', '');
      visual.append(drawStructure(index), element('p', value));
      return visual;
    }
    const visual = element('div', '');
    const bars = distributions[lesson]?.[index];
    visual.className = bars ? 'example-bars' : 'example-signal';
    if (bars) {
      for (const [name, percent] of bars) {
        const row = element('div', '');
        const meter = element('progress', '');
        meter.max = 100;
        meter.value = percent;
        meter.setAttribute('aria-label', name);
        row.append(element('span', name), meter, element('span', percent + '%'));
        visual.append(row);
      }
    } else {
      const parts = value.split(/\s+(?:→|=)\s+/);
      parts.forEach((part, i) => {
        if (i) visual.append(element('span', '→'));
        visual.append(element('strong', part));
      });
    }
    if (lesson !== 4) return visual;
    const wrapper = element('div', '');
    wrapper.append(visual);
    const steps = temperatureDistribution(index + 1);
    const stages = [
      ['第一步：看分数', item => item.logit + ' ÷ ' + (index + 1) + ' = ' + item.scaled],
      ['第二步：取指数', item => 'exp(' + item.scaled + ') ≈ ' + item.exponential.toFixed(3)],
      ['第三步：除以总和', item => item.exponential.toFixed(3) + ' ÷ ' +
        steps.reduce((sum, row) => sum + row.exponential, 0).toFixed(3) + ' ≈ ' + item.probability.toFixed(1) + '%'],
    ];
    for (const [label, describe] of stages) {
      const details = element('details', '');
      details.append(element('summary', label));
      const list = element('ul', '');
      for (const item of steps) list.append(element('li', item.name + '：' + describe(item)));
      details.append(list);
      wrapper.append(details);
    }
    return wrapper;
  }
  function element(tag, text) {
    const node = document.createElement(tag);
    node.textContent = text;
    return node;
  }
  const toolbar = element('div', '');
  toolbar.className = 'diagram-toolbar';
  const label = element('span', '交互图示');
  label.className = 'diagram-kicker';
  toolbar.append(label);
  const heading = element('h2', question);
  const controls = element('div', '');
  controls.className = 'example-controls';
  const result = element('div', '');
  result.className = 'example-result';
  result.setAttribute('aria-live', 'polite');
  const buttons = states.map(([label, value, explanation], index) => {
    const button = element('button', label);
    button.type = 'button';
    button.setAttribute('aria-pressed', 'false');
    button.onclick = () => {
      buttons.forEach((candidate, i) => candidate.setAttribute('aria-pressed', String(i === index)));
      const snapshot = element('div', '');
      snapshot.append(drawValue(value, index), element('p', explanation));
      result.replaceChildren(snapshot);
    };
    controls.append(button);
    return button;
  });
  function showPrediction() {
    buttons.forEach(button => button.setAttribute('aria-pressed', 'false'));
    result.replaceChildren(element('p', '先想一想，再选择上方的状态核对。'));
  }

  const reset = element('button', '重置实验');
  reset.type = 'button';
  reset.onclick = () => {
    showPrediction();
    buttons[0].focus({preventScroll: true});
  };
  controls.append(reset);
  showPrediction();
  host.append(toolbar, heading, element('p', prediction), controls, result);
})();
