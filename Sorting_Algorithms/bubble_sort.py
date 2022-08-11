def bubble_sort(list):
    n = len(list)
    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):
            if list[j] > list[j + 1]:
                swapped = True
                list[j], list[j+1] = list[j+1], list[j]

        if not swapped:
            return
        swapped = False

unsorted_list = [14,33,27,10,35,19,42,44]
print('Unsorted list: {}'.format(unsorted_list))
bubble_sort(unsorted_list)
print('Sorted list:   {}'.format(unsorted_list))

unsorted_list = [12,70,13,32,40,83,21,85,11,87,65,21]
print('Unsorted list: {}'.format(unsorted_list))
bubble_sort(unsorted_list)
print('Sorted list:   {}'.format(unsorted_list))

sorted_list = [1,2,3,4,5,6,7,8,9,10]
print('Unsorted list: {}'.format(sorted_list))
bubble_sort(unsorted_list)
print('Sorted list:   {}'.format(sorted_list))
