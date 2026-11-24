prior=.2; lik_h=.8; lik_not=.1
posterior=lik_h*prior/(lik_h*prior+lik_not*(1-prior))
print('posterior:',round(posterior,6))
for propensity in [.2,.8,0.]:
    print('propensity:',propensity,'IPS weight:',1/propensity if propensity else 'undefined')
# Identical evidence is not an independent second observation.
print('one observation posterior remains:',round(posterior,6))
