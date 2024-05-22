# Exercise 7
# Your solution comes here
print("enter a 4 digit number;")
num=int(input("enter a 4 digit number:"))
num1=num//1000
num2=num%1000//100
num3=num%100//10
num4=num%10
print(num1+num2+num3+num4)