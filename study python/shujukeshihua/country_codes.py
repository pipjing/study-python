# coding:utf8
from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """根据制定国家，返回两个字母的国别码"""
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    return None



