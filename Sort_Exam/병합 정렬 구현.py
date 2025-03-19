def merge_sort(arr) :
    if len(arr) == 1 :
        return arr
    
    mid = len(arr) // 2

    high_list = merge_sort(arr[mid:])
    low_list = merge_sort(arr[:mid])

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

num_list = [1,7,3,9,2,7,4,2,3,5]

print(merge_sort(num_list))

