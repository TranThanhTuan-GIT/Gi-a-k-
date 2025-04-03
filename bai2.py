def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Input
num = int(input("Nhập số nguyên không âm n: "))
print(f"Giai thừa của {num} là {factorial(num)}.")
