
def is_contained(p1, p2):
    p1_start = int(p1.split("-")[0])
    p1_end = int(p1.split("-")[1])

    p2_start = int(p2.split("-")[0])
    p2_end = int(p2.split("-")[1])

    if((p2_start >= p1_start and p2_end <= p1_end)):
        return True
    elif(p1_start >= p2_start and p1_end <= p2_end):
        return True
    else: return False

if __name__ == "__main__":
    with open('input.txt', 'r') as f:

        res = 0
        for line in f.readlines():
            line = line.rstrip()
            p1 = line.split(",")[0]
            p2 = line.split(",")[1]
            print(f"{p1} and {p2}")
            if(is_contained(p1, p2)):
                res += 1
        print(res)



        