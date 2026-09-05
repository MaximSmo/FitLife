WATER_PER_KG = 30
ML_IN_L = 1000


def _calc_bmi(user_weight, user_height):
    bmi = user_weight / (user_height ** 2)
    return round(bmi, 1)


def _calc_water_volume(user_weight):
    water_ml = user_weight * WATER_PER_KG
    water_l = water_ml / ML_IN_L
    return round(water_l, 2)


def _get_user_age():
    user_age = int(input('Теперь подскажите свой возраст (полных лет):\n'))
    if user_age >= 50:
        print("\nВ таком возрасте важно следить за объемом потребляемой воды!")
    else:
        print(
            "\nЕще вся жизнь впереди, но все равно сейчас расчитаем сколько "
            "нужно воды, чтобы прожить долгую и счастливую жизнь.\n"
        )
    return user_age


def _get_user_weight():
    user_weight = float(input(
        f"{user_name}, теперь укажите свой вес в кг.\nЗнаю, вопрос не "
        "скромный, но без этого я не смогу грамотно произвести вычисления!\n"
        "(Для разделения десятичных дробей используйте точку)\n"
    ))
    return user_weight


def _get_user_height():
    user_height = float(input(
        "\nИ последнее, что я уточню - это Ваш рост.\n"
        "Значение укажите в метрах.\n"
        "(Для разделения десятичных дробей используйте точку)\n"
    ))
    return user_height


def _get_last_check():
    print(
        f"{user_name}, перед началом расчетов давайте подтвердим данные."
        f"\nВаш возраст - {user_age} лет"
        f"\nВаш вес = {user_weight} кг."
        f"\nВаш рост = {user_height} м."
        "\nЕсли данные верны, то введите 'Да', если нет введите 'Нет' и у вас "
        "будет возможность ввести показатели еще раз.",
        sep=""
    )
    return input()


with open("intro.txt", "r", encoding="utf-8") as file_intro:
    for line in file_intro:
        print(line.strip())

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
    sep=""
)
