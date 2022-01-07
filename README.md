# Bulk Check WHOIS by [DRKWNG](https://drkwng.rocks)
Bulk check domains WHOIS data and export it into CSV.

1. `git clone https://github.com/drkwng/check-whois`
2. Create a `domains.txt` file in the program folder with the domains list you want to check (each domain line by line)
3. Start `main.py`
4. Find result in the program folder (`whois_result.csv`): status, creation_date, expiration_date, updated_date, name_servers

Add your TLDs RegExps into `tlds.py`.
