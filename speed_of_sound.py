temperature = float(input("Введите температуру в градусах Цельсия: "))

speed_of_sound = 331.4 + (0.6 * temperature)

print("Скорость звука при {} градусах Цельсия: {:.2f} м/с".format(temperature, speed_of_sound))
