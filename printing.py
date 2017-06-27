
# Printing functions
from reports import *


def print_count_games(file_name='game_stat.txt'):
    '''
    Prints out how many games are in the file.
    '''
    print("There are {0} games in the given {1} file.".format(count_games(file_name), file_name))


def print_decide(year, file_name='game_stat.txt'):
    '''
    Prints out whether is a game from a given year or not.
    '''
    if decide(file_name, year):
        print('There\'s a game in {}.'.format(year))
    else:
        print('There isn\'t any game in {}.'.format(year))


def print_get_latest(file_name='game_stat.txt'):
    '''
    Prints out the title of the latest game.
    '''
    print('The title of the latest game is: {}.'.format(get_latest(file_name)))


def print_count_by_genre(genre, file_name='game_stat.txt'):
    '''
    Prints out how many games are by genre.
    '''
    print('There are {0} games in the {1} genre.'.format(count_by_genre(file_name, genre), genre))


def print_get_line_number_by_title(title, file_name='game_stat.txt'):
    '''
    Prints out the line number where the given title is.
    '''
    try:
        print('{0} is in the {1}. line.'.format(title, get_line_number_by_title(file_name, title)))
    except ValueError:
        print('{} isn\'t  in the file!'.format(title))


def print_sort_abc(file_name='game_stat.txt'):
    '''
    Prints out the titles in alphabetical order.
    '''
    ordered_list = sort_abc(file_name)
    longest = 0
    for i in ordered_list:
        if len(i) > longest:
            longest = len(i)
    print(round((longest / 2 - 6)) * '-', 'Titles', round((longest / 2 - 6)) * '-')
    for i in ordered_list:
        print(i)


def print_get_genres(file_name='game_stat.txt'):
    '''
    Prints out the genres in alphabetical order.
    '''
    ordered_list = get_genres(file_name)
    longest = 0
    for i in ordered_list:
        if len(i) > longest:
            longest = len(i)
    print('Genres')
    print(int(longest) * '-')
    for i in ordered_list:
        print(i)


def print_when_was_top_sold_fps(file_name='game_stat.txt'):
    '''
    Prints out when was the top sold fps released.
    '''
    which_genre = "First-person shooter"
    try:
        print('The top sold {0} was released in {1}.'.format(which_genre, when_was_top_sold_fps(file_name)))
    except ValueError:
        print('There\'s no game with {} genre.'.format(which_genre))


def main():
    '''
    Test printings.
    '''
    print_count_games()
    print()
    print_decide(1977)
    print()
    print_get_latest()
    print()
    print_count_by_genre("RPG")
    print()
    print_get_line_number_by_title("Crysis")
    print()
    print_sort_abc()
    print()
    print_get_genres()
    print()
    print_when_was_top_sold_fps()


if __name__ == '__main__':
    main()
