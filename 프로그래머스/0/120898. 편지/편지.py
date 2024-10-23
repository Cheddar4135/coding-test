def solution(message):
    return len(message)*2

def solution(message):
    """비트 시프트 연산
    a>>n : 2진수a의 최하위비트에 0이 n개만큼 추가. a*2^n
    a<<n: 2진수a의 최상위비트에 0(양수)이나 1(음수)이 n개만큼 추가, 최하위비트n개는 삭제. a*(0.5)^n

    시프트연산은 곱하기보다 컴퓨터의 부담이 적으니까 웬만하면 이 방식이 좋겠군.
    """
    return len(message)<<1
