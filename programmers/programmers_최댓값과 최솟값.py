
def solution(s):
    l = list(map(int, s.split()))
    l.sort()
    return str(l[0])+' '+str(l[-1])
    
