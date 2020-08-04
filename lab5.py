import random
def deck(categories, num_of_cards_per_cat):
    """
    (list, int) -> list
    Given a list of strings representation as category names and an integer
    indicating the number of cards in one category,
    return a deck of cards as a list. For example, with ["spades", "hearts"], 2,
    return a list of list: [["spades", 1],["spades",2], ["hearts", 1], ["hearts"
    , 2]], where 1 and 2 are the index of the cards.
    >> deck(["spades", "hearts"], 2)
    [["spades", 1],["spades",2], ["hearts", 1], ["hearts", 2]]
    >> deck(["spades", "hearts"], -5)
    []
    """
    deck_of_cards = []
    if num_of_cards_per_cat <= 0:
        deck_of_cards = []
    index = range(1, num_of_cards_per_cat+1)
    for category in categories:
        for i in index:
            deck_of_cards.append([category, i])
    return deck_of_cards


def random_shuffle(lst):
    """
    (list) -> list
    Receives a deck of cards and returns a randomly ordered
    list containing all of the same elements.
    The returned list should preserve the order of the categories. See below
    console outputs as an example, where "s" and "d" stay in the same order as
    the input and only the numbers are shuffled.
    >> random_shuffle([["s",1],["s",2],["s",3],["d",1],["d",2],["d",3]])
    [["s",3],["s",1],["s",2],["d",2],["d",1],["d",3]]
    """
    spades = []
    clubs = []
    diamonds = []
    hearts = []
    spades_copy = []
    clubs_copy = []
    hearts_copy = []
    diamonds_copy = []
    for lists in lst:
        if lists[0] == 's':
            spades.append(lists)
        elif lists[0] == 'c':
            clubs.append(lists)
        elif lists[0] == 'd':
            diamonds.append(lists)
        elif lists[0] == 'h':
            hearts.append(lists)
            
    random_numbers_list1 = random.sample(range(0, len(spades)), len(spades))
    counter = range(0, len(spades))
    for index in counter:
        spades_copy.append(spades[random_numbers_list1[index]])
    
    random_numbers_list2 = random.sample(range(0, len(hearts)), len(hearts))
    counter = range(0, len(hearts))
    for index in counter:
        hearts_copy.append(hearts[random_numbers_list2[index]])

    random_numbers_list3 = random.sample(range(0, len(clubs)), len(clubs))
    counter = range(0, len(clubs))
    for index in counter:
        clubs_copy.append(clubs[random_numbers_list3[index]])

    random_numbers_list4 = random.sample(range(0, len(diamonds)), len(diamonds))
    counter = range(0, len(diamonds))
    for index in counter:
        diamonds_copy.append(diamonds[random_numbers_list4[index]])
    
    items_in_original_order = [lst[0][0]]
    counter = 0
    for item in lst:
        if item[0] != items_in_original_order[len(items_in_original_order)-1]:
            items_in_original_order.append(lst[counter][0])
        counter += 1
    
    output = []
    counter = range(0,len(items_in_original_order))
    for index in counter:
        if items_in_original_order[index] == 's':
            output.extend(spades_copy)
        elif items_in_original_order[index] == 'c':
            output.extend(clubs_copy)
        elif items_in_original_order[index] == 'h':
            output.extend(hearts_copy)
        elif items_in_original_order[index] == 'd':
            output.extend(diamonds_copy)
    while output == lst:
        last_item = output.pop()
        output.insert(-2, last_item)
    return output


def reverse(lst):
    """
    (list) -> list
    Receives a list and returns a reverse ordered list containing all of the 
    same elements.
    >> reverse([["spades", 1],["spades",2], ["hearts", 1], ["hearts", 2]])
    [["hearts", 2], ["hearts", 1], ["spades", 2],["spades",1]]
    """
    lst_copy = lst.copy()
    lst_copy.reverse()
    return lst_copy