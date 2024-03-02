from utils import entropy

def countOccurences(values: list) -> dict:
    d: dict = {}
    for value in values:
        if d.get(value) == None:
            d[value] = 1
        else:
            d[value] += 1
    return d

def main():
    file = open('data/titanic-homework.csv', 'r')

    lines = file.read().splitlines()
    for line in lines:
        # print(line)
        # print('\t'.join(line.split(',')))

        line_values = line.split(',')
        print(line_values[4])
        # for v in line.split(','):
        #     print(f'{v}')

    test = map(lambda x: x.split(',')[4], lines)
    occurences = countOccurences(test)
    e = entropy(occurences, len(lines))
    print(e)
    
    file.close()

if __name__ == '__main__':
    main()