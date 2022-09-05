def swap(p1, p2):
    temp = lst[p1]
    lst[p1] = lst[p2]
    lst[p2] = temp

def partition(start, end):
    # Select the last element as pivot
    pivot = lst[end]
    
    # Putting the pivot index with the start index
    pivot_index = start
    
    # Looping the list in the selected fragment
    for x in range(start, end):
        # If the element in (x) index is less or equal than pivot
        if lst[x] < pivot:
            # swap() the (x) element with the element in the pivot index
            swap(x, pivot_index)
            
            # Increment pivot index
            pivot_index += 1
    
    # Do the last swap() to put the pivot where correspond
    swap(pivot_index, end)
    
    # Return pivot_index
    return pivot_index

def quicksort(start_index, end_index):
    # Base case, an element or invalid fragment
    if start_index >= end_index:
        return

    pivot_index = partition(start_index, end_index)
    
    quicksort(start_index, pivot_index - 1)
    quicksort(pivot_index + 1, end_index)


lst = [3, 15, 7, 19, 11, 1]

print(lst)

quicksort(0, len(lst) - 1)

print(lst)
