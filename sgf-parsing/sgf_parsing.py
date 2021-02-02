import re

class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True


def parse(input_string):
    if input_string == '(;)':
        return SgfTree()
    
    value_reg = r'\[((?:[A-Za-z\s]|\\.)+)\]'
    property_reg = r'([A-Z]+)((?:'+value_reg+')+)'

    sgf_reg = r'\(;(?P<node>'+property_reg+')(?P<children>(\(?;'+property_reg+'\))*)\)?'

    whole_match = re.match(sgf_reg, input_string)
    if whole_match:
        f = re.findall(property_reg, whole_match['children'])
        children = []
        if f:
            for child in f:
                children.append(SgfTree({child[0]:re.findall(value_reg, child[1])}))
        nm = re.match(property_reg, whole_match['node'])
        nmg = nm.groups()
        vals = re.findall(value_reg, nmg[1])
        vals = [v.replace('\\','').expandtabs(1) for v in vals]
        prop = {nmg[0]:vals}
        return SgfTree(prop.children)
    else:
        raise ValueError("Bad input {}".format(input_string))
