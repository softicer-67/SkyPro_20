''' 1. Напишите низкоуровневый алгоритм работы со статическим массивом
(реализованы операции записи, чтения, вставки, удаления).'''


class Tabl:
    def __init__(self, max_capacity):
        self.maxi = max_capacity
        self.arr = []

    def length(self):
        return len(self.arr)

    def add_el(self, el):
        if self.maxi > self.length():
            self.arr += [el]
        else:
            print('Not enough memory')

    def get_all_arr(self):
        return self.arr

    def insert_el(self, idx, el):
        if self.maxi > self.length():
            self.arr = self.arr[:idx] + [el] + self.arr[idx:]
        else:
            print('Not enough memory')

    def del_el(self, idx):
        self.arr = self.arr[:idx] + self.arr[idx+1:]


if __name__ == '__main__':

    arr = Tabl(5)
    print('\nДобавление\n')
    arr.add_el(2)
    arr.add_el(3)
    arr.add_el(4)
    arr.add_el(5)
    print(arr.get_all_arr())
    print('\nУдаление\n')
    arr.del_el(0)
    print(arr.get_all_arr())
    print('\nВставка\n')
    arr.insert_el(0, 2)
    arr.insert_el(0, 1)
    print(arr.get_all_arr())
    print('\nПроверка\n')
    arr.add_el(6)
    print()



''' 2. Напишите собственные хэш-функции. Подайте на вход разнообразные ключи,
убедитесь, что слишком часто коллизии не возникают, иначе, усовершенствуйте функцию.'''

my_dict = {}


def func(text):
    my_hash = id(text) >> 5

    if my_hash not in my_dict:
        my_dict[my_hash] = [text]
    else:
        my_dict[my_hash].append(text)


def main():
    func('лес')
    func('книга')
    func('текст')
    func('текст1')
    func('проба')
    func('проба')
    func(12345)


if __name__ == '__main__':
    main()
    print(my_dict)
