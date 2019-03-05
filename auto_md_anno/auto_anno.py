from analy_code import AnalyCode
from ver_control import VerControl
from write_document import WriteDocument, WriteUpdate
from check_code import CodeCheck
import os
import pickle


if __name__ == '__main__':
    dir_name = 'test'
    analysis_code = AnalyCode()
    version_control = VerControl()
    code_check = CodeCheck()
    write_anno = WriteDocument()
    write_update = WriteUpdate()

    path_name = os.path.join('.AutoAnno', dir_name)
    path_name_record = os.path.join(dir_name, '.AutoAnno')

    try:
        os.makedirs(path_name)
        os.makedirs(path_name_record)
        new_version = '0.0.0'
        dic_old = None
    except FileExistsError:
        list_file = sorted(os.listdir(path_name))
        if len(list_file):
            old_version, new_version = version_control.run(list_file)
            dic_old = pickle.load(open(os.path.join(path_name, 'db_%s' % old_version), 'rb'))
        else:
            new_version = '0.0.0'
            dic_old = {}

    dic_new = analysis_code.run(dir_name)
    judge_code_check = code_check.run(dic_new, dic_old)
    if judge_code_check:
        pickle.dump(dic_new, open(os.path.join(path_name, 'db_%s' % new_version), 'wb'))
        pickle.dump(judge_code_check, open(os.path.join(path_name, 'du_%s' % new_version), 'wb'))
        cache_anno = write_anno.run(dic_new, new_version)
        cache_update = write_update.run(judge_code_check, new_version)
        with open(os.path.join(path_name_record, '%s_%s.md' % (dir_name, new_version)), 'w') as f:
            f.write(cache_anno)
        with open(os.path.join(dir_name, 'README_temp.md'), 'w') as f:
            f.write(cache_anno)
        if new_version == '0.0.0':
            with open(os.path.join(dir_name, 'UpdateLog.md'), 'w') as f:
                f.write(cache_update)
        else:
            with open(os.path.join(dir_name, 'UpdateLog.md'), 'a') as f:
                f.write(cache_update)
    else:
        print('Not Change')
