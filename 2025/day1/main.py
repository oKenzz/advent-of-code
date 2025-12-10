def main():
    start_pos: int = 50
    zero_count: int = 0
    with open("input.txt", "r") as file:
        for line in file:
            direction: str = line[0]
            steps: int = int(line[1:])

            if direction == "L":
                start_pos = (start_pos - steps) % 100
            else:
                start_pos = (start_pos + steps) % 100

            if start_pos == 0:
                zero_count += 1
    print(zero_count)


if __name__ == "__main__":
    main()
