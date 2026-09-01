import socket

#Escaneo de puertos
def scan_ports(host, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

#Prueba de la función de escaneo de puertos
if __name__ == "__main__":
    ip_objetivo = "192.168.1.1"
    
    puertos_a_escanear = [21, 22, 23, 25, 53, 80, 110, 443, 8080]
    
    print(f"Escaneando puertos en {ip_objetivo}...")
    puertos_abiertos = scan_ports(ip_objetivo, puertos_a_escanear)
    if puertos_abiertos:
        print(f"Puertos abiertos encontrados: {puertos_abiertos}")
    else:
        print("No se encontraron puertos abiertos.")
        