def fibonacci(n):
    if n < 0:
        return "Giá trị n không hợp lệ. Vui lòng nhập n >= 0."
    
    fib = [0] * (n + 1)
    
    if n >= 1:
        fib[1] = 1
    
    
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        
    return fib[n]


n = int(input("Nhập vào số n để tính số Fibonacci thứ n: "))
result = fibonacci(n)
print(f"Số Fibonacci thứ {n} là: {result}")
