def fibonacci_ct(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    gt2, gt1 = 0, 1
    for _ in range(2, n + 1):
        ht = gt1 + gt2
        gt2, gt1 = gt1, ht

    return gt1

n = int(input("Nhập số n: "))
print(f"Số Fibonacci thứ {n} là: {fibonacci_ct(n)}")

#Chỉ lưu hai số gần nhất trong dãy.
#Giảm bộ nhớ từ O(n) xuống O(1)
#+1 tối ưu

