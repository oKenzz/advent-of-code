def main():
    with open("input.txt", "r") as file:
        count = 0
        for line in file:
            current = line.strip()
            highest = "0"
            highest_mark = 0
            second_highest = "0"
            joltage = 0
            for i in range(len(current)):
                if highest < current[i]:
                    highest = current[i]
                    highest_mark = i

            if highest_mark != len(current) - 1:
                for j in range(highest_mark + 1, len(current)):
                    if second_highest < current[j]:
                        second_highest = current[j]
                    joltage = int(highest + second_highest)
            else:
                for j in range(highest_mark):
                    if second_highest < current[j]:
                        second_highest = current[j]
                    joltage = int(second_highest + highest)
            print(joltage)
            count += joltage
        print(count)


if __name__ == "__main__":
    main()
