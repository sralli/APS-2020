def root(arr, i):
    while(arr[i]!=i):
        i=arr[i]
    return i

def weighted_union( u, v):
    global arr, size
    rootu, rootv = root(arr, u), root(arr,v)

    if size[rootu]<size[rootv]:
        arr[rootu] = arr[rootv]
        size[rootv]+=size[rootu]
    else:
        arr[rootv]=arr[rootu]
        size[rootu]+=size[rootv]
    
    return arr, size


if __name__ == "__main__":
    global arr, size
    arr = [0,1,2,3,4,5]
    size = [1,1,1,1,1]
    print(weighted_union(0,1))
    print(weighted_union(1,2))
    print(weighted_union(3,2))

    















