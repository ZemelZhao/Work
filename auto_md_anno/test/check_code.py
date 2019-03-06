import os
import pickle
from hash_std import HashStd
from ver_control import VerControl

class CodeCheck:
    def __init__(self):
        self.hash_std = HashStd()
        self.create_special_hash_code()

    def create_special_hash_code(self):
        self.hash_code_empty = self.hash_std.hash('')

    def run(self, dic_new, dic_old=None):
        dic_res = self.check_all(dic_new, dic_old)
        return dic_res

    def check_all(self, dic_new, dic_old=None):
        dic_res = {'name': 0, 'files': {}, 'dirs':{}}
        dic_res['name'] = dic_new['name']
        if dic_old:
            if dic_new['hash_code'] == dic_old['hash_code']:
                return {}
            else:
                dic_files_new = dic_new['files']
                dic_files_old = dic_old['files']
                dic_dirs_new = dic_new['dirs']
                dic_dirs_old = dic_old['dirs']
                dic_res['files'] = self.check_files(dic_files_new, dic_files_old)
                dic_res['dirs'] = self.check_dirs(dic_dirs_new, dic_dirs_old)
        else:
            dic_files_new = dic_new['files']
            dic_dirs_new = dic_new['dirs']
            dic_res['files'] = self.check_files(dic_files_new, {})
            dic_res['dirs'] = self.check_dirs(dic_dirs_new, {})

        return dic_res

    def check_dirs(self, dic_new, dic_old=None):
        dic_res = {'modify':{}, 'add':{}, 'delete':[]}
        if dic_old and dic_new:
            if dic_old['hash_code'] == dic_new['hash_code']:
                return {}
            else:
                dic_dir_new = dic_new['dir']
                dic_dir_old = dic_old['dir']
                list_dir_new = sorted(dic_dir_new.keys())
                list_dir_old = sorted(dic_dir_old.keys())
                for i in list_dir_old[:]:
                    if i in list_dir_new:
                        list_dir_new.remove(i)
                        if dic_dir_new[i]['hash_code'] != dic_dir_old[i]['hash_code']:
                            dic_res['modify'][i] = self.check_files(dic_new[i], dic_old[i])
                    else:
                        dic_res['delete'].append(i)
                for i in list_dir_new[:]:
                    dic_res['add'][i] = self.check_files(dic_dir_new[i], {})
        elif dic_new:
                dic_dir_new = dic_new['dir']
                list_dir_new = sorted(dic_dir_new.keys())
                for i in list_dir_new[:]:
                    dic_res['add'][i] = self.check_files(dic_dir_new[i], {})
        elif dic_old:
                dic_dir_old = dic_old['dir']
                list_dir_old = sorted(dic_dir_old.keys())
                for i in list_dir_old[:]:
                    dic_res['delete'].append(i)
        else:
            dic_res = {}
        return dic_res

    def check_files(self, dic_new, dic_old=None):
        dic_res = {'modify': {}, 'add': {}, 'delete':[]}
        if dic_new and dic_old:
            if dic_new['hash_code'] == dic_old['hash_code']:
                return {}
            else:
                dic_file_new = dic_new['file']
                dic_file_old = dic_old['file']
                list_file_new = sorted(dic_file_new.keys())
                list_file_old = sorted(dic_file_old.keys())
                for i in list_file_old[:]:
                    if i in list_file_new:
                        list_file_new.remove(i)
                        if dic_file_new[i]['hash_code'] != dic_file_old[i]['hash_code']:
                            dic_res['modify'][i] = self.check_file(dic_file_new[i], dic_file_old[i])
                    else:
                        dic_res['delete'][i] = self.check_file({}, dic_file_old[i])
                for i in list_file_new[:]:
                    dic_res['add'][i] = self.check_file(dic_file_new[i], {})
        elif dic_old:
            dic_file_old = dic_old['file']
            list_file_old = sorted(dic_file_old.keys())
            for i in list_file_old:
                dic_res['delete'].append(i)
        elif dic_new:
            dic_file_new = dic_new['file']
            list_file_new = sorted(dic_file_new.keys())
            for i in list_file_new:
                dic_res['add'][i] = self.check_file(dic_file_new[i], {})
        else:
            dic_res = {}
        return dic_res

    def check_file(self, dic_new, dic_old=None):
        dic_res = {'import':False, 'execute':False,
                   'define':{'func':{'modify':[], 'add':[], 'delete':[]},
                             'class':{'modify':{}, 'add':{}, 'delete':[]}}}
        if dic_old and dic_new:
            list_hash_old = dic_old['hash_code']
            list_hash_new = dic_new['hash_code']
            if list_hash_old[1] != list_hash_new[1]:
                if list_hash_old[1] == self.hash_code_empty:
                    dic_res['import'] = 'add'
                elif list_hash_new[1] == self.hash_code_empty:
                    dic_res['import'] = 'delete'
                else:
                    dic_res['import'] = 'modify'
            if list_hash_old[3] != list_hash_new[3]:
                if list_hash_old[3] == self.hash_code_empty:
                    dic_res['execute'] = 'add'
                elif list_hash_new[3] == self.hash_code_empty:
                    dic_res['execute'] = 'delete'
                else:
                    dic_res['execute'] = 'modify'
            if list_hash_old[2] != list_hash_new[2]:
                dic_func_new = dic_new['func']
                dic_func_old = dic_old['func']
                dic_class_new = dic_new['class']
                dic_class_old = dic_old['class']
                list_func_new = sorted(dic_func_new.keys())
                list_func_old = sorted(dic_func_old.keys())
                list_class_new = sorted(dic_class_new.keys())
                list_class_old = sorted(dic_class_old.keys())
                for i in list_func_old[:]:
                    if i in list_func_new:
                        list_func_new.remove(i)
                        if dic_func_new[i]['hash_code'] != dic_func_old[i]['hash_code']:
                            dic_res['define']['func']['modify'].append(i)
                    else:
                        dic_res['define']['func']['delete'].append(i)
                for i in list_func_new[:]:
                    dic_res['define']['func']['add'].append(i)
                for i in list_class_old[:]:
                    if i in list_class_new:
                        list_class_new.remove(i)
                        if dic_class_new[i]['hash_code'] != dic_class_old[i]['hash_code']:
                            dic_res['define']['class']['modify'][i] = self.check_class(dic_class_new[i], dic_class_old[i])
                    else:
                        dic_res['define']['class']['delete'].append(i)
                for i in list_class_new[:]:
                    dic_res['define']['class']['add'][i] = self.check_class(dic_class_new[i], {})
        elif dic_new:
            dic_func_new = dic_new['func']
            dic_class_new = dic_new['class']
            list_func_new = sorted(dic_func_new.keys())
            list_class_new = sorted(dic_class_new.keys())
            for i in list_class_new:
                dic_res['define']['class']['add'][i] = self.check_class(dic_class_new[i], {})
            for i in list_func_new:
                dic_res['define']['func']['add'].append(i)
        else:
            dic_res = {}
        return dic_res

    def check_class(self, dic_new, dic_old=None):
        dic_res = {'modify': [], 'add': [], 'delete':[]}
        if dic_new and dic_old:
            dic_func_new = dic_new['func']
            dic_func_old = dic_old['func']
            list_func_new = sorted(dic_func_new.keys())
            list_func_old = sorted(dic_func_old.keys())
            for i in list_func_old[:]:
                if i in list_func_new:
                    list_func_new.remove(i)
                    if dic_func_new[i]['hash_code'] != dic_func_old[i]['hash_code']:
                        dic_res['modify'].append(i)
                else:
                    dic_res['delete'].append(i)
            for i in list_func_new[:]:
                dic_res['add'].append(i)
        elif dic_new:
            dic_func_new = dic_new['func']
            list_func_new = sorted(dic_func_new.keys())
            for i in list_func_new[:]:
                dic_res['add'].append(i)
        else:
            dic_res = {}
        return dic_res


if __name__ == '__main__':
    ver_control = VerControl()
    dir_name = 'test_check'
    path_name = os.path.join('.AutoAnno', dir_name)
    dic_old = pickle.load(open(os.path.join(path_name, 'db_0.0.0'), 'rb'))
    list_file = sorted(os.listdir(path_name))
    lastest_version = ver_control.run(list_file)[0]
    dic_new = pickle.load(open(os.path.join(path_name, 'db_%s' % lastest_version), 'rb'))
    code_check = CodeCheck()
    code_check.run(dic_new, dic_old)
