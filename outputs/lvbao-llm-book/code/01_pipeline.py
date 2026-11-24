from common import VOCAB, weather_hidden, decode, softmax
import math
ids = [VOCAB.index(t) for t in ['今天', '天气']]
h = weather_hidden()
weights = [[0.]*5 for _ in range(2)]
p = softmax(decode(h, weights))
print('input IDs:', ids)
print('hidden:', [round(v,6) for v in h])
print('probabilities:', p)
print('target:', VOCAB[2], 'loss:', round(-math.log(p[2]),6))
