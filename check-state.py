# -*- coding: utf-8 -*-
import re

files = {
    'DEP': r'c:\Projects\REPORTS\тексти\DEP Retention - Table data.txt',
    'FTD': r'c:\Projects\REPORTS\тексти\FTD Retention Flow - Table data.txt',
    'SU':  r'c:\Projects\REPORTS\тексти\SU Retention - Table data.txt',
    'WF':  r'c:\Projects\REPORTS\тексти\Welcome Flow - Table data.txt'
}

for name, path in files.items():
    d = open(path, encoding='utf-8', newline='').read()
    codes = re.findall(r'data-promocode="([^"]+)"', d)
    body_codes = re.findall(r'class="promocode">([^<]+)<', d)
    print(f'\n=== {name} ===')
    print(f'  Header codes ({len(codes)}): {codes}')
    print(f'  Body codes ({len(body_codes)}): {body_codes}')
