import sys

def read_input_file(filename):
    try:
        with open(sys.argv[1], "r") as file:
            print()
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        exit(1)

def sticks_and_weights(n, L, l_n, w_n):
    weight = 0
    sticks = []
    ratio_dict = {}
    for i in range(n):
        ratio_dict[i] = w_n[i] / l_n[i]
    sorted_dict = sorted(ratio_dict.items(), key=lambda item: item[1], reverse=True)

    for key, _ in sorted_dict:
        currentLength = l_n[key]
        if L == 0:
            break
        if L >= currentLength:
            L -= currentLength
            weight += w_n[key]
        else:
            weight += w_n[key] * (L / currentLength)
            L = 0
        sticks.append(key+1)
    return weight, sticks

def write_output_file(filename, weight, sticks):
    new_filename = filename.replace("Input", "Output")
    with open(new_filename, "w") as file:
        file.write(f"{weight}\n")
        file.write(" ".join(map(str, sticks)) + "\n")

if __name__ == "__main__":
    input = "Input.txt"
    output = "Output.txt"

    if len(sys.argv) == 2:
        input = sys.argv[1]

    no_of_sticks, tube_length, lengths_of_sticks, weights_of_sticks = read_input_file(input)
    sticks, weight = sticks_and_weights(no_of_sticks, tube_length, lengths_of_sticks, weights_of_sticks)
    print(sticks, weight)
    write_output_file(input, weight, sticks)