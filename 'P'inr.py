print("'Python' is not recognized")
c,p,s=input(),0,[]
while len(c)>p:
 if c[p]==";":break
 elif c[p]==":":s.append(c[p+1]);p+=1
 elif c[p]=="\\":print(c[p+1],end="");p+=1
 elif c[p]==">":
  if s[0]==s[1]:p+=1
  else:continue
 p+=1
