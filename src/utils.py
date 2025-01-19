def validar_peso(peso):
    try:
        peso = int(peso)
        if peso <= 0:
            raise ValueError
        return peso
    except ValueError:
        raise ValueError("O peso deve ser um número inteiro positivo.")

def validar_valor(valor):
    try:
        valor = int(valor)
        if valor < 0:
            raise ValueError
        return valor
    except ValueError:
        raise ValueError("O valor deve ser um número inteiro não negativo.")
