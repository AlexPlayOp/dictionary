import random


file_name = 'test.txt'


def main():
    i = str(input())
    if i == "список":
        word_list = read_file(file_name)
        for w in word_list:
            print(w.strip())
    if i == "Добавить":
        b = str(input())
    if i == "случайно":
        word_list = read_file(file_name)
        n = int(input('сколько слов? '))
        while n != 0:
            b = random.randint(0, len(word_list)-1)
            print(word_list[b].strip())
            n -= 1


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.readlines()


if __name__ == "__main__":
    main()
