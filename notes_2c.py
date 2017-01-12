import copy

# 1 ####################################################################################

class AutoSetterMetaclass(type):
    def __new__(cls, name, bases, classdict):
        d = {}
        for attr in classdict:
            if attr.startswith("_"+name+"__"):
                def setter(self, value, attr=attr):
                    return setattr(self, attr, value)
                settername = "set" + attr[3+len(name):]
                setter.__name__ = settername
                d[settername] = setter
            d[attr] = classdict[attr]
        return super(AutoSetterMetaclass, cls).__new__(cls, name, bases, d)


class Nowa(metaclass=AutoSetterMetaclass):
    __x = 1
    def __init__(self):
        pass

# 2 ####################################################################################

class Property2:
    def __init__(self, getter=None, setter=None, deleter=None, doc=None):
        self.getter = getter
        self.setter = setter
        self.deleter = deleter
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if self.getter is None:
            pass
        return self.getter(obj)

    def __set__(self, obj, value):
        return self.setter(obj, value)

    def __delete__(self, obj):
        return self.deleter(obj)

class Dummy(object):
    def __init__(self, val):
        self.__x = val

    def getx(self):
        return self.__x

    def setx(self, val):
        self.__x = val * 10
        print("x is read only")

    x = Property2(getx, setx)

# 3 ####################################################################################

class Counter(object):
    def __init__(self, f):
        self.f = f
        self._counter = 0

    def __call__(self, *args, **kwargs):
        self._counter += 1
        print(self._counter)
        return self.f(*args, **kwargs)


@Counter
def test_f():
    print("W funkcji")

# 4 ####################################################################################

class UpperCaseMetaclass(type):
    def __new__(cls, name, bases, classdict):
        d = {}
        for attr in classdict:
            if not attr.startswith("__") and not attr.endswith("__"):
                d[attr.upper()] = classdict[attr]
            else:
                d[attr] = classdict[attr]

        return super(UpperCaseMetaclass, cls).__new__(cls, name, bases, d)


class UpperTest(metaclass=UpperCaseMetaclass):
    x = 2
    ala = 21

    def __init__(self):
        pass

    def dupa(self):
        print("jestem dupa")

# __metaclass__ = UpperCaseMetaclass # Only in Py2

# 5 ####################################################################################

class RunTimer(object):
    def __init__(self, f):
        self.f = f
        self.initial_defaults = self.f.__defaults__

    def __call__(self, *args, **kwargs):
        self.f.__defaults__ = copy.deepcopy(self.initial_defaults)
        return self.f(*args, **kwargs)


@RunTimer
def test_func_5(l=[]):
    l.append(1)
    return l


# 6 ####################################################################################

class InterfaceCheckerMetaClass(type):
    def __init__(cls, name, bases, classdict):
        interfaces = classdict["__interfaces__"]
        attrs = {}
        for interface in interfaces:
            attrs.update({k: v for k, v in interface.__dict__.items() if not k.startswith("__")})
        for attr, attr_object in attrs.items():
            if attr not in classdict and callable(attr_object):
                raise NotImplementedError("{} not implemented".format(attr))

        super(InterfaceCheckerMetaClass, cls).__init__(name, bases, classdict)


class BaseA:
    def z_base_a(self):
        pass
    a = 1

class BaseB:
    def z_base_b(self):
        pass

class InterfaceClass(metaclass=InterfaceCheckerMetaClass):
    __interfaces__ = [BaseA, BaseB]

    def __init__(self):
        pass

    def z_base_a(self):
        pass

    def z_base_b(self):
        pass

# 7 ####################################################################################


class SingleTonMetaClass(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        print(cls.instances)
        if cls not in cls.instances:
            clsobj = super(SingleTonMetaClass, cls).__call__(*args, **kwargs)
            cls.instances[cls] = clsobj
        return cls.instances[cls]


class SingleTon:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            return super(SingleTon, cls).__new__(cls, *args, **kwargs)
        else:
            return SingleTon.instance

    def __init__(self):
        if SingleTon.instance is None:
            SingleTon.instance = self


class Dziedziczaca(SingleTon):
    def __init__(self):
        super(SingleTon, self).__init__(self)
        self.k = "AKUKU"


class Jakas(metaclass=SingleTonMetaClass):
    def __init__(self, val):
        self.val = val

class Jakas2(metaclass=SingleTonMetaClass):
    def __init__(self, val):
        self.val = val



if __name__ == '__main__':
    # 7

    # A = SingleTon()
    # A.a = 4
    # print(A.a)
    # B = SingleTon()
    # B.a = 5
    # print(A.a)
    # print(B.a)
    # print(A)
    # print(B)
    # print(A is B)
    # KK = Dziedziczaca()
    # print(KK is A)

    A = Jakas(7)
    B = Jakas(8)
    print(A.val)
    print(B.val)
    print(A is B)
    C = Jakas2(10)
    D = Jakas2(10)
    print(C is A)

    # 6
    # A = InterfaceClass()

    # 5
    # print(test_func_5())
    # print(test_func_5())
    # print(test_func_5())

    # 4
    # U = UpperTest()
    # print(dir(U))
    # print(U.ALA)
    # U.DUPA()

    # 3
    # test_f()
    # test_f()
    # print(test_f._counter)

    # 2
    # a = Dummy(1)
    # print(a.x)
    # a.x = 2
    # print(a.x)

    # 1
    # N = Nowa()
    # N.setx(2)
    # print(N._Nowa__x)