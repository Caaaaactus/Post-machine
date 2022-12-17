import pytest
from APP_class import App

def test_corect_input_tape():
    app = App()
    tape1 = ['0']*20
    assert app._corect_input_tape(tape1) == True

    app = App()
    tape1 = ['1'] * 20
    assert app._corect_input_tape(tape1) == True

    app = App()
    tape1 = ['01'] * 20
    assert app._corect_input_tape(tape1) == True

    app = App()
    tape1 = ['7'] * 20
    assert app._corect_input_tape(tape1) == False

    app = App()
    tape1 = ['*'] * 20
    assert app._corect_input_tape(tape1) == False

def test_corect_step():
    app = App()
    app.command_list=['v2', 's2']
    step = 0
    assert app._corect_step(step) == False

    step = 1
    assert app._corect_step(step) == True

    step = 2
    assert app._corect_step(step) == True

    step = 3
    assert app._corect_step(step) == False

    step = '!'
    assert app._corect_step(step) == False

    step = 'd'
    assert app._corect_step(step) == False

def test_reset():
    pass




