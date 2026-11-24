from common import softmax
import math
scores=[[2.,1.,0.],[0.,2.,1.],[1.,0.,2.]]
rows=[softmax(row) for row in scores]
cols=[softmax(list(col)) for col in zip(*scores)]
row_loss=sum(-math.log(rows[i][i]) for i in range(3))/3
col_loss=sum(-math.log(cols[i][i]) for i in range(3))/3
print('image-to-text loss:',round(row_loss,6))
print('text-to-image loss:',round(col_loss,6))
print('symmetric loss:',round((row_loss+col_loss)/2,6))
