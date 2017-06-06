def main():
    n = int(input())
    lst = []
    final_str = ""
    temp_lst = ""
    while n>0:
        lst.append(sorted([int(i) for i in input().strip().split()]))
        n-=1
    for j in lst:
        for i in range(j[0],j[-1]):
            if i not in j:
                temp_lst += str(i) + " "
        final_str += temp_lst.strip() + "\n"
        temp_lst = ''
    return final_str
print(main())