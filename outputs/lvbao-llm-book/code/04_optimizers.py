import math
eta, b1, b2 = .1,.9,.999
sgd=adagrad=adam=acc=m=v=0.
print('step gradient SGD Adagrad Adam m_hat v_hat')
for t,g in enumerate([2.,-2.,2.,-2.],1):
    sgd -= eta*g
    acc += g*g
    adagrad -= eta*g/(math.sqrt(acc)+1e-8)
    m=b1*m+(1-b1)*g
    v=b2*v+(1-b2)*g*g
    mh=m/(1-b1**t); vh=v/(1-b2**t)
    adam -= eta*mh/(math.sqrt(vh)+1e-8)
    print(t,g,*[round(x,6) for x in [sgd,adagrad,adam,mh,vh]])
