def merge(left_list, right_list):
    #Result list
    merged = []
    
    #Index
    left_index = 0
    right_index = 0
    
    # Looping while both lists have elements without process
    while left_index < len(left_list) and right_index < len(right_list):
        # If left is minor or equal add the left value
        if left_list[left_index] <= right_list[right_index]:
            merged.append(left_list[left_index])
            
            # Move left_index one step
            left_index += 1
        else: # If right is minor add the right value
            merged.append(right_list[right_index])
            
            # Move right_index one step
            right_index += 1
    
    # If left over elements in the left list put all in merged
    while left_index < len(left_list):
        merged.append(left_list[left_index])
        left_index += 1
        
    # If left over elements in the right list put all in merged
    while right_index < len(right_list):
        merged.append(right_list[right_index])
        right_index += 1
    
    return merged

def merge_sort(lst):
    
    # Base case, one element ordered list
    if len(lst) < 2:
        return lst
    
    # Get middle point of the list
    half = round(len(lst) / 2)
    
    left = []
    right = []
    
    # Add to the left from begin until before half
    for x in range(0, half):
        left.append(lst[x])
    
    # Add to the right from half until end of the list
    for x in range(half, len(lst)):
        right.append(lst[x])
    
    # Inductive Cases
    # Make merge_sort() of the right and left lists
    temp_left_list = merge_sort(left)
    temp_right_list = merge_sort(right)
    
    # Makes the merge from inductive case returns
    ordered = merge(temp_left_list, temp_right_list)
    
    return ordered

left_list = [6, 7, 9, 11]
right_list = [8, 10, 12, 13]

result = merge(left_list, right_list)

print(result)

values = [3, 15, 7, 19, 11, 1]

merged_list = merge_sort(values)

print(merged_list)