def swap(it1, it2):
    temp = lst[it1]
    lst[it1] = lst[it2]
    lst[it2] = temp

lst = [3, 15, 7, 19, 11, 1]

print(f"Inital List State: {lst}")

# Selection Sort
# Looping elements in the list
for i in range(0, len(lst)):
    # minor_index is the current position when the loop start
    minor_index = i
    
    # finding new minor_index
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[minor_index]:
            minor_index = j
    
    # Swap current position with minor_index
    swap(i, minor_index)

print(f"Final List State: {lst}")
