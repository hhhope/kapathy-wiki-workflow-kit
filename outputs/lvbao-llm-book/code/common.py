"""Shared numerical helpers for the book. Python standard library only."""
import math

VOCAB = ['今天', '天气', '很', '好', '<结束>']
E = [[1., 0.], [0., 1.], [1., 1.], [-1., 1.], [0., 0.]]

def softmax(xs, temperature=1.):
    if temperature <= 0:
        raise ValueError('temperature must be positive')
    z = [x / temperature for x in xs]
    m = max(z)
    ex = [math.exp(x - m) for x in z]
    return [v / sum(ex) for v in ex]

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def attention(query, keys, values):
    scores = [dot(query, key) / math.sqrt(len(query)) for key in keys]
    weights = softmax(scores)
    output = [sum(w*v[j] for w, v in zip(weights, values))
              for j in range(len(values[0]))]
    return scores, weights, output

def weather_hidden():
    # Identity Q/K/V projections; query is the last token, “天气”.
    _, _, out = attention(E[1], E[:2], E[:2])
    return [out[j] + E[1][j] for j in range(2)]

def decode(hidden, weights):
    return [sum(hidden[j]*weights[j][i] for j in range(len(hidden)))
            for i in range(len(VOCAB))]

if __name__ == '__main__':
    assert abs(sum(softmax([3,2,1]))-1)<1e-12
    print('common helpers OK')
