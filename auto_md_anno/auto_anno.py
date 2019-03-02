from analy_code import AnalyCode
from ver_control import VerControl
from write_document import WriteDocument
import os
import pickle


if __name__ == '__main__':
    analysis_code = AnalyCode()
    version_control = VerControl()
    write_anno = WriteDocument()

    dic_anno = analysis_code.run('test_dir')
    pickle.dump(dic_anno, open('db', 'wb'))
    write_anno.run(dic_anno)
