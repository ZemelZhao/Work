import os

class CodeCheck:
    def __init__(self):
        pass

    def run(self, dic_new, dic_old=None):
        dic_res = self.check_all(dic_new, dic_old)

        return dic_res

    def check_all(self, dic_new, dic_old=None):
        dic_res = {'files': {}, 'dirs':{}}
        if dic_old == None:
            dic_res = dic_new
        else:
            if dic_new['hash_code'] == dic_old['hash_code']:
                return {}
            else:
                dic_files_new = dic_new['files']
                dic_files_old = dic_old['files']
                dic_dirs_new = dic_new['dirs']
                dic_dirs_old = dic_old['dirs']
                dic_res['files'] = self.check_files(self.dic_files_new, self.dic_files_old)
                dic_res['dirs'] = self.check_dirs(self.dic_dirs_new, self.dic_dirs_old)

    def check_dirs(self, dic_new, dic_old=None):
        dic_res = {}
        if dic_old == None:
            pass
        else:
            pass

    def check_files(self, dic_new, dic_old=None):
        dic_res = {'modify': {}, 'add': {}, 'delete':{}}
        if dic_old == None:
            pass
        else:
            if dic_new['hash_code'] == dic_old['hash_code']:
                return {}
            else:
                dic_file_new = dic_new['file']
                dic_file_old = dic_old['file']
                list_file_new = sorted(dic_file_new.keys())
                list_file_old = sorted(dic_file_old.keys())
                list_add = []
                list_modify = []
                list_delete = []
                for i in list_file_old[:]:
                    if i in list_file_new:
                        list_file_new.remove(i)
                        if dic_files_new[i]['hash_code'] != dic_files_old[i]['hash_code']:
                            list_modify.append(i)
                    else:
                        list_delete.append(i)
                list_add = list_file_new[:]

    def check_file(self, dic_new, dic_old=None):
        dic_res = {'import':False, 'execute':False, 'define':{'modify':{}, 'add':{}, 'delete':{}}}

    def check_class(self, dic_new, dic_old=None):
        dic_res = {'modify': {}, 'add': {}, 'delete':{}}

    def check_func(self, dic_new, dic_old=None):
        dic_res = {'modify': {}, 'add': {}, 'delete':{}}

