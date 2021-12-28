import re

# 凯撒密码
def caesar(t, n, keys='abcdefghijklmnopqrstuvwxyz'):
    s = list(keys)
    r = ''
    for i in t:
        if i in s:
            r += s[(s.index(i) + n)% len(keys)]
        else:
            r += i
    return r


# 摩斯密码
def morse_dec(string, a='.', b='-', p=None):
    morse = {
        '.-'  :'A', '-...':'B', '-.-.':'C', '-..' :'D', '.'   :'E',
        '..-.':'F', '--.' :'G', '....':'H', '..'  :'I', '.---':'J',
        '-.-':'K', '.-..' : 'L', '--' :'M', '-.' :'N', '---':'O',
        '.--.' : 'P', '--.-' : 'Q', '.-.':'R', '...':'S', '-'  :'T',
        '..-':'U', '...-' : 'V', '.--':'W', '-..-' : 'X', '-.--' : 'Y',
        '--..' : 'Z', '.----' : '1', '..---' : '2', '...--' : '3',
        '....-' : '4', '.....' : '5', '-....' : '6', '--...' : '7',
        '---..' : '8','----.' : '9','-----' : '0',
        '-...-' : '=', '.-.-':'~', '.-...' :'<AS>', '.-.-.' : '<AR>', '...-.-' : '<SK>',
        '-.--.' : '<KN>', '..-.-' : '<INT>', '....--' : '<HM>', '...-.' : '<VE>',
        '.-..-.' : '\\', '.----.' : '\'', '...-..-' : '$', '-.--.' : '(', '-.--.-' : ')',
        '--..--' : ',', '-....-' : '-', '.-.-.-' : '.', '-..-.' : '/', '---...' : ':',
        '-.-.-.' : ';', '..--..' : '?', '..--.-' : '_', '.--.-.' : '@', '-.-.--' : '!'
    }
    _a, _b = '.', '-'
    _names = string.split() if p is None else string.split(p)
    r = []
    for ps in _names:
        ps = ps.replace(a, _a).replace(b, _b)
        ge = morse.get(ps)
        if ge:
            r.append(ge)
        else:
            r.append('[undefined:{}]'.format(ps))
    return ''.join(r)

def morse_enc(string, a='.', b='-', p=None):
    morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P':
        '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
        'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        '=': '-...-', '~': '.-.-', '<AS>': '.-...', '<AR>': '.-.-.',
        '<SK>': '...-.-', '(': '-.--.', '<INT>': '..-.-', '<HM>': '....--',
        '<VE>': '...-.', '\\': '.-..-.', "'": '.----.', '$': '...-..-',
        ')': '-.--.-', ',': '--..--', '-': '-....-', '.': '.-.-.-', '/': '-..-.',
        ':': '---...', ';': '-.-.-.', '?': '..--..', '_': '..--.-', '@': '.--.-.', '!': '-.-.--'
    }
    _a, _b = '.', '-'
    r = []
    for i in string:
        if i.upper() in morse:
            v = morse[i.upper()].replace(_a, a).replace(_b, b)
        else:
            v = '[undefined:{}]'.format(i)
        r.append(v)
    return ' '.join(r) if p is None else p.join(r)


# 栅栏密码
def rail_fence_enc(string, n, padding=None):
    b = []
    q = []
    for idx,i in enumerate(string, 1):
        q.append(i)
        if idx % n == 0:
            b.append(q)
            q = []
    r = []
    if q:
        for i in '~!@#$%^&*': # 自动选一个padding进行处理
            if i not in string:
                padding = i
                break
        if padding is None:
            raise ('cannot find a padding, cos ~!@#$%^&* all in string.')
        q += [padding] * (n - len(q))
        b.append(q)
    for i in zip(*b):
        r.extend(i)
    return ''.join(r), padding

def rail_fence_dec(string, n, padding=None):
    a = len(string)/n
    b = len(string)//n
    n = b if a == b else b+1
    b = []
    for i in range(0,n):
        b.append(string[i::int(n)])
    r = []
    for i in zip(b):
        r.extend(i)
    return ''.join(r).rstrip(padding)


# ook!
def parse_ook_to_brainfuckmap(string, abc=('!', '?', '.')):
    maps = {
        ('!', '?'): '[',
        ('?', '!'): ']',
        ('.', '.'): '+',
        ('!', '!'): '-',
        ('.', '?'): '>',
        ('?', '.'): '<',
        ('!', '.'): '.',
        ('.', '!'): ',',
    }
    a, b, c = [i if i not in r'$()*+.[]?\/^{}' else '\\'+i for i in abc]
    rexgep = '|'.join([a, b, c])
    v = re.findall(rexgep, string)
    r = []
    for i in zip(v[::2],v[1::2]):
        t = [j.replace(a[-1], '!')\
              .replace(b[-1], '?')\
              .replace(c[-1], '.') for j in i]
        t = tuple(t)
        r.append(maps.get(t))
    return ''.join(r)

