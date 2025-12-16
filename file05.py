def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data)
    l1 = []
    x = 0
    for i in f.read():
        if i.isdigit():
            l1.append(i)
        x+=1
    return [len(l1),x-len(l1)]
print(main('./data/data05.txt'))
# Read data from file