
# Report functions

from math import ceil


def get_most_played(file_name):
    '''
    Returns with the title of the most played game.
    '''
    title = ""
    copies = 0
    # It opens the given file.
    with open(file_name, 'r') as f:
        # Iterates through all the line in the file.
        for line in f:
            # Splits the string along the tabs and the created list is given to the 'list_from_line' variable.
            list_from_line = line.split("\t")
            # Compare the related element of the list with the value of the 'copies' variable.
            if float(list_from_line[1]) > float(copies):
                # If the condition is evaluated True, it gives new value to the 'copies'
                # variable and it updates the related title too.
                copies = list_from_line[1]
                title = list_from_line[0]
    return title


def sum_sold(file_name):
    '''
    Returns with the total of the copies sold.
    '''
    # I make a variable and give it a float type of value 0.
    total = float(0)
    with open(file_name, 'r') as f:
        for line in f:
            list_from_line = line.split("\t")
            # Adds the value of the related property (total copies sold (million)) at every line.
            total += float(list_from_line[1])
    return total


def get_selling_avg(file_name):
    '''
    Returns with the value of the average selling.
    '''
    pieces = 0
    total = float(0)
    with open(file_name, 'r') as f:
        for line in f:
            list_from_line = line.split("\t")
            # Adds the value of the related item to the total at every iteration.
            total += float(list_from_line[1])
            # Increments the value of 'pieces' with one at every iteration.
            pieces += 1
            # Calculates the average using a simple division.
        average_selling = total / pieces
    return average_selling


def count_longest_title(file_name):
    '''
    Returns with the lenght of the longest title.
    '''
    # I make a variable to store the length of the longest string.
    longest = 0
    with open(file_name, 'r') as f:
        for line in f:
            list_from_line = line.split("\t")
            # Compare the length of related item with the actual value of 'longest'.
            if len(list_from_line[0]) > longest:
                # If the condition evaluated True, longest get a new value. Else if there
                # any other line it continues the iteration.
                longest = len(list_from_line[0])
    return longest


def get_date_avg(file_name):
    '''
    Returns with the average of the release dates.
    '''
    data = 0
    total_of_years = 0
    with open(file_name, 'r') as f:
        for line in f:
            list_from_line = line.split("\t")
            total_of_years += int(list_from_line[2])
            data += 1
        # I use the ceil function from the math module to round up the value.
        avg_release_date = ceil(total_of_years / data)
    return avg_release_date


def get_game(file_name, title):
    '''
    Returns a list of the properties of the selected game.
    '''
    with open(file_name, 'r') as f:
        for line in f:
            list_from_line = line.split("\t")
            # It tests whether is the wanted title in the line.
            if (list_from_line[0]).lower() == (title).lower():
                # If the condition True, it converts the 2nd element of the list to float.
                list_from_line[1] = float(list_from_line[1])
                # Makes an integer from the 3rd element of the list.
                list_from_line[2] = int(list_from_line[2])
                # Checks if is there a new line character.
                if '\n' in list_from_line[4]:
                    # Remove the new line character from the end of the string.
                    list_from_line[4] = list_from_line[4][:-1]
                return list_from_line


def count_grouped_by_genre(file_name):
    '''
    Returns a dictionary where each genre is associated with the count
    of the games of its genre.
    '''
    dict_of_genres = {}
    with open(file_name, 'r') as f:
        for line in f:
            list_from_line = line.split("\t")
            # I make a variable to store the list's element which is the genre.
            genre = list_from_line[3]
            # Checks whether the actual line's genre doesn't exist yet.
            if genre not in dict_of_genres:
                # If the condition evaluates true, it creates a new key-value pair in the dictionary with the value 1.
                dict_of_genres[genre] = 1
            # If the genre is already exists in the dictionary:
            else:
                # Increments its value by 1.
                dict_of_genres[genre] += 1
    return dict_of_genres


def get_date_ordered(file_name):
    '''
    This function returns the date ordered list of the titles in descending order,
    but it can't manage the secondary ordering rule.
    '''
    date_ordered_list = []

    with open(file_name, 'r') as f:
        for line in f:
            list_from_line = line.split("\t")
            if len(date_ordered_list) == 0 or int(list_from_line[2]) < int(date_ordered_list[-1][1]):
                date_ordered_list.append([list_from_line[0], list_from_line[2]])
            else:
                for i in range(0, len(date_ordered_list)):
                    if list_from_line[2] > date_ordered_list[i][1]:
                        date_ordered_list.insert(i, [list_from_line[0], list_from_line[2]])
                        break
        list_of_title = []
        for i in date_ordered_list:
            list_of_title.append(i[0])
        return list_of_title
