import os

def make_markdown():
    data = draw_class()
    with open('result.md', 'w') as f:
        f.write('| No. | 类名称 | 父类 | 主要功能 | 函数数目|\n')
        f.write('|:--:|:---------:|:---------:|:----------------:|:--------:|\n')
        for i in range(len(data.keys())):
            order = i + 1
            class_name = list(data.keys())[i]
            inherit_class = ''
            inherit_class_temp = data[class_name]['inherit']
            for i in inherit_class_temp:
                inherit_class += i + ' '
            inherit_class = inherit_class[:-1]
            main_func = ''
            num_func = len(data[class_name]['function'])
            f.write('|%d|%s|%s|%s|%d|\n' % (order, class_name, inherit_class, main_func, num_func))
        for i in range(len(data.keys())):
            class_name = list(data.keys())[i]
            f.write('### %d.%s\n' % (i+1, class_name))
            f.write('| No. | 函数名称 | 主要功能 | 传入参数数目 | 输出参数数目|\n')
            f.write('|:--:|:---------:|:---------:|:----------------:|:--------:|\n')
            cache_func_key = list(data[class_name]['function'].keys())
            for j in range(len(cache_func_key)):
                order = j + 1
                func_name = fix_func_name(cache_func_key[j])
                main_func = ''
                num_input = len(data[class_name]['function'][cache_func_key[j]]['input'])
                num_output = len(data[class_name]['function'][cache_func_key[j]]['output'])
                f.write('|%d|%s|%s|%d|%d|\n' % (order, func_name, main_func, num_input, num_output))
            for j in range(len(cache_func_key)):
                func_name = cache_func_key[j]
                f.write('##### %d. %s\n' % (j+1, fix_func_name(func_name)))
                f.write('__Input__\n')
                length_input = len(data[class_name]['function'][func_name]['input'])
                if length_input != 0:
                    f.write('| No. | 参数名称 | 主要功能 | 参数类型 |\n')
                    f.write('|:--:|:---------:|:---------:|:----------------:|\n')
                    list_arg_list = data[class_name]['function'][func_name]['input']
                    for k in range(length_input):
                        order = k + 1
                        arg_name = list_arg_list[k]
                        main_func = ''
                        arg_type = ''
                        f.write('|%d|%s|%s|%s|\n' % (order, arg_name, main_func, arg_type))


                f.write('__Output__\n')
                length_output = len(data[class_name]['function'][func_name]['output'])
                if length_output != 0:
                    f.write('| No. | 参数名称 | 主要功能 | 参数类型 |\n')
                    f.write('|:--:|:---------:|:---------:|:----------------:|\n')
                    list_arg_list = data[class_name]['function'][func_name]['output']
                    for k in range(length_output):
                        order = k + 1
                        arg_name = list_arg_list[k]
                        main_func = ''
                        arg_type = ''
                        f.write('|%d|%s|%s|%s|\n' % (order, arg_name, main_func, arg_type))

def fix_func_name(data):
    res = ''
    for i in data:
        if i != '_':
            res += i
        else:
            res += '\_'
    return res


def draw_class():
    data = cache_global
    cache_class_name = []
    cache_class_line = []
    cache_res = {}
    judge = 0
    for i in range(len(data)):
        if data[i][:tab_width*class_level+5] == tab_width*class_level*' ' + 'class':
            start = data[i].index(' ')
            try:
                end = data[i].index('(')
            except ValueError:
                end = data[i].index(':')
            cache_class_name.append(data[i][start+1 : end])
            if len(cache_class_line) != 0:
                cache_class_line[-1].append(i)
            cache_class_line.append([i])
        if data[i][:11] == 'if __name__':
            cache_class_line[-1].append(i)
            judge = 1
    if judge == 0:
        cache_class_line[-1].append(i)
    for i in range(len(cache_class_name)):
        cache_res[cache_class_name[i]] = draw_function(cache_class_line[i])
    return cache_res

def draw_function(index):
    data = cache_global
    cache_func_name = []
    cache_func_line = []
    cache_res = {'inherit':[], 'function':{}}
    try:
        index_class_start = data[index[0]].index('(')
        index_class_end = data[index[0]].index(')')
        cache_inherit = data[index[0]][index_class_start+1 : index_class_end].split(',')
        for i in range(len(cache_inherit)):
            cache_inherit[i] = cache_inherit[i].lstrip()
        cache_res['inherit'] = cache_inherit
    except:
        cache_res['inherit'] = ['']

    for i in range(index[0], index[1]):
        if data[i][:tab_width*func_level+3] == tab_width*func_level*' ' + 'def':
            start = data[i].index('def ')
            end = data[i].index('(')
            cache_func_name.append(data[i][start+3 : end])
            if len(cache_func_line) != 0:
                cache_func_line[-1].append(i)
            cache_func_line.append([i])
    cache_func_line[-1].append(index[1])
    for i in range(len(cache_func_name)):
        cache_res['function'][cache_func_name[i]] = draw_arg(cache_func_line[i])
    return cache_res

def draw_arg(index):
    cache_res = {'input': [], 'output' : []}
    cache_res_input = []
    cache_res_output = []
    input_cache = ''
    output_start = 0
    input_start = index[0]
    for i in range(index[0], index[1]):
        if ':' in cache_global[i]:
            input_end = i
            break
    for i in range(input_start, input_end+1):
        input_cache += cache_global[i][:-1]

    for i in range(index[0], index[1]):
        if ' return ' in cache_global[i]:
            output_start = i
            break
    index_cache_input_start = input_cache.index('(')
    index_cache_input_end = input_cache.index(')')
    cache_input = input_cache[index_cache_input_start+1: index_cache_input_end].split(',')
    for i in range(len(cache_input)):
        cache_input[i] = cache_input[i].lstrip()
        if '=' in cache_input[i]:
            index_temp = cache_input[i].index('=')
            cache_input[i] = cache_input[i][:index_temp]
        if cache_input[i] == 'self':
            continue
        else:
            cache_res_input.append(cache_input[i])

    if output_start != 0:
        output_cache = cache_global[output_start][:-1]
        index_output_start = output_cache.index(' return ')
        cache_res_output = output_cache[index_output_start+8:].split(',')
    cache_res['input'] = cache_res_input
    cache_res['output'] = cache_res_output
    return cache_res


if __name__ == '__main__':
    tab_width = 4
    class_level = 0
    func_level = 1
    cache_global = []
    with open('head.py') as f:
        cache_global_init = f.readlines()
    for i in cache_global_init:
        if i != '\n':
            cache_global.append(i)
    make_markdown()

