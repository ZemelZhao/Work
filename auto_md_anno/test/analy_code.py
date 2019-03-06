import os
import linecache
from hash_std import HashStd
import numpy as np
import pickle
import sys

class AnalyCode(object):
    def __init__(self):
        self.tab_width = 4
        self.cache_data = {}
        self.hash_std = HashStd()

    def get_prog_file_system(self):
        self.cache_dir_system = {'files': [], 'dirs': {}}
        for root, dirs, files in os.walk(self.prog_address):
            for i in files[:]:
                if i[0] == '.':
                    files.remove(i)
                elif i[-3:] != '.py':
                    files.remove(i)
                elif i == 'test.py' or i == 'try.py' or i == '__init__.py' or i == 'setup.py':
                    files.remove(i)
                else:
                    pass
            if root == self.prog_address:
                self.cache_dir_system['files'] = files
            else:
                dirs = root[len(self.prog_address)+1 :]
                if dirs != '__pycache__' and dirs[0] != '.' and ('AutoAnno' not in dirs):
                    self.cache_dir_system['dirs'][dirs] = files
        return self.cache_dir_system

    def read_doc(self, address):
        with open(address) as f:
            data_code_init = f.readlines()
        doc_name = os.path.split(address)[1]
        data_code_fixed = self.filter_doc_useless_line(data_code_init)
        dic_res = {'hash_code':[0, 0, 0, 0], 'line_num': 0, 'func':{}, 'class':{}}
        stat = 0
        cache_import_code = []
        cache_define_code = []
        cache_execute_code = []
        cache_code = []
        for i in data_code_fixed:
            if i[:3] == 'def' or i[:5] == 'class' or i[:1] == '@':
                stat = 1
            elif i[:5] == 'if __':
                stat = 2
            else:
                pass
            if stat == 0:
                cache_import_code.append(i)
            elif stat == 1:
                cache_define_code.append(i)
            else:
                cache_execute_code.append(i)
        dic_res['line_num'] = len(data_code_fixed)
        dic_res['hash_code'][0] = self.hash_list(data_code_fixed)
        dic_res['hash_code'][1] = self.hash_list(cache_import_code)
        dic_res['hash_code'][2] = self.hash_list(cache_define_code)
        dic_res['hash_code'][3] = self.hash_list(cache_execute_code)
        for i in range(len(cache_define_code)):
            code_line = cache_define_code[i]
            if code_line[:self.tab_width] != ' '*self.tab_width:
                if code_line[:3] == 'def':
                    cache_code.append([i, 'func'])
                elif code_line[:5] == 'class':
                    cache_code.append([i, 'class'])
                elif code_line[:1] == '@':
                    cache_code.append([i, 'decorator'])
                else:
                    cache_code.append([i, 'execute'])
        data_add = []
        for i in range(len(cache_code)):
            if i < len(cache_code) - 1:
                data = cache_define_code[cache_code[i][0]: cache_code[i+1][0]]
            else:
                data = cache_define_code[cache_code[i][0]: ]
            if cache_code[i][1] == 'decorator':
                data_add.append(cache_define_code[cache_code[i][0]: cache_code[i+1][0]][0])
            elif cache_code[i][1] == 'func':
                name_func, dic_func = self.read_func(data_add + data)
                data_add = []
                dic_res['func'][name_func] = dic_func
            elif cache_code[i][1] == 'class':
                name_class, dic_class = self.read_class(data)
                dic_res['class'][name_class] = dic_class
            else:
                pass
        return doc_name, dic_res

    def read_class(self, data):
        dic_res = {'hash_code': 0, 'line_num': 0, 'superclass':[], 'func':{}}
        cache_class_code_head = ''
        dic_res['hash_code'] = self.hash_list(data)
        dic_res['line_num'] = len(data)
        for i in range(len(data)):
            cache_class_code_head += data[i]
            if data[i][-1] == ':':
                break
        data_code = data[i+1:]
        if '(' in cache_class_code_head:
            flag_func_name = cache_class_code_head.index('(')
            class_name = cache_class_code_head[6 : flag_func_name].strip()
            cache_class_inherit = cache_class_code_head[flag_func_name+1 :
                                                        -(cache_class_code_head[::-1].index(')')+1)]
            cache_class_inherit = [name.strip() for name in cache_class_inherit.split(',')]
            if 'object' in cache_class_inherit:
                cache_class_inherit.remove('object')
        else:
            class_name = cache_class_code_head[6: -1].strip()
            cache_class_inherit = ['object']
        dic_res['superclass'] = cache_class_inherit
        cache_code = []
        for i in range(len(data_code)):
            code_line = data_code[i]
            if code_line[:self.tab_width*2] != ' '*self.tab_width*2:
                if code_line[self.tab_width:self.tab_width+3] == 'def':
                    cache_code.append([i, 'func'])
                elif code_line[self.tab_width:self.tab_width+1] == '@':
                    cache_code.append([i, 'decorator'])
                else:
                    cache_code.append([i, 'execute'])
        data_add = []
        for i in range(len(cache_code)):
            if i < len(cache_code) - 1:
                data = data_code[cache_code[i][0]: cache_code[i+1][0]]
            else:
                data = data_code[cache_code[i][0]: ]
            if cache_code[i][1] == 'decorator':
                data_add.append(data_code[cache_code[i][0]: cache_code[i+1][0]][0])
            elif cache_code[i][1] == 'func':
                name_func, dic_func = self.read_func(data_add + data)
                dic_res['func'][name_func] = dic_func
            else:
                pass
        return class_name, dic_res

    def read_func(self, data):
        dic_res = {'hash_code': 0, 'line_num': 0, 'decorator': [], 'input':[], 'output':0}
        for i in range(len(data)):
            if data[i].strip()[0] == '@':
                data[i] = data[i].strip()
                if '(' in data[i]:
                    dic_res['decorator'].append(data[i][1:data[i].index('(')].strip())
                else:
                    dic_res['decorator'].append(data[i][1:].strip())
            else:
                break
        data = data[i:]
        cache_func_code_head = ''
        dic_res['hash_code'] = self.hash_list(data)
        dic_res['line_num'] = len(data)
        for i in data[:]:
            cache_func_code_head += i
            if i[-1] == ':':
                break
        flag_func_name = cache_func_code_head.index('(')
        func_name = cache_func_code_head[cache_func_code_head.index('def')+4 :
                                          flag_func_name]
        cache_func_input = cache_func_code_head[flag_func_name+1 :
                                                 -(cache_func_code_head[::-1].index(')')+1)]
        cache_func_input = [l for l in cache_func_input.split(',')]
        for i in range(len(cache_func_input)):
            if '=' in cache_func_input[i]:
                cache_func_input[i] = cache_func_input[i][:cache_func_input[i].index('=')]
            cache_func_input[i] = cache_func_input[i].strip()
        if cache_func_input[0] == 'self':
            cache_func_input.pop(0)
        for i in cache_func_input[:]:
            if i == '':
                cache_func_input.remove(i)
        dic_res['input'] = cache_func_input
        for i in data:
            if i.strip()[:6] == 'return':
                dic_res['output'] = 1
        return func_name, dic_res

    def read_files(self, list_file, dir_name='.'):
        dic_res = {'hash_code': 0, 'line_num':0, 'file': {}}
        hash_temp = ''
        for i in sorted(list_file):
            name_file, dic_file = self.read_doc(os.path.join(self.prog_address, dir_name, i))
            dic_res['file'][name_file] = dic_file
            hash_temp += dic_file['hash_code'][0]
            dic_res['line_num'] += dic_file['line_num']
        dic_res['hash_code'] = self.hash_system(dic_res)
        return dic_res

    def filter_doc_useless_line(self, cache_code_data):
        data_code_temp = cache_code_data[:]
        data_code_temp = self.filter_oneline_anno(data_code_temp)
        data_code_temp = self.filter_multiline_anno(data_code_temp)
        data_code_temp = self.fix_nonstandard_line_head(data_code_temp)
        data_code_res = self.filter_redun_space(data_code_temp)
        return data_code_res

    def run(self, address):
        self.address = address
        self.prog_address = os.path.join(os.getcwd(), address)
        self.prog_file_system = self.get_prog_file_system()
        dic_res = {'name': address, 'hash_code': 0, 'line_num': 0, 'files': {'hash_code': 0, 'line_num': 0, 'file': {}}, 'dirs': {'hash_code': 0, 'line_num': 0, 'dir': {}}}
        list_file_1_dir = self.prog_file_system['files']
        dic_res['files'] = self.read_files(list_file_1_dir)
        for i in self.prog_file_system['dirs']:
            dic_res['dirs']['dir'][i] = self.read_files(self.prog_file_system['dirs'][i], i)
            dic_res['dirs']['hash_code'] = self.hash_system(dic_res['dirs'])
            dic_res['dirs']['line_num'] += dic_res['dirs']['dir'][i]['line_num']
        dic_res['hash_code'] = self.hash_system((dic_res))
        dic_res['line_num'] = dic_res['files']['line_num'] + dic_res['dirs']['line_num']
        return dic_res

    def find_all_element_uncross(self, cache, data):
        res = []
        length = len(data)
        temp = -length
        while True:
            try:
                num = cache[temp+length : ].index(data)
                temp += num+length
                res.append(num)
            except ValueError:
                break
        for i in range(1, len(res)):
            res[i] += length + res[i-1]
        return res

    def filter_oneline_anno(self, data_code_temp):
        length_code_line = len(data_code_temp)
        for i in range(length_code_line):
            if '#' in data_code_temp[i]:
                data_code_line = data_code_temp[i]
                if '"' in data_code_line or "'" in data_code_line:
                    list_index_1_qm = np.array(self.find_all_element_uncross(data_code_line, "'"))
                    list_index_2_qm = np.array(self.find_all_element_uncross(data_code_line, '"'))
                    list_index_1_anno = np.array(self.find_all_element_uncross(data_code_line, "'''"))
                    list_index_2_anno = np.array(self.find_all_element_uncross(data_code_line, '"""'))
                    list_index_anno = np.array(self.find_all_element_uncross(data_code_line, '#'))
                    if len(list_index_1_anno) + len(list_index_2_anno) > 0:
                        for j in list_index_anno:
                            if len(list_index_1_anno[list_index_1_anno < j]) > 0:
                                if len(list_index_1_anno[list_index_1_anno > j]) > 0:
                                    data_code_temp[i] = '\n'
                                    break
                                else:
                                    if len(list_index_1_qm[list_index_1_qm < j]) % 2 == 1 and len(list_index_2_qm[list_index_2_qm < j]) % 2 == 0:
                                        data_code_temp[i] = data_code_line[:j] + '\n'
                                        break
                            elif len(list_index_2_anno[list_index_2_anno < j]) > 0:
                                if len(list_index_2_anno[list_index_2_anno > j]) > 0:
                                    data_code_temp[i] = '\n'
                                    break
                                else:
                                    if len(list_index_1_qm[list_index_1_qm < j]) % 2 == 0 and len(list_index_2_qm[list_index_2_qm < j]) % 2 == 1:
                                        data_code_temp[i] = data_code_line[:j] + '\n'
                                        break
                            else:
                                if len(list_index_1_qm[list_index_1_qm < j]) % 2 == 0 and len(list_index_2_qm[list_index_2_qm < j]) % 2 == 0:
                                    data_code_temp[i] = data_code_line[:j] + '\n'
                                    break
                    else:
                        for j in list_index_anno:
                            if len(list_index_1_qm[list_index_1_qm < j]) % 2 == 0 and len(list_index_2_qm[list_index_2_qm < j]) % 2 == 0:
                                data_code_temp[i] = data_code_line[:j] + '\n'
                                break
                else:
                    index_annot = data_code_line.index('#')
                    data_code_temp[i] = data_code_line[:index_annot] + '\n'
        return data_code_temp

    def filter_multiline_anno(self, data_code_temp):
        index_code_line_1 = [] # '
        index_code_line_2 = [] # "
        use_code = [-1, -1]
        length_code_line = len(data_code_temp)
        for i in range(length_code_line):
            judge_anno = True
            if "'''" in data_code_temp[i]:
                code_line = data_code_temp[i]
                list_anno_flag = self.find_all_element_uncross(code_line, "'''")
                if len(list_anno_flag) >= 2:
                    data_code_temp[i] = '\n'
                else:
                    if use_code[0] != -1:
                        use_code[0] = -1
                    else:
                        index_anno_flag = list_anno_flag[0]
                        if len(index_code_line_1) % 2 == 0:
                            for j in code_line[:index_anno_flag]:
                                if j != '\t' or j != ' ':
                                    use_code[1] = i
                                    judge_anno = False
                        else:
                            for j in code_line[index_anno_flag+3:]:
                                if j != '\t' or j != ' ' or j!='\n':
                                    use_code[1] = i
                                    judge_anno = False
                                    break
                        if judge_anno:
                            index_code_line_1.append(i)


        for i in range(length_code_line):
            judge_anno = True
            if '"""' in data_code_temp[i]:
                code_line = data_code_temp[i]
                list_anno_flag = self.find_all_element_uncross(code_line, '"""')
                if len(list_anno_flag) >= 2:
                    data_code_temp[i] = '\n'
                else:
                    if use_code[1] != -1:
                        use_code[1] = -1
                    else:
                        index_anno_flag = list_anno_flag[0]
                        if len(index_code_line_2) % 2 == 0:
                            for j in code_line[:index_anno_flag]:
                                if j != '\t' or j != ' ':
                                    use_code[1] = i
                                    judge_anno = False
                        else:
                            for j in code_line[index_anno_flag+3:]:
                                if j != '\t' or j != ' ' or j!='\n':
                                    use_code[1] = i
                                    judge_anno = False
                                    break
                        if judge_anno:
                            index_code_line_2.append(i)

        for i in range(len(index_code_line_1) // 2):
            for j in range(index_code_line_1[2*i], index_code_line_1[2*i+1] + 1):
                data_code_temp[j] = '\n'
        for i in range(len(index_code_line_2) // 2):
            for j in range(index_code_line_2[2*i], index_code_line_2[2*i+1] + 1):
                data_code_temp[j] = '\n'
        return data_code_temp

    def fix_nonstandard_line_head(self, data_code_temp):
        length_code_line = len(data_code_temp)
        data_code_res = []
        for i in range(length_code_line):
            num_tab = 0
            code_line = data_code_temp[i]
            for j in code_line:
                if j != '\t' and j != ' ':
                    break
                else:
                    if j == '\t':
                        num_tab += 1
            data_code_temp[i] = num_tab*self.tab_width*' ' + code_line[num_tab:]
        return data_code_temp

    def filter_redun_space(self, data_code_temp):
        length_code_line = len(data_code_temp)
        data_code_res = []
        for i in range(length_code_line):
            code_line = data_code_temp[i]
            judge = False
            for j in range(1, len(code_line) + 1):
                if code_line[-j] != ' ' and code_line[-j] != '\t' and code_line[-j] != '\n':
                    judge = True
                    break
            if judge:
                data_code_temp[i] = code_line[:-j+1]
            else:
                data_code_temp[i] = ''
        for i in data_code_temp:
            if i != '':
                data_code_res.append(i)
        return data_code_res

    def hash_list(self, cache):
        res = ''
        for i in cache:
            res += i
        return self.hash_std.hash(res)

    def hash_system(self, dic):
        res = ''
        list_key = dic.keys()
        if 'file' in list_key:
            dic_data = dic['file']
            judge = 0
        elif 'dir' in list_key:
            dic_data = dic['dir']
            judge = 1
        else:
            dic_data = {'files': dic['files'], 'dirs': dic['dirs']}
            judge = 2
        for i in dic_data:
            try:
                if judge:
                    res += dic_data[i]['hash_code']
                else:
                    res += dic_data[i]['hash_code'][0]
            except:
                pass
        return self.hash_std.hash(res)


if __name__ == '__main__':
    ana = AnalyCode()
    dic_res = ana.run('test')
    print(dic_res)
    pickle.dump(dic_res, open('db', 'wb'))
    print('Done')

