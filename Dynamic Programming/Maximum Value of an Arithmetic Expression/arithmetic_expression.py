# python3

# Utility method to check whether a character
# is operator or not
def isOperator(op):
    return (op == '+' or op == '*' or op == '-')


def find_maximum_value(dataset):
    # def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    num = []
    opr = []
    tmp = ""

    # store operator and numbers in different vectors
    for i in range(len(dataset)):
        if (isOperator(dataset[i])):
            opr.append(dataset[i])
            num.append(int(tmp))
            tmp = ""
        else:
            if dataset[i-1] == '-':
                tmp += dataset[i-1]+dataset[i]
                #num.append(int(dataset[i-1]+dataset[i]))
            else:
                tmp += dataset[i]

            # storing last number in vector
    num.append(int(tmp))

    llen = len(num)
    minVal = [[0 for i in range(llen)] for i in range(llen)]
    maxVal = [[0 for i in range(llen)] for i in range(llen)]

    # initializing minval and maxval 2D array
    for i in range(llen):
        for j in range(llen):
            minVal[i][j] = 10 ** 9
            maxVal[i][j] = 0

            # initializing main diagonal by num values
            if (i == j):
                minVal[i][j] = maxVal[i][j] = num[i]

                # looping similar to matrix chain multiplication
    # and updating both 2D arrays
    for L in range(2, llen + 1):
        for i in range(llen - L + 1):
            j = i + L - 1
            for k in range(i, j):

                minTmp = 0
                maxTmp = 0

                # if current operator is '+', updating tmp
                # variable by addition
                if (opr[k] == '+' or '-'):

                    minTmp = minVal[i][k] + minVal[k + 1][j]
                    maxTmp = maxVal[i][k] + maxVal[k + 1][j]

                    # if current operator is '*', updating tmp
                # variable by multiplication
                elif (opr[k] == '*'):

                    minTmp = minVal[i][k] * minVal[k + 1][j]
                    maxTmp = maxVal[i][k] * maxVal[k + 1][j]

                    # updating array values by tmp variables
                if (minTmp < minVal[i][j]):
                    minVal[i][j] = minTmp
                if (maxTmp > maxVal[i][j]):
                    maxVal[i][j] = maxTmp

                    # last element of first row will store the result
    print("Minimum value : ", minVal[0][llen - 1], ", Maximum value : ", maxVal[0][llen - 1])


if __name__ == "__main__":
    print(find_maximum_value(input()))
