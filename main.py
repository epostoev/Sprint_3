import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items
    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError("'Нельзя добавить товар, если в его названии нет символов или их больше 40'")
        if name not in self.__item_price:
            raise NameError("Позиция отсутствует в товарном справочнике")
        else:
            self.__name_items.append(name)
            self.__number_items += 1
    
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError("Позиция отсутствует в чеке")
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    def check_amount(self):
        total = []
        for item in self.__name_items:
            price = self.__item_price[item]
            total.append(price)
            total_sum = sum(total)
        if len(self.__name_items) > 10:
            total_sum *=0.9
        return total_sum


# kassa_1 = OnlineSalesRegisterCollector()

# # print(kassa_1.name_items)
# # print(kassa_1.number_items)
# kassa_1.add_item_to_cheque("чипсы")
# kassa_1.add_item_to_cheque("чипсы")
# kassa_1.add_item_to_cheque("чипсы")
# kassa_1.add_item_to_cheque("чипсы")
# kassa_1.add_item_to_cheque("чипсы")
# kassa_1.add_item_to_cheque("чипсы")
# kassa_1.add_item_to_cheque("чипсы")
# kassa_1.add_item_to_cheque("чипсы")
# kassa_1.add_item_to_cheque("чипсы")
# # print(kassa_1.name_items)
# # print(kassa_1.number_items)
# kassa_1.add_item_to_cheque("кола")
# # print(kassa_1.name_items)
# # print(kassa_1.number_items)
# # input()
# # kassa_1.delete_item_from_check("чипсы")
# # print(kassa_1.name_items)
# # print(kassa_1.number_items)

# print(kassa_1.__dict__)
# print(kassa_1.check_amount())
