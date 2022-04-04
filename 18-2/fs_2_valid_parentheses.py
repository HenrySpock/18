def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    par_count = 0

    for pnum in parens:
        if pnum == '(':
            par_count += 1
        elif pnum == ')':
            par_count -= 1 
        if par_count < 0:
            return False

    return par_count == 0