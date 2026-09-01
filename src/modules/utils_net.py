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

if __name__ == "__main__":
    print(f"[+] IP Local detectada: {obtener_ip_local()}")
    print(f"[+] ¿Es '192.168.1.1' válida?: {validar_ip('192.168.1.1')}")