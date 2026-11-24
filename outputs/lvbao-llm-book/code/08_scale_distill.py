import math
compute=6*1_000_000*20_000_000
for n in [500_000,1_000_000,2_000_000]:
    print('N:',n,'D under same compute:',int(compute/(6*n)))
teacher=[.7,.2,.1]; student=[.6,.3,.1]
kl=sum(p*math.log(p/q) for p,q in zip(teacher,student))
print('KL(teacher || student):',round(kl,6))
assert kl>=0
