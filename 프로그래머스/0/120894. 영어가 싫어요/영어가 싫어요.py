def solution(numbers):
    """
    공백 없이 조합된 영어들을 어떻게 split할 것인가.
    일단 딕셔너리를 사용해 풀자.
    """
    chg_dic={"zero":'0',"one":'1',"two":'2',"three":'3',"four":'4',"five":'5',"six":'6',"seven":'7',"eight":'8',"nine":'9'}
    start=0
    answer=""
    for i in range(len(numbers)+1):
        num = numbers[start:i]
        print(num)
        if num in chg_dic:
            answer+=chg_dic[num]
            print("answer:",answer)
            start=i
            print(start)
    return int(answer)