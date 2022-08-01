import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'

@pytest.mark.it('You should create a function named "some_func"')
def test_function_exists(app):
    try:
        assert app.some_func
    except AttributeError:
        raise AttributeError('The function "some_func" should exists')

@pytest.mark.it('The function "some_func" should return the integer value 5')
def test_function_returns_specified(app):
    try:
        assert app.some_func() == 5
    except AttributeError:
        raise AttributeError('The function "some_func" should return 5')

@pytest.mark.it('You should create a variable named a')
def test_variable_exists(app):
    try:
        assert app.a
    except AttributeError:
        raise AttributeError('The variable "a should exist on app.py')

@pytest.mark.it('Variable a should be equal to 5')
def test_variable_equals_5(app):
    try:
        assert app.a == 5
    except AttributeError:
        raise AttributeError('The variable "a" equal 5')

@pytest.mark.it('The printed value on the console should be integer 5')
def test_for_file_output(capsys, app):
    import app
    captured = capsys.readouterr()
    assert "5\n" == captured.out