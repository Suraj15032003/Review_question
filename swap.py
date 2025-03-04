# Q2

def swap_idx(arr):
    for i in range(0, len(arr) - 2, 4): 
        arr[i], arr[i+2] = arr[i+2], arr[i]
        arr[i+1], arr[i+3] = arr[i+3], arr[i+1]

arr = [2, 5, 11, 30, 7, 15, 9, 4, 3, 18] 
swap_idx(arr)
print(arr)