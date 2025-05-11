# how to solve this game
# game development is not easy
# i have to find at least one outcome
n =6
win =False
p=0
while(n>0):
    print(n)
    if not p and n>3:
        if ((T:=n-3)>3):
            n=T
            # continue
        elif((T:=n-2)>3):
            n=T
            # continue
        else:
            n=n-1
            # continue
        # if n<=0:
        #     win =True
        p=1
    elif not p:
        win=True
        n=0
    else:
        n-=3
        if n<=0:
            win =False 
        p=0
print(win)

# actual answer
class Solution:
    def canWinNim(self, n: int) -> bool:
        # how to solve this game
        # game development is not easy
        # i have to find at least one outcome
        win =False
        p=0
        while(n>0):
            # print(n)
            if n>3:
                if ((T:=n-3)>3):
                    n=T
                    # continue
                elif((T:=n-2)>3):
                    n=T
                    # continue
                else:
                    n=n-1
                    # continue
                # if n<=0:
                #     win =True
            else:
                n=0
            if p:
                p=0
            else:
                p=1
        if p:
            win=True
        else:
            win=False
            # elif not p:
            #     win=True
            #     n=0
            # elif p:
            #     n-=3
            #     if n<=0:
            #         win =False 
            #     p=0
        return win
            