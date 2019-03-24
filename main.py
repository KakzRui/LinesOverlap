import ast
from overlap_lines import overlap


def main():
    try:
        x1, x2 = ast.literal_eval(input('Enter co-ordinates for line 1 using comma separated: '))
        x3, x4 = ast.literal_eval(input('Enter co-ordinates for line 2 using comma separated: '))
        line1 = (x1, x2)
        line2 = (x3, x4)
        result = overlap(line1, line2)
        print(result)
    except (ValueError, SyntaxError):
        print('Invalid co-ordinates, please enter 2 numbers with comma separated')


if __name__ == '__main__':
    main()
