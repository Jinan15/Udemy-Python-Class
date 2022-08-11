def merge_sort(list):
    if len(list) == 1:
        return list
    if len(list) == 2:
        if list[0] > list[1]:
            temp = list[0]
            list[0] = list[1]
            list[1] = temp
            return list
        else:
            return list

    left = merge_sort(list[0:int(len(list)/2)])
    right = merge_sort(list[int(len(list)/2):])
    left_pointer = 0
    right_pointer = 0

    ret = []

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            ret.append(left[left_pointer])
            left_pointer += 1
        else:
            ret.append(right[right_pointer])
            right_pointer += 1
    while right_pointer < len(right):
        ret.append(right[right_pointer])
        right_pointer += 1
    while left_pointer < len(left):
        ret.append(left[left_pointer])
        left_pointer += 1

    return ret

unsorted_list = [14,33,27,10,35,19,42,44]
sorted_list = merge_sort(unsorted_list)
print('Unsorted list: {}'.format(unsorted_list))
print('Sorted list:   {}'.format(sorted_list))

unsorted_list = [12,70,13,32,40,83,21,85,11,87,65,21]
sorted_list = merge_sort(unsorted_list)
print('Unsorted list: {}'.format(unsorted_list))
print('Sorted list:   {}'.format(sorted_list))
