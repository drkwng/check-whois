# RegEx taken from @DanyCork (python-whois)
# https://github.com/DannyCork/python-whois
# TLDs Scrape Whois Data RegExps


# COM, NAME, NET, PRO, WEBSITE TLDs
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

ru_rf = {
    'parent': 'base',

    'creation_date': r'\ncreated:\s*(.+)',
    'expiration_date': r'\npaid-till:\s*(.+)',

    'name_servers': r'\nnserver:\s*(.+)',
    'status': r'\nstate:\s*(.+)',
}

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

org = {
    'parent': 'base',

    'expiration_date': r'\nRegistry Expiry Date:\s?(.+)',
    'updated_date': r'\nLast Updated On:\s?(.+)',

    'name_servers': r'Name Server:\s?(.+)\s*',
}

uk = {
    'parent': 'base',

    'registrant': r'Registrant:\n\s*(.+)',

    'creation_date': r'Registered on:\s*(.+)',
    'expiration_date': r'Expiry date:\s*(.+)',
    'updated_date': r'Last updated:\s*(.+)',

    'name_servers': r'Name Servers:\s*(.+)\s*',
    'status': r'Registration status:\n\s*(.+)',
}
