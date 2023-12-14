import p_box
input_login = input("Введите логин:")
code = input("Придумайте пароль:")
input_code = input("Введите придуманный Вами пароль:")
food_guess = input(p_box.food)
exactly_guess = input(p_box.food_name.get(p_box.get_key(p_box.food_count, int(food_guess))))