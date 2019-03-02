import os
import pickle

class WriteDocument:
    def __init__(self):
        pass

    def run(self, data, version='0.0.0'):
        data = pickle.load(open('db', 'rb'))
        document_file = 'Document_%s_%s.md' % (data['name'], version)
        self.version = version
        self.markdown_result = ''
        self.make_doc_markdown(data)
        with open(document_file, 'w') as f:
            f.write(self.markdown_result)


    def make_table_introduce_all(self, dic):
        res_str = ''
        dic_files = dic['files']
        dic_dirs = dic['dirs']
        list_files = sorted(dic_files.keys())
        list_dirs = sorted(dic_dirs.keys())
        if len(list_files):
            res_str += '__文件__\n'
            res_str += self.make_table_file_intro(dic_files)
            res_str += '__文件夹__\n'
            res_str += self.make_table_dir_intro(dic_dirs)
        return res_str

    def make_table_file_intro(self, dic):
        res_str = ''
        res_str += '|No.|FileName|Note|ClassNum|FuncNum|\n'
        res_str += '|:-:'*5 + '|\n'
        list_file = sorted(dic.keys())
        for i in range(len(list_file)):
            index = i + 1
            file_name = list_file[i]
            note = ''
            num_class = len(dic[list_file[i]]['class'])
            num_func = len(dic[list_file[i]]['func'])
            res_str += '|%d|%s|%s|%d|%d|\n' % (index, file_name, note, num_class, num_func)
        return res_str

    def make_table_dir_intro(self, dic):
        res_str = ''
        res_str += '|No.|DirName|Note|FileNum|\n'
        res_str += '|:-:'*4 + '|\n'
        list_dir = sorted(dic.keys())
        print(dic)
        for i in range(len(list_dir)):
            index = i + 1
            dir_name = list_dir[i]
            note = ''
            num_file = len(dic[list_dir[i]])
            res_str += '|%d|%s|%s|%d|\n' % (index, dir_name, note, num_file)
        return res_str

    def make_doc_markdown(self, dic):
        self.markdown_result += self.make_section_lv1(dic)

    def make_section_lv1(self, dic):
        res_str = ''
        res_str += '# Version %s\n' % (self.version)
        res_str += '软件说明: \n\n\n\n'
        res_str += '本文档将按照各文件、文件夹顺序逐一叙述\n'
        res_str += self.make_table_introduce_all(dic)
        return res_str


    def make_section_lv2(self, dic):
        pass

    def make_section_lv3(self, dic):
        pass

    def make_section_lv4(self, dic):
        pass



if __name__ == '__main__':
    a = WriteDocument()
    a.run(1)
