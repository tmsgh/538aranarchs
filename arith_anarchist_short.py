# https://fivethirtyeight.com/features/when-will-the-arithmetic-anarchists-attack/
# code ignores leap years
from statistics import mode;t=[31,28,31,30,31,30,31,31,30,31,30,31];a=[[d,m,y] for y in range(1,100) for m in range(1,13) for d in range(1,32) if d<=(t[m-1]+(not y%4 and m==2))];b=[n for n in a if n[2]==n[0]*n[1]];c=[n[2] for n in b];d=[n[0] for n in enumerate(a) if n[1] in b];print(len(b)," attacks; most attacks in",mode(c),"; safest years=",[n for n in range(1,100) if n not in c],"; longest gap = ",max([d[n+1]-d[n] for n in range(len(d)-1)])-1," days")
