

# https://school.programmers.co.kr/learn/courses/30/lessons/150370
# 한 달(1 month) - 28 days

def solution(today, terms, privacies):
    ans = []

    # 날짜를 일 단위로 변환하는 함수(int)
    def dateToDay(date):
        year, month, day = map(int, date.split("."))
        return (year*12*28)+(month*28)+day

    # 오늘 날짜를 일 단위로 변환(int)
    today = dateToDay(today)

    # 약관 종류 key / 유효 기간을 value(int)로 가지는 dict 생성
    termsInfo = dict()
    for term in terms:
        term = term.split()
        termsInfo[term[0]] = int(term[1])*28

    for i in range(len(privacies)):
        date, term = privacies[i].split() # 날짜와 약관이 들어있는 요소를 분리,
        if dateToDay(date)+termsInfo[term] <= today: # 날짜와 약관 기간을 합친 day가 '오늘' 이랑 겹치기만 해도 파기
            ans.append(i+1)
            # 정답 추가
    
    return ans

