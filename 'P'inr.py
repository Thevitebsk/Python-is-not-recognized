print("'Python' is not recognized")
c,p,s,l,trla=input(),0,[],[],""
while len(c)>p:
 if c[p]==";":break
 elif c[p]==":":
  if c[p-1]==" ":l.append(str(c[p+1]));p+=1
  else:s.append(c[p+1]);p+=1
 elif c[p]=="?"and c[p+1]=="[":
  if s[0]==s[1]:None
  else:
   while c[p]!="]":p+=1
 elif c[p]=="@":s.append(input())
 elif c[p]=="|":print(c[p+1],end="");p+=1
 if c[p]=="j":
  trla=c[p+1]
  while 1:
   if len(c)-1==p:p=0
   if c[p-1]==trla and c[p]==":":break
   p+=1
 p+=1
