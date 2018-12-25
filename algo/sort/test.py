from sort import *
import numpy as np

with open('data.txt', 'r') as f:
    data = [int(i[:-1]) for i in f.readlines()]


res_bubble = bubble_sort(data[:])
res_select = select_sort(data[:])
res_insert = insert_sort(data[:])

res_shell = shell_sort(data[:])

res_merge = merge_sort(data[:])
res_quick = quick_sort(data[:])
res_heap = heap_sort(data[:])

res_count = count_sort(data[:])
res_bucket = bucket_sort(data[:])
res_radix = radix_sort(data[:])

res_ref = sorted(data)
print('bubble_sort result: ', res_ref == res_bubble)
print('select_sort result: ', res_ref == res_select)
print('insert_sort result: ', res_ref == res_insert)
print('shell_sort result: ', res_ref == res_shell)
print('merge_sort result: ', res_ref == res_merge)
print('quick_sort result: ', res_ref == res_quick)
print('heap_sort result: ', res_ref == res_heap)
print('count_sort result: ', res_ref == res_count)
print('bucket_sort result: ', res_ref == res_bubble)
print('radix_sort result: ', res_ref == res_radix)
