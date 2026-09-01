import re

def verificar_fortaleza_password(password):
    longitud_minima = 8
    puntuacion = 0
    criterios_fallidos = []

    # 1. Validar longitud
    if len(password) >= longitud_minima:
        puntuacion += 1
    else:
        criterios_fallidos.append(f"Debe tener al menos {longitud_minima} caracteres.")

    # 2. Validar minúsculas
    if re.search(r"[a-z]", password):
        puntuacion += 1
    else:
        criterios_fallidos.append("Faltan letras minúsculas.")

    # 3. Validar mayúsculas
    if re.search(r"[A-Z]", password):
        puntuacion += 1
    else:
        criterios_fallidos.append("Faltan letras mayúsculas.")

    # 4. Validar números
    if re.search(r"\d", password):
        puntuacion += 1
    else:
        criterios_fallidos.append("Faltan números.")

    # 5. Validar caracteres especiales
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        puntuacion += 1
    else:
        criterios_fallidos.append("Faltan símbolos especiales (!@#$%^&*...).")

    # Evaluar resultado final
    print(f"\nEvaluando contraseña analizada...")
    if puntuacion == 5:
        print("[+] Resultado: Contraseña MUY FUERTE.")
    elif puntuacion >= 3:
        print("[!] Resultado: Contraseña MODERADA. Se puede mejorar.")
    else:
        print("[-] Resultado: Contraseña DÉBIL.")

    if criterios_fallidos:
        print("\nSugerencias de mejora:")
        for falla in criterios_fallidos:
            print(f" - {falla}")

def run(param):
    """Función estándar requerida para la integración en la interfaz Tkinter."""
    if not param:
        param = "CyberSuite2026!"
        
    print(f"Probando con la clave: {param}")
    verificar_fortaleza_password(param)

if __name__ == "__main__":
    # Permite ejecutar el script de forma independiente por consola
    run("CyberSuite2026!")