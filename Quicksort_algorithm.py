def quick_sort(lst):
    # 1. Base case: lists with 0 or 1 elements are already sorted
    if len(lst) < 2:
        return lst
    
    # 2. Choose a pivot (using the first element as allowed)
    pivot = lst[0]
    
    # 3. Partitioning into three sublists
    # We slice lst[1:] so we don't compare the pivot against itself in the 'less' and 'greater' steps
    less_than = [x for x in lst[1:] if x < pivot]
    equal_to = [x for x in lst if x == pivot]
    greater_than = [x for x in lst[1:] if x > pivot]
    
    # 4. Recursively sort the sublists and combine them
    return quick_sort(less_than) + equal_to + quick_sort(greater_than)
