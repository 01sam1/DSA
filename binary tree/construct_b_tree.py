from math import log2,floor
from collections import namedtuple
# class Node:
#     def __init__(self,val=None,left=None,right=None):
#         self.val =val
#         self.left =left
#         self.right =right

T =namedtuple('T',['val','left','right'])
def cB(ele,a,b):
    return T(ele,a,b)
# li =[0,10,5,6,'null','null',8,7,'null','null','null',4]
li =[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
length =len(li)-1
def cN(index):
    if index<=length-2**floor(log2(length)):
        return cB(li[index],li[index*2],li[index*2+1])
    elif index<=length:
        return cB(li[index],'null','null')
    else:
        exit(0)
def main():
    ans =cN(8)
    print(ans.val,ans.left,ans.right)
main()

