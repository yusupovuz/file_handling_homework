def main(data):
    f = open(data)
    a = f.read().split(',')
    return a
print(main('./data/data01.txt'))