# A deterministic retrieval illustration; this does not call a language model.
docs=[{'id':'A','year':2024,'limit':100,'score':.95},
      {'id':'B','year':2026,'limit':200,'score':.85}]
ranked=sorted(docs,key=lambda x:-x['score'])
print('highest similarity:',ranked[0]['id'])
# In this toy setting both policies apply to the same subject and the latest supersedes.
applicable=max(docs,key=lambda x:x['year'])
print('answer with version condition:',applicable['limit'],'source:',applicable['id'],'year:',applicable['year'])
assert applicable['id']=='B'
