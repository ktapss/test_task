"""
Сортировка слиянием не совсем самая оптимальная из возможных
алгоритмов сортировки, тем не менее, используется в многосоставных
алгоритмах и проста в реализации.
Более быстрый вариант сортировки - timsort, реализованный в python.
Он даст лучшую асимптотику O(1), тогда как сортировка слиянием в лучшем
случае сработает за O(n)
"""

def merge(list_1:list, list_2:list):
    merged_list = []
    i = j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            merged_list.append(list_1[i])
            i += 1
        else:
            merged_list.append(list_2[j])
            j += 1
    merged_list += list_1[i:] + list_2[j:]
    return merged_list
    
    
def merge_sort(array):
    if len(array) == 1:
        return array
    left_list = merge_sort(array[:len(array)//2])
    right_list = merge_sort(array[len(array)//2:])
    return merge(left_list, right_list)
