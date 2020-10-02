"""Find 2 numbers from the list that adds up to n"""


def find_sum_1(lst, n):
    for i, val in enumerate(lst):
        for j, val_2 in enumerate(lst):
            if lst[i] + lst[j] == n and i != j:
                return [lst[i], lst[j]]  # O(n^2)


def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if lst[mid] == item:
            found = mid

        else:
            if lst[mid] < item:
                first = mid + 1

            else:
                last = mid - 1

    return found


def find_sum_2(lst, n):
    lst.sort()

    for j in lst:
        index = binary_search(lst, n - j)
        if index:
            return [j, n - j]  # O(nlogn)


def find_sum_3(lst, n):
    found_values = {}

    for ele in lst:
        try:
            found_values[n - ele]
            return [n - ele, ele]
        except:
            found_values[ele] = 0

    return False  # O(n)


def find_sum_4(lst, n):
    found_values = set()

    for ele in lst:
        if n - ele in found_values:
            return [n - ele, ele]
        found_values.add(ele)

    return False  # O(n)


def test_find_sum():
    assert find_sum_1([1, 2, 3, 4], 5) == [1, 4]
    assert find_sum_2([1, 2, 3, 4], 5) == [1, 4]
    assert find_sum_3([1, 2, 3, 4], 5) == [1, 4]
    assert find_sum_4([1, 2, 3, 4], 5) == [1, 4]
    print("All test cases passed")


if __name__ == "__main__":
    test_find_sum()
