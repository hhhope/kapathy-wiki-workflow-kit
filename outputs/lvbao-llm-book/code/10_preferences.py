import math
for gap in [-2,0,2]:
    p=1/(1+math.exp(-gap))
    print('reward gap:',gap,'P(prefer A):',round(p,6))
for alpha in [.3,.7]:
    a=alpha; b=1-alpha
    print('truth weight:',alpha,'reward A:',a,'reward B:',b)
# Assistant-only SFT labels: -100 is a conventional ignore marker here.
prompt=[0,1,2]; answer=[3,4]
labels=[-100]*len(prompt)+answer
print('labels:',labels,'effective targets:',sum(x!=-100 for x in labels))
