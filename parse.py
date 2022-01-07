# https://github.com/drkwng/check-whois
# https://t.me/drkwng
# Whois Data Parser


import re

import socket
from urllib.parse import urlparse


class GetWhois:
    def __init__(self):
        self.inter_zones = ['com', 'net', 'edu']

    @classmethod
    def get_domain(cls, url):
        """
        Get domain name from URL
        :param url: str
        :return: str
        """
        if 'http' not in url:
            url = f'http://{url}'
        if 'www' in url:
            url = url.replace('www.', '')

        domain = urlparse(url).netloc

        return domain

    @staticmethod
    def get_whois_service(response):
        """
        Get Whois service to send request
        :param response: bytes
        :return: str
        """
        try:
            service = re.search(r'whois:*(\S+)', response.decode()).group(0)
        except AttributeError:
            service = ''

        return service

    @staticmethod
    def get_whois(domain, service):
        """
        Send request to get Whois data by domain name
        :param domain: str
        :param service: str
        :return: bytes
        """
        whois_raw = b""

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            try:
                s.connect((service, 43))
                s.send((domain + "\r\n").encode())
                while True:
                    data = s.recv(4096)
                    whois_raw += data
                    if not data:
                        break

            except Exception as e:
                print(e, type(e))

        return whois_raw

    def worker(self, url):
        """
        :param url: str
        :return: str
        """
        domain = self.get_domain(url)
        if domain.split('.')[-1] in self.inter_zones:
            service = 'whois.verisign-grs.com'
            whois_data = self.get_whois(domain, service).decode()
        else:
            whois_service = self.get_whois(domain, 'whois.iana.org')
            service = self.get_whois_service(whois_service)
            whois_data = self.get_whois(domain, service).decode()

        return whois_data


if __name__ == '__main__':
    import sys
    from time import sleep

    get_whois = GetWhois()
    urls = sys.argv[1:]
    for u in urls:
        print(get_whois.worker(u))
        sleep(2)

