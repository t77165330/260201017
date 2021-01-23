a = float(input("Enter a please: "))
b = float(input("Enter b please: "))
c = float(input("Enter c please: "))

delta = b**2-4*a*c
if delta > 0:
 root1 = (-b + (delta)**(1/2))/2*a
 root2 = (-b - (delta)**(1/2))/2*a
 print("root1:",root1)
 print("root2:",root2)

elif delta == 0:
 root = -b/a
 print("root:", root )
else:
 root1 = ((-b + (-delta)**(1/2))/2*a)
 root2 = ((-b - (-delta)**(1/2))/2*a)
 print("root1:",root1 , "i")
 print("root2:",root2 , "i")
