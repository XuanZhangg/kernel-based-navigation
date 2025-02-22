# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_pyRVO')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pyRVO')
    _pyRVO = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pyRVO', [dirname(__file__)])
        except ImportError:
            import _pyRVO
            return _pyRVO
        try:
            _mod = imp.load_module('_pyRVO', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _pyRVO = swig_import_helper()
    del swig_import_helper
else:
    import _pyRVO
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pyRVO.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _pyRVO.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _pyRVO.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _pyRVO.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _pyRVO.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _pyRVO.SwigPyIterator_equal(self, x)

    def copy(self):
        return _pyRVO.SwigPyIterator_copy(self)

    def next(self):
        return _pyRVO.SwigPyIterator_next(self)

    def __next__(self):
        return _pyRVO.SwigPyIterator___next__(self)

    def previous(self):
        return _pyRVO.SwigPyIterator_previous(self)

    def advance(self, n):
        return _pyRVO.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _pyRVO.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _pyRVO.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _pyRVO.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _pyRVO.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _pyRVO.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _pyRVO.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _pyRVO.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class vectorPos(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorPos, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorPos, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pyRVO.vectorPos_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pyRVO.vectorPos___nonzero__(self)

    def __bool__(self):
        return _pyRVO.vectorPos___bool__(self)

    def __len__(self):
        return _pyRVO.vectorPos___len__(self)

    def __getslice__(self, i, j):
        return _pyRVO.vectorPos___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pyRVO.vectorPos___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pyRVO.vectorPos___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pyRVO.vectorPos___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pyRVO.vectorPos___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pyRVO.vectorPos___setitem__(self, *args)

    def pop(self):
        return _pyRVO.vectorPos_pop(self)

    def append(self, x):
        return _pyRVO.vectorPos_append(self, x)

    def empty(self):
        return _pyRVO.vectorPos_empty(self)

    def size(self):
        return _pyRVO.vectorPos_size(self)

    def swap(self, v):
        return _pyRVO.vectorPos_swap(self, v)

    def begin(self):
        return _pyRVO.vectorPos_begin(self)

    def end(self):
        return _pyRVO.vectorPos_end(self)

    def rbegin(self):
        return _pyRVO.vectorPos_rbegin(self)

    def rend(self):
        return _pyRVO.vectorPos_rend(self)

    def clear(self):
        return _pyRVO.vectorPos_clear(self)

    def get_allocator(self):
        return _pyRVO.vectorPos_get_allocator(self)

    def pop_back(self):
        return _pyRVO.vectorPos_pop_back(self)

    def erase(self, *args):
        return _pyRVO.vectorPos_erase(self, *args)

    def __init__(self, *args):
        this = _pyRVO.new_vectorPos(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _pyRVO.vectorPos_push_back(self, x)

    def front(self):
        return _pyRVO.vectorPos_front(self)

    def back(self):
        return _pyRVO.vectorPos_back(self)

    def assign(self, n, x):
        return _pyRVO.vectorPos_assign(self, n, x)

    def resize(self, *args):
        return _pyRVO.vectorPos_resize(self, *args)

    def insert(self, *args):
        return _pyRVO.vectorPos_insert(self, *args)

    def reserve(self, n):
        return _pyRVO.vectorPos_reserve(self, n)

    def capacity(self):
        return _pyRVO.vectorPos_capacity(self)
    __swig_destroy__ = _pyRVO.delete_vectorPos
    __del__ = lambda self: None
vectorPos_swigregister = _pyRVO.vectorPos_swigregister
vectorPos_swigregister(vectorPos)

class vectorMat2XT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorMat2XT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorMat2XT, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pyRVO.vectorMat2XT_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pyRVO.vectorMat2XT___nonzero__(self)

    def __bool__(self):
        return _pyRVO.vectorMat2XT___bool__(self)

    def __len__(self):
        return _pyRVO.vectorMat2XT___len__(self)

    def __getslice__(self, i, j):
        return _pyRVO.vectorMat2XT___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pyRVO.vectorMat2XT___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pyRVO.vectorMat2XT___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pyRVO.vectorMat2XT___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pyRVO.vectorMat2XT___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pyRVO.vectorMat2XT___setitem__(self, *args)

    def pop(self):
        return _pyRVO.vectorMat2XT_pop(self)

    def append(self, x):
        return _pyRVO.vectorMat2XT_append(self, x)

    def empty(self):
        return _pyRVO.vectorMat2XT_empty(self)

    def size(self):
        return _pyRVO.vectorMat2XT_size(self)

    def swap(self, v):
        return _pyRVO.vectorMat2XT_swap(self, v)

    def begin(self):
        return _pyRVO.vectorMat2XT_begin(self)

    def end(self):
        return _pyRVO.vectorMat2XT_end(self)

    def rbegin(self):
        return _pyRVO.vectorMat2XT_rbegin(self)

    def rend(self):
        return _pyRVO.vectorMat2XT_rend(self)

    def clear(self):
        return _pyRVO.vectorMat2XT_clear(self)

    def get_allocator(self):
        return _pyRVO.vectorMat2XT_get_allocator(self)

    def pop_back(self):
        return _pyRVO.vectorMat2XT_pop_back(self)

    def erase(self, *args):
        return _pyRVO.vectorMat2XT_erase(self, *args)

    def __init__(self, *args):
        this = _pyRVO.new_vectorMat2XT(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _pyRVO.vectorMat2XT_push_back(self, x)

    def front(self):
        return _pyRVO.vectorMat2XT_front(self)

    def back(self):
        return _pyRVO.vectorMat2XT_back(self)

    def assign(self, n, x):
        return _pyRVO.vectorMat2XT_assign(self, n, x)

    def resize(self, *args):
        return _pyRVO.vectorMat2XT_resize(self, *args)

    def insert(self, *args):
        return _pyRVO.vectorMat2XT_insert(self, *args)

    def reserve(self, n):
        return _pyRVO.vectorMat2XT_reserve(self, n)

    def capacity(self):
        return _pyRVO.vectorMat2XT_capacity(self)
    __swig_destroy__ = _pyRVO.delete_vectorMat2XT
    __del__ = lambda self: None
vectorMat2XT_swigregister = _pyRVO.vectorMat2XT_swigregister
vectorMat2XT_swigregister(vectorMat2XT)

class vectorMatT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorMatT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorMatT, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pyRVO.vectorMatT_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pyRVO.vectorMatT___nonzero__(self)

    def __bool__(self):
        return _pyRVO.vectorMatT___bool__(self)

    def __len__(self):
        return _pyRVO.vectorMatT___len__(self)

    def __getslice__(self, i, j):
        return _pyRVO.vectorMatT___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pyRVO.vectorMatT___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pyRVO.vectorMatT___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pyRVO.vectorMatT___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pyRVO.vectorMatT___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pyRVO.vectorMatT___setitem__(self, *args)

    def pop(self):
        return _pyRVO.vectorMatT_pop(self)

    def append(self, x):
        return _pyRVO.vectorMatT_append(self, x)

    def empty(self):
        return _pyRVO.vectorMatT_empty(self)

    def size(self):
        return _pyRVO.vectorMatT_size(self)

    def swap(self, v):
        return _pyRVO.vectorMatT_swap(self, v)

    def begin(self):
        return _pyRVO.vectorMatT_begin(self)

    def end(self):
        return _pyRVO.vectorMatT_end(self)

    def rbegin(self):
        return _pyRVO.vectorMatT_rbegin(self)

    def rend(self):
        return _pyRVO.vectorMatT_rend(self)

    def clear(self):
        return _pyRVO.vectorMatT_clear(self)

    def get_allocator(self):
        return _pyRVO.vectorMatT_get_allocator(self)

    def pop_back(self):
        return _pyRVO.vectorMatT_pop_back(self)

    def erase(self, *args):
        return _pyRVO.vectorMatT_erase(self, *args)

    def __init__(self, *args):
        this = _pyRVO.new_vectorMatT(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _pyRVO.vectorMatT_push_back(self, x)

    def front(self):
        return _pyRVO.vectorMatT_front(self)

    def back(self):
        return _pyRVO.vectorMatT_back(self)

    def assign(self, n, x):
        return _pyRVO.vectorMatT_assign(self, n, x)

    def resize(self, *args):
        return _pyRVO.vectorMatT_resize(self, *args)

    def insert(self, *args):
        return _pyRVO.vectorMatT_insert(self, *args)

    def reserve(self, n):
        return _pyRVO.vectorMatT_reserve(self, n)

    def capacity(self):
        return _pyRVO.vectorMatT_capacity(self)
    __swig_destroy__ = _pyRVO.delete_vectorMatT
    __del__ = lambda self: None
vectorMatT_swigregister = _pyRVO.vectorMatT_swigregister
vectorMatT_swigregister(vectorMatT)

class vectorVec(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorVec, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorVec, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pyRVO.vectorVec_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pyRVO.vectorVec___nonzero__(self)

    def __bool__(self):
        return _pyRVO.vectorVec___bool__(self)

    def __len__(self):
        return _pyRVO.vectorVec___len__(self)

    def __getslice__(self, i, j):
        return _pyRVO.vectorVec___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pyRVO.vectorVec___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pyRVO.vectorVec___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pyRVO.vectorVec___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pyRVO.vectorVec___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pyRVO.vectorVec___setitem__(self, *args)

    def pop(self):
        return _pyRVO.vectorVec_pop(self)

    def append(self, x):
        return _pyRVO.vectorVec_append(self, x)

    def empty(self):
        return _pyRVO.vectorVec_empty(self)

    def size(self):
        return _pyRVO.vectorVec_size(self)

    def swap(self, v):
        return _pyRVO.vectorVec_swap(self, v)

    def begin(self):
        return _pyRVO.vectorVec_begin(self)

    def end(self):
        return _pyRVO.vectorVec_end(self)

    def rbegin(self):
        return _pyRVO.vectorVec_rbegin(self)

    def rend(self):
        return _pyRVO.vectorVec_rend(self)

    def clear(self):
        return _pyRVO.vectorVec_clear(self)

    def get_allocator(self):
        return _pyRVO.vectorVec_get_allocator(self)

    def pop_back(self):
        return _pyRVO.vectorVec_pop_back(self)

    def erase(self, *args):
        return _pyRVO.vectorVec_erase(self, *args)

    def __init__(self, *args):
        this = _pyRVO.new_vectorVec(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _pyRVO.vectorVec_push_back(self, x)

    def front(self):
        return _pyRVO.vectorVec_front(self)

    def back(self):
        return _pyRVO.vectorVec_back(self)

    def assign(self, n, x):
        return _pyRVO.vectorVec_assign(self, n, x)

    def resize(self, *args):
        return _pyRVO.vectorVec_resize(self, *args)

    def insert(self, *args):
        return _pyRVO.vectorVec_insert(self, *args)

    def reserve(self, n):
        return _pyRVO.vectorVec_reserve(self, n)

    def capacity(self):
        return _pyRVO.vectorVec_capacity(self)
    __swig_destroy__ = _pyRVO.delete_vectorVec
    __del__ = lambda self: None
vectorVec_swigregister = _pyRVO.vectorVec_swigregister
vectorVec_swigregister(vectorVec)

class vectorT(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorT, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pyRVO.vectorT_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pyRVO.vectorT___nonzero__(self)

    def __bool__(self):
        return _pyRVO.vectorT___bool__(self)

    def __len__(self):
        return _pyRVO.vectorT___len__(self)

    def __getslice__(self, i, j):
        return _pyRVO.vectorT___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pyRVO.vectorT___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pyRVO.vectorT___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pyRVO.vectorT___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pyRVO.vectorT___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pyRVO.vectorT___setitem__(self, *args)

    def pop(self):
        return _pyRVO.vectorT_pop(self)

    def append(self, x):
        return _pyRVO.vectorT_append(self, x)

    def empty(self):
        return _pyRVO.vectorT_empty(self)

    def size(self):
        return _pyRVO.vectorT_size(self)

    def swap(self, v):
        return _pyRVO.vectorT_swap(self, v)

    def begin(self):
        return _pyRVO.vectorT_begin(self)

    def end(self):
        return _pyRVO.vectorT_end(self)

    def rbegin(self):
        return _pyRVO.vectorT_rbegin(self)

    def rend(self):
        return _pyRVO.vectorT_rend(self)

    def clear(self):
        return _pyRVO.vectorT_clear(self)

    def get_allocator(self):
        return _pyRVO.vectorT_get_allocator(self)

    def pop_back(self):
        return _pyRVO.vectorT_pop_back(self)

    def erase(self, *args):
        return _pyRVO.vectorT_erase(self, *args)

    def __init__(self, *args):
        this = _pyRVO.new_vectorT(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _pyRVO.vectorT_push_back(self, x)

    def front(self):
        return _pyRVO.vectorT_front(self)

    def back(self):
        return _pyRVO.vectorT_back(self)

    def assign(self, n, x):
        return _pyRVO.vectorT_assign(self, n, x)

    def resize(self, *args):
        return _pyRVO.vectorT_resize(self, *args)

    def insert(self, *args):
        return _pyRVO.vectorT_insert(self, *args)

    def reserve(self, n):
        return _pyRVO.vectorT_reserve(self, n)

    def capacity(self):
        return _pyRVO.vectorT_capacity(self)
    __swig_destroy__ = _pyRVO.delete_vectorT
    __del__ = lambda self: None
vectorT_swigregister = _pyRVO.vectorT_swigregister
vectorT_swigregister(vectorT)

class vectorChar(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorChar, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorChar, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _pyRVO.vectorChar_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pyRVO.vectorChar___nonzero__(self)

    def __bool__(self):
        return _pyRVO.vectorChar___bool__(self)

    def __len__(self):
        return _pyRVO.vectorChar___len__(self)

    def __getslice__(self, i, j):
        return _pyRVO.vectorChar___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pyRVO.vectorChar___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pyRVO.vectorChar___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pyRVO.vectorChar___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pyRVO.vectorChar___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pyRVO.vectorChar___setitem__(self, *args)

    def pop(self):
        return _pyRVO.vectorChar_pop(self)

    def append(self, x):
        return _pyRVO.vectorChar_append(self, x)

    def empty(self):
        return _pyRVO.vectorChar_empty(self)

    def size(self):
        return _pyRVO.vectorChar_size(self)

    def swap(self, v):
        return _pyRVO.vectorChar_swap(self, v)

    def begin(self):
        return _pyRVO.vectorChar_begin(self)

    def end(self):
        return _pyRVO.vectorChar_end(self)

    def rbegin(self):
        return _pyRVO.vectorChar_rbegin(self)

    def rend(self):
        return _pyRVO.vectorChar_rend(self)

    def clear(self):
        return _pyRVO.vectorChar_clear(self)

    def get_allocator(self):
        return _pyRVO.vectorChar_get_allocator(self)

    def pop_back(self):
        return _pyRVO.vectorChar_pop_back(self)

    def erase(self, *args):
        return _pyRVO.vectorChar_erase(self, *args)

    def __init__(self, *args):
        this = _pyRVO.new_vectorChar(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _pyRVO.vectorChar_push_back(self, x)

    def front(self):
        return _pyRVO.vectorChar_front(self)

    def back(self):
        return _pyRVO.vectorChar_back(self)

    def assign(self, n, x):
        return _pyRVO.vectorChar_assign(self, n, x)

    def resize(self, *args):
        return _pyRVO.vectorChar_resize(self, *args)

    def insert(self, *args):
        return _pyRVO.vectorChar_insert(self, *args)

    def reserve(self, n):
        return _pyRVO.vectorChar_reserve(self, n)

    def capacity(self):
        return _pyRVO.vectorChar_capacity(self)
    __swig_destroy__ = _pyRVO.delete_vectorChar
    __del__ = lambda self: None
vectorChar_swigregister = _pyRVO.vectorChar_swigregister
vectorChar_swigregister(vectorChar)

class RVOSimulator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RVOSimulator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RVOSimulator, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _pyRVO.new_RVOSimulator(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def getUseHash(self):
        return _pyRVO.RVOSimulator_getUseHash(self)

    def getRadius(self):
        return _pyRVO.RVOSimulator_getRadius(self)

    def clearAgent(self):
        return _pyRVO.RVOSimulator_clearAgent(self)

    def clearObstacle(self):
        return _pyRVO.RVOSimulator_clearObstacle(self)

    def getNrObstacle(self):
        return _pyRVO.RVOSimulator_getNrObstacle(self)

    def getNrAgent(self):
        return _pyRVO.RVOSimulator_getNrAgent(self)

    def getObstacle(self, i):
        return _pyRVO.RVOSimulator_getObstacle(self, i)

    def getAgentPositions(self):
        return _pyRVO.RVOSimulator_getAgentPositions(self)

    def getAgentVelocities(self):
        return _pyRVO.RVOSimulator_getAgentVelocities(self)

    def getAgentPosition(self, i):
        return _pyRVO.RVOSimulator_getAgentPosition(self, i)

    def getAgentVelocity(self, i):
        return _pyRVO.RVOSimulator_getAgentVelocity(self, i)

    def addAgent(self, pos, vel):
        return _pyRVO.RVOSimulator_addAgent(self, pos, vel)

    def setAgentPosition(self, i, pos):
        return _pyRVO.RVOSimulator_setAgentPosition(self, i, pos)

    def setAgentVelocity(self, i, vel):
        return _pyRVO.RVOSimulator_setAgentVelocity(self, i, vel)

    def setAgentTarget(self, i, target, maxVelocity):
        return _pyRVO.RVOSimulator_setAgentTarget(self, i, target, maxVelocity)

    def addObstacle(self, vss):
        return _pyRVO.RVOSimulator_addObstacle(self, vss)

    def setNewtonParameter(self, maxIter, gTol, d0, coef=1):
        return _pyRVO.RVOSimulator_setNewtonParameter(self, maxIter, gTol, d0, coef)

    def setAgentRadius(self, radius):
        return _pyRVO.RVOSimulator_setAgentRadius(self, radius)

    def setTimestep(self, timestep):
        return _pyRVO.RVOSimulator_setTimestep(self, timestep)

    def timestep(self):
        return _pyRVO.RVOSimulator_timestep(self)

    def optimize(self, requireGrad, output):
        return _pyRVO.RVOSimulator_optimize(self, requireGrad, output)

    def updateAgentTargets(self):
        return _pyRVO.RVOSimulator_updateAgentTargets(self)

    def getDXDX(self):
        return _pyRVO.RVOSimulator_getDXDX(self)

    def getDXDV(self):
        return _pyRVO.RVOSimulator_getDXDV(self)

    def debugNeighbor(self, scale):
        return _pyRVO.RVOSimulator_debugNeighbor(self, scale)

    def debugEnergy(self, scale, dscale=1):
        return _pyRVO.RVOSimulator_debugEnergy(self, scale, dscale)
    __swig_destroy__ = _pyRVO.delete_RVOSimulator
    __del__ = lambda self: None
RVOSimulator_swigregister = _pyRVO.RVOSimulator_swigregister
RVOSimulator_swigregister(RVOSimulator)

class MultiRVOSimulator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MultiRVOSimulator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MultiRVOSimulator, name)
    __repr__ = _swig_repr

    def __init__(self, batchSize, rad, d0=1, gTol=1e-4, coef=1, timestep=1, maxIter=1000, radixSort=False, useHash=True):
        this = _pyRVO.new_MultiRVOSimulator(batchSize, rad, d0, gTol, coef, timestep, maxIter, radixSort, useHash)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def getRadius(self):
        return _pyRVO.MultiRVOSimulator_getRadius(self)

    def clearAgent(self):
        return _pyRVO.MultiRVOSimulator_clearAgent(self)

    def clearObstacle(self):
        return _pyRVO.MultiRVOSimulator_clearObstacle(self)

    def getNrObstacle(self):
        return _pyRVO.MultiRVOSimulator_getNrObstacle(self)

    def getObstacle(self, i):
        return _pyRVO.MultiRVOSimulator_getObstacle(self, i)

    def getNrAgent(self):
        return _pyRVO.MultiRVOSimulator_getNrAgent(self)

    def getAgentPosition(self, i):
        return _pyRVO.MultiRVOSimulator_getAgentPosition(self, i)

    def getAgentVelocity(self, i):
        return _pyRVO.MultiRVOSimulator_getAgentVelocity(self, i)

    def addAgent(self, pos, vel):
        return _pyRVO.MultiRVOSimulator_addAgent(self, pos, vel)

    def setAgentPosition(self, i, pos):
        return _pyRVO.MultiRVOSimulator_setAgentPosition(self, i, pos)

    def setAgentVelocity(self, i, vel):
        return _pyRVO.MultiRVOSimulator_setAgentVelocity(self, i, vel)

    def setAgentTarget(self, i, target, maxVelocity):
        return _pyRVO.MultiRVOSimulator_setAgentTarget(self, i, target, maxVelocity)

    def addObstacle(self, vss):
        return _pyRVO.MultiRVOSimulator_addObstacle(self, vss)

    def setNewtonParameter(self, maxIter, gTol, d0, coef=1):
        return _pyRVO.MultiRVOSimulator_setNewtonParameter(self, maxIter, gTol, d0, coef)

    def setAgentRadius(self, radius):
        return _pyRVO.MultiRVOSimulator_setAgentRadius(self, radius)

    def setTimestep(self, timestep):
        return _pyRVO.MultiRVOSimulator_setTimestep(self, timestep)

    def timestep(self):
        return _pyRVO.MultiRVOSimulator_timestep(self)

    def getBatchSize(self):
        return _pyRVO.MultiRVOSimulator_getBatchSize(self)

    def getSubSimulator(self, id):
        return _pyRVO.MultiRVOSimulator_getSubSimulator(self, id)

    def optimize(self, requireGrad, output):
        return _pyRVO.MultiRVOSimulator_optimize(self, requireGrad, output)

    def updateAgentTargets(self):
        return _pyRVO.MultiRVOSimulator_updateAgentTargets(self)

    def getDXDX(self):
        return _pyRVO.MultiRVOSimulator_getDXDX(self)

    def getDXDV(self):
        return _pyRVO.MultiRVOSimulator_getDXDV(self)
    __swig_destroy__ = _pyRVO.delete_MultiRVOSimulator
    __del__ = lambda self: None
MultiRVOSimulator_swigregister = _pyRVO.MultiRVOSimulator_swigregister
MultiRVOSimulator_swigregister(MultiRVOSimulator)

class CoverageEnergy(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CoverageEnergy, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CoverageEnergy, name)
    __repr__ = _swig_repr

    def __init__(self, sim, range, visibleOnly=True):
        this = _pyRVO.new_CoverageEnergy(sim, range, visibleOnly)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def loss(self, pos):
        return _pyRVO.CoverageEnergy_loss(self, pos)

    def grad(self):
        return _pyRVO.CoverageEnergy_grad(self)

    def debugCoverage(self, scale):
        return _pyRVO.CoverageEnergy_debugCoverage(self, scale)
    __swig_destroy__ = _pyRVO.delete_CoverageEnergy
    __del__ = lambda self: None
CoverageEnergy_swigregister = _pyRVO.CoverageEnergy_swigregister
CoverageEnergy_swigregister(CoverageEnergy)

class MultiCoverageEnergy(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MultiCoverageEnergy, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MultiCoverageEnergy, name)
    __repr__ = _swig_repr

    def __init__(self, sim, range, visibleOnly=True):
        this = _pyRVO.new_MultiCoverageEnergy(sim, range, visibleOnly)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def loss(self, pos):
        return _pyRVO.MultiCoverageEnergy_loss(self, pos)

    def grad(self):
        return _pyRVO.MultiCoverageEnergy_grad(self)
    __swig_destroy__ = _pyRVO.delete_MultiCoverageEnergy
    __del__ = lambda self: None
MultiCoverageEnergy_swigregister = _pyRVO.MultiCoverageEnergy_swigregister
MultiCoverageEnergy_swigregister(MultiCoverageEnergy)


def drawRVOApp(*args):
    return _pyRVO.drawRVOApp(*args)
drawRVOApp = _pyRVO.drawRVOApp
# This file is compatible with both classic and new-style classes.


