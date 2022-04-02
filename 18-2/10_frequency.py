LIST1 = [1, 2, 3, 4, 5, 6, 1 ,3 ,5 ,2 ,4 , 5, 1 ,1 , 5,]
LIST2 = ["car", "truck", "airplane", "train", "motorcycle", "car", "car", "car", "car", "car",]

def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """

    return lst.count(search_term)