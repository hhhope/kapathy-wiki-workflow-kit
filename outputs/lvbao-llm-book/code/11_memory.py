for lam in [0,1,3,9]:
    w=(lam-1)/(lam+1)
    old_loss=(w-1)**2; new_loss=(w+1)**2
    print('protection:',lam,'w:',round(w,4),'old loss:',round(old_loss,4),'new loss:',round(new_loss,4))
# Parameter rounding can erase some very small edits; this is a toy example.
original=1.234; edited=1.231
print('before quantization:',original,edited)
print('rounded to 2 decimal places:',round(original,2),round(edited,2))
