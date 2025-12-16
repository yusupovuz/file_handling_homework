def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data)
    l = []
    x = -9999999
    for i in f.readlines():
        if len(i)>x:
            x = len(i)
    return x-1
print(main('./data/data10.txt'))

# Read data from file