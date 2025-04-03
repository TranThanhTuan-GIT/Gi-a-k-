def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  
                swapped = True
        print(f"Bước {i+1}: {arr}")  
        if not swapped:
            break


arr = [64, 34, 25, 12, 22, 11, 90]  

bubble_sort(arr)
# để tự nhập 
#arr = list(map(int, input("Nhập các số nguyên cách nhau bởi dấu cách: ").split()))
#print("\nMảng ban đầu:", arr)
#bubble_sort(arr)
#print("\nMảng sau khi sắp xếp:", arr)
