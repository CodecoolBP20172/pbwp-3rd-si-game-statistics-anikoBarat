
# Report functions


def count_games(file_name):
    '''
    Counts how many games are in the file.
    '''
    with open(file_name, 'r') as f:
        count = 0
        for line in f:
            count += 1
        return count


def decide(file_name, year):
    '''
    Decides whether is a game from a given year or not.
    '''
    with open(file_name, 'r') as f:
        for line in f:
            # Here I make a list of strings from one line from the file.
            list_from_line = line.split("\t")
            # Examine the existance of the given year at the related index (years are in the third column in the file).
            if str(year) == list_from_line[2]:
                return True
            else:
                continue
        return False


def get_latest(file_name):
    '''
    Gets the title of the latest game.
    '''
    with open(file_name, 'r') as f:
        # I make two variables to store the needed values during the iteration.
        latest = 0
        title = 0
        for line in f:
            list_from_line = line.split("\t")
            # If the data (year) at the related index is bigger than the value of
            # latest, I change the variables values to it.
            if int(list_from_line[2]) > int(latest):
                latest = list_from_line[2]
                title = list_from_line[0]
        return title


def count_by_genre(file_name, genre):
    '''
    Counts how many games are by genre.
    '''
    with open(file_name, 'r') as f:
        # I make a variable to store the amount of the wanted genre.
        count = 0
        for line in f:
            list_from_line = line.split("\t")
            # If it finds the wanted genre, it increments the value of 'count'.
            if genre == list_from_line[3]:
                count += 1
        return count


def get_line_number_by_title(file_name, title):
    '''
    Gets the line number where the given title is.
    '''
    with open(file_name, 'r') as f:
        # I make a variable to store the line numbers. It starts from the first line of the file.
        line_number = 1
        for line in f:
            list_from_line = line.split("\t")
            # If it finds the wanted title at the related index, it returns the value of 'line_number'.
            if title == list_from_line[0]:
                return line_number
            # If not, increments the value of 'line_number' with one.
            else:
                line_number += 1
        # If there isn't any title in the file with the wanted title, raises ValueError exception.
        raise ValueError


def sort_abc(file_name):
    '''
    Gets a list from the titles in alphabetical order.
    '''
    with open(file_name, 'r') as f:
        # I make an empty list to store the strings.
        ordered_list = []
        for line in f:
            list_from_line = line.split("\t")
            # Tests whether the list is empty or the value at the related index in the
            # line is bigger than the list's last title (lower() method detailed in the next function).
            if len(ordered_list) == 0 or (list_from_line[0]).lower() > (ordered_list[len(ordered_list) - 1]).lower():
                ordered_list.append(list_from_line[0])
            else:
                # It iterates through the 'ordered_list'.
                for i in range(0, len(ordered_list)):
                    # Tests the actual title if its smaller than the list's element at the index i.
                    if (list_from_line[0]).lower() < (ordered_list[i]).lower():
                        # If the condition is true, it inserts the title to the list to the index i.
                        ordered_list.insert(i, list_from_line[0])
                        # If it founds the first bigger element it breaks the iteration (if not we
                        # would find another bigger values).
                        break
    return ordered_list


def get_genres(file_name):
    '''
    Gets a list from the genres in alphabetical order.
    '''
    with open(file_name, 'r') as f:
        # This function follow the same logic as sort_abc() do.
        ordered_list = []
        for line in f:
            list_from_line = line.split("\t")
            # It was needed to convert to lower case the genres for the comparison
            # because upper case letters have smaller values than lower case
            # ones/ASCII/ --> RPG causes problem).
            if len(ordered_list) == 0 or (list_from_line[3]).lower() > (ordered_list[len(ordered_list) - 1]).lower():
                # When it appends it uses the original letters.
                ordered_list.append(list_from_line[3])
            else:
                for i in range(0, len(ordered_list)):
                    if (list_from_line[3]).lower() < (ordered_list[i]
                                                      ).lower() and list_from_line[3] not in ordered_list:
                        ordered_list.insert(i, list_from_line[3])
                        break
    return ordered_list


def when_was_top_sold_fps(file_name):
    '''
    Gets the year when the top sold fps was released.
    '''
    with open(file_name, 'r') as f:
        # I make two variables to store the needed values.
        top_amount = 0
        year_of_release = 0
        # I make a variable to store the wanted genre (I would like to make my function more flexible with this).
        which_genre = "First-person shooter"
        for line in f:
            list_from_line = line.split("\t")
            # Tests whether it found match.
            if list_from_line[3] == which_genre:
                # Compare the actual tested value with the value of the theoretically biggest.
                if float(list_from_line[1]) > float(top_amount):
                    # If the condition above true, it gives the new 'biggest' value to the 'top_amount' variable.
                    top_amount = list_from_line[1]
                    # If true, it updates the related value of 'year_of_relase' too.
                    year_of_release = list_from_line[2]
        # If there isn't any game with the wanted genre, it raises a ValueError
        # (Hypothesis: zero solded amount means no game).
        if top_amount == 0:
            raise ValueError
        else:
            return int(year_of_release)
