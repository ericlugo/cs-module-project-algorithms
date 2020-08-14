import sys


def rock_paper_scissors(n):
    choices = {
        1: "rock",
        2: "paper",
        3: "scissors",
    }
    result_grid = []
    for _ in choices:
        result_grid.append(rps_helper(n, result_grid, choices))
    print(result_grid)


def rps_helper(plays, end_res, choices, cur_res=[]):
    if plays == 0:
        print(cur_res)
        return end_res.append(cur_res)
    else:
        print(plays)
        for key in choices.keys():
            # print(choices[key])
            cur_res.append(choices[key])
            return rps_helper(plays-1, end_res, choices, cur_res)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

"""
rock_paper_scissors(n):
    - create a dictionary corresponding to the three playable choices
    _ create the primary array that will house all response arrays
    - call the helper with the number of items per array, the dictionary
        that it will use to create the play arrays, and a cache to memoize
        the possible outcomes since it is likely that many options will
        repeat during generation.

rps_helper(n, response, cache = {}):
    - if length==0 return current_response
    - else:

"""
