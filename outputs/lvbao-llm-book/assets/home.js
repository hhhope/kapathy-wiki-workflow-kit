(() => {
  const slider = document.querySelector('#temperature');
  if (!slider) return;
  const baseline = temperatureDistribution(1);
  const rows = document.querySelectorAll('.probabilities > div');
  const temperature = document.querySelector('#temp-value');
  const comparison = document.querySelector('#temperature-comparison');

  function refresh(announce) {
    const value = Number(slider.value);
    const probabilities = temperatureDistribution(value).map(item => item.probability);
    temperature.textContent = value.toFixed(1);
    rows.forEach((row, i) => {
      row.querySelector('b').style.width = probabilities[i] + '%';
      row.querySelector('output').textContent = probabilities[i].toFixed(1) + '%';
    });
    const last = probabilities[2].toFixed(1);
    const direction = value > 1 ? '升到' : '降到';
    if (announce) {
      comparison.textContent = value === 1
        ? 'T=1 对照：' + baseline.map(item => item.name + ' ' + item.probability.toFixed(1) + '%').join('，') + '。'
        : `对照 T=1：「笔记本」从 ${baseline[2].probability.toFixed(1)}% ${direction} ${last}%。`;
    }
  }
  slider.addEventListener('input', () => refresh(false));
  slider.addEventListener('change', () => refresh(true));
  document.querySelector('#temperature-reset').onclick = () => {
    slider.value = 1;
    refresh(true);
  };
  refresh(true);
})();
(()=>{const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;const aurora=document.createElement('div');aurora.className='aurora';document.body.prepend(aurora);const canvas=document.createElement('canvas');canvas.id='starfield';canvas.setAttribute('aria-hidden','true');document.body.prepend(canvas);const ctx=canvas.getContext('2d');let w,h,stars=[],frame;function size(){w=innerWidth;h=innerHeight;const d=Math.min(devicePixelRatio||1,2);canvas.width=w*d;canvas.height=h*d;ctx.setTransform(d,0,0,d,0,0);stars=Array.from({length:w<650?30:65},()=>({x:Math.random()*w,y:Math.random()*h,r:Math.random()*1.2+.3,s:Math.random()*.18+.04}))}function draw(){ctx.clearRect(0,0,w,h);for(const p of stars){ctx.beginPath();ctx.fillStyle='rgba(164,156,220,.38)';ctx.arc(p.x,p.y,p.r,0,7);ctx.fill();if(!reduce){p.y-=p.s;if(p.y<0)p.y=h}}if(!reduce&&!document.hidden)frame=requestAnimationFrame(draw)}addEventListener('resize',()=>{size();if(reduce)draw()});document.addEventListener('visibilitychange',()=>{cancelAnimationFrame(frame);if(!document.hidden)draw()});size();draw();document.querySelectorAll('.extension-grid>a').forEach(card=>card.addEventListener('pointermove',e=>{const r=card.getBoundingClientRect();card.style.setProperty('--mx',e.clientX-r.left+'px');card.style.setProperty('--my',e.clientY-r.top+'px')}));})();
