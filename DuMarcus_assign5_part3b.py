"""
Marcus Du
3/16/2021
Section 006
Part 3b: Find all Prime Numbers between 1 and 1000
"""

for num in range(1, 1000 + 1):
   if num==1:
       print("1 is technically not a prime number.")
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num,"is a prime number!")