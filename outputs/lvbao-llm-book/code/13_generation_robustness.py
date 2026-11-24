import math
for pdata, pg in [(.5,.5),(.8,.2),(.2,.8)]:
    print('ideal GAN discriminator:',pdata/(pdata+pg))
x0=2.; abar=.25; noise=1.
xt=math.sqrt(abar)*x0+math.sqrt(1-abar)*noise
print('diffusion noisy sample:',round(xt,6))
x=[.5,.5]; signs=[1,-1]; eps=.1
attacked=[min(1.,max(0.,v+eps*s)) for v,s in zip(x,signs)]
print('FGSM example:',attacked)
