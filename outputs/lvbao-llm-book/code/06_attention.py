from common import E, attention, weather_hidden
scores, weights, out=attention(E[1],E[:2],E[:2])
print('query:', E[1])
print('scores:',[round(x,6) for x in scores])
print('weights:',[round(x,6) for x in weights])
print('weighted value:',[round(x,6) for x in out])
print('after residual:',[round(x,6) for x in weather_hidden()])
# First position cannot attend to future “天气”.
_, first_weights, first_out=attention(E[0],E[:1],E[:1])
print('first position causal weights:',first_weights,'output:',first_out)
assert first_weights==[1.]
