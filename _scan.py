import re, sys
p=r'C:\Projects\REPORTS\тексти\оші\html\Oshi Welcome Flow Updated.html'
s=open(p,'r',encoding='utf-8').read()
lines=s.split('\n')
for i,l in enumerate(lines,1):
    if re.search(r'EMAIL #|INAPP #|SMS #|DEFAULT|\(AU\)|\(CA\)|\(DE\)', l):
        print(i, l[:200])
