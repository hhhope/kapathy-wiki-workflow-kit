from common import VOCAB, E, dot
import math
ids = [VOCAB.index(t) for t in ['今天', '天气']]
print('IDs:', ids, 'embeddings:', [E[i] for i in ids])
u, v = [1,0], [1,1]
cos = dot(u,v)/math.sqrt(dot(u,u)*dot(v,v))
print('cosine:', round(cos,6))
print('scaled cosine:', round(dot(u,[10,10])/math.sqrt(200),6))
assert abs(cos-1/math.sqrt(2))<1e-12
