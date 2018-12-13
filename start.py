import sys
from inspect import *
from pprint import *

# module for testing
module_name = 'test_module'
#test_module = __import__(module_name)
from test_module import *

#x = E.__mro__
'''
class MyAttr:
    def __init__(owner, value, name):
        self.owner = owner
        self.value = value
        self.name = name

def get_members(cls):
    dictionary = cls.__dict__

    [for key, value in dictionary]
'''
#a = C()
#pprint(getmembers(A, isroutine))

# TODO: remove __module__, __dict__, __doc__, __weakref__
obj = object().__class__
def mytest(tesstcls):
    pprint(tesstcls.__dict__)
    pprint(tesstcls.__dir__())
    #pprint(dir(tesstcls))
    #pprint(tesstcls.__mro__)
    print("--------------------------------")
#mytest(A)


def printClass(cls):
    pass

#classes = getmembers(sys.modules[module_name], isclass)
#pprint([attribute for attribute, value in Root.__dict__.items()])
'''
fns = inspect.getmembers(sys.modules[module_name], inspect.isfunction)
classtree = inspect.getclasstree([cls[1] for cls in classes], False)
myprint(classes)    
myprint(fns)
myprint(classtree)

classtreeAB = inspect.getclasstree([test_module.A, test_module.B], True)
myprint(classtreeAB)
'''


def type2str(value):
    """Get member value and traslate it in our 'type'"""
    if isfunction(value): return "method"
    else: return "attribute"

class ChainNode:
    def __init__(self, cls, value):
        self.classInfo = cls
        self.attributeValue = value

def find_override(maincls, attrname):
    """Generator through MRO for attribute overriding"""
    for cls in maincls.__mro__[:-1]:
        for name, value in cls.__dict__.items():
            if attrname == name:
                yield ChainNode(cls, value)

def transitive_inheritance(cls):
    """Create overriding generator for each class attribute"""
    members = filter(
            lambda x: not x.startswith('__'), 
            dir(cls)
        )
    return {m: find_override(cls, m) for m in members} 

def generate_chain(cls):
    """Transitive inheritance chains for class"""
    attrs = transitive_inheritance(cls)
    return {name: [x for x in gen] for name, gen in attrs.items()}

# task 1
def fullchain2str(cls):
    lines = []
    fullchain = generate_chain(cls)
    for name, hierarchy in fullchain.items():
        lastVal = hierarchy[0].attributeValue        
        chainS = ' --> '.join(x.classInfo.__name__ for x in hierarchy)
        line = f"{type2str(lastVal)} '{name}': {chainS}"
        lines.append('\n' + line)

    separ = '\n' + '-'*100
    return f'Start point: {cls.__name__}' + separ + ''.join(lines) + separ

# test 1
# print(fullchain2str(A))

def generate_first_node(cls):
    """Look for only first member using"""
    attrs = transitive_inheritance(cls)

    return {name: next(iter(gen)) for name, gen in attrs.items()}

# task 6
def get_root_members(cls):
    try:
        root = cls.__mro__[-2]
        if root.__name__ == cls.__name__:
            return "Same classes: All root members"
        else:
            members = []
            fullchain = generate_first_node(cls)
            
            for name, node in fullchain.items(): 
                if node.classInfo == root:
                    members.append(f'{type2str(node.attributeValue)}: {name}')
            return members
    except:
        return "Object class is not used"

# test 6
# pprint(get_root_members(F))

def get_dict_extremum(data, maximum):
    """Get all extremum dictionary keys by its value"""
    if not data:
        return None

    reducer = max if maximum else min
    reducer_key = reducer(data.values())

    return [k for k in data if data[k] == reducer_key]

# task 4
def common_subclasses(a, b, greatest=True):
    """Find common subclass class for two classes"""
    # recursively get all subclasses for class
    def get_subclasses(cls):
        for subclass in cls.__subclasses__():
            yield from get_subclasses(subclass)
            yield subclass
    
    getSet = lambda cls: set(x for x in get_subclasses(cls))

    common = {x: len(x.__mro__)
        for x in getSet(a) & getSet(b)}
    
    return get_dict_extremum(common, greatest)

# test 4   
#pprint(common_subclasses(Root, A))

# task 5
def common_superclasses(a, b, greatest=True):
    """Find common superclass class between two classes"""
    mroA, mroB = a.__mro__, b.__mro__

    # enumarate mro hierarchy 
    getenummro = lambda mro: {t: i for i, t in enumerate(mro)}
    enumdictA, enumdictB = getenummro(mroA), getenummro(mroB)
    
    common = {x: enumdictA[x] + enumdictB[x]
        for x in enumdictA.keys() & enumdictB.keys()}
    
    # do not consider object in hierarchy
    del common[object().__class__]

    return get_dict_extremum(common, not greatest)

# test 5
#pprint(common_superclasses(E, F, True))

'''
def psame(cls):
    return f'Classes are the same {cls.__name__}'
def psuperclass(sub, sup, queue):
    head = f'{sup.__name__} is a superclass for {sub.__name__}'
    heararchy = ' --> '.join(queue)
    return head + '\n' + heararchy
'''

def get_relation_mro(a, b):
    mro = a.__mro__
    # if b is a superclass
    if b in mro:
        index = mro.index(b)
        return 1, list(mro[:index + 1])      
    else:
        # if a is a superclass 
        mro = b.__mro__
        if a in mro:
            index = mro.index(a)
            return 1, list(mro[:index + 1])
        else:
            return None

# task 3
def relation_classes(a, b):
    """Relation between two classes.
        Returns 2 params (type, tuple)
            type:   0 - the same, 
                    1 - superclass,
                    2 - common superclasses
                    3 - common subclasses
                    4 - independent
            tuple: classes from heirarchy   
    """
    
    # if the same
    if a == b: return 0, None
        
    # if is superclass
    sub = get_relation_mro(a, b)
    if sub is not None: return sub
    
    commonsub, commonsup = common_subclasses(a, b, False), common_superclasses(a, b)
    
    # if classes have common subclasses
    if commonsub: return 2, commonsub
    # if classes have common superclasses
    elif commonsup: return 3, commonsup
    else: return 4, None

# test 3
# pprint(relation_classes(A, A))

module = sys.modules[module_name]
def gettopclasses(module):
    allClasses = [v for n, v in getmembers(module, isclass)]
    return filter(lambda cls: not cls.__subclasses__(), allClasses)

# task 2
def get_all_overridings(module):
    return [generate_chain(x) for x in gettopclasses(module)]

# test 2
pprint(get_all_overridings(module))