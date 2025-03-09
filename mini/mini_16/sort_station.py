from stack import Stack

# "Operation": [Priority, Left-to-right associativity, Unary]
PRIORITY_DICT = {"!": [2, False, True],
                 "++": [2, False, True],
                 "--": [2, False, True],
                 "*": [3, True, False],
                 "/": [3, True, False],
                 "%": [3, True, False],
                 "+": [4, True, False],
                 "-": [4, True, False],
                 "<<": [5, True, False],
                 ">>": [5, True, False],
                 "==": [7, True, False],
                 "!=": [7, True, False],
                 "&": [8, True, False],
                 "^": [9, True, False],
                 "|": [10, True, False],
                 "&&": [11, True, False],
                 "||": [12, True, False],
                 "=": [14, False, False]}


def polish_notation(expr):
    if type(expr) is not list:
        expr = expr.replace("(", "( ")
        expr = expr.replace(")", " )")
        expr = expr.split()

    stack = Stack()

    res = ""

    i = -1
    n = len(expr)

    while i < n - 1:
        i += 1

        if expr[i] == "(":
            k = 1
            sk = 0
            while expr[i + k] != ")" or sk != 0:
                if expr[i + k] == "(":
                    sk += 1

                if expr[i + k] == ")":
                    sk -= 1

                k += 1

            res += polish_notation(expr[(i+1):(i+k)]) + " "
            i += k
            continue

        if expr[i].isnumeric():
            res += expr[i] + " "
            continue

        if expr[i] in PRIORITY_DICT.keys():
            if stack.top() is None:
                stack.push(expr[i])
                continue

            op_info = PRIORITY_DICT[expr[i]]

            if not op_info[1]:
                stack.push(expr[i])
                continue

        while stack.top() is not None and PRIORITY_DICT[stack.top()][0] <= op_info[0]:
            res += stack.pop() + " "

        stack.push(expr[i])

    while stack.top() is not None:
        res += stack.pop() + " "

    res = res[:-1]

    return res
