
from transpose.models import TransposeDependencyError

# check for the requirements of the module
try:
    from .plot import *
except ImportError as e:
    raise TransposeDependencyError(['plotly', 'pandas', 'kaleido'])