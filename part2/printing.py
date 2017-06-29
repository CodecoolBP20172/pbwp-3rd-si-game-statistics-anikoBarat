
# Printing functions

from reports import *


def print_get_most_played(file_name='game_stat.txt'):
    print('The most played game is: {}.'.format(get_most_played(file_name)))


def print_sum_sold(file_name='game_stat.txt'):
    print('The total sold copies are: {} million'.format(sum_sold(file_name)))


def print_get_selling_avg(file_name='game_stat.txt'):
    print('The average selling is {:.2f} million copies.'.format(get_selling_avg(file_name)))


def print_count_longest_title(file_name='game_stat.txt'):
    print('The longest title is {} character long.'.format(count_longest_title(file_name)))


def print_get_date_avg(file_name='game_stat.txt'):
    print('The average of the release dates is {}.'.format(get_date_avg(file_name)))


def print_get_game(title, file_name='game_stat.txt'):
    returned_list = get_game(file_name, title)
    # The string will be displayed centered in a 60 character width place.
    print('{:^60}'.format('Properties of the game'))
    print(60 * '-')
    # For the first argument there's a fixed 20 width place, for the second it isn't determined.
    print('{:20}{:<}'.format('Title:', returned_list[0]))
    print('{:20}{:<}'.format('Total copies sold:', returned_list[1]))
    print('{:20}{:<}'.format('Release date:', returned_list[2]))
    print('{:20}{:<}'.format('Genre:', returned_list[3]))
    print('{:20}{:<}'.format('Publisher:', returned_list[4]))


def print_count_grouped_by_genre(file_name='game_stat.txt'):
    returned_dictionary = count_grouped_by_genre(file_name='game_stat.txt')
    print('{:^27}'.format('Game quantity per genre'))
    print(27 * '-')
    for i in returned_dictionary:
        print('{:25}{:<}'.format(i, returned_dictionary[i]))


def main():
    '''
    Test printings.
    '''
    print_get_most_played()
    print()
    print_sum_sold()
    print()
    print_get_selling_avg()
    print()
    print_count_longest_title()
    print()
    print_get_date_avg()
    print()
    print_get_game('Minecraft')
    print()
    print_count_grouped_by_genre()


if __name__ == '__main__':
    main()
