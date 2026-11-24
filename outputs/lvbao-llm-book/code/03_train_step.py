from common import weather_hidden, decode, softmax
import math
h = weather_hidden()
w = [[0.]*5 for _ in range(2)]
target, eta = 2, 0.5
p = softmax(decode(h,w))
loss_before = -math.log(p[target])
grad_z = [pi-(i==target) for i,pi in enumerate(p)]
grad_w = [[hj*gz for gz in grad_z] for hj in h]
# Check the analytic gradient against a numerical central difference.
eps=1e-5
for j in range(2):
    for i in range(5):
        w[j][i]+=eps
        plus=-math.log(softmax(decode(h,w))[target])
        w[j][i]-=2*eps
        minus=-math.log(softmax(decode(h,w))[target])
        w[j][i]+=eps
        assert abs((plus-minus)/(2*eps)-grad_w[j][i])<1e-7
w = [[v-eta*g for v,g in zip(row,grad)] for row,grad in zip(w,grad_w)]
p_after = softmax(decode(h,w))
loss_after = -math.log(p_after[target])
print('hidden:', [round(x,6) for x in h])
print('dL/dlogits:', grad_z)
print('before:', round(loss_before,6), 'after:', round(loss_after,6))
print('target probability:', round(p_after[target],6))
assert loss_after < loss_before
