import sys, os, json
if os.path.isdir("./.venv/lib/"):
    sys.path.append('null/site-packages')
def pytest_addoption(parser):
    parser.addoption("--stdin", action="append", default=[],
        help="json with the stdin to pass to test functions")
def pytest_generate_tests(metafunc):
    if 'stdin' in metafunc.fixturenames:
      if hasattr(metafunc,"config"):
          metafunc.parametrize("stdin",metafunc.config.getoption('stdin'))
      elif hasattr(metafunc,"configuration"):
          metafunc.parametrize("stdin",metafunc.configuration.getoption('stdin'))
      else:
          raise Exception("Imposible to retrieve text configuration object")
    if 'app' in metafunc.fixturenames:
        try:
          sys.path.append('.learn/dist')
          import cached_app
          metafunc.parametrize("app",[cached_app.execute_app])
        except SyntaxError:
          metafunc.parametrize("app",[lambda : None])
        except ImportError:
          metafunc.parametrize("app",[cached_app])
        except AttributeError:
          metafunc.parametrize("app",[cached_app])
    if 'configuration' in metafunc.fixturenames:
        metafunc.parametrize("configuration", [json.loads('{"port":3000,"editor":{"mode":"preview","agent":"vscode","version":"1.0.72"},"dirPath":"./.learn","configPath":"learn.json","outputPath":".learn/dist","publicPath":"/preview","publicUrl":"https://3000-umikami-wtfpython-6xak56y2h2g.ws-us58.gitpod.io","contact":"https://github.com/learnpack/learnpack/issues/new","language":"auto","autoPlay":true,"grading":"isolated","exercisesPath":".learn/exercises","webpackTemplate":null,"disableGrading":false,"disabledActions":[],"actions":["Build"],"entries":{"html":"index.html","vanillajs":"index.js","react":"app.jsx","node":"app.js","python3":"app.py","java":"app.java"},"difficulty":"easy","duration":1,"description":"collection of python problems","title":"wtfpython","slug":"wtfpython","translations":[]}')])
