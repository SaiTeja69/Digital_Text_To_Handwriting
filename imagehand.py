import numpy as np
from PIL import Image

base ='fonts/'
def make_image(list1,count):
 imgs    = [ Image.open(i) for i in list1 ]
 #min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
 min_shape=(10*y,10*y)
 imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
 imgs_comb = Image.fromarray( imgs_comb)
 imgs_comb.save( str(count)+'.jpg' )  
def multiple_lines(count):
 list1=[]
 for i in range(1,count+1,1):
  z=str(i)+".jpg"
  list1.append(z)
 imgs    = [ Image.open(i) for i in list1 ]
 min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
# min_shape=(300*y,200*y)
 imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
 imgs_comb = Image.fromarray( imgs_comb)
 imgs_comb.save( 'final.jpg')
 
 
#list_im = ['Test1.jpg', 'Test2.jpg', 'Test3.jpg']
x=open("new.txt","r")
#print("ENTER TEXT TO CONVERT")
#x.write(input()+"\n")
list1=[]
listx=[i for i in x.read()]
if '\n' in listx[-1]:
	pass
else:
	listx[-1]=listx[-1]+'\n' 
y=0
count=0
for i in listx:
 if i=='\n':
  count=count+1
  if(len(list1)<50):
   for i in range(len(list1),50,1):
    list1.append('fonts/space.jpg')
  make_image(list1,count)
  list1.clear()
  continue
 if(i>='a' and i<= 'z') :
  z=base+i+".jpg"
 else:
  z=base+'space.jpg'
 list1.append(z)
 y=y+1
if(count>0):
 multiple_lines(count)
