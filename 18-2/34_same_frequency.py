def num_frequency(coll):
    """Returns frequency counter mapping of coll."""

    inst = {}

    for num in coll:
        inst[num] = inst.get(num, 0) + 1

    return inst


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """

    return num_frequency(str(num1)) == num_frequency(str(num2))
