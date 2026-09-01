import socket

def obtener_ip_local():
    try:
        # Crea un socket temporal para descubrir la IP local activa
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_local = s.getsockname()[0]
        s.close()
        return ip_local
    except Exception:
        return "127.0.0.1"

def validar_ip(ip):
    partes = ip.split(".")
    if len(partes) != 4:
        return False
    for parte in partes:
        if not parte.isdigit() or not 0 <= int(parte) <= 255:
            return False
    return True

def run(param):
    """Función estándar requerida para la integración en la interfaz Tkinter."""
    print(f"[+] IP Local detectada: {obtener_ip_local()}")
    
    # Si el usuario proporciona una IP en la entrada de la interfaz, la validamos; si no, usamos una por defecto
    ip_a_probar = param.strip() if param else "192.168.1.1"
    es_valida = validar_ip(ip_a_probar)
    
    print(f"[+] ¿Es '{ip_a_probar}' una IP válida?: {es_valida}")

if __name__ == "__main__":
    # Permite seguir ejecutando el script de forma independiente por consola
    run("192.168.1.1")