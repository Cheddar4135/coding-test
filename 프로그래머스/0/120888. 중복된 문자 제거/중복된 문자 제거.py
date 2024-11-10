def solution(my_string):
    """
    main idea: 리스트로 바꿔서 set함수로 중복제거 후 다시 문자열로 반환
    --> 문제점: set으로 하면 순서가 뒤죽박죽이 된다. 2번째로 중복해서 나온문자를 제거해야한다.
    
    main idea: 문자열 왼쪽부터 오른쪽으로 순회하면서 해당 문자가 이미 나온 문자라면 제거 
        1. for c in my_string: 
        2. 처음 나온 문자라면 count[c] = 1
        3. 만약 두번째 나온 문자라면 해당 인덱스의 문자 제거. 아 이러려면 리스트로 바꿔서 제거해야겠네. 
    """
    my_list = list(my_string)
    print(my_list)
    cnt = ''
    for i,item in enumerate(my_list):
        if not item in cnt:
            cnt+=item
    return "".join(cnt)