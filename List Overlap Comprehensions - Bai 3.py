import random
def List_Overlap_Comprehensions(L1,L2):
    L=set([i for i in L1 if i in L2 ])
    if not L:
        print ("Khong co phan tu trung")
    else:
        print (set([i for i in L1 if i in L2 ]))

n=int(input("Nhap do dai list n: "))
x=random.sample(range(1,101),n)
m=int(input("Nhap do dai list m: "))
y=random.sample(range(1,101),m)

List_Overlap_Comprehensions(x,y)
