import os
from tabulate import tabulate


def output_analysis(data):
    table = []
    headers = ["word", "times"]

    for key in data:
        table.append([key, data[key]])

    table = sorted(table, key=lambda item: item[1], reverse=True)

    print(tabulate(table, headers, tablefmt="pretty"))


def analysis_words(file):
    word_dict = {}

    for line in file:
        # 分割单词就像程序员的命运一样，永远不知道会出什么岔子。遇到一个解决一个
        line_words = (
            str(line).replace("\n", "").replace(",", "").replace(".", "").split(" ")
        )
        line_words = list(filter(lambda x: x, line_words))
        for word in line_words:
            if word in word_dict:
                word_dict[word] = word_dict[word] + 1
            else:
                word_dict[word] = 1

    return word_dict


"""
英语单词均以空格进行分割（无视语义）按照空格，分割出所有单词。
"""
if __name__ == "__main__":
    file_name = "The Impact of Technology on Society.txt"

    with open(os.path.join(os.path.dirname(__file__), f"./{file_name}"), "r") as file:
        words_info = analysis_words(file)
        output_analysis(words_info)
