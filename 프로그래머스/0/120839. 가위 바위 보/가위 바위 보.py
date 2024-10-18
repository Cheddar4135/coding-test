def solution(rsp):
    victory = {'2':'0','0':'5','5':'2'}
    return ''.join(victory[c] for c in rsp)