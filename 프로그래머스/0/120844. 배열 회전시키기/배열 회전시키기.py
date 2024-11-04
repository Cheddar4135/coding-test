def solution(numbers, direction):
    """
    main idea
        iterate the list, let's save the elements in to new array with the 2ways.
        1. right인 경우, new[i+1] = numbers[i] if i!=마지막, else new[0] = numbers[i]
        2. left인 경우, new[i-1] = numbers[i] if i!=첫번째, else new[마지막] = numbers[0]
    """
    new = [0 for i in range(len(numbers))]
    if direction =="right":
        for i in range(len(numbers)):
            if i ==len(numbers)-1:
                new[0]=numbers[i] 
            else:
                new[i+1]=numbers[i]
    if direction =="left":
        for i in range(len(numbers)):
            if not i:
                new[-1]=numbers[i] 
            else:
                new[i-1]=numbers[i]
    return new