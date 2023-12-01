numbers_text = {"zero": 0, "one": 1, "two":2, "three": 3, "four":4, "five":5, "six": 6, "seven":7, "eight": 8, "nine":9}

def find_first_digit(input):
    current_str = ""
    for i in range(0, len(input)-1):
        current_str += input[i]
        if input[i].isdigit():
            return input[i]
        else:
            for k in numbers_text.keys():
                if k in current_str:
                    return str(numbers_text[k])

def find_last_digit(input):
    current_str = ""
    for i in range(len(input)-1, -1, -1):
        current_str = input[i:]
        if input[i].isdigit():
            return input[i]
        else:
            for k in numbers_text.keys():
                if k in current_str:
                    return str(numbers_text[k])

def sum_all_first_last_digits(input_file):
    calculate_sum = 0
    with open(input_file) as file:
        for line in file:
            # print(line)
            first_digit = find_first_digit(line)
            # print("first: ", first_digit)
            last_digit = find_last_digit(line)
            # print("last: ", last_digit)
            calculate_sum += int(first_digit + last_digit)
            # print(calculate_sum)
    return calculate_sum


if __name__ == "__main__":
    print(sum_all_first_last_digits("input.txt"))