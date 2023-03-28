# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 18:15:03 2022

@author: peppe
"""

# Import gettext module
import gettext

# Set the local directory
localedir = 'locales'

def set_locale(language: str, domain: str):
    t = gettext.translation(domain, localedir, fallback=True, languages=[language])
    t.install()
    return t.gettext

def choose_language() -> str:
    language_choose_is_valid = False
    while(not language_choose_is_valid):
        
        language_chosen = input('Choose the language:\n1. English\n2. Italiano\n\n')
        language_choose_is_valid = language_chosen in ['1', '2']
        
        if(not language_choose_is_valid):
            print('Please choose a valid option\n\n')
        
    return 'it' if language_chosen == '2' else 'en'