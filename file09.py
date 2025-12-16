def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data)
    l1 = []
    x = 9999999999
    for i in f.read():
        if i.isdigit():
            if int(i)<x:
                x = int(i)
    return x
print(main('./data/data09.txt'))

# Read data from file