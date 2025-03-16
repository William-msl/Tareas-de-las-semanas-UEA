def temperatura_promedio(ciudades_temperaturas):
    temperaturas_promedio = {}

    for ciudad, semanas in ciudades_temperaturas.items():
        total_temp = 0
        num_dias = 0

        for semana in semanas:
            for dia in semana:
                total_temp += dia["temp"]
                num_dias += 1

        temperaturas_promedio[ciudad] = total_temp / num_dias

    return temperaturas_promedio


# Diccionario de ciudades con temperaturas por semanas y días
ciudades_temperaturas = {
    "Quito": [
        [
            {"day": "Lunes", "temp": 16}, {"day": "Martes", "temp": 16}, {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 16}, {"day": "Viernes", "temp": 17}, {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 17}
        ],
        [
            {"day": "Lunes", "temp": 17}, {"day": "Martes", "temp": 17}, {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 17}, {"day": "Viernes", "temp": 18}, {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 18}
        ],
        [
            {"day": "Lunes", "temp": 17}, {"day": "Martes", "temp": 17}, {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 17}, {"day": "Viernes", "temp": 18}, {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 18}
        ],
        [
            {"day": "Lunes", "temp": 17}, {"day": "Martes", "temp": 17}, {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 16}, {"day": "Viernes", "temp": 17}, {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 18}
        ]
    ],
    "Cuenca": [
        [
            {"day": "Lunes", "temp": 16}, {"day": "Martes", "temp": 16}, {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 17}, {"day": "Viernes", "temp": 17}, {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 17}
        ],
        [
            {"day": "Lunes", "temp": 15}, {"day": "Martes", "temp": 16}, {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 15}, {"day": "Viernes", "temp": 16}, {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 17}
        ],
        [
            {"day": "Lunes", "temp": 15}, {"day": "Martes", "temp": 15}, {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 15}, {"day": "Viernes", "temp": 16}, {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 15}
        ],
        [
            {"day": "Lunes", "temp": 16}, {"day": "Martes", "temp": 16}, {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 17}, {"day": "Viernes", "temp": 16}, {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 16}
        ]
    ],
    "Guayaquil": [
        [
            {"day": "Lunes", "temp": 29}, {"day": "Martes", "temp": 30}, {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 30}, {"day": "Viernes", "temp": 31}, {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 29}
        ],
        [
            {"day": "Lunes", "temp": 29}, {"day": "Martes", "temp": 30}, {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 30}, {"day": "Viernes", "temp": 31}, {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 30}
        ],
        [
            {"day": "Lunes", "temp": 31}, {"day": "Martes", "temp": 30}, {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 30}, {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 29}
        ],
        [
            {"day": "Lunes", "temp": 29}, {"day": "Martes", "temp": 31}, {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 31}, {"day": "Viernes", "temp": 31}, {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 30}
        ]
    ]
}

# Llamamos a la función para calcular las temperaturas promedio
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Mostramos los resultados
print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"Promedio de temperaturas en {ciudad}: {promedio:.2f}°C")
