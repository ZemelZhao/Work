import os

class VerControl:

    def run(self, cache_list):
        last_version = self.get_lastest_version(cache_list)
        new_version = self.get_new_version(last_version)
        str_last_version = '%d.%d.%d' % (last_version[0], last_version[1], last_version[2])
        str_new_version = '%d.%d.%d' % (new_version[0], new_version[1], new_version[2])
        return str_last_version, str_new_version

    def get_lastest_version(self, cache_list):
        for i in range(len(cache_list)):
            data_name = cache_list[i]
            data_version = data_name[-(data_name[::-1].index('_')):]
            list_version = [int(i) for i in data_version.split('.')]
            cache_list[i] = list_version
        return sorted(cache_list)[-1]

    def get_new_version(self, cache_list, ltype=0):
        cache_res = cache_list[:]
        if ltype == 0:
            cache_res[2] += 1
        elif ltype == 1:
            cache_res[1] += 1
            cache_res[2] = 0
        else:
            cache_res[0] += 1
            cache_res[1] = 0
            cache_res[2] = 0
        return cache_res



if __name__ == '__main__':
    ver_control = VerControl()
