"""Basic mathematical operations in Python"""


def math_op(a, b):
    normal_division = a / b
    floor_division = a // b
    modulus = a % b
    power = a ** b

    return [normal_division, floor_division, modulus, power]


def check_parity(n):
    # If the number is even then result = 0
    # If the number is odd then result = 1
    result = (n % 2)
    return result


if __name__ == '__main__':
    [normal_division, floor_division, modulus, power] = math_op(3, 2)
    print('---Mathematical operations between 3 and 2---\n')
    print(f'Normal division = {normal_division}')
    print(f'Floor division = {floor_division}')
    print(f'Modulus = {modulus}')
    print(f'Power = {power}\n\n')

    print('---Check if the given numbers are even or odd---\n')
    print(f'Result for 2 = {check_parity(2)}')
    print(f'Result for -2 = {check_parity(-2)}')
    print(f'Result for 7 = {check_parity(7)}')
    print(f'Result for 11 = {check_parity(11)}')
