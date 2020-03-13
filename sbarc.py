class bridge:
 def __init__(self,height):
  self.height=height
  out=[]
  temp=[]
  import copy
  width=2*height-1
  self.width=width
  #some hard coded things for small bridges
  done=False
  if height<8:
   if height==1:
    self.data=[[1]]
   if height==2:
    self.data=[[1,1,1],[0,1,0]]
   if height==3:
    self.data=[[1,1,1,1,1],[0,1,0,1,0],[0,0,1,0,0]]
   if height==4:
    self.data=[[1,1,1,1,1,1,1],[0,1,0,1,0,1,0],[0,0,1,0,1,0,0],[0,0,0,1,0,0,0]]
   if height==5:
    self.data=[[1,1,1,1,1,1,1,1,1],[0,1,0,1,0,1,0,1,0],[0,0,1,0,0,0,1,0,0],[0,0,0,1,0,1,0,0,0],[0,0,0,0,1,0,0,0,0]]
   if height==6:
    self.data=[[1,1,1,1,1,1,1,1,1,1,1],[0,1,0,1,0,1,0,1,0,1],[0,0,1,0,1,0,1,0,1,0,0],[0,0,0,1,0,0,0,1,0,0,0],[0,0,0,0,1,0,1,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0]]
   if height==7:
    self.data=[[1,1,1,1,1,1,1,1,1,1,1,1,1],[0,1,0,1,0,1,0,1,0,1,0,1,0],[0,0,1,0,1,0,0,0,1,0,1,0,0],[0,0,0,1,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,1,0,0,0,0],[0,0,0,0,0,1,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0]]
   done=True
  if not done:
   for a in range(width):
    temp.append(0)
   for a in range(height):
    out.append(copy.copy(temp))
   for a in range(width):
    out[0][a]=1
   for a in range(1,height):
    out[a][a]=1
    out[a][width-a-1]=1
   tails=[]
   for a in range(1,width,2):
    out[1][a]=1
    if out[2][a-1]==0 and out[2][a+3]==0:
     tails.append(a+1)
   metadata=copy.deepcopy(out)
   tails.pop(0)
   tails.pop(len(tails)-1)
   if len(tails)%2==1:
    tails.pop(tails.index(height-1))
   l1=[]
   l2=[]
   for a in range(int(len(tails)/2)):
    l1.append(tails[a])
    l2.append(tails[a+int(len(tails)/2)])
   l1.reverse()
   metatotals=[]
   for a in range(2*len(l1)):
    metatotals.append(0)
   metago=[]
   for a in range(2*len(l1)):
    metago.append(0)
   for a in range(len(l1)):
    x=l1[a]
    for c in range(2):
     index=a+c*len(l1)+2
     if out[2][x-2]==0 and out[2][x+2]==0 or a==0 or a==len(l1)-1:
      cond=copy.copy([True,True,True])
      tots=copy.copy([0,0,0])
      xs=copy.copy([x,x,x])
      y=2
      while cond.count(True)>0:
       y+=1
       for b in range(3):
        if cond[b]:
         xs[b]+=b-1
         tots[b]+=1
         if out[y][xs[b]]==1:
          cond[b]=False
      go=tots.index(min(tots))-1
      if tots[0]==tots[2]:
       if go==-1 and c==0:
        go=1
      y=2
      while out[y][x]==0:
       metadata[y][x]=index
       out[y][x]=1
       y+=1
       x+=go
     x=l2[a]
     metatotals[index-2]=min(tots)
     metago[index-2]=go
   #scan portion
   change=True
   while change:
    change=False
    for a in range(len(l1)-1,-1,-1):
     x=l1[a]
     idk=x
     for c in range(2):
      index=a+c*len(l1)
      if out[2][x-2]==0 and out[2][x+2]==0 or a==0 or a==len(l1)-1:
       for y in range(height):
        for z in range(width):
         if metadata[y][z]==index+2:
          out[y][z]=0
          metadata[y][z]=0
       cond=copy.copy([True,True,True])
       tots=copy.copy([0,0,0])
       xs=copy.copy([x,x,x])
       y=2
       while cond.count(True)>0:
        y+=1
        for b in range(3):
         if cond[b]:
          xs[b]+=b-1
          tots[b]+=1
          if out[y][xs[b]]==1:
           cond[b]=False
       go=tots.index(min(tots))-1
       y=2
       if metago[index]!=go:
        change=True
        metatotals[index]=min(tots)
        metago[index]=go
       if tots[0]==tots[2]:
        if go==-1 and c==0:
         go=1
       while out[y][x]==0:
        metadata[y][x]=index+2
        out[y][x]=1
        y+=1
        x+=go
      x=l2[a]
   self.data=copy.deepcopy(out)
   self.metadata=copy.deepcopy(metadata)
 def print(self,debug=False):
  if debug:
   for b in range(5,0,-1): 
    for a in range(self.width):
     if len(str(a))>=b:
      print(str(a)[len(str(a))-b],end="")
     else:
      print(" ",end="")
    print("")
  for h in self.data:
   o=""
   for j in h:
    if j==1:
     o+="0"
    else:
     o+=" "
   print(o)
 def eff(self):
  tot=0
  for a in self.data:
   for b in a:
    tot+=b
  return int(100*(1-(tot/(self.height*self.height))))
 def amount(self):
  out=0
  for a in self.data:
   for b in a:
    out+=b
  return out
 def check(self):
  for a in range(1,self.width-1):
   for b in range(self.height-1):
    if self.data[b][a]==1:
     if self.data[b+1][a-1]==0 and self.data[b+1][a]==0 and self.data[b+1][a+1]==0:
      return False
  return True