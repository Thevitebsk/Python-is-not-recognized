print("'Python' is not recognized")
c,p,s=input(),0,[]
while len(c)>p:
 if c[p]==";":break
 elif c[p]==":":s.append(c[p+1]);p+=1
 elif c[p]=="?"and c[p+1]=="[":
  if s[0]==s[1]:None
  else:
   while c[p]!="]":p+=1
 elif c[p]=="@":s.append(input())
 elif c[p]=="|":print(c[p+1],end="");p+=2
 p+=1
