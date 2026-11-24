validation=[.9,.7,.65,.68,.70,.72]
best=float('inf'); best_epoch=0; bad=0
patience=2; min_delta=.01
for epoch,loss in enumerate(validation,1):
    if loss < best-min_delta:
        best=loss; best_epoch=epoch; bad=0
    else:
        bad+=1
    if bad>=patience:
        print('stop at:',epoch,'restore:',best_epoch,'loss:',best)
        break
q=.75; a=6.
print('dropout retained:',a/q,'expected:',q*(a/q)+(1-q)*0)
assert best_epoch==3
