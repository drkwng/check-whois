# Whois Bulk Check Tool by @drkwng
# https://github.com/drkwng/check-whois
# https://t.me/drkwng


import json
import csv

from time import sleep

from pprint import pprint

from parse import GetWhois
from process import get_regex, scrape_whois


def write_data(domain, data, mode, res_file='whois_result.csv'):
    """
    Write data into CSV file
    :param domain: str
    :param data: dict
    :param mode: str
    :param res_file: str
    :return:
    """
    with open(res_file, mode, encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        if mode == 'w':
            header = ['domain', 'status', 'creation_date', 'expiration_date', 'updated_date', 'name_servers']
            writer.writerow(header)

        row = [
            domain, data['status'], data['creation_date'],
            data['expiration_date'], data['updated_date'],
            data['name_servers']
        ]
        writer.writerow(row)


def worker(file):
    with open(file, 'r', encoding='utf-8') as f:

        # Get list of domains
        _domains = []
        for line in f:
            _domains.append(GetWhois.get_domain(line.strip()))

        get_whois = GetWhois()

        for num, i in enumerate(_domains):
            try:
                data = get_whois.worker(i)

                regex = get_regex(i)
                whois_data = scrape_whois(data, regex)
                write_data(i, whois_data, 'w' if num == 0 else 'a')

                pprint([i, whois_data])
                print('\n==================\n')
                sleep(2)

            except Exception as e:
                print(i, e)


if __name__ == '__main__':
    domains = 'domains.txt'
    worker(domains)

