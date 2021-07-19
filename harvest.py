############
# Part 1   #
############


from typing import Coroutine


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types

    Arguments:
        None

    Return:
        - list of melon types."""

    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')
    all_melon_types.append(cas)

    cren = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings.

    Arguments:
        - melon_types: List of the different possible types of melons.

    Return:
        None
    """

    for melon in melon_types:
        print(f'{melon.name} pairs well with:')
        for pairing in melon.pairings:
            print(f'{pairing}')
        print()

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code.

    Arguments:
        - List of melon instances.

    Return:
        - Dictionary with format Dictionary[melon.code] = the melon instance object
    """

    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon

    return melon_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest.

    Attributes:
        type: type of melon
        shape_rating: rating given for the quality of the melon's shape
        color_rating: rating given for the quality of the melon's color
        field: the number of the field the melon is harvested from
        harvested_by: the first name of the person the melon was harvested by
    """

    def __init__(self, type, shape_rating, color_rating, field, harvested_by):
        """Initialize a harvested melon.

        Return: None
        """

        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by

    def is_sellable(self):
        """Return whether a harvested melon is sellable.

        Arguments:
            - melon: instance of the harvested melon

        Return:
            True or False
        """

        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects.

    Arguments:
        - melon_types: takes in a list of the different types of melons

    Return:
        - returns a list of melon object instances."""

    melons = []

    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    melons.extend([melon_1, melon_2, melon_3, melon_4, melon_5,
                melon_6, melon_7, melon_8, melon_9])

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable.

    Arguments:
        - melons: list of melon instances

    Return:
        None"""

    for melon in melons:
        harvested_by = f'Harvested by {melon.harvested_by}'
        field = f'from Field {melon.field}'
        status = '(CAN BE SOLD)' if melon.is_sellable() else '(NOT SELLABLE)'

        print(f'{harvested_by} {field} {status}')

def process_melon_file(filename):
    """Takes in a text file and creates a melon instance for each line.

    Arguments:
        - filename: a text file with each row being the details for a different melon instance

    Return:
        - List of all melon object instances
    """

    melon_data = open(filename)

    melon_list = []

    for line in melon_data:
        _, shape_rating, _, color_rating, _, code, _, _, harvested_by, _, _, field = line.rstrip().split(" ")

        melon_types = make_melon_types()
        melons_by_id = make_melon_type_lookup(melon_types)
        type = melons_by_id[code]

        melon_object = Melon(type, shape_rating, color_rating, field, harvested_by)

        melon_list.append(melon_object)

    return melon_list
