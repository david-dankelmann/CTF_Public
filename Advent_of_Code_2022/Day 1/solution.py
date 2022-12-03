with open('input.txt', 'r') as f:
    max_cal = 0
    curr_cal = 0
    for line in f.readlines():
        line = line.rstrip()
        if(line == ""):
            if(max_cal < curr_cal):
                max_cal = curr_cal
            curr_cal = 0
            continue
        curr_cal += int(line)
    print(max_cal)