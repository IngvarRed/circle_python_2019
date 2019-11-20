'''
Write a function that takes a file name. It reads and outputs statistics:
- number of rows
- number of words
- number of letters
'''


def file_count(name_f):
    with open(name_f) as file_o:
        text = file_o.read()
        f_lines = text.split('\n')
        print(f'file "{name_f}" have :  {len(f_lines)} lines;', end='')
        f_words = []
        for line in f_lines:
            f_words += (line.split(' '))
        print(f'  {len(f_words)} words;', end='')
        f_lett = 0
        for lett in f_words:
            f_lett += len(lett)
        print(f'  {f_lett} letters;')
    return


file_count("text.txt")
