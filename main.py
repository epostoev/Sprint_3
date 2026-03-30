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
    
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax=[]
        total=[]
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
        for item in twenty_percent_tax:
            price = self.__item_price[item]
            total.append(price)
        sum_20 = sum(total)
        if len(self.__name_items) > 10:
            sum_20 *= 0.9
        twenty_percent_check = sum_20 * 0.2
        return twenty_percent_check
    
    def ten_percent_tax_calculation(self):
        ten_percent_tax=[]
        total=[]
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
        for item in ten_percent_tax:
            price = self.__item_price[item]
            total.append(price)
        sum_10 = sum(total)
        if len(self.__name_items) > 10:
            sum_10 *= 0.9
        ten_percent_check = sum_10 * 0.1
        return ten_percent_check
    
    def total_tax(self):
        total = self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
        return total
    
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        if len(str(telephone_number)) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return f"+7{telephone_number}"
    



kassa_1 = OnlineSalesRegisterCollector()

print(kassa_1.name_items)
print(kassa_1.number_items)
kassa_1.add_item_to_cheque("молоко")
kassa_1.add_item_to_cheque("чипсы")
kassa_1.add_item_to_cheque("чипсы")
kassa_1.add_item_to_cheque("чипсы")
kassa_1.add_item_to_cheque("чипсы")
kassa_1.add_item_to_cheque("чипсы")
kassa_1.add_item_to_cheque("чипсы")
kassa_1.add_item_to_cheque("кола")
kassa_1.add_item_to_cheque("печенье")
kassa_1.add_item_to_cheque("кефир")
kassa_1.add_item_to_cheque("кола")
input()
print(kassa_1.name_items)
print(kassa_1.number_items)

print(kassa_1.check_amount())
print(kassa_1.twenty_percent_tax_calculation())
print(kassa_1.ten_percent_tax_calculation())
print(kassa_1.total_tax())

# 1. Проверка правильного номера
try:
    number = OnlineSalesRegisterCollector.get_telephone_number(9001112233)
    print(f"Корректный номер: {number}")
except ValueError as e:
    print(f"Ошибка: {e}")

# 2. Проверка: передаем строку вместо числа
try:
    OnlineSalesRegisterCollector.get_telephone_number("9001112233")
except ValueError as e:
    print(f"Ошибка (строка вместо int): {e}")

# 3. Проверка: слишком короткий номер
try:
    OnlineSalesRegisterCollector.get_telephone_number(12345)
except ValueError as e:
    print(f"Ошибка (мало цифр): {e}")
