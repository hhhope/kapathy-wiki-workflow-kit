(() => {
  const main = document.querySelector('body > main');
  if (!main) return;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const title = main.querySelector(':scope > h1');
  if (title) {
    const hero = document.createElement('section'); hero.className = 'atlas-hero';
    title.before(hero);
    const eyebrow = hero.previousElementSibling;
    if (eyebrow?.classList.contains('eyebrow')) hero.append(eyebrow);
    const label = document.createElement('div'); label.className = 'atlas-hero-label';
    label.textContent = 'LLM ATLAS / EXPLORE THE MODEL'; hero.append(label, title);
    const signal = document.createElement('div'); signal.className = 'atlas-signal'; signal.setAttribute('aria-hidden','true');
    for(let i=0;i<22;i++) { const bar=document.createElement('i'); bar.style.setProperty('--h',`${8+Math.sin(i*.7)**2*24}px`);bar.style.setProperty('--delay',`${-i*.13}s`);signal.append(bar); }
    hero.append(signal);
  }
  if (reduce.matches) return;
  const aurora=document.createElement('div');aurora.className='atlas-aurora';aurora.setAttribute('aria-hidden','true');document.body.prepend(aurora);
  const canvas=document.createElement('canvas');canvas.id='atlas-cosmos';canvas.setAttribute('aria-hidden','true');document.body.prepend(canvas);
  const ctx=canvas.getContext('2d');
  let width=0,height=0,stars=[],frame=0,last=0;
  const resize=()=>{width=innerWidth;height=innerHeight;const d=Math.min(devicePixelRatio||1,2);canvas.width=width*d;canvas.height=height*d;ctx?.setTransform(d,0,0,d,0,0);stars=Array.from({length:width<760?30:65},()=>({x:Math.random()*width,y:Math.random()*height,r:.4+Math.random(),v:.025+Math.random()*.035,phase:Math.random()*6.28}));};
  const draw=time=>{
    if(!ctx)return;
    const delta=Math.min(time-last||16,40);last=time;ctx.clearRect(0,0,width,height);
    for(const p of stars){p.y-=p.v*delta;if(p.y<0)p.y=height;ctx.beginPath();ctx.fillStyle=`rgba(179,167,232,${.18+.17*(1+Math.sin(time*.0006+p.phase))/2})`;ctx.arc(p.x,p.y,p.r,0,Math.PI*2);ctx.fill();}
    for(let i=0;i<stars.length;i++)for(let j=i+1;j<stars.length;j++){const a=stars[i],b=stars[j],distance=Math.hypot(a.x-b.x,a.y-b.y);if(distance<115){ctx.strokeStyle=`rgba(139,117,210,${(1-distance/115)*.1})`;ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();}}
    frame=requestAnimationFrame(draw);
  };
  const resume=()=>{cancelAnimationFrame(frame);if(!document.hidden&&!reduce.matches)frame=requestAnimationFrame(draw);};
  resize();resume();addEventListener('resize',resize);document.addEventListener('visibilitychange',resume);reduce.addEventListener('change',resume);
  // Keep instructional content visible, including when reached by a hash link or Tab.
})();
