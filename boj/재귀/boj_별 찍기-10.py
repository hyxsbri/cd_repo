





def starlink(n):

    if n == 1:
        return ['*']
    arr = []
    Stars = starlink(n//3)

    for star in Stars:
        arr.append(star*3)
    for star in Stars:
        arr.append(star+' '*(n//3)+star)
    for star in Stars:
        arr.append(star*3)

    return arr

N = int(input())
print('\n'.join(starlink(N)))        





























