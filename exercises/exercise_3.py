# Exercise 3
# Your solution comes here
n=int(input("How many seconds have passed from the beginning of the day?"))
hours = (n // 3600) % 24
minutes = (n // 60) % 60
seconds = n % 60

print(f"{hours}:{minutes:02d}:{seconds:02d}")
