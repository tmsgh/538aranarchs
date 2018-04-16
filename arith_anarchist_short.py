# https://fivethirtyeight.com/features/when-will-the-arithmetic-anarchists-attack/
# code ignores leap years
# 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096 
# no attacks on any Feb 29th
# longest gap = # of days w/o attack between attacks) includes a leap year
t=[0,31,59,90,120,151,181,212,243,273,304,334,366];print(sum([(y+1)==next(x[0] for x in enumerate(t) if x[1] > d)*(d+1-t[next(x[0] for x in enumerate(t) if x[1] > d)-1]) for d in range(365) for y in range(99)]));from statistics import mode;print(mode([y+1 for d in range(365) for y in range(99) if (y+1)==next(x[0] for x in enumerate(t) if x[1] > d)*(d+1-t[next(x[0] for x in enumerate(t) if x[1] > d)-1])]));print([n for n in list(range(1,100)) if n not in [y+1 for d in range(365) for y in range(99) if (y+1)==next(x[0] for x in enumerate(t) if x[1] > d)*(d+1-t[next(x[0] for x in enumerate(t) if x[1] > d)-1])]]);a=sorted([y*365+d+1 for d in range(365) for y in range(99) if (y+1)==next(x[0] for x in enumerate(t) if x[1] > d)*(d+1-t[next(x[0] for x in enumerate(t) if x[1] > d)-1])]);print(max([a[n+1]-a[n] for n in range(len(a)-1)]))
