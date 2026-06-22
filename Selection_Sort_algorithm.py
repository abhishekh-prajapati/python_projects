def selection_sort(items):
    # Loop through the entire list
    for i in range(len(items)):
        # Assume the current position holds the minimum value
        min_index = i
        
        # Look through the rest of the unsorted list
        for j in range(i + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j
                
        # Only swap if a smaller element was actually found
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]
            
            
    return items
