from collections import namedtuple
from typing import TypeAlias

# nodeType =TypeVar('nodeType',)
T:TypeAlias = object
# N :T =namedtuple('N',['val','left','right'],defaults=[None,'null','null'],rename=True)
class N:
    def __init__(self,val=None,left='null',right='null'):
        self.val=val
        self.left=left
        self.right=right
    def __str__(self):
        return f'{self.val} {self.left} {self.right}'
        
class Bst:
    def __init__(self):
        self.root:T ='null'
        '''if value not exist use None for pointer use null(string)'''
        
    def createNode(self,val:int):
        '''if return 1 then sucessfully node inserted else failure'''
        node:T =N(val,'null','null')
        if self.root=='null':
            self.root = node
            return 1
        return self.__fitNode(self.root,node)
        
        
    def __fitNode(self,root:T,n:T):
        if n.val<root.val:
            if root.left!='null':
                return self.__fitNode(root.left,n)
            else:
                root.left=n
                return 1
        else:
            if root.right!='null':
                return self.__fitNode(root.right,n)
            else:
                root.right=n
                return 1
    def search(self,key):
        is_key_exist =self.__search_node(self.root,key)
        if is_key_exist:
            a=is_key_exist
            
            left =a.left.val if a.left!='null' else 'null'
            right =a.right.val if a.right!='null' else 'null'

            # print('key is present')
            print('value={} left_child={} right_child={}'.format(a.val,left,right))
            
            return 'key is present'
        else:
            return 'key is not present'
        
    def __search_node(self,root,key):
        if not root.val: return 0
        if key==root.val:
            return root
        elif key<root.val:
            return self.__search_node(root.left,key)
        else:
            return self.__search_node(root.right,key)
        
    def travrsal(self):
        pass


# ------------------------
# start creating objects
# 1) call createnode for node insertion
# 2) call search for searching
a =Bst()
# a.createNode(10)
# print(a.root)
# a.root.left =N(25)
# print(a.root)
nodes =[10,25,-5,5,-10,36]
for ele in nodes:
    print(a.createNode(ele),end=' ')
print()
print(a.search(-5))


            
            
        
    