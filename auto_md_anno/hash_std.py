import hashlib as hb

class HashStd:
    def __init__(self, htype=1):
        self.list_htype = [hb.md5, hb.sha1, hb.sha224, hb.sha256, hb.sha384, hb.sha512]
        self.htype = self.list_htype[htype]

    def hash(self, data):
        return self.htype(data.encode('utf8')).hexdigest()

if __name__ == '__main__':
    hs = HashStd(1)
    a = hs.hash('')



