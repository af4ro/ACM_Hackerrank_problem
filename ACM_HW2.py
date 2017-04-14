
import _collections
visited = set()
temp_list1 = []
temp_list2 =[]
bonds_tuple = []
bonds = _collections.defaultdict(list)
vals = {}

def main():
    lowest_sum = 99999999
    n = int(input())
    j = 1
    for i in input().strip().split():
        vals[j] = int(i)
        j+=1
    total_sum = sum(vals.values())
    while n>1:
        i = input().split()
        bonds[int(i[0])].append(int(i[1]))
        bonds[int(i[1])].append(int(i[0]))
        bonds_tuple.append((int(i[0]),int(i[1])))
        n-=1
    sum1 = 0
    sum2 = 0
    for j,k in bonds_tuple:
        temp_list1.append(j)
        visited.add(j)
        visited.add(k)
        while temp_list1!=[]:
            current = temp_list1.pop(0)
            print(current)
            if current in visited:
                continue
            if current in bonds:
                sum1+=vals[current]
                temp_list1.extend(bonds[current])
            visited.add(current)
        temp_list1.append(k)
        '''while True:
            if temp_list1 == []:
                break
            current = temp_list1.pop(0)
            if current in bonds:
                sum2+=vals[current]
                temp_list1.extend(bonds[current])
        '''
        if abs(sum1-sum2) < lowest_sum:
            lowest_sum = abs(sum1-sum2)
    print(lowest_sum)



'''
def sums(visited, sum, number_check):
    for i in bonds[number_check]:
        if i not in visited:
            visited.append(i)
            sum+=vals[i]
            sum+=sums(visited,0,i)
    return sum
'''
main()
"""
vals = {}
def main():
    lowest_sum = 99999999
    n = int(input())
    j = 1
    for i in input().strip().split():
        vals[j] = int(i)
        j+=1
    total_sum = sum(vals.values())
    while n>1:
        i = input().split()
        bonds[int(i[0])].append(int(i[1]))
        bonds[int(i[1])].append(int(i[0]))
        bonds_tuple.append((int(i[0]),int(i[1])))
        n-=1
"""