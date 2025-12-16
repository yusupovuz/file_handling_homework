def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data)
    l = []
    for i in f.read().split():
        for j in i:
            if j.isalpha():
                l.append(j)
    return l
print(main('./data/data04.txt'))
# Read data from file