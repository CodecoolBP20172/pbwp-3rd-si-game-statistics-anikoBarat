
# Export functions

from reports import *


def export_reports_part2(import_file_name='game_stat.txt', export_file_name='reports_part2.txt'):
    '''
    Exports the reports into a single export file.
    '''
    # Here I assemble the output string.
    content = ""
    content += str(get_most_played(import_file_name)) + '\n'
    content += str(sum_sold(import_file_name)) + '\n'
    content += str(get_selling_avg(import_file_name)) + '\n'
    content += str(count_longest_title(import_file_name)) + '\n'
    content += str(get_date_avg(import_file_name)) + '\n'
    content += str(get_game(import_file_name, 'Minecraft')) + '\n'
    content += str(count_grouped_by_genre(import_file_name)) + '\n'

    # Here I write it to a file.
    file = open(export_file_name, "w")
    file.write(content)
    file.close()


def main():
    export_reports_part2()


if __name__ == '__main__':
    main()
