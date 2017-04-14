class TN:
    def __init__(self,number, value, children = []):
        self.number = number
        self.value     = value
        self.children  = children

    def sums(self, notovisit):
        if self.children == []: return 1
        else:
            l = 0
            for i in self.children:
                if i != notovisit:
                    l+=self.sums(i,notovisit)
            return l

def main():
    trees = []
    total_sum = 0
    n = int(input())
    j=0
    bonds = []
    for i in input().strip().split():
        trees.append(TN(j+1,int(i)))
        total_sum+= int(i)
        j+=1
    visited = set(1)
    for i in range(n-1):
        l = input().split()
        bonds.append(l)
        if int(l[0]) in visited:
            trees[int(l[0])-1].children.append(trees[int(l[1])-1])
            visited.add(int(l[1]))
        else:
            trees[int(l[1])-1].children.append(trees[int(l[0])-1])
            visited.add(int(l[0]))

    m = total_sum


