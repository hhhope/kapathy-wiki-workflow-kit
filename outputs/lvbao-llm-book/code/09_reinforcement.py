gamma=.9
print('two-step discounted final reward:',gamma**2*10)
reward=1.; q_next=[2.,10.]
print('max-based Bellman target:',reward+gamma*max(q_next))
print('if unsupported action is excluded:',reward+gamma*q_next[0])
# A potential shaping sum telescopes under discounted accounting.
potential=[1.,2.,4.]
fs=[gamma*potential[i+1]-potential[i] for i in range(2)]
print('discounted shaping:',fs[0]+gamma*fs[1])
print('boundary term:',-potential[0]+gamma**2*potential[-1])
