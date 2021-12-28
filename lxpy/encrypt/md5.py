# -*- coding: utf-8 -*-
# @Author  : lx
# @IDE ：PyCharm
import hashlib
# md5
def get_md5(string):
    m = hashlib.md5()
    m.update(string.encode())
    return m.hexdigest()

