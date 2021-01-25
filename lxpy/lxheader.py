# -*- coding: utf-8 -*-
# @Author  : lx

def copy_headers_dict(headers_raw):
    """ headers Converts
    Example:
     copy_headers = '''
          accept-encoding: gzip
          accept-language: zh-CN
          upgrade-insecure-requests: 1
          user-agent: Mozilla/5.0 Safari/537.36
        '''
     print(headers_raw_to_dict(copy_headers))
    """
    if headers_raw is None:
        return None

    headers = headers_raw.splitlines()
    headers_tuples = [header.split(":", 1) for header in headers]

    result_dict = {}
    for header_item in headers_tuples:
        if not len(header_item) == 2:
            continue

        item_key = header_item[0].strip()
        item_value = header_item[1].strip()
        result_dict[item_key] = item_value

    return result_dict




import random
def get_ua():
    """Get some user-agent ,But not necessarily accepted by the website"""
    first_num = random.randint(55, 62)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)
    os_type = [
        '(Windows NT 6.1; WOW64)',
        '(Windows NT 10.0; WOW64)',
        '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)
    ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                  )
    userAgent = {"user-agent":ua}
    return userAgent
