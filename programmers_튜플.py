
def solution(s):
    ans = []
    s = s[2: -2]
    s = s.split('},{')
    s.sort(key = len)
    for i in s:
        x = i.split(',')
        for j in x:
            if int(j) not in ans:
                ans.append(int(j))
    return ans
    