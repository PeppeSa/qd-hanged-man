# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 18:37:55 2022

@author: peppe
"""

import sys
sys.path.append('.\\src')
from i18n import set_locale, choose_language

# let the user choose his favourite language
language = choose_language()

# set it as language for this run
_ = set_locale(language)

# translate message
print(_("Hello World"))