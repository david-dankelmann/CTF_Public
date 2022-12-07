
s1 = ["F", "C", "P", "G", "Q", "R"]
s2 = ["W", "T", "C", "P"]
s3 = ["B", "H", "P", "M", "C"]
s4 = ["L", "T", "Q", "S", "M", "P", "R"]
s5 = ["P", "H", "J", "Z", "V", "G", "N"]
s6 = ["D", "P", "J"]
s7 = ["L", "G", "P", "Z", "F", "J", "T", "R"]
s8 = ["N", "L", "H", "C", "F", "P", "T", "J"]
s9 = ["G", "V", "Z", "Q", "H", "T", "C", "W"]

stack_map = {"1" : s1, "2" : s2, "3" : s3, "4" : s4, "5" : s5, "6" : s6, "7" : s7, "8" : s8, "9" : s9}

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            line = line.replace("move ", "") #Remove garbage
            line = line.replace("to ", "")
            line = line.replace("from ", "")

            amount = int(line.split(" ")[0]) #split by whitespace
            source = stack_map[line.split(" ")[1]] #get the right stack variable from the number/string
            target = stack_map[line.split(" ")[2]]

            #print(line)
            #print(f"{source} + {target}")

            target[:] = target + source[-amount:][::-1] #Don't forget to reverse the slice.
            source[:] = source[:-amount]

            #print(f"{source} + {target}")
            #print("\n")
            
        #print result
        res = ""
        for key, stack in stack_map.items():
            print(f"Stack {key}: {stack}")
            res += stack[-1]
        print(f"Top Elements: {res}")



        