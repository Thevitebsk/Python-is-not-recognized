print("'Python' is not recognized")
pl=int(input("Amout of lines:"));c=[];mc="";cp=0;print(pl);sv=[]
for ic in range(pl):c.append(input())
mc=c[0];p=0;s=0
while len(c)>0:
 while len(mc)>p:
  if mc[p]=="t":print(c[int(mc[p+1])]);p+=1
  elif mc[p]==";":s=1;break
  elif mc[p]=="g":mc=c[p];p=-1
  p+=1
 if s==1:break
 sv.append(c.pop(0))
 if len(c)>0:mc=c[0];p=0
