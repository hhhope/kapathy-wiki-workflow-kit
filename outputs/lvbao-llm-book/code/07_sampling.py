from common import softmax
for t in [.5,1.,2.]:
    p=softmax([3,2,1],t)
    print('T:',t,'p:',[round(x,6) for x in p])
p=softmax([3,2,1]); order=sorted(range(3),key=lambda i:-p[i])
kept=[]; total=0.
for i in order:
    kept.append(i); total+=p[i]
    if total>=.8: break
print('top-p=.8 retained IDs:',kept)
print('renormalized:',[round(p[i]/total,6) for i in kept])
