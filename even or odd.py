a=input()
if a.isnumeric():
    b=int(a)
    if b%2==0:
        print("Even")
    else:
        print("Odd")
else:
    print("Invalid")
