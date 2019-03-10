#! python3
# practice

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):
    col_length = len(table)
    raw_length = len(table[0])

    col_with = [0] * col_length
    for i in range(col_length):
        col_with[i] = max_length(table_data[i])

    # display table
    for i in range(raw_length):
        for j in range(col_length):
            print(table[j][i].rjust(col_with[j]), end=' ')
        print()

def max_length(ls):
    M = 0
    for i in ls:
        if len(i) > M:
            M = len(i)
    return M

if __name__ == '__main__':
    print_table(table_data)
