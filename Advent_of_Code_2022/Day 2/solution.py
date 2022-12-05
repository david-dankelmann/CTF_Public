with open('input.txt', 'r') as f:
    score_value = {"X" : 1, "Y" : 2, "Z" : 3}
    game_result = {"AX" : 3, "BY" : 3, "CZ" : 3, "AY" : 6, "AZ" : 0, "BX" : 0, "BZ" : 6, "CX" : 6, "CY" : 0}

    score = 0
    for line in f.readlines():
        line = line.rstrip()
        enemy = line[0]
        advice = line[2]

        score += score_value[advice] + game_result[enemy+advice]
    print(score)

