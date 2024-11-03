print("'Python' is not recognized")
c,p,v=input(),0,{"n":[],"v":[]}
while len(c)>p:
 if c[p]==";":break
 elif c[p]==":":v["n"].append(c[p+1]);v["v"].append(c[p+2]);p+=2
 elif c[p]=="\\":print(c[p+1],end="");p+=1
 elif c[p]==">":continue
 p+=1
