# -*- coding: utf-8 -*-
# @Author  : lx
# @IDE ：PyCharm

# 将js中的 eval 压缩加密的代码还原成压缩前的代码
def parse_evaljs(s):
    import re
    x = r"\}\(('(?:[^'\\]|\\.)*') *, *(\d+) *, *(\d+) *, *'((?:[^'\\]|\\.)*)'\.split\('\|'\) *, *(\d+) *, *(\{\})"
    p, a, c, k, e, d = re.findall(x, s)[0]
    p, a, c, e, k, d = eval(p), int(a), int(c), int(e), k.split('|'), {}
    def evaljs_code(p, a, c, k, e, d):
        def e(c):
            x = '' if c < a else e(int(c/a))
            c = c % a
            return x + (chr(c + 29) if c > 35 else '0123456789abcdefghijklmnopqrstuvwxyz'[c])
        for i in range(c): d[e(i)] = k[i] or e(i)
        return re.sub(r'\b(\w+)\b', lambda e: d.get(e.group(0)) or e.group(0), p)
    return evaljs_code(p, a, c, k, e, d)
