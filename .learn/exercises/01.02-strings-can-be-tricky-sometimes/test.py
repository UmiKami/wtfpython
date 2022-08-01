import io, sys, pytest, os, re
path = os.path.dirname(os.path.abspath(__file__))+'/app.py'


@pytest.mark.it('You should create a variable named a')
def test_variable_exists(app):
    import app
    try:
        assert app.a
    except AttributeError:
        raise AttributeError('The variable "a" should exist on app.py')

@pytest.mark.it('Variable "a" should be equal to "some_string"')
def test_variable_equals_5(app):
    import app
    try:
        assert app.a == "some_string"
    except AttributeError:
        raise AttributeError('The variable "a" should equal "some_string"')

@pytest.mark.it('You should use method "id" and it should be called with variable a')
def test_function_exists(app):
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\bprint\b\s*\(\s*\bid\b\s*\(\s*a\s*\)\s*\)\s*")
        assert bool(regex.search(content)) == True

@pytest.mark.it('You should use method "id" and it should be called with the value of "a" concatenated')
def test_function_exists_with_concat(app):
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"id\s*\(\s*\"some\"\s*\+\s*\"_\"\s*\+\s*\"string\"\s*\)")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The printed value on the console should be correct id for both the value of a and the resultant value of its concatenation')
def test_for_file_output(capsys, app):
    app()
    import app
    captured = capsys.readouterr()
    toCompare = str(id(app.a)) + "\n" + str(id("some" + "_" + "string")) + "\n"
    assert toCompare == captured.out

