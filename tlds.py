# Some RegExs taken from @DanyCork (python-whois)
# https://github.com/DannyCork/python-whois
# Scrape Whois Data RegExp For TLDs


base = {
    'parent': None,

    'registrar': r'Registrar:\s?(.+)',
    'registrant': r'Registrant\s*Organi(?:s|z)ation:\s?(.+)',
    'registrant_country': r'Registrant Country:\s?(.+)',

    'creation_date': r'Creation Date:\s?(.+)',
    'expiration_date': r'Registry Expiry Date:\s?(.+)',
    'updated_date': r'Updated Date:\s?(.+)',

    'name_servers': r'Name Server:\s*(.+)\s*',
    'status': r'Status:\s?(.+)',
    'emails': r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

com = co = edu = net = io = info = biz = org = name = pro = website = club = travel = base

mobi = {
    'parent': 'base',

    'expiration_date': r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date': r'\nUpdated Date:\s?(.+)',
}

online = {
    'parent': 'base',

    'registrar': r'Registrar:\s*(.+)',

    'creation_date': r'Creation Date:\s?(.+)',
    'expiration_date': r'Registry Expiry Date:\s?(.+)',
    'updated_date': r'Updated Date:\s?(.+)',

    'status': r'Status:\s?(.+)',
}

cc = {
    'parent': 'base',

    'registrar': r'Registrar:\s*(.+)',

    'creation_date': r'created:\s+(\S+)',
    # 'expiration_date': r'Registry Expiry Date:\s?(.+)',
    'updated_date': r'changed:\s+(\S+)',

    'name_servers': r'nserver:\s*(.+)\s*',
    'status': r'status:\s+(.+)',
}

################
# RU / UA / KZ
################
ua = {
    'parent': 'base',

    'registrar': r'\nregistrar:\s*(.+)',
    'registrant_country': r'\ncountry:\s*(.+)',

    'creation_date': r'\ncreated:\s*(.+)',
    'expiration_date': r'\nexpires:\s*(.+)',
    'updated_date': r'\nmodified:\s*(.+)',

    'name_servers': r'\nnserver:\s*(.+)',
    'status': r'\nstatus:\s*(.+)',
}

ru = {
    'parent': 'base',

    'creation_date': r'\ncreated:\s*(.+)',
    'expiration_date': r'\npaid-till:\s*(.+)',

    'name_servers': r'\nnserver:\s*(.+)',
    'status': r'\nstate:\s*(.+)',
}

su = {
    'parent': 'ru',
}

ru_rf = {
    'parent': 'ru',
}

kz = {
    'parent': None,

    'registrar': r'Current Registar:\s?(.+)',
    'registrant': r'Organization Name\.+:\s?(.+)',
    'registrant_country': r'Country\.+:\s?(.+)',

    'creation_date': r'Domain created:\s?(.+)',
    'updated_date': r'Last modified :\s?(.+)',

    'name_servers': r'\s* server\.+:\s*(.+)\s*',
    'status': r'Domain status :\s?(.+)',
    'emails': r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

################
# USA / Canada
################

us = {
    'parent': 'base',
    'registrant': r'Registrant Name:\s?(.+)',
    'status': r'DNSSEC:\s?(.+)'
}

ca = {
    'parent': 'base',
}

################
# EUROPE
################
eu = {
    'parent': 'base',

    'registrant': r'Registrant:\n\s*(.+)',
    'registrar': r'Registrar:\n\s*Name: (.+)',

    # Bad RegEx - only 2 NS (correct it if you can)
    'name_servers': r'Name servers:\n(?:\s+(\S+)\n)(?:\s+(\S+)\n)'
}

uk = {
    'parent': 'base',

    # No effect
    'registrant': r'Registrant:\n\s*(.+)',

    'creation_date': r'Registered on:\s*(.+)',
    'expiration_date': r'Expiry date:\s*(.+)',
    'updated_date': r'Last updated:\s*(.+)\r',

    # No effect
    'status': r'Registration status:\n\s*(.+)',
}
