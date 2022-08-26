# cards: a list of numbers in decreasing order
# query: a number whose position is to be determined
# problem: find the query in the input with the least amount of checking the list

# write down possible cases

# always implement the bruteforce solution before the optimal solution

# Binary search Solution
# 1. Find the middle element of the list.
# 2. If it matches queried number,return the middle position as the answer.
# 3. If it is less than the queried number,then search the first half of the list
# 4. If it is greater than the queried number,then search the second half of the list
# 5. If no more elements remain,return -1.


tests: [dict] = []
tests.append({
    'input': {'cards': list(range(20, 1, -2)),
              'query': 12},
    'output': 4
})


def test_location(cards, query, mid) -> str:
    mid_number = cards[mid]
    if mid_number == query:
        # check if the index before it is valid
        # this solution is to check the first occurence of the query
        if mid - 1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'


def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'right':
            lo = mid + 1
        elif result == 'left':
            hi = mid - 1

    return -1


assert locate_card(**tests[0]['input']) == tests[0]['output']

# BINARY SEARCH TIME COMPLEXITY = O(log N)
# Generic Binary Search
# Here is the general strategy behind binary search,which is applicable toavariety of problems:
# 1. Come up with a condition to determine whether the answer lies before,after or at a given position
# 2. Retrieve the midpoint and the middle element of the list.
# 3. If it is the answer,return the middle position as the answer.
# 4. If answer lies before it,repeat the search with the first half of the list
# 5. If the answer lies after it,repeat the search with the second half of the list.
