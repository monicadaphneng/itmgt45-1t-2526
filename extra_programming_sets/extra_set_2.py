'''Extra Programming Set 2

This assignment will challenge you with a variety of common programming problems
that test your logical thinking, string and list manipulation skills, and
ability to work with nested data structures.
'''

def is_pangram(sentence):
    '''Pangram Checker.

    A pangram is a sentence that contains every single letter of the alphabet
    at least once.

    This function should be case-insensitive.
    Non-alphabetic characters (numbers, punctuation, spaces) should be ignored.

    Examples:
    is_pangram("The quick brown fox jumps over the lazy dog") -> True
    is_pangram("The five boxing wizards jump quickly.") -> True
    is_pangram("Hello world") -> False
    is_pangram("") -> False

    Hint: The `string` module has a useful constant `string.ascii_lowercase`.
    Alternatively, you can create the alphabet string yourself.

    Parameters
    ----------
    sentence: str
        the sentence to check.

    Returns
    -------
    bool
        True if the sentence is a pangram, False otherwise.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def pascal_triangle(n):
    '''Pascal's Triangle.

    Generate the first n rows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly
    above it. The edges of the triangle are all 1s.

    Example for n = 5:
    Row 0: [1]
    Row 1: [1, 1]
    Row 2: [1, 2, 1]
    Row 3: [1, 3, 3, 1]
    Row 4: [1, 4, 6, 4, 1]

    The function should return a list of lists, where each inner list
    is a row of the triangle.

    Examples:
    pascal_triangle(1) -> [[1]]
    pascal_triangle(3) -> [[1], [1, 1], [1, 2, 1]]
    pascal_triangle(0) -> []

    Parameters
    ----------
    n: int
        the number of rows to generate.

    Returns
    -------
    list[list[int]]
        a list of lists of integers representing the triangle.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def merge_sorted_lists(list1, list2):
    '''Merge Two Sorted Lists.

    Given two lists of integers, each sorted in ascending order, merge them
    into a single sorted list.

    Try to do this in a single pass through both lists, without simply
    concatenating them and calling a sort function.

    Examples:
    merge_sorted_lists([1, 2, 4], [1, 3, 4]) -> [1, 1, 2, 3, 4, 4]
    merge_sorted_lists([], [0]) -> [0]
    merge_sorted_lists([5, 8, 9], [1, 2, 3]) -> [1, 2, 3, 5, 8, 9]

    Parameters
    ----------
    list1: list[int]
        the first sorted list.
    list2: list[int]
        the second sorted list.

    Returns
    -------
    list[int]
        a single merged and sorted list.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def longest_common_prefix(strs):
    '''Longest Common Prefix.

    Write a function to find the longest common prefix string amongst a list of strings.

    If there is no common prefix, return an empty string "".

    Examples:
    longest_common_prefix(["flower", "flow", "flight"]) -> "fl"
    longest_common_prefix(["dog", "racecar", "car"]) -> ""
    longest_common_prefix(["apple"]) -> "apple"
    longest_common_prefix([]) -> ""

    Note: All given inputs are in lowercase letters a-z.

    Parameters
    ----------
    strs: list[str]
        a list of strings.

    Returns
    -------
    str
        the longest common prefix.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def digital_root(n):
    '''Digital Root.

    The digital root of a non-negative integer is the single-digit value
    obtained by an iterative process of summing digits, on each step using
    the result from the previous step as input to the next. The process
    continues until a single-digit number is reached.

    For example, the digital root of 65,536 is 7, because:
    6 + 5 + 5 + 3 + 6 = 25
    2 + 5 = 7

    Examples:
    digital_root(16) -> 7
    digital_root(942) -> 6  (9 + 4 + 2 = 15, 1 + 5 = 6)
    digital_root(132189) -> 6
    digital_root(493193) -> 2

    Parameters
    ----------
    n: int
        a non-negative integer.

    Returns
    -------
    int
        the single-digit digital root.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass

def transpose_matrix(matrix):
    '''Transpose Matrix.

    Given a 2D integer array `matrix`, return the transpose of `matrix`.

    The transpose of a matrix is the matrix flipped over its main diagonal,
    switching the row and column indices of the matrix.

    This means that `transpose[i][j]` will be `matrix[j][i]`.

    You can assume the input matrix is not empty and is rectangular
    (all rows have the same number of columns).

    Example 1:
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    transpose_matrix(matrix) -> [[1, 4, 7],
                                 [2, 5, 8],
                                 [3, 6, 9]]

    Example 2:
    matrix = [[1, 2],
              [3, 4]]
    transpose_matrix(matrix) -> [[1, 3],
                                 [2, 4]]

    Example 3 (Non-square matrix):
    matrix = [[1, 2, 3],
              [4, 5, 6]]
    transpose_matrix(matrix) -> [[1, 4],
                                 [2, 5],
                                 [3, 6]]

    Parameters
    ----------
    matrix: list[list[int]]
        A 2D list of integers representing the matrix.

    Returns
    -------
    list[list[int]]
        The transposed matrix.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass
