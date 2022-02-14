def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"No hay suficiente agua para {astronauts} astronautas despues de {days_left} días!")
    return f"Total de agua después de {days_left} días es: {total_water_left} litros"

#water_left(5, 100, 2)

#try:
#    water_left(5, 100, 2)
#except RuntimeError as err:
#    print("Error al calcular el agua:", err)

#water_left("3", "200", None)

def water_left_ext(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            argument / 10
        except TypeError:
            raise TypeError(f"Todos los argumentos deben ser enteros, se recibió: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"No hay suficiente agua para {astronauts} astronautas despues de {days_left} días!")
    return f"Total de agua después de {days_left} días es: {total_water_left} litros"

water_left_ext("3", "200", None)