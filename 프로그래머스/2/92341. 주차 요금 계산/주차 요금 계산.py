from collections import defaultdict

def normtime(clock):
    hh, mm = clock.split(':')
    return int(hh)*60 + int(mm)
    
def gettime(timelist):
    if len(timelist) % 2:
        timelist.append(normtime("23:59"))
    time = 0
    for i,t in enumerate(timelist):
        if i % 2:
            time +=t
        else:
            time -=t
    
    return time

def solution(fees, records):
    # {차량번호: 총 이용시간} 구하기
    cartime = defaultdict(list)

    for row in records:
        clock, carnum, inout = row.split(" ")
        minute = normtime(clock)
        cartime[carnum].append(minute)
    
    for k, v in cartime.items():
        #print(f"key:{k},value:{v}")
        cartime[k] = gettime(v)
        
    btime = fees[0]
    bfee = fees[1]
    utime = fees[2]
    ufee = fees[3]
    
    carlist = sorted(cartime, key=lambda x: int(x))
    carfee = []
    for car in carlist:
        ttime = cartime[car]
        if ttime <= btime:
            tfee = bfee
        else:
            tfee = bfee
            ttime -= btime
            tfee += ((ttime + utime - 1)// utime) * ufee
        carfee.append(tfee)
    
    return carfee