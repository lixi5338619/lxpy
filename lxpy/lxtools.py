# -*- coding: utf-8 -*-
# @Author  : lx

import re

def html_format(string):
    """ html去除标签 """
    dr = re.compile(r'<[^>]+>', re.S)
    not_format = dr.sub('', string)
    return not_format


def jsonp_to_json(jsonp):
    result = re.findall(r'\w+[(]{1}(.*)[)]{1}',jsonp,re.S)
    return result


def re_xpath(node,compile):
    """
    :param compile: './/span[re:match(@class, "allstar(\d0)")]/@class'
    """
    namespaces = {"re": "http://exslt.org/regular-expressions"}
    result = node.xpath(compile, namespaces=namespaces)
    return result


def url_parse(url:str):
    # 提取url中的params参数，返回item
    p = url.split('?')[1]
    item = {}
    if '&' in p:
        param = p.split('&')
        for v in param:
            k = v.split('=')
            item[k[0]] = k[1]
    else:
         k = p.split('=')
         item[k[0]] = k[1]
    return item


