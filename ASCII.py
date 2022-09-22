from conversion_table import table


def ser_check(asc):
    for i in asc:
        if i.isdigit():
            return True
    return False


def serialize(asc_art):
    if ser_check(asc_art):
        return asc_art
    rows = asc_art.split("\n")
    serialized = ''
    for row in rows:
        row += '3'
        count = ['', 0]
        for char in row:
            if count[0] == char:
                count[1] += 1
            else:
                if count[0] != '':
                    serialized += str(count[1]) + count[0]
                count = [char, 1]
        serialized += '\n'
    return serialized


def deserialize(ser_asc):
    if not ser_check(ser_asc):
        return ser_asc
    rows = ser_asc.split("\n")
    deserialized = ''
    for row in rows:
        mul = ''
        for i in row:
            if i.isdigit():
                mul += i
            else:
                deserialized += int(mul)* i
                mul = ''
        deserialized += '\n'
    return deserialized


def convert(asc, n):
    if n == 0:
        return asc
    else:
        if ser_check(asc):
            asc = deserialize(asc)
        for i in asc:
            if i in table:
                asc = asc.replace(i, table[i][n-1])
            elif i != '\n':
                asc = asc.replace(i, 'X')
        return serialize(asc)


def rotate(asc_art, degree):
    rotated = ''
    if ser_check(asc_art):
        des_asc_art = deserialize(asc_art)
    else:
        des_asc_art = asc_art
    rows = des_asc_art.split('\n')
    if degree == 360:
        for row in rows:
            rotated += row[::-1] + '\n'
    elif degree == 90:
        for i in range(len(rows[0])):
            for row in rows[::-1]:
                rotated += row[i]
            rotated += '\n'
    elif degree == 270:
        for i in reversed(range(len(rows[0]))):
            for row in rows:
                rotated += row[i]
            rotated += '\n'
    elif degree == 180:
        for row in rows[::-1]:
            for i in reversed(range(len(rows[0]))):
                rotated += row[i]
            rotated += '\n'
    elif degree == 0:
        rotated = des_asc_art
    if ser_check(asc_art):
        return serialize(rotated)
    else:
        return rotated


def main():
    first_input_check = False
    file_check = False
    rotation_check = False
    conversion_check = False
    while not first_input_check:
        first_input = input("Would you like to serialize or deserialize?: ")
        if first_input == 'serialize' or first_input == 'deserialize':
            first_input_check = True
        else:
            print("This is not an option...")
    while not file_check:
        file_input = input("Enter file path: ")
        try:
            f = open(file_input, 'r')
            content = f.read()
            f.close()
            file_check = True
        except FileNotFoundError:
            print(f'There is no such file as {file_input}, try again.')
    while not rotation_check:
        degrees_list = [0, 90, 180, 270, 360]
        rotation_input = input("How would you like to rotate the picture?[0, 90, 180, 270, 360]: ")
        if int(rotation_input) in degrees_list:
            content = rotate(content, int(rotation_input))
            rotation_check = True
        else:
            print("Please follow the instructions..")
    while not conversion_check:
        print(f'The conversion table:\n{table}')
        con = [0, 1, 2]
        conversion_input = input("How would you like so convert the characters?[0, 1, 2]: ")
        if int(conversion_input) in con:
            content = convert(content, int(conversion_input))
            conversion_check = True
        else:
            print("Please follow the instructions..")
    if first_input == 'serialize':
        content = serialize(content)
    else:
        content = deserialize(content)
    w_file = open(f'output_{file_input[:-4]}.txt', 'w')
    w_file.write(content)
    w_file.close()


if __name__ == '__main__':
    main()

