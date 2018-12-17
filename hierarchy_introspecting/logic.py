from ._instances import *

def get_class_members(cls):
    """Get members that defined only in that class"""
    return filter(
        lambda x: not x.startswith('__'), 
        dir(cls)
    )

def _find_override(maincls, attrname):
    """Generator through MRO for attribute overriding"""
    for cls in maincls.__mro__[:-1]:
        for name, value in cls.__dict__.items():
            if attrname == name:
                yield ChainNode(cls, value)

def _transitive_inheritance(cls):
    """Create overriding generator for each class attribute"""
    members = get_class_members(cls)
    return {m: _find_override(cls, m) for m in members}

# task 1
def generate_chain(cls):
    """Transitive inheritance chains for class"""
    chains = list()
    chainGen = _transitive_inheritance(cls)
    for name, hierarchyGen in chainGen.items():
        classes = list()
        initType = None
        for x in iter(hierarchyGen):   
            if not initType: 
                initType = x.attribute_value
            classes.append(x.class_info)
        chains.append(MemberChain(name, initType, classes))
    return chains

def generate_first_node(cls):
    """Look for only first member using"""
    attrs = _transitive_inheritance(cls)

    return {name: next(iter(gen)) for name, gen in attrs.items()}

# task 6
def get_root_members(cls):
    root = cls.__mro__[-2]
    if root.__name__ == cls.__name__:
        return None
    else:
        chain = generate_first_node(cls)
        return {name: mc for name, mc in chain.items() if mc.class_info == root}

def _get_dict_extremum(data, maximum):
    """Get all extremum dictionary keys by its value"""
    if not data:
        return None

    reducer = max if maximum else min
    reducer_key = reducer(data.values())

    return (k for k in data if data[k] == reducer_key)

# task 4
def common_subclasses(hierarchy, greatest=True):
    """Find common subclass class for two classes"""
    # recursively get all subclasses for class
    def get_subclasses(cls):
        for subclass in cls.__subclasses__():
            yield from get_subclasses(subclass)
            yield subclass
    
    get_set = lambda cls: set(x for x in get_subclasses(cls))
    
    sets = map(get_set, hierarchy)
    common = {x: len(x.__mro__)
        for x in set.intersection(*sets)}
    
    return _get_dict_extremum(common, greatest)

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

    return _get_dict_extremum(common, not greatest)

def get_relation_mro(a, b):
    mro = a.__mro__
    # if b is a superclass
    if b in mro:
        index = mro.index(b)
        return mro[:index + 1]   
    else:
        # if a is a superclass 
        mro = b.__mro__
        if a in mro:
            index = mro.index(a)
            return mro[:index + 1]
        else:
            return None

# task 3
def relation_classes(a, b):
    """Get relation between two classes"""
    
    # if the same
    if a == b: return Relation(Relation.SAME, [a])
        
    # if is superclass
    sub = get_relation_mro(a, b)
    if sub is not None: return Relation(Relation.SUPER, sub)
    
    commonsub = common_subclasses([a, b], False)
    commonsup = common_superclasses(a, b)
    
    # if classes have common subclasses
    if commonsub: 
        return Relation(Relation.COMMON_SUB, [a, b] + list(commonsub))
    # if classes have common superclasses
    elif commonsup: 
        return Relation(Relation.COMMON_SUPER, [a, b] + list(commonsup))
    else: 
        return Relation(Relation.INDEPENDENT, [a, b])

# task 2
def get_class_overridings(cls):
    overridings = []
    members = get_class_members(cls)
    for mem in members:
        igenerator = iter(_find_override(cls, mem))
        next(igenerator)
        try:
            override = next(igenerator)
            overridings.append(OverridedMember(mem, override, cls))
        except:
            continue
    return overridings
