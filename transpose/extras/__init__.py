from transpose.models import TransposeDependencyError

# check for the requirements of the module
try:
    pass
except ImportError:
    raise TransposeDependencyError(["plotly", "pandas", "kaleido"])
