import math
up,down=1.5,.6
arithmetic=(up+down)/2
log_growth=(math.log(up)+math.log(down))/2
print('expected one-step multiplier:',arithmetic)
print('one-up-one-down multiplier:',up*down)
print('expected log growth:',round(log_growth,6))
assert arithmetic>1 and log_growth<0
# Two functions match the same two observations but extrapolate differently.
for x in [0,1,2]:
    linear=x; alternative=x+2*x*(x-1)
    print('x:',x,'f:',linear,'g:',alternative)
