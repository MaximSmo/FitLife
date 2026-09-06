WATER_PER_KG = 30
ML_IN_L = 1000


def _calc_bmi(user_weight, user_height):
    bmi = user_weight / (user_height ** 2)
    return round(bmi, 1)


def _calc_water_volume(user_weight):
    water_l = (user_weight * WATER_PER_KG) / ML_IN_L
    return round(water_l, 2)


def _get_user_age():
    while True:
        try:
            user_age = int(input(
                "Теперь подскажите свой возраст (полных лет):\n"
            ))
            break
        except ValueError:
            print("Значение нужно ввести в числовом формате, например, 33")
    if user_age >= 50:
        print("\nВ таком возрасте важно следить за объемом потребляемой воды!")
    else:
        print(
            "\nЕще вся жизнь впереди, но все равно сейчас расчитаем сколько "
            "нужно воды, чтобы прожить долгую и счастливую жизнь.\n",
        )
    return user_age


def _get_user_weight():
    print(
        f"{user_name}, теперь укажите свой вес в кг.\nЗнаю, вопрос не "
        "скромный, но без этого я не смогу грамотно произвести вычисления!\n"
        "(Для разделения десятичных дробей используйте точку)\n",
    )
    while True:
        try:
            user_weight = float(input())
            break
        except ValueError:
            print("Значение нужно ввести в числовом формате, например, 33")
    return user_weight


def _get_user_height():
    print(
        "\nИ последнее, что я уточню - это Ваш рост.\n"
        "Значение укажите в метрах.\n"
        "(Для разделения десятичных дробей используйте точку)\n",
    )
    while True:
        try:
            user_height = float(input())
            break
        except ValueError:
            print("Значение нужно ввести в числовом формате, например, 33")
    return user_height


def _get_last_check():
    print(
        f"{user_name}, перед началом расчетов давайте подтвердим данные."
        f"\nВаш возраст - {user_age} лет"
        f"\nВаш вес = {user_weight} кг."
        f"\nВаш рост = {user_height} м."
        "\nЕсли данные верны, то введите 'Да', если нет введите 'Нет' и у вас "
        "будет возможность ввести показатели еще раз.",
        sep="",
    )
    return input()


print(
    "Приветствую! Я - бот, который поможет Вам рассчитать индекс массы тела"
    "и рекомендуемую норму воды в день.\n"
    "Для этого мне нужно задать Вам несколько вопросов.\n"
    "Пожалуйста, отвечайте на них честно и внимательно.\n"
    "Для разделения десятичных дробей используйте точку.\n"
    "Для начала познакомимся! Как к вам обращаться?\n",
)
user_name = input()
print("\nРад знакомству, ", user_name, "!", sep="", flush=True)

user_age = _get_user_age()
user_weight = _get_user_weight()
user_height = _get_user_height()
last_check = _get_last_check()

while True:
    if last_check.lower() == "да":
        bmi = _calc_bmi(user_weight, user_height)
        water_volume = _calc_water_volume(user_weight)
        break
    else:
        user_age = _get_user_age()
        user_weight = _get_user_weight()
        user_height = _get_user_height()
        last_check = _get_last_check()

print(
    f"\nОтчет для пользователя: {user_name} ({user_age})"
    f"\nВаш индекс массы тела = {bmi}"
    f"\nРекомендуемая норма воды: {water_volume} л. воды в день"
    "\n\nСпасибо большое, что дали возможность проявить себя! Будьте здоровы!",
    sep="",
)
