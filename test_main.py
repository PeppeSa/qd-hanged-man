
# -*- coding: utf-8 -*-
"""
Created on 2023-03-13

@author: Giulia
"""




#def choosen_word() -> str:  
#scelta = input('Inserisci una lettera -> ')  
#return scelta

from pytest_mock import MockerFixture
import main

def test_choosen_word(mocker: MockerFixture, monkeypatch: MockerFixture) -> None:

    #arrange
    mock_user_input = 'a'
    monkeypatch.setattr('builtins.input', lambda _: mock_user_input)
    spy = mocker.spy(main, "choosen_word")

    #act
    res = main.choosen_word()

    #assert
    assert res == 'a'
    assert type(res) is str
    assert spy.call_count == 1
