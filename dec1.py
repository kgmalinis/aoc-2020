from functools import reduce

class Dec1:
    # here we are reading in the input, and splitting it so that we get all the numbers
    def __init__(self, input_file = 'input.txt'):
        with open(input_file, 'r') as puzzle:
            self.input = list(map(int, puzzle.read().split('\n')))
            
            # converts our input into a set
            self.input_set = set(self.input)
            
    # in part 1, we are finding the 2 numbers that add to 2020 and multiplying them for the answer
    def part_one(self):
        # lambda() is an anonymous function that evaluates a single expression 
        nums = list(filter(lambda x: 2020 - x in self.input_set, self.input))
        
        # reduce() reduces a list of items to a single, cumulative value
        return reduce(lambda x, y: x * y, nums)
    
    # in part 2, we are essentially doing the same thing but different 
    def part_two(self):
        # yes, this is O(n^3) but I'm lazy
        for i in range(len(self.input)):
            for j in range(i, len(self.input)):
                for k in range(j, len(self.input)):
                    if self.input[i] + self.input[j] + self.input[k] == 2020:
                        return self.input[i] * self.input[j] * self.input[k]

# this is to display everything all fancily 
if __name__ == "__main__":
    answer = Dec1()
    print('Part 1: ', answer.part_one())
    print('Part 2: ', answer.part_two())