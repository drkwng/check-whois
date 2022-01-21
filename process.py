# https://github.com/drkwng/check-whois
# https://t.me/drkwng
# Get RexExp And Whois Process Functions

import re
import tlds


def update_dicts(list_of_dicts):
    final_dict = {}
    for elem in list_of_dicts:
        for key, value in elem.items():
            final_dict[key] = value

    final_dict.pop('parent')

    return final_dict


def get_regex(domain):
    """
    Get full RegExp from tlds.py
    :param domain: str
    :return: dict
    """
    zone_slug = domain.split('.')[-1]
    if zone_slug == 'xn--p1ai':
        tld_tmp = 'ru_rf'
    else:
        tld_tmp = zone_slug

    regexp_list = [getattr(tlds, tld_tmp), ]

    while True:
        if getattr(tlds, tld_tmp)['parent']:
            tld_tmp = getattr(tlds, tld_tmp)['parent']
            regexp_list = [getattr(tlds, tld_tmp)] + regexp_list
        else:
            break

    regexp = update_dicts(regexp_list)
    return regexp


def scrape_whois(data, whois_regexp):
    """
    Scraper Whois data by RegExp
    :param data: str
    :param whois_regexp: dict
    :return: dict
    """
    whois_result = {}
    for field, regexp in whois_regexp.items():
        whois_result[field] = ['']
        if regexp is not None:
            whois_result[field] = re.findall(regexp, data)

    return whois_result


if __name__ == '__main__':
    from pprint import pprint

    domain = input('Test regex search from tlds.py\n '
                   'Enter domain name: ').strip()
    regex = get_regex(domain)
    pprint(regex)
