def list_ends(L):
  L2 = (L[0::len(L) - 1])
  return L2

L = input("Nhap day so cach nhau khoang trang: ").split()
L2=list_ends(L)
print(L2)





