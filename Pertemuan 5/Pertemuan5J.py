#Implementasi algoritma Median dua array urut berbeda ukuran

def Solution(arr):
    n = len(arr)

    # Jika panjang array genap
    if n % 2 == 0:
        z = n // 2
        e = arr[z]
        q = arr[z - 1]
        ans = (e + q) / 2
        return ans

    # Jika panjang array ganjil
    else:
        z = n // 2
        ans = arr[z]
        return ans

arr1 = [-5, 3, 6, 12, 15]
arr2 = [-12, -10, -6, -3, 4, 10]

arr3 = arr1 + arr2

arr3.sort()

print("Median = ", Solution(arr3))