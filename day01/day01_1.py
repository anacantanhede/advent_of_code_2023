def find_first_digit(input):
    for i in input:
        if i.isdigit():
            return i

def find_last_digit(input):
    for i in reversed(input):
        if i.isdigit():
            return i

def sum_all_first_last_digits(input_file):
    calculate_sum = 0
    with open(input_file) as file:
        for line in file:
            first_digit = find_first_digit(line)
            # print("first: ", first_digit)
            last_digit = find_last_digit(line)
            # print("last: ", last_digit)
            calculate_sum += int(first_digit + last_digit)
    return calculate_sum


if __name__ == "__main__":
    print(sum_all_first_last_digits("input"))