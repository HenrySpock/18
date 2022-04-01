# 1. 
foods = ["asparagus", "Bruscetta", "cabbage", "Dates", "eggs", "Elderberries", "Fajita", "garlic", "Haddock", "ice cream", "Jambalaya", "kale", "Lobster", "meatballs", "Noodles", "orange", "Pizza", "quesadilla", "Reuben", "spinach", "Tater tots", "unagi", "Venison", "waffles", "Xoconostle", "yogurt", "Ziti"]
for word in foods:
    print(word.upper())

phrase = ["I", "don't", "wanna", "!"]

# 2.
def print_upper_words(words):
    """Print every word (passed in or from list) on a separate line, all printed letters uppercased.

        >>> print_upper_words(phrase)
        I
        DON'T
        WANNA
        !

        >>> print_upper_words(["why", "me", "man"])
        WHY
        ME
        MAN!
    """

    for word in words:
        print(word.upper())

# 3.
def print_upper_only_e(words):
    """Print every word (passed in or from list) that starts with "e" or "E" on a separate line, 
    all printed letters uppercased.

        >>> print_upper_only_e(["eggs", "Elderberries"])
        EGGS
        ELDERBERRIES
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

# 4.
def print_upper_words_initial(words, initial):
    """Print every word (passed in or from list) that starts with passed in letter(s) on a separate line, 
    all printed letters uppercased.

        >>> print_upper_words_initial(foods, "a", "b", "c"])
        ASPARAGUS
        CABBAGE
    """

    for word in words:
        for char in initial:
            if word.startswith(char):
                print(word.upper())
                break


