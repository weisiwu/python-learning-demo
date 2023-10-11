import os
from tabulate import tabulate

def analysis_words(file):
    return
    
def output_analysis(data):
    table = []
    headers = ["word","times"]

    for info in data:
        table.append([info[0], info[1]])

    print(tabulate(table, headers, tablefmt="grid"))

    """
    英语单词均以空格进行分割（无视语义）按照空格，分割出所有单词。
    """
if __name__ == '__main__':
    file_name = 'The Impact of Technology on Society.txt'
    
    output_analysis([["Sun",696000],["Earth",6371],["Moon",1737,],["Mars",3390,]])
    # with open(os.path.join(os.path.dirname(__file__), f'./{file_name}'), 'r') as file:
    #     analysis_words(file)