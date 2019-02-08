from . import pieqt
from . import App
<<<<<<< HEAD
=======
import pkgutil

__all__ = []
for loader, module_name, is_pkg in  pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    _module = loader.find_module(module_name).load_module(module_name)
    globals()[module_name] = _module
>>>>>>> df1e8e7e24444aa50c035e63fb4529ea539706ee
