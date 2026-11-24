(() => {
  const reduce=matchMedia('(prefers-reduced-motion: reduce)');
  let serial=0;
  function mount(img) {
    const path = img.getAttribute('data-diagram-source');
    const source = path ? new URL(path, location.href) : null;
    if (source && source.origin !== location.origin) return;
    const svg=img;svg.setAttribute('role','group');
    const nodes=[...svg.querySelectorAll('.atlas-diagram-node')];if(!nodes.length)return;
    svg.querySelectorAll('path[marker-end]').forEach((path,i)=>{
      const ns='http://www.w3.org/2000/svg';
      const dot=document.createElementNS(ns,'circle');dot.setAttribute('r','3');dot.setAttribute('fill','#cbb8ff');dot.setAttribute('class','diagram-flow-dot');dot.style.filter='drop-shadow(0 0 5px #ad8bff)';
      const motion=document.createElementNS(ns,'animateMotion');motion.setAttribute('path',path.getAttribute('d'));motion.setAttribute('dur',`${2.4+i*.15}s`);motion.setAttribute('repeatCount','indefinite');dot.append(motion);svg.append(dot);
    });

    // Each embedded SVG owns its marker IDs, including when a page has several diagrams.
    const prefix=`diagram-${serial++}-`;
    svg.querySelectorAll('[id]').forEach(el=>{const old=el.id;el.id=prefix+old;svg.querySelectorAll('*').forEach(other=>{for(const attr of [...other.attributes])if(attr.value.includes(`url(#${old})`))other.setAttribute(attr.name,attr.value.replaceAll(`url(#${old})`,`url(#${prefix+old})`));});});
    const figure=img.closest('figure')||img.parentElement;
    figure.classList.add('atlas-diagram');
    const anchor=img.closest('a');
    const toolbar=document.createElement('div');toolbar.className='diagram-toolbar';
    const kicker=document.createElement('span');kicker.className='diagram-kicker';kicker.textContent='INTERACTIVE ATLAS / 图示导览';
    const actions=document.createElement('div');actions.className='diagram-actions';
    const makeButton=(label,handler)=>{const el=document.createElement('button');el.type='button';el.textContent=label;el.onclick=handler;return el;};
    let selected=0,timer=null;
    const stop=()=>{clearInterval(timer);timer=null;play.textContent='自动导览';play.setAttribute('aria-pressed','false');};
    const play=makeButton('自动导览',()=>{if(timer){stop();return;}if(selected===nodes.length-1)select(0);play.textContent='暂停';play.setAttribute('aria-pressed','true');timer=setInterval(()=>{if(selected===nodes.length-1){stop();return;}select(selected+1);},2600);});play.setAttribute('aria-pressed','false');
    const previous=makeButton('←',()=>{stop();select(Math.max(0,selected-1));});previous.setAttribute('aria-label','上一个图示节点');
    const next=makeButton('→',()=>{stop();select(Math.min(nodes.length-1,selected+1));});next.setAttribute('aria-label','下一个图示节点');
    actions.append(previous,play,next);toolbar.append(kicker,actions);
    const viewport=document.createElement('div');viewport.className='diagram-viewport';viewport.tabIndex=0;viewport.setAttribute('aria-label','交互图示，可横向滚动');
    const tabs=document.createElement('div');tabs.className='diagram-tabs';tabs.setAttribute('aria-label','选择图示节点');
    const detail=document.createElement('div');detail.className='diagram-detail';detail.setAttribute('aria-live','polite');
    const status=document.createElement('span');status.className='diagram-status';
    const title=document.createElement('strong'),description=document.createElement('p');detail.append(status,title,description);
    const data=nodes.map(node=>node.dataset.title ? [node.dataset.title, node.dataset.detail] : [...node.querySelectorAll('text')].sort((a,b)=>Number(a.getAttribute('y'))-Number(b.getAttribute('y'))).map(t=>t.textContent.trim()));
    const buttons=data.map((texts,i)=>{const button=makeButton(String(i+1).padStart(2,'0')+' '+texts[0],()=>{stop();select(i);});tabs.append(button);return button;});
    tabs.addEventListener('keydown', event => {
      const current = buttons.indexOf(event.target);
      if (current < 0) return;
      const target = {
        ArrowLeft: Math.max(0, current - 1),
        ArrowRight: Math.min(buttons.length - 1, current + 1),
        Home: 0,
        End: buttons.length - 1,
      }[event.key];
      if (target === undefined) return;
      event.preventDefault();
      stop();
      select(target);
      buttons[target].focus({preventScroll: true});
    });
    function select(index){
      selected=index;
      nodes.forEach((node,i)=>{node.classList.toggle('is-selected',i===index);node.setAttribute('aria-pressed',String(i===index));});
      buttons.forEach((button,i)=>button.setAttribute('aria-pressed',String(i===index)));
      status.textContent=`EXPLORE ${String(index+1).padStart(2,'0')} / ${String(nodes.length).padStart(2,'0')}`;
      title.textContent=data[index][0];description.textContent=data[index].slice(1).join(' · ')||'查看此节点与图中其他部分的连接关系。';
      if(!reduce.matches){detail.classList.remove('diagram-node-enter');void detail.offsetWidth;detail.classList.add('diagram-node-enter');}
      const focused = document.activeElement;
      previous.disabled = index === 0;
      next.disabled = index === nodes.length - 1;
      if ([previous, next].some(control => control === focused && control.disabled)) {
        buttons[index].focus({preventScroll: true});
      }
      const node=nodes[index].getBoundingClientRect(),box=viewport.getBoundingClientRect();
      if(node.left<box.left||node.right>box.right)viewport.scrollTo({left:viewport.scrollLeft+node.left-box.left-(box.width-node.width)/2,behavior:reduce.matches?'instant':'smooth'});
    }
    nodes.forEach((node,i)=>{const activate=()=>{stop();select(i);};node.addEventListener('click',activate);node.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();activate();}});});
    (anchor||img).replaceWith(toolbar,viewport,tabs,detail);viewport.append(svg);
    let caption=figure.querySelector('figcaption');if(!caption){caption=document.createElement('figcaption');figure.append(caption);}
    caption.replaceChildren(document.createTextNode('点选节点查看说明；自动导览按图示阅读顺序聚焦，不代表实时模型计算。 '));
    if (source && !document.body.classList.contains('diagram-standalone')) {
      const link = document.createElement('a');
      link.href = source.href.replace(/\.svg$/, '.html');
      link.target = '_blank';
      link.rel = 'noopener';
      link.textContent = '展开图示 ↗';
      caption.append(link);
    }
    let inView = false;
    function syncMotion() {
      const reduced = reduce.matches;
      const paused = !inView || document.hidden || reduced;
      const hadPlayFocus = document.activeElement === play;
      play.disabled = reduced;
      play.title = reduced ? '减少动态效果已开启。可手动逐节点查看。' : '';
      if (reduced && hadPlayFocus) buttons[selected].focus({preventScroll: true});
      figure.classList.toggle('diagram-motion-paused', paused);
      if (paused) {
        stop();
        svg.pauseAnimations?.();
      } else {
        svg.unpauseAnimations?.();
      }
    }
    const observer = new IntersectionObserver(([entry]) => {
      inView = entry.isIntersecting;
      syncMotion();
    });
    observer.observe(figure);
    document.addEventListener('visibilitychange', syncMotion);
    reduce.addEventListener('change', syncMotion);
    syncMotion();
    select(0);
  }
  document.querySelectorAll('svg[data-diagram-source],svg[data-atlas-inline]').forEach(mount);
})();
