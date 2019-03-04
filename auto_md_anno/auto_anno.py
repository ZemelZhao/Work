from analy_code import AnalyCode
from ver_control import VerControl
from write_document import WriteDocument, WriteUpdate
from check_code import CodeCheck
import os
import pickle


if __name__ == '__main__':
    dir_name = 'test_dir'
    analysis_code = AnalyCode()
    version_control = VerControl()
    write_anno = WriteDocument()
    code_check = CodeCheck()

    path_name = os.path.join('.AutoAnno', dir_name)

    try:
        os.mkdir(path_name)
        version = '0.0.0'
        dic_old = None
    except FileExistsError:
        list_file = sorted(os.listdir(path_name))
        if len(list_file):
            version = version_control.run(list_file[-1])
            dic_old = pickle.load(open(os.path.join(path_name, list_file[-1]), 'rb'))
        else:
            version = '0.0.0'
            dic_old = None

    dic_new = analysis_code.run(dir_name)
    judge_code_check = code_check.run(dic_new, dic_old)
    if judge_code_check:
        pickle.dump(dic_new, open(os.path.join(os.path.join(path_name, 'db_%s' % version)), 'wb'))
    else:
        print('Not Change')
