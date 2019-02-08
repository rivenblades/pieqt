import pieqt
import importlib
import pkgutil
def import_submodules(package, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = __name__ + '.' + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))
    return results
#import_submodules(pieqt)
import types

def list_modules(module_name):
    try:
        module = __import__(module_name, globals(), locals(), [module_name.split('.')[-1]])
    except ImportError:
        return
    print(module_name)
    for name in dir(module):
        if type(getattr(module, name)) == types.ModuleType:
            list_modules('.'.join([module_name, name]))

def import_submodules1(package, recursive=True):
    """
    Import all submodules of a module, recursively,
    including subpackages.

    From http://stackoverflow.com/questions/3365740/how-to-import-all-submodules

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    import importlib
    import pkgutil
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for _loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name)) 
import pkgutil

# this is the package we are inspecting -- for example 'email' from stdlib
import os
l = [m[1] for m in filter(lambda a: type(a[1]) == type(pieqt), pieqt.__dict__.items())]

print(l)

l0=[m[0] for m in filter(lambda a: type(a[1]) == type(pieqt), pieqt.__dict__.items())]
print(l0)
for lib in l0:
	__import__(lib)
print(PySide2.QtWidgets.QApplication)
