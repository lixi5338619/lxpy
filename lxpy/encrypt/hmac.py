# -*- coding: utf-8 -*-
# @Author  : lx
# @IDE ：PyCharm

import hmac
import hashlib
# hmac
def get_hamc(key,text,model=hashlib.sha256):
    key = key.encode()
    texts = text.encode()
    mac = hmac.new(key, texts, model)
    mac.digest()
    return mac.hexdigest()
