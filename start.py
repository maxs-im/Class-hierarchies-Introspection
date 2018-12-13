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

class ChainNode:
    """Instance to know about member at some moment of hierarchy"""
    def __init__(self, cls, value):
        self.classInfo = cls
        self.attributeValue = value

def find_override(maincls, attrname):
    """Generator through MRO for attribute overriding"""
    for cls in maincls.__mro__[:-1]:
        for name, value in cls.__dict__.items():
            if attrname == name:
                yield ChainNode(cls, value)

def get_class_members(cls):
    """Get members that defined only in that class"""
    return filter(
        lambda x: not x.startswith('__'), 
        dir(cls)
    )

def transitive_inheritance(cls):
    """Create overriding generator for each class attribute"""
    members = get_class_members(cls)
    return {m: find_override(cls, m) for m in members} 


# def generate_chain(cls):
#     """Transitive inheritance chains for class"""
#     attrs = transitive_inheritance(cls)
#     return {name: [x for x in gen] for name, gen in attrs.items()}

class MemberChain:
    """Instance that defines member transitive inheritance"""
    def __init__(self, name, value, hierarchy):
        self.name = name
        self.value = value
        self.hierarchy = hierarchy
    
    # def type2str(value):
    #     """Get member value and traslate it in our 'type'"""
    #     if isfunction(value): return "method"
    #     else: return "attribute"
    
    # chainS = ' --> '.join(x.classInfo.__name__ for x in ihierarchy)
    # line = f"{type2str(lastVal)} '{name}': {chainS}"
    # lines.append('\n' + line)

    # separ = '\n' + '-'*100
    # return f'Start point: {cls.__name__}' + separ + ''.join(lines) + separ

# task 1
def generate_chain(cls):
    """Transitive inheritance chains for class"""
    chains = []
    chainGen = transitive_inheritance(cls)
    for name, hierarchyGen in chainGen.items():
        classes = []
        initType = None
        for x in iter(hierarchyGen):   
            if not initType: 
                initType = x.attributeValue
            classes.append(x.classInfo)
        chains.append(MemberChain(name, initType, classes))
    return chains            
    
# test 1
print(generate_chain(A))

def generate_first_node(cls):
    """Look for only first member using"""
    attrs = transitive_inheritance(cls)

    return {name: next(iter(gen)) for name, gen in attrs.items()}

class RootMember:
    def __init__(self, name, value, ):
        self.name = name
        self.value = value
    # f'{type2str(node.attributeValue)}: {name}'

# task 6
def get_root_members(cls):
    root = cls.__mro__[-2]
    if root.__name__ == cls.__name__:
        # "Same classes: All root members"
        return None
    else:
        fullchain = generate_first_node(cls)
        return (
            RootMember(name, node.attributeValue) 
            for name, node in fullchain.items() if node.classInfo == root
        )

# test 6
#pprint([g for g in iter(get_root_members(F))])

def get_dict_extremum(data, maximum):
    """Get all extremum dictionary keys by its value"""
    if not data:
        return None

    reducer = max if maximum else min
    reducer_key = reducer(data.values())

    return (k for k in data if data[k] == reducer_key)

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
#pprint([x for x in iter(common_subclasses(Root, A))])

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
#pprint([x for x in iter(common_superclasses(E, F, True))])

class Relation:
    """Instance to know about Relation between two classes"""
    
    """
            type:   0 - the same, 
                    1 - superclass,
                    2 - common superclasses
                    3 - common subclasses
                    4 - independent
            path: class heirarchy (from - to)
    """
    def __init__(self, type, path=None):
        self.type = type
        self.path = path

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
        return Relation(1, mro[:index + 1])    
    else:
        # if a is a superclass 
        mro = b.__mro__
        if a in mro:
            index = mro.index(a)
            return Relation(1, mro[:index + 1])
        else:
            return None

# task 3
def relation_classes(a, b):
    """Get relation between two classes"""
    
    # if the same
    if a == b: return Relation(0)
        
    # if is superclass
    sub = get_relation_mro(a, b)
    if sub is not None: return sub
    
    commonsub = common_subclasses(a, b, False)
    commonsup = common_superclasses(a, b)
    
    # if classes have common subclasses
    if commonsub: 
        return Relation(2, commonsub)
    # if classes have common superclasses
    elif commonsup: 
        return Relation(3, commonsup)
    else: 
        return Relation(4)

# test 3
#pprint(relation_classes(A, A))



class OverridedMember:
    """Instance to know about overriding"""
    def __init__(self, name, chain, sub):
        self.name = name
        self.value = chain.attributeValue
        self.oldC = chain.classInfo
        self.newC = sub

def get_class_overridings(cls):
    overridings = []
    members = get_class_members(cls)
    for mem in members:
        igenerator = iter(find_override(cls, mem))
        next(igenerator)
        try:
            override = next(igenerator)
            overridings.append(OverridedMember(mem, override, cls))
        except:
            continue
    return overridings

# task 2
def get_all_overridings(module):
    allClasses = [v for n, v in getmembers(module, isclass)]
    return filter(bool, (get_class_overridings(cls) for cls in allClasses))

# test 2
#pprint(list(get_all_overridings(module)))