

def findDuplicateItem(rucksack):
    mid = len(rucksack) // 2
    first_half = rucksack[:mid]
    second_half = rucksack[mid:]
    for c in first_half:
        if(c in second_half):
            return c
    raise Exception("No duplicate found.")


def calcPriority(item):
    
    if(item.isupper()):
        return ord(item) - 65 + 27
    else: #lowercase
        return ord(item) - 96
        

    


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        prio_sum = 0
        for line in f.readlines():
            line = line.rstrip()
            duplicate_item = findDuplicateItem(line)
            prio_sum += calcPriority(duplicate_item)
        print(prio_sum)