# python3

# https://www.geeksforgeeks.org/edit-distance-dp-5/

def edit_distance(first_string, second_string):
    # Create a table to store results of subproblems
    m = len(first_string)
    n = len(second_string)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif first_string[i - 1] == second_string[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

                # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
