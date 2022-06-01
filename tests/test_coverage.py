import os

import pathlib


def test_coverage():
    apis = ['block', 'nft', 'token', 'ens']
    files = {}

    for api in apis:
        # get list of filenames in found api resource
        module_path = '{}/transpose/src/api/{}'.format(pathlib.Path(__file__).parent.parent.resolve(), api)
        py_files = [f[:-3] for f in os.listdir(module_path) if f.endswith('.py') and f != '__init__.py' and f != 'base.py']

        # go through every file
        for py_file in py_files:
            if not os.path.exists('{}/test_{}{}.py'.format(pathlib.Path(__file__).parent.resolve(), api, py_file)):
                raise ValueError('Missing test file for {}/test_{}{}.py'.format(pathlib.Path(__file__).parent.resolve(), api, py_file))
                
    assert True