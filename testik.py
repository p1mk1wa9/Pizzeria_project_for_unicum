import p_box
print("Добро пожаловать в пиццерию Фреди Фазбера!")
login = "fR3449 f@z83r"
input_login = input("Введите логин:")
code = input("Придумайте пароль:")
if input_login == login:
    input_code = input("Введите придуманный Вами пароль:")
    if input_code == code:
        while True:
            # Все меню(варианты)
            # __________________________________________________________________________________________________________
            food = "Что будете заказывать?(Введите цифру)\n"\
             "1>>>Пиццы\n"\
             "2>>>Суши/Роллы\n"\
             "3>>>Кальсони\n"\
             "4>>>Салаты\n"\
             "5>>>Супы\n"\
             "6>>>Напитки\n"\
             "7>>>Мороженое"


            pizza = "Выберите пиццу (выбор осуществляется без : и цены)\n"\
                  "1>>Маргарита: 400 руб\n"\
                  "2>>Пеперони: 420 руб\n"\
                  "3>>Карбонара большая: 500 руб\n"\
                  "4>>Цыплёнок барбекю: 485 руб\n"\
                  "5>>4 сыра: 450 руб"

            pay = "Выберите оплату\n"\
                  "1>>Наличные\n"\
                  "2>>Безналичные"

            question = "Ещё будете что-то заказывать?\n"\
                             "1>>Да\n"\
                             "2>>Нет"

            sushi_rolls = "Выберите суши/роллы (выбор осуществляется без : и цены)\n" \
                          "1>>Филадельфия: 280 руб\n" \
                          "2>>Филадельия лайт с огурцом: 269 руб\n" \
                          "3>>Калифорния: 279 руб\n" \
                          "4>>Лава: 319 руб\n" \
                          "5>>С тунцом: 339 руб\n" \
                          "6>>В кляре: 299 руб\n" \
                          "7>>Бостон: 339 руб"
            # __________________________________________________________________________________________________________


            # Все меню(функции)
            # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
            def food_menu(food):
                return food

            def pizza_menu(pizza):
                return pizza

            def pay_menu(pay):
                return pay

            def question_menu(question):
                return question

            def sushi_menu(sushi_rolls):
                return sushi_rolls
            # |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

            print(food_menu(food))
            food_guess = input(":")
            food_list = ["1","2","3","4","5","6","7"]
            food_count = {"Пиццы" : 1, "Суши/Роллы" : 2, "Кальсони" : 3, "Салаты" : 4, "Супы" : 5, "Напитки" : 6, "Мороженое" : 7}
            food_name = {"Пиццы" : pizza, "Суши/Роллы" : sushi_rolls}
            exactly_guess = input(food_name.get(p_box.get_key(food_count, int(food_guess))))
            pizza_count = {"Маргарита" : 1, "Пеперони" : 2, "Карбонара большая" : 3, "Цыплёнок барбекю" : 4, "4 сыра" : 5}
            pizza_price = {"Маргарита" : 400, "Пеперони" : 420, "Карбонара большая" : 500, "Цыплёнок барбекю" : 450, "4 сыра" : 450}
            print(pay_menu(pay))
            pay_guess = input(":")
            if pay_guess == "1":
                print("К оплате:", pizza_price.get(p_box.get_key(pizza_count, int(exactly_guess))))
                pay_cash = int(input("Оплатите:"))
                if pay_cash >= pizza_price.get(p_box.get_key(pizza_count, exactly_guess)):
                    print("Ваша сдача:", pay_cash - pizza_price.get(p_box.get_key(pizza_count, exactly_guess)))
                    print("Спасибо за покупку :)")
                    print(question_menu(question))
                    question_guess = input(":")
                    if question_guess == "1":
                        continue
                    else:
                        print("Хорошего дня!")
                        exit()
            elif pay_guess == "2":
                print("К оплате:", pizza_price.get("Маргарита"))
                print("Успешно!")
                print("Спасибо за покупку :)")
                print(question)
                print(question_menu(question))
                question_guess = input(":")
                if question_guess == "1":
                    continue
                else:
                    print("Хорошего дня!")
                    exit()