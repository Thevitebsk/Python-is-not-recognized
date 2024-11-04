print("'Python' is not recognized")
pl=int(input("Amout of lines:"));c=[];n=1;mc=""
for ic in range(pl):c.append(input(f"{n}:"));n+=1
mc=c[0];p=0
while len(c)>0:
 while len(mc)>p:
  if mc[p]=="t" and len(c)>1:print(c[p+1]);p+=1
  elif mc[p]==";":break
  p+=1
 c.pop(0)
