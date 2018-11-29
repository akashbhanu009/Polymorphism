class Duck:
    def Talk(self):
        print("Quak...Quak...")

class Dog:
    def Bark(self):
        print("Bow...Bow..")

class Goat:
    def Fight(self):
        print("meaaaa....")

class Human:
    def Sound(self):
        print("Shuting...Laguhing.....")

"""Python Best Method"""

def f1 (obj):
    if hasattr (obj,"Talk"):
        obj.Talk()
    elif hasattr (obj,"Bark"):
        obj.Bark()
    elif hasattr (obj,"Fight"):
        obj.Fight()
    elif hasattr(obj,"Sound"):
        obj.Sound()

d=Duck()
f1(d)
d=Dog()
f1(d)
g=Goat()
f1(g)
h=Human()
f1(h)
    
'''ANOTHER METHOD:-
def f1(obj):
    f1(obj)
    
i=[Duck(),Dog(),Goat(),Human()]
for obj in i:
    f1(obj)
'''

'''NEXT METHOD:-

def f1(obj):
    f1(obj)

d=Duck()
f1(d) 

d=Dog()
f1(d)

g=Goat()
f1(g)

h=Human()
f1(h)
'''
