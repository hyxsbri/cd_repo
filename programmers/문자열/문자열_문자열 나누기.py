

# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    cnt_s = s
    cntr1=[]
    # 첫글자 카운터
    cntr2=[]
    # 이외글자 카운터
    ans=0

    for i in range(len(s)):

        if len(cntr1)==0:
            cntr1.append(s[i])
        elif s[i] in cntr1:
            cntr1.append(s[i])
        elif s[i] not in cntr1:
            cntr2.append(s[i])

        if len(cnt_s)!=1:
            cnt_s = cnt_s[1:]
            # 문자열이 하나 남은게 아니면 첫 글자 탈락시키기
        else:
            continue
            # 문자열이 하나 남았으면 첫 글자 탈락 pass

        if len(cntr1)==len(cntr2):
            ans+=1
            cntr1.clear()
            cntr2.clear()

    if cnt_s:
        ans+=1  
    return ans

