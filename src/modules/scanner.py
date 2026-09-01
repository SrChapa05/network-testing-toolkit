import socket

def run(host):
    """Función principal que la interfaz llamará pasando el objetivo."""
    ports = [21, 22, 23, 25, 53, 80, 110, 443, 8080]
    
    print(f"Escaneando puertos en {host}...")
    open_ports = []
    
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"[+] Puerto {port}: ABIERTO")
                open_ports.append(port)
            sock.close()
        except Exception as e:
            print(f"[!] Error en puerto {port}: {e}")

    if open_ports:
        print(f"\nResumen - Puertos abiertos encontrados: {open_ports}")
    else:
        print("\nNo se encontraron puertos abiertos.")

# Opcional: Si aún quieres poder ejecutar este script individualmente por terminal
if __name__ == "__main__":
    run("192.168.1.1")