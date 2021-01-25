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

