# Swap function 
def swap(it1, it2):
    temp = lst[it1]
    lst[it1] = lst[it2]
    lst[it2] = temp

lst = [2, 5, 9, 3, 76, 14, 8, 1]

print(f"Num of items: {len(lst)}")

# Iterate the list
for x in range(1, len(lst)):
    # Verify if do Swap()
    # Ordering List
    for y in range(0, len(lst) - x):
        if lst[y] > lst[y + 1]:
            swap(y, y + 1)
        
    print(f"Loop {x}: {lst}")
        
print(lst)