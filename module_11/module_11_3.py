import requests
import inspect

someobj = 42

def introspection_info(obj):
    attributs = []
    methods_wrapper = []
    methods = []
    for atr in dir(someobj):
        _type = str(type(getattr(someobj, atr)))
        attributs = []
        if _type == "<class 'method-wrapper'>":
            methods_wrapper.append(atr)
        if _type == "<class 'method'>":
            methods.append(atr)
        if _type in ("<class 'int'>", "<class 'str'>", "class float", "<class 'dict'>", "<class 'set'>",
                     "<class 'list'>", "<class 'tuple'>"):
            attributs.append(atr)
    mod = inspect.getmodule(someobj)
    attrs = {}
    attrs['type'] = type(someobj)
    attrs['attributes'] = attributs
    attrs['methods'] = methods
    attrs['methods wrapper'] = methods_wrapper
    attrs['module'] = mod
    return attrs

number_info = introspection_info(42)
print(number_info)



