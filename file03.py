def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data)
    l = []
    for i in f.read().split():
        for j in i:
            if j.isdigit():
                l.append(j)
    return l
print(main('./data/data03.txt'))


