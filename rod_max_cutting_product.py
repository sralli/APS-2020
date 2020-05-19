def rod_cutting(n):
    result = [0 for i in range(n+1)]
    result[0] =0
    result[1] =0 
    for i in range(2, n+1):
        for j in range(i):
            result[i] = max(result[i], j*(i-j), j*result[i-j]) 
    return result[n]


n = int(input('Enter the number '))
print(rod_cutting(n))
