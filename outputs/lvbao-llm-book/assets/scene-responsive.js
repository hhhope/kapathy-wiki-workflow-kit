(() => {
  const predictions = {
    'rl-story': ['连续向右走三步，哪一步才拿到奖励？', '前两步奖励是 0，第三步到达杯子才得 10。还可以看轨迹下方的折扣回报，核对前面的动作如何获得信用。'],
    'forget-story': ['删掉一条训练记录后，右侧代表参数影响的点会变吗？', '左侧记录减少，右侧参数影响仍在。要改变模型，还需要处理训练影响并验证结果。'],
    'clip-story': ['换成飞机图，哪条文字会得到最高分？', '「飞机在天空中」应排在第一。对照高亮的矩阵行，看看变化来自切换图片还是修改文字。'],
    'convolution-story': ['窗口从左上移到右上，响应会增大还是减小？', '左上是 −1，右上是 2。把高亮的四个像素分别乘上相同位置的核权重，再加起来。'],
    'bayes-story': ['筛出出现证据 E 的人之后，计算比例的分母是多少？', '分母是 16 + 8 = 24，不是 100。保留的 24 人中有 16 人属于 H。'],
    'selftrain-story': ['只用「狗」这个错误伪标签训练一轮，预测正确性与置信度各会怎样？', '置信度会上升，答案仍然错误。打开人工核验，再比较后续更新的方向。'],
  };
  const controlSelector = 'button, input, select';

  document.querySelectorAll('main section[id$="-story"]').forEach(scene => {
    const exercise = predictions[scene.id];
    if (exercise) {
      const prompt = document.createElement('aside');
      prompt.className = 'note';
      const question = document.createElement('p');
      question.textContent = '先预测：' + exercise[0];
      const check = document.createElement('details');
      const summary = document.createElement('summary');
      summary.textContent = '操作后核对';
      const answer = document.createElement('p');
      answer.textContent = exercise[1];
      check.append(summary, answer);
      prompt.append(question, check);
      scene.before(prompt);
    }

    let previousControl;
    function rememberControl(event) {
      const control = event.target.closest(controlSelector);
      if (control === document.activeElement) {
        previousControl = {control, index: [...scene.querySelectorAll(controlSelector)].indexOf(control)};
      }
    }
    scene.addEventListener('click', rememberControl, true);
    scene.addEventListener('change', rememberControl, true);

    function update() {
      scene.querySelectorAll('svg').forEach(svg => {
        if (svg.parentElement.classList.contains('scene-diagram-scroll')) return;
        const box = document.createElement('div');
        box.className = 'scene-diagram-scroll';
        box.tabIndex = 0;
        box.setAttribute('aria-label', '教学图，可横向滚动查看');
        svg.before(box);
        box.append(svg);

        const hint = document.createElement('small');
        hint.className = 'scene-scroll-hint';
        hint.textContent = '横向滑动看完整图 ↔';
        box.after(hint);
      });
      if (previousControl && !previousControl.control.isConnected) {
        const controls = scene.querySelectorAll(controlSelector);
        const replacement = controls[previousControl.index];
        const target = replacement?.disabled
          ? [...controls].find(control => !control.disabled)
          : replacement;
        if (document.activeElement === document.body) target?.focus({preventScroll: true});
        previousControl = undefined;
      }
    }

    new MutationObserver(update).observe(scene, {childList: true});
    update();
  });
})();
