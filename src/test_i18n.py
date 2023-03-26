# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:56:12 2022

@author: peppe
"""

# import sys
# caution: path[0] is reserved for script path (or '' in REPL)
# path[1] should be the path to the project
# sys.path.insert(1, 'C:\\Users\\peppe\\Documents\\qd-hanged-one')

from pytest_mock import MockerFixture
import i18n

def test_choose_language(mocker: MockerFixture, monkeypatch: MockerFixture) -> None:
    #arrange
    mock_user_input = '2'
    monkeypatch.setattr('builtins.input', lambda _: mock_user_input)
    spy = mocker.spy(i18n, "choose_language")
    
    #act
    res = i18n.choose_language()
    
    #assert
    assert res == 'it'
    assert type(res) is str
    assert spy.call_count == 1

def test_set_locale(mocker: MockerFixture) -> None:
    #arrange
    mock_language = 'it'
    spy = mocker.spy(i18n, "set_locale")

    #act
    res = i18n.set_locale(mock_language)

    #assert
    assert spy.call_count == 1