"""
Marcus Du
3/16/2021
Section 006
Part 3b: Find all Prime Numbers between 1 and 1000
"""
start=int(input("Start number: "))
end=int(input("End number: "))
if start<=0 or end<=0:
    print("Start and end must be positive")
    start=int(input("Start number: "))
    end==int(input("End number: "))
if end<=start:
    print("End number must be greater than start number")
    start=int(input("Start number: "))
    end==int(input("End number: "))

for num in range(start, end + 1):
   if num==1:
       print("1 is technically not a prime number.")
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num,"is a prime number!")