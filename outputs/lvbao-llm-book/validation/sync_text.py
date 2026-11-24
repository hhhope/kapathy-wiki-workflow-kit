"""Rebuild the static reading companion from the current visible course HTML."""
from pathlib import Path
from html.parser import HTMLParser
import re
root=Path(__file__).resolve().parents[1]
class Reader(HTMLParser):
 def __init__(self):super().__init__();self.active=False;self.out=[];self.links=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='main':self.active=True
  if not self.active:return
  if t in ('h1','h2','h3','h4'):self.out.append('\n\n'+'#'*int(t[1])+' ')
  elif t in ('p','tr','li','div','figure'):self.out.append('\n\n')
  elif t in ('td','th'):self.out.append(' | ')
  elif t=='a':self.links.append(a.get('href',''));self.out.append('[')
  elif t=='img':self.out.append('!['+a.get('alt','图示')+']('+a.get('src','')+')')
  elif t=='iframe':self.out.append('[原视频播放器]('+a.get('src','')+')')
  elif t=='pre':self.out.append('\n\n```text\n')
 def handle_endtag(self,t):
  if t=='main':self.active=False
  if not self.active:return
  if t=='a' and self.links:self.out.append(']('+self.links.pop()+')')
  elif t=='pre':self.out.append('\n```\n')
 def handle_data(self,d):
  if self.active:self.out.append(d)
parts=['# 从零理解LLM · 14课与6个扩展专题\n\n与当前课页同步的静态文字版。图可在网页放大；实验的计算过程与动态状态请打开各课操作。材料为教学改写，不是33集逐字转录。']
for p in sorted((root/'course').glob('*.html')):
 if not (p.stem.isdigit() or p.stem.startswith('extension-')):continue
 reader=Reader();reader.feed(p.read_text());parts.append('[打开本课]('+p.name+')\n\n'+re.sub(r'\n{3,}','\n\n',''.join(reader.out)))
(root/'course/全文.md').write_text('\n\n---\n\n'.join(parts)+'\n')
print('Synchronized 20 teaching pages to course/全文.md')
