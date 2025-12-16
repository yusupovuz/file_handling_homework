def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data)
    l = []
    x = 0
    for i in f.readlines():
        l.append(len(i)-1)
    l[-1]+=1
    return l
    
print(main('./data/data06.txt'))

# Read data from file