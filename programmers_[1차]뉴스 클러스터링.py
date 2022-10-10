
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    l1 = []
    l2 = []
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            l1.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            l2.append(str2[i]+str2[i+1])
            
    from collections import Counter
    c1 = Counter(l1)
    c2 = Counter(l2)
    inter = list((c1 & c2).elements())
    union = list((c1 | c2).elements())
    if len(inter) == 0 and len(union) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
    