print("'Python' is not recognized")
c,p,s=input(),0,[]
while len(c)>p:
 print(c[p])
 if c[p]==";":break
 elif c[p]==":":s.append(c[p+1]);p+=1
 elif c[p]=="\\":print(c[p+1],end="");p+=1
 elif c[p]=="?"and c[p+1]=="[":
  if s[0]==s[1]:
   while c[p]!="]":p+=1
  else:None
 elif c[p]=="@":s.append(input())
 p+=1
