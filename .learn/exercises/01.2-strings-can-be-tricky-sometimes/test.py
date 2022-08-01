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
        regex = re.compile(r"/^[a-z]*\s*\(\s*[a-z]*\s*\(\s*a\s*\)\s*\)\s*")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The printed value on the console should be correct id for both the value of a and the concatenation of its value')
def test_for_file_output(capsys, app):
    import app
    aID = id(app.a)
    concatID = id("some" + "_" + "string")
    captured = capsys.readouterr()
    if aID == concatID:
        for i in range(2):
            assert (str(aID) + "\n")  == captured.out

# @pytest.mark.it('Method id should should have been called with variable a')
# def test_method_called_with_a(app):
#     try:
#         assert app.id.assert_called_with(app.a)
#     except AttributeError:
#         raise AttributeError('The function "myFunction" should exists')


