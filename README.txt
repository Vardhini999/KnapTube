*Team Members*

# Ancita Maria Andrade
	UID: U01085022
	email: andrade.12@wright.edu
# Chaitanya Vardhini Anumula
	UID: U01094128
	email: anumula.12@wright.edu
# Sai Sree Korrapati
	UID: U01090060
	email: korrapati.16@wright.edu


* Heuristic Used for Greedy *

Sorting in descending order of weight to length ratio of the sticks


* Algorithm *

# L be the tube length to be filled
# For all sticks, get the weight to length ratio
# Sort the ratios in the descending order ( nlogn )
# total_weight = 0
# for each stick in the sorted sticks (n)
    l be the length of the stick
    w be the weight of the stick
    if L is 0
        return total_weight
    if L is greater than l
        add w to total_weight
        subtract l from L
    else 
        add fraction of the stick and it's corresponding weight to the total weight
        L = 0

* Time complexity *

Given n sticks

Sorting the sticks in the desceinding order of their weight:length taken "nlogn"
Iterating over n sticks and adding the weights takes "n" times

So, the Time complexity would be
O(T) = O(nlogn) + O(n) => O(nlogn)

So, the time complexity is O(nlogn)

* Notes *
# To run the program type 
python3 assignment2.py Input.txt 

or

python3 assignment2.py Tests/Input*.txt where * is [1-6]

* The test case Input6.txt is same as the Input.txt
* If there are multiple sticks with same weight:length,
 then the algorithm takes the sticks in the order of which it is provided in the input