def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data)
    x = 0
    for i in f.read():
        if i.isdigit():
            x+=int(i)
    return x
print(main('./data/data07.txt'))

# Read data from file