#!/usr/bin/env python3

def bubble_sort(data):
    length = len(data)
    for i in range(length):
        for j in range(length-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def select_sort(data):
    length = len(data)
    for i in range(length):
        num_max = data[0]
        numiter = 0
        for j in range(1, length-i):
            if data[j] > num_max:
                num_max = data[j]
                numiter = j
        data[length-i-1], data[numiter] = data[numiter], data[length-i-1]
    return data

def insert_sort(data):
    length = len(data)
    res = [data[0]]
    for i in range(1, length):
        temp = data[i]
        for j in range(i-1, -2, -1):
            if res[j] < temp:
                break
        res.insert(j+1, temp)
    return res

def shell_sort(data):
    length = len(data)
    cache_shell = []
    num = length
    while(num - 1):
        num //= 2
        cache_shell.append(num)
    for i in cache_shell:
        for j in range(length-i):
            if data[j] > data[j+i]:
                data[j], data[i+j] = data[i+j], data[j]
    data = insert_sort(data)
    return data

def merge_sort(data):
    def _merge(l, r):
        res = []
        while len(l)*len(r):
            if l[0] > r[0]:
                res.append(r.pop(0))
            else:
                res.append(l.pop(0))
        res += (l + r)
        return res

    def _sort(cache):
        length = len(cache)
        if length < 2:
            return cache
        else:
            l = cache[:length // 2]
            r = cache[length // 2:]
            return _merge(_sort(l), _sort(r))

    return _sort(data)

def quick_sort(data):
    def sort(cache, l, h):
        if l >= h - 1:
            pass
        else:
            flag = cache[h-1]
            cache_l = []
            cache_r = []
            for i in range(l, h-1):
                if cache[i] >= flag:
                    cache_r.append(cache[i])
                else:
                    cache_l.append(cache[i])
            cache_l.append(flag)
            cache[l : h] = cache_l + cache_r
            sort(cache, l, l + len(cache_l)-1)
            sort(cache, h - len(cache_r), h)
    sort(data, 0, len(data))
    return data

def heap_sort(data):
    def max_heapify(cache, loc, heapsize):
        l = loc*2 + 1
        r = loc*2 + 2
        while (l < heapsize):
            if cache[l] > cache[loc]:
                max_loc = l
            else:
                max_loc = loc
            if r < heapsize:
                if cache[r] > cache[max_loc]:
                    max_loc = r
            if (max_loc != loc):
                cache[max_loc], cache[loc] = cache[loc], cache[max_loc]
                loc = max_loc
                l = loc*2 + 1
                r = loc*2 + 2
            else:
                break
        return cache

    def build_max_heap(cache, heapsize):
        for i in range((heapsize-2) // 2, -1, -1):
            cache = max_heapify(cache, i, heapsize)
        return cache

    def sort(cache):
        length = len(cache)
        cache = build_max_heap(cache, length)
        for i in range(length-1, 0, -1):
            cache[0], cache[i] = cache[i], cache[0]
            cache = max_heapify(cache, 0, i)
        return cache

    return sort(data)

def count_sort(data, num_min=None, num_max=None):
    if num_min == None:
        num_max = data[0]
        num_min = data[0]
        for i in data[1:]:
            if i > num_max:
                num_max = i
            if i < num_min:
                num_min = i
    cache_count = (num_max - num_min + 1)*[0]
    res = []
    for i in data:
        cache_count[i - num_min] += 1
    for i in range(len(cache_count)):
        if cache_count[i]:
            res += cache_count[i]*[num_min+i]
    return res

def bucket_sort(data, num_min=None, num_max=None):
    if num_min == None:
        num_max = data[0]
        num_min = data[0]
        for i in data[1:]:
            if i > num_max:
                num_max = i
            if i < num_min:
                num_min = i
    num_step = 10
    step = (num_max - num_min) // num_step + 1
    cache = [[] for i in range(num_step)]
    res = []
    for i in data:
        cache[(i - num_min) // step].append(i)
    for i in range(num_step):
        cache[i] = insert_sort(cache[i])
    for i in range(num_step):
        res += cache[i]

    return res

def radix_sort(data, num_max=None):
    length = len(data)
    if num_max == None:
        num_max = data[0]
        for i in range(1, length):
            if num_max < data[i]:
                num_max = data[i]
    log_temp = num_max
    num = 0
    while log_temp > 0:
        num += 1
        log_temp //= 10
    for i in range(num):
        temp = 10**i
        res = [[] for i in range(10)]
        for j in range(length):
            res[(data[j] // temp) % 10].append(data[j])
        data = []
        for i in range(10):
            data += res[i]
    return data

