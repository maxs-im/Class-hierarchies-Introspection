from inspect import isfunction

el = '\n'
separator = 100*'-'
smallseparator = separator[0:int(len(separator)/2)]

class Member:
    ATTRIBUTE_TYPE = 1
    FUNCTION_TYPE = 2

    @staticmethod
    def get_val_type(value):
        if isfunction(value):
            return Member.FUNCTION_TYPE
            
        return Member.ATTRIBUTE_TYPE

    @staticmethod
    def type2str(value):
        """Get member value and traslate it in our 'type'"""
        tp = Member.get_val_type(value)

        if tp == Member.FUNCTION_TYPE: 
            return "method"

        return "attribute"

    

class ChainNode:
    """Instance to know about member at some moment of hierarchy"""
    def __init__(self, cls, value):
        self.class_info = cls
        self.attribute_value = value

class MemberChain(Member):
    """Instance that defines member transitive inheritance"""
    def __init__(self, name, value, hierarchy):
        self.name = name
        self.value = value
        self.hierarchy = hierarchy
    
    def __str__(self):
        chainS = ' --> '.join(x.class_info.__name__ for x in self.hierarchy)
        line = f"{Member.type2str(self.value)} '{self.name}': {chainS}"
        return line + chainS

    #return f'Start point: {cls.__name__}' + separ + ''.join(lines) + separ

class RootMember:
    def __init__(self, name, value, ):
        self.name = name
        self.value = value

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
    SAME, SUPER, COMMON_SUPER, COMMON_SUB, INDEPENDENT = tuple(range(5))

    def __init__(self, typei, path=None):
        self.type = typei
        self.path = path

    def __str__(self):
        tp = self.type

        if tp == Relation.SAME:
            return Relation._psame(self.path[0])
        elif tp == Relation.SUPER:
            return Relation._psuperclass(self.path)
        elif tp == Relation.COMMON_SUB:
            return Relation._pcommonclasses(self.path, 'subclass')
        elif tp == Relation.COMMON_SUPER:
            return Relation._pcommonclasses(self.path, 'superclass')
        else:
            return 'Classes are from different hierarchy'

    @staticmethod
    def _psame(cls):
        return f'Classes are the same {cls.__name__}'
    
    @staticmethod
    def make_class_path(path):
        return ' --> '.join(map(lambda x: x.__name__, path))

    @staticmethod
    def _psuperclass(queue):
        head = f'{queue[-1].__name__} is a superclass for {queue[0].__name__}'
        heararchy = Relation.make_class_path(queue)
        return head + el + heararchy
    
    @staticmethod
    def _pcommonclasses(path, name):
        head = f'{path[0].__name__} and {path[1].__name__} have common {name}'
        heararchy = ' & '.join(map(lambda x: x.__name__, path[2:]))
        return head + el + heararchy
    

class OverridedMember(Member):
    """Instance to know about overriding"""
    def __init__(self, name, chain, sub):
        self.name = name
        self.value = chain.attribute_value
        self.oldC = chain.class_info
        self.newC = sub

    def __str__(self):
        return f'{self.name} of {self.oldC.__name__} redefined in the {self.newC.__name__}'

