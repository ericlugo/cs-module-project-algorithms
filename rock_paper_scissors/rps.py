import sys

def rock_paper_scissors(n):
    result = []
    return rock_paper_scissors_helper(n, result)

def rock_paper_scissors_helper(n, result, choices=["rock", "paper", "scissors"], current_list=[]):
    if n == 0:
        result.append(current_list[:])  # GOAL
    else:
        for index in range(3):
            current_list.append(choices[index])  # CHOICE
            rock_paper_scissors_helper(n-1, result, choices, current_list)  # CONSTRAINT
            current_list.pop(len(current_list)-1)  # BACKTRACKING
    return result

# def rock_paper_scissors(n, result=[], choices=["rock", "paper", "scissors"], current_list=[]):
#     if n == 0:
#         result.append(current_list[:])  # GOAL
#     else:
#         for index in range(3):
#             current_list.append(choices[index])  # CHOICE
#             rock_paper_scissors(n-1, result, choices, current_list)  # CONSTRAINT
#             current_list.pop(len(current_list)-1)  # BACKTRACKING
#     return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
