# Problem Set 4A
# Name: Deniz Sert
# Collaborators: Frank Gonzales
# Time Spent: 3:00
# Late Days Used: 0

#NOTE: My computer's OS got wiped -> no Python Interpreter -> I WAS NOT ABLE TO RUN THE TESTS
#I wrote the code "blindly" using online IDEs

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
tree1 = [[37, 20], [[0, 4], 1]]
tree2 = [[30, 2], 5]
tree3 = [[11], [12, 13, 14], [10]]


# Part A1: Addition on tree leaves

def add_tree(tree):
    """
        Recursively computes the addition of all tree leaves.
        Returns an integer representing the addition.
        
        Inputs
        tree: A list (potentially containing sublists) that
        represents a tree structure.
        Outputs
        total: An int equal to the addition of all leaves of the tree.
        
        """
    
    # TODO: Your code here
    sum = 0
    if len(tree) == 0:
        return 0
    
    for e in tree:
        if type(e) == list:
            sum += add_tree(e)
        else:
            sum+=e
    
    return sum




# Part A2: Arbitrary operations on tree leaves

def summation(a,b):
    """
        Example operator function.
        Takes in two integers, returns their sum.
        """
    return a + b

def product(a,b):
    """
        Example operator function.
        Takes in two integers, returns their product.
        """
    return a * b

def op_tree(tree, op, base_case):
    """
        Recursively runs a given operation on tree leaves.
        Return type depends on the specific operation.
        
        Inputs
        tree: A list (potentially containing sublists) that
        represents a tree structure.
        op: A function that takes in two inputs and returns the
        result of a specific operation on them.
        base_case: What the operation should return as a result
        in the base case (i.e. when the tree is empty).
        """
    
    # TODO: Your code here
    counter = 0
    if len(tree) == 0:
        return base_case
    
    for e in tree:
        if type(e) == list:
            counter = op(op_tree(e, op, base_case), counter)
        else:
            counter = op(e, op, base_case)
    
    return counter
# Part A3: Searching a tree

def search_div_two(a, b):
    """
        Operator function that searches for divisible-by-two values within its inputs.
        
        Inputs
        a, b: integers or booleans
        Outputs
        True if either input is equal to True or divisible-by-two, and False otherwise
        """
    
    # TODO: Your code here
    
    #checks the different cases that a and b could be (int or bool)
    
    #a and b are both ints
    if type(a) == int and type(b) == int:
        if a%2==0 or b%2==0:
            return True
    #a and b are b both bools
    elif type(a) == bool and type(b) == bool:
        if a == True or b == True:
            return True
    #a is an int and b is a bool
    elif type(a) == int and type(b) == bool:
        if b == True or a%2==0:
            return True
    #a is a bool and b is an int
    elif type(b) == int and type(a) == bool:
        if a == True or b%2==0:
            return True
    #none of the cases were true
    else:
        return False

if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below.
    pass
    tree4 = [[37, 20], [[0, 4], 1]]
    
    
    
    print(add_tree(tree4.pop(0)))
