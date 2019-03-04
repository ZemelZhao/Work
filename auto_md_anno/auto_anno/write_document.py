import os
import pickle

class WriteDocument:
    def __init__(self):
        pass

    def run(self, data, version='0.0.0'):
        document_file = 'Document_%s_%s.md' % (data['name'], version)
        self.version = version
        self.markdown_result = ''
        self.make_doc_markdown(data)
        with open(document_file, 'w') as f:
            f.write(self.markdown_result)


    def make_table_introduce_all(self, dic):
        judge = False
        res_str = ''
        dic_files = dic['files']['file']
        dic_dirs = dic['dirs']['dir']
        list_files = sorted(dic_files.keys())
        list_dirs = sorted(dic_dirs.keys())
        if len(list_files):
            res_str += '__文件__\n'
            res_str += self.make_table_file_intro(dic_files)
            res_str += '__文件夹__\n'
            res_str += self.make_table_dir_intro(dic_dirs)
            judge = True
        if judge:
            return res_str
        else:
            return ''

    def make_table_introduce_file(self, dic):
        judge = False
        res_str = ''
        dic_class = dic['class']
        dic_func = dic['func']
        if len(dic_func):
            res_str += '__函数__\n'
            res_str += self.make_table_func_intro(dic_func)
            judge = True
        if len(dic_class):
            res_str += '__类__\n'
            res_str += self.make_table_class_intro(dic_class)
            judge = True
        if judge:
            return res_str
        else:
            return ''

    def make_table_dir_intro(self, dic):
        judge = False
        res_str = ''
        res_str += '|No.|DirName|FileNum|Note|\n'
        res_str += '|:-:'*4 + '|\n'
        list_dir = sorted(dic.keys())
        for i in range(len(list_dir)):
            judge = True
            index = i + 1
            dir_name = list_dir[i]
            note = ''
            num_file = len(dic[list_dir[i]])
            res_str += '|%d|%s|%d|%s|\n' % (index, self.fix_markdown_str(dir_name), num_file, note)
        if judge:
            return res_str
        else:
            return ''

    def make_table_file_intro(self, dic):
        judge = False
        res_str = ''
        res_str += '|No.|FileName|ClassNum|FuncNum|Note|\n'
        res_str += '|:-:'*5 + '|\n'
        list_file = sorted(dic.keys())
        for i in range(len(list_file)):
            judge = True
            index = i + 1
            file_name = list_file[i]
            note = ''
            num_class = len(dic[list_file[i]]['class'])
            num_func = len(dic[list_file[i]]['func'])
            res_str += '|%d|%s|%d|%d|%s|\n' % (index, self.fix_markdown_str(file_name), num_class, num_func, note)
        if judge:
            return res_str
        else:
            return ''

    def make_table_class_intro(self, dic):
        judge = False
        res_str = ''
        res_str += '|No.|ClassName|SuperClass|FuncNum|Note|\n'
        res_str += '|:-:'*5 + '|\n'
        list_dir = sorted(dic.keys())
        for i in range(len(list_dir)):
            judge = True
            index = i + 1
            class_name = list_dir[i]
            super_class = ''
            for j in dic[class_name]['superclass']:
                super_class += '%s ' % self.fix_markdown_str(j)
            super_class = super_class[:-1]
            note = ''
            num_func = len(dic[list_dir[i]]['func'])
            res_str += '|%d|%s|%s|%d|%s|\n' % (index, self.fix_markdown_str(class_name), self.fix_markdown_str(super_class), num_func, note)
        if judge:
            return res_str
        else:
            return ''

    def make_table_func_intro(self, dic):
        judge = False
        res_str = ''
        res_str += '|No.|FuncName|InputNum|OutputBool|DecorNum|Note|\n'
        res_str += '|:-:'*6 + '|\n'
        list_dir = sorted(dic.keys())
        for i in range(len(list_dir)):
            judge = True
            index = i + 1
            func_name = list_dir[i]
            num_decorator = len(dic[list_dir[i]]['decorator'])
            note = ''
            num_input = len(dic[list_dir[i]]['input'])
            bool_output = str(bool(dic[list_dir[i]]['output']))
            res_str += '|%d|%s|%d|%s|%d|%s|\n' % (index, self.fix_markdown_str(func_name), num_input, bool_output, num_decorator, note)
        if judge:
            return res_str
        else:
            return ''

    def make_table_decorator_intro(self, cache_list):
        judge = False
        res_str = ''
        res_str += '__修饰器__\n'
        res_str += '|No.|DecoratorName|Note|\n'
        res_str += '|:-:'*3 + '|\n'
        for i in range(len(cache_list)):
            judge = True
            index = i + 1
            name_decorator = cache_list[i]
            note = ''
            res_str += '|%d|%s|%s|\n' % (index, self.fix_markdown_str(name_decorator), note)
        if judge:
            return res_str
        else:
            return ''

    def make_table_arg_intro(self, cache_list):
        judge = False
        res_str = ''
        res_str += '__传入参数__\n'
        res_str += '|No.|InputName|Type|Note|\n'
        res_str += '|:-:'*4 + '|\n'
        for i in range(len(cache_list)):
            judge = True
            index = i + 1
            arg_name = cache_list[i]
            type_name = ''
            note = ''
            res_str += '|%d|%s|%s|%s|\n' % (index, self.fix_markdown_str(arg_name), type_name, note)
        if judge:
            return res_str
        else:
            return ''

    def make_doc_markdown(self, dic):
        order = 1
        self.markdown_result += self.make_section_all(dic, 1)
        dic_files = dic['files']['file']
        dic_dirs = dic['dirs']['dir']
        list_file = sorted(dic_files.keys())
        list_dir = sorted(dic_dirs.keys())
        for i in list_file:
            self.markdown_result += self.make_section_flle(dic_files[i], i, 2, order)
            order += 1
        for i in list_dir:
            self.markdown_result += self.make_section_dir(dic_dirs[i], i, 2, order)
            order += 1

    def make_section_all(self, dic, lv):
        res_str = ''
        res_str += '#'*lv + ' Version %s\n' % (self.version)
        res_str += '软件说明: \n\n\n\n'
        res_str += '本文档将按照各文件、文件夹顺序逐一叙述\n'
        res_str += self.make_table_introduce_all(dic)
        return res_str

    def make_section_dir(self, dic, name, lv, order):
        res_str = ''
        res_str += '#'*lv + ' %d. %s\n' % (order, self.fix_markdown_str(name))
        dic_files = dic['file']
        list_file = sorted(dic_files.keys())
        order = 1
        for i in list_file:
            res_str += self.make_section_flle(dic_files[i], i, lv+1, order)
        return res_str

    def make_section_flle(self, dic, name, lv, order):
        res_str = ''
        dic_class = dic['class']
        dic_func = dic['func']
        res_str += '#'*lv + ' %d. %s\n' % (order, self.fix_markdown_str(name))
        res_str += self.make_table_introduce_file(dic)
        list_func = sorted(dic_func)
        list_class = sorted(dic_class)
        order = 1
        for i in list_func:
            res_str += self.make_section_func(dic_func[i], i, lv+1, order)
            order += 1
        for i in list_class:
            res_str += self.make_section_class(dic_class[i], i, lv+1, order)
            order += 1
        return res_str

    def make_section_class(self, dic, name, lv, order):
        res_str = ''
        dic_func = dic['func']
        res_str += '#'*lv + ' %d. %s   (CLASS)\n' % (order, self.fix_markdown_str(name))
        res_str += self.make_table_func_intro(dic['func'])
        list_func = sorted(dic_func)
        order = 1
        for i in list_func:
            res_str += self.make_section_func(dic_func[i], i, lv+1, order)
            order += 1
        return res_str

    def make_section_func(self, dic, name, lv, order):
        res_str = ''
        res_temp = ''
        list_input = dic['input']
        bool_output = bool(dic['output'])
        list_decorator = dic['decorator']
        if len(list_decorator):
            res_temp += self.make_table_decorator_intro(list_decorator)
        if len(list_input):
            res_temp += self.make_table_arg_intro(list_input)
        if bool_output:
            res_temp += '__传出参数__\n'
        if res_temp != '':
            res_str += '#'*lv + ' %d. %s\n' % (order, self.fix_markdown_str(name))
            res_str += res_temp
        return res_str

    def fix_markdown_str(self, data):
        res_str = ''
        for i in data:
            if i == '_':
                res_str += '\_'
            else:
                res_str += i
        return res_str


if __name__ == '__main__':
    a = WriteDocument()
    a.run(pickle.load(open('db', 'rb')))
