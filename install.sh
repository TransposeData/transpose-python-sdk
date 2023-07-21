pip install -r requirements.txt
pip install -r dev-requirements.txt
pip install pre-commit
pre-commit install --hook-type pre-commit --hook-type commit-msg
