def unnested(l):
    if l == []:
        return []
    if type(l[0]) == list:
        return unnested(l[0]) + unnested(l[1:])
    return l[:1] + unnested(l[1:])
l = [1,3,[4,5,[7]],[],[8,9,[[]]]]
print(unnested(l))
