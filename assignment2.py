import sys

def read_input_file(filename):
    try:
        with open(filename, "r") as file:
            # Reading the input data and parsing
            n = int(file.readline().strip())  # Total no of sticks
            L = int(file.readline().strip())  # Length of the tube
            length_sticks = list(map(int, file.readline().strip().split()))  # Lengths of sticks
            weights_sticks = list(map(int, file.readline().strip().split()))  # Weights of sticks
        return n, L, length_sticks, weights_sticks
    except Exception as e:
        print(f"Error reading file {filename}: {e}")
        exit(1)

#function which will calculate the maximum weight of the sticks that can be put in the tube
def get_maximum_weight(n, L, l_n, w_n):
    weight = 0
    sticks = []
    ratio_dict = {}
    #Heuristic: Sort in descending order of the sticks by their weight to length ratio and storing it in a dictionary where key is the index of the stick
    for i in range(n):
        ratio_dict[i] = w_n[i] / l_n[i]
    #Sorting the dictionary by the ratio of weight to length( sorting takes  n log n time)
    sorted_dict = sorted(ratio_dict.items(), key=lambda item: item[1], reverse=True)

    #iterating through each stick in the dictionary ( n time)
    for key, _ in sorted_dict:
        currentLength = l_n[key]
        if L == 0:
            break
        #if the current length of the stick is less than the remaining length of the tube, add the weight of the stick to the total weight
        if L >= currentLength:
            L -= currentLength
            weight += w_n[key]
        else: #if the current length of the stick is greater than the remaining length of the tube, add the fraction of the stick and it's weight to the total weight
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
    weight, sticks = get_maximum_weight(no_of_sticks, tube_length, lengths_of_sticks, weights_of_sticks)
    write_output_file(input, weight, sticks)
