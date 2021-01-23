a = (input("Enter the mail: "))

c = list(a)
d =len(c)-1
i = 0
while i <len(c):
    if c[i] == "@":
        i = len(c)
    else:
        if c[i] == ".":
            del(c[i])
            i = i - 1
    i = i + 1

c1 = ""
for i in c:
  c1 = c1 + i
b = c1.upper()
if b == "CENG113@EXAMPLE.COM":
    print("Your email is ceng113@example.com")
else:
    b = b.lower()
    print("your email is", b)
    print("Your email is not ceng113@example.com")