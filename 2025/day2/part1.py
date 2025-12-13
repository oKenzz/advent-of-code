def main():
    with open("input.txt", "r") as file:
        input = file.read().split(",")
        count = 0
        for id_range in input:
            ranges = id_range.split("-")
            interval = int(ranges[1]) - int(ranges[0])
            current = int(ranges[0])
            for i in range(interval + 1):
                combinations = find_unique_substrings(str(current))
                valid = check_if_id_valid(str(current), combinations)
                if not valid:
                    count += current
                print(f"Id: {current}, valid: {valid}")
                current += 1
    print(count)


def check_if_id_valid(id: str, substrings: set) -> bool:
    length = len(id)
    for substring in substrings:
        if length / 2 == len(substring):
            return not (id[0 : len(substring)] == id[len(substring) :])
    return True


def find_unique_substrings(string: str) -> set:
    length = len(string)
    unique_substrings = set()
    for i in range(length):
        current = ""
        for j in range(i, length):
            current += string[j]
            unique_substrings.add(current)

    return unique_substrings


if __name__ == "__main__":
    main()
