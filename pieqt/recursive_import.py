import sys
import importlib
from pieqt import*
def recursive_import(package):
	modules = [m[1] for m in filter(lambda a: type(a[1]) == type(package), package.__dict__.items())]
	print(modules)
	for module in modules:
		#if isinstance(module, str):
			#package = importlib.import_module(package)
	# is there an __all__?  if so respect it
		if "__all__" in module.__dict__:
			names = module.__dict__["__all__"]
		else:
			# otherwise we import all names that don't begin with _
			names = [x for x in module.__dict__ if not x.startswith("_")]

		# now drag them in
		globals().update({k: getattr(module, k) for k in names})
recursive_import(pieqt)
print(globals())
print(QApplication)


