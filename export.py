
# Export functions
from reports import *


def export_reports(import_file_name='game_stat.txt', export_file_name='reports.txt'):
    '''
    Exports the reports into a single export file.
    '''
    # Here I assemble the output string.
    content = ""
    content += str(count_games(import_file_name)) + '\n'
    content += str(decide(import_file_name, 2005)) + '\n'
    content += str(get_latest(import_file_name)) + '\n'
    content += str(count_by_genre(import_file_name, 'Real-time strategy')) + '\n'
    content += str(get_line_number_by_title(import_file_name, 'Half-Life')) + '\n'
    content += str(sort_abc(import_file_name)) + '\n'
    content += str(get_genres(import_file_name)) + '\n'
    content += str(when_was_top_sold_fps(import_file_name)) + '\n'

    # Here I write it to a file.
    file = open(export_file_name, "w")
    file.write(content)
    file.close()


def main():
    export_reports()


if __name__ == '__main__':
    main()
