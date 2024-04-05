# n = 2
# init_seat = ['..._.#.', '.##_...', '.#._.##', '..._...']
# m = 3
# groups_descr = [['2', 'left', 'aisle'], ['3', 'right', 'window'], ['2', 'left', 'window'], ['3', 'left', 'aisle'], ['1', 'right', 'window'], ['2', 'right', 'window'], ['1', 'right', 'window']]

import re


place_letter = ['A', 'B', 'C', '_', 'D', 'E', 'F']
n = int(input())
init_seat = []

for i in range(1, n+1):
    start_row = input()
    init_seat.append(start_row)

m = int(input())
groups_descr = []

for i in range(m):
    group_desc = input().split()
    groups_descr.append(group_desc)


def print_text(i, result):
    text = ''
    for n in range(result.start(), result.end()):
        if n != 3:
            text += f' {i + 1}{place_letter[n]}'

    print(f'Passengers can take seats:{text}')

    for new_row in init_seat:
        print(new_row)


for group in groups_descr:
    num, side, position = int(group[0]), group[1], group[2]
    sym, sym_2, sym_3 = '\.' * num, 'X' * num, '#' * num
    for i, row in enumerate(init_seat):
        if side == 'left' and position == 'aisle':
            result = re.search(r'{0}\_'.format(sym), row)

            if result:
                init_seat[i] = re.sub(r'{0}\_'.format(sym), '{0}_'.format(sym_2), init_seat[i])

                print_text(i, result)

                init_seat[i] = re.sub(r'{0}\_'.format(sym_2), '{0}_'.format(sym_3), init_seat[i])

                break

        elif side == 'left' and position == 'window':
            result = re.match(r'{0}'.format(sym), row)

            if result:
                init_seat[i] = sym_2 + row[result.end():]

                print_text(i, result)

                init_seat[i] = sym_3 + row[result.end():]

                break

        elif side == 'right' and position == 'aisle':
            result = re.search(r'\_{0}'.format(sym), row)

            if result:
                init_seat[i] = re.sub(r'\_{0}'.format(sym), '_{0}'.format(sym_2), init_seat[i])

                print_text(i, result)

                init_seat[i] = re.sub(r'\_{0}'.format(sym_2), '_{0}'.format(sym_3), init_seat[i])

                break

        elif side == 'right' and position == 'window':
            sym = '.' * num
            if sym in row[7-len(sym):]:
                new_row = row[:7-len(sym)] + sym_2
                init_seat[i] = new_row

                text = ''
                for n in range(len(row[:7-len(sym)]), len(row)):
                    if n != 3:
                        text += f' {i + 1}{place_letter[n]}'

                print(f'Passengers can take seats:{text}')

                for new_row in init_seat:
                    print(new_row)

                init_seat[i] = row[:7-len(sym)] + sym_3

                break

    else:
        print('Cannot fulfill passengers requirements')
