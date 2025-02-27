def separa_letras(string):
    # Revisa si la entrada es una variable de tipo int
    if type(string) is int:
        return (-100, None, None)

    # Revisa si la entrada es un string que contiene números enteros
    # mediante el método isnumeric de Python
    if string.isnumeric():
        return (-100, None, None)

    # Revisa si la entrada es un string vacio o un string de espacios
    # en blanco mediante el método isspace de Python
    if string.isspace() or not string:
        return (-300, None, None)

    # Revisa si el string contiene algún caracter fuera del abecedario
    # mediante el método isalpha de Python
    if not string.isalpha():
        return (-200, None, None)

    # Luego de verificar los casos de error se inicializa dos variables
    # de tipo string para que estos luego contengan las mayúsculas y
    # minúsculas del string que se recibe a la entrada de la función. Mediante
    # un for loop y la función isupper() se analiza cada elemento del string
    # inicial y dependiendo de si este es una mayúscula o minúscula se agrega
    # a la variable respectiva.
    upper = lower = ""
    for i in string:
        if i.isupper():
            upper = upper+i
        else:
            lower = lower+i
    return (0, upper, lower)


def potencia_manual(base, exponente):

    # Verificar que los parámetros no sean de tipo string
    if type(exponente) is str or type(base) is str:
        return (-400, None)

    # Caso especial: potencia igual a 0
    if (exponente == 0):
        return (0, 1)

    # Caso especial: potencia negativa
    if exponente < 0:
        res = 1 / potencia_manual(base, -exponente)[1]
        return (0, res)

    # El cálculo de la potencia se inicializa una variable temporal y se le
    # asigna el valor de la base. Se inicia un primer for loop que realiza un
    # número de iteraciones igual al exponente – 1. Esto se debe a que el
    # proceso de multiplicación inicia con el segundo término, o también se
    # puede considerar que el primer término fue multiplicado por 1. Pero en
    # lugar de realizar mutilaciones se utilizan sumas, para esto se cuenta
    # con un segundo for loop que realiza una cantidad de iteraciones igual a
    # la base – 1. Para esto se sigue una lógica similar al primer for loop
    # en donde se puede decir que el primer termino se suma con un cero.  La
    # variable temporal se le asigna como nuevo valor el resultado de la
    # sumatorio y se repite el proceso.
    x = base
    for i in range(exponente-1):
        y = x
        for j in range(base-1):
            x = x+y
    return (0, x)
