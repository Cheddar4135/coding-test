"""난이도:
> 총평
  약간 구현 막막함 느껴짐. 전처리같은것부터 귀찮.
> 문제분석
  입력: 멜로디문자열, ["재생시작,재생끝,노래제목,멜로디"]
  1. 각 음은 1분. 중간에 끊길 수 있다. 
  2. 가장 재생시간 긴 음악 먼저-> 입력된 음악 제목 먼저
  
  7음. 14분 -> 멜로디2번
  6음. 5분 -> 5번째음까지
  
> 풀이전략:
  1. 멜로디 파싱 #B 등의 음을 문자열하나로 암호화
  2. 실제 재생된 멜로디 문자열 구하기
  3. 복수개일때 우선순위조건대로 하나 반환하기
"""

def solution(m, musicinfos):

    # 기능1, #음 매핑규칙설계
    changes = {"C#":"c", "D#":"d","F#":"f","G#":"g","A#":"a" }
    def nomalize(melody):
        for old, new in changes.items():
            melody = melody.replace(old,new)
        return melody
    
    results = []
    # 기능2, musicinfos 전처리하기
    for id, music in enumerate(musicinfos):
        # 기능2.1 시간 전처리
        start, end, name, melody = music.split(',')
        sh, sm = [int(i) for i in start.split(':')]
        eh, em = [int(i) for i in end.split(':')]
        time = eh*60+em-sh*60-sm
        #print(f"재생시간:{time}")
        
        # 기능2.2 멜로디 전처리
        melody = nomalize(melody)           
        
        # 기능2.3 멜로디 합치기
        max_melody = melody* (time // len(melody) +1)
        played_melody = max_melody[:time]
        #print(f"전처리된 멜로디:{played_melody}")
        
        if nomalize(m) in played_melody:
            results.append((-time, id, name))
    if results:
        return sorted(results)[0][2]
    else:
        return "(None)"