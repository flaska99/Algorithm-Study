def merge_sort_while(arr) :
    if len(arr) == 1 :
        return arr
    
    mid = len(arr) // 2

    high_list = merge_sort_while(arr[mid:])
    low_list = merge_sort_while(arr[:mid])

    merged_list = []
    l = h = 0

    while l < len(low_list) and h < len(high_list) :
        if low_list[l] < high_list[h] :
            merged_list.append(low_list[l])
            l += 1
        
        else :
            merged_list.append(high_list[h])
            h += 1
        
    merged_list += low_list[l:]
    merged_list += high_list[h:]
    return merged_list

def merge_sort_recusion(arr):
    if len(arr) <= 1:
        return arr
    
    mid  = len(arr) // 2
    left = merge_sort_recusion(arr[:mid])
    right = merge_sort_recusion(arr[mid:])

    return merge_recusion(left, right)

def merge_recusion(left, right) :
    result = []
    i = j = 0

    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            result.append(left[i])
            i += 1
        
        else:
            result.append(right[j])
            j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

arr = [5, 2, 4, 7, 1, 3, 6]
sorted_arr = merge_sort_recusion(arr)
print(sorted_arr)


    



