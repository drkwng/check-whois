# https://github.com/drkwng/check-whois
# https://t.me/drkwng
# Whois Process Functions


import re
import tlds


def get_full_regex(domain):
    """
    Get full RegExp from tlds.py
    :param domain: str
    :return: dict
    """
    print(domain)
    if re.match("^.*(.com|.net|.pro|.website)$", domain):
        tld = 'base'
    elif domain.endswith('.xn--p1ai'):
        tld = 'ru_rf'
    else:
        tld = domain.split('.')[-1]

    if getattr(tlds, tld)['parent']:
        parent_tld = getattr(tlds, tld)['parent']
        regex = {**getattr(tlds, parent_tld), **getattr(tlds, tld)}
    else:
        regex = getattr(tlds, tld)

    return regex


def scrape_whois(data, whois_regex):
    """
    Scraper Whois data by RegExp
    :param data: str
    :param whois_regex: dict
    :return: dict
    """
    whois_result = {}
    for field, regex in whois_regex.items():
        whois_result[field] = ['']
        if regex is not None:
            whois_result[field] = re.findall(regex, data)

    return whois_result
