"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> rando = WordFinder("tfn.txt")
    1547 words read

    >>> rando.random() 
    'Ion Scythe'

    >>> rando.random() 
    'Tap-Out'
    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        word_list = open(path)

        self.words = self.parse(word_list)

        print(f"{len(self.words)} words read")

    def parse(self, word_list):
        """Parse word_list -> list of words."""

        return [word.strip() for word in word_list]

    def random(self):
        """Return random word."""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> special = SpecialWordFinder("spaces.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, word_list):
        """Parse word_list -> list of words, skipping blanks/comments."""

        return [word.strip() for word in word_list 
                if word.strip() and not word.startswith("#")]