lower = int(input("Please enter a number for the lower range: "))
high = int(input("Please enter a number for the higher range: "))
l = []
even = []
odd = []
for i in range(lower,high+1):
    l.append(i*i)
print("The number of square numbers between the ranges are",l)
for i in l:
    if(i % 2 == 0):
        print("The number is even.")
    else:
        print("The number is odd.")