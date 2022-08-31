def swap(it1, it2):
    temp = lst2[it1]
    lst2[it1] = lst2[it2]
    lst2[it2] = temp

lst = [2, 5, 9, 3, 76, 14, 8, 1]
lst2 = [2, 14, 6, 18, 10, 0]

target_position = 0
data = 0

def insertion_sort_form_1():
    print(f"Init List State: {lst}")

    # Looping list
    for i in range(1, len(lst)):
        # Get data
        data = lst[i]
        
        # Indicates target position
        target_position = i
        
        # Looping elements unitl the target position
        while target_position > 0 and lst[target_position - 1] > data:
            lst[target_position] = lst[target_position - 1]
            target_position = target_position - 1
        
        # Put data on the target position
        lst[target_position] = data

    print(f"Final List State: {lst}")

# Another implementation
def insertion_sort_form_2():
    print(f"Init List State: {lst2}")
    
    # Looping list
    for i in range(1, len(lst2)):
        # Indicates target position
        target_position = i
        
        # Looping elements unitl the target position
        while target_position > 0 and lst2[target_position] < lst2[target_position - 1]:
            swap(target_position, target_position - 1)
            target_position = target_position - 1

    print(f"Final List State: {lst2}")
    

insertion_sort_form_1()

