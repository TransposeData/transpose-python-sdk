from transpose.models import TransposeDependencyError

# check for the requirements of the module
try:
    from .plot import *  # noqa
except ImportError:
    raise TransposeDependencyError(["plotly", "pandas", "kaleido"])
