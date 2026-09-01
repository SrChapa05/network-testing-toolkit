import socket

def obtener_banner(ip, puerto):
    try:
        # Configuramos un socket con timeout de 3 segundos
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            s.connect((ip, puerto))
            
            # Algunos servicios requieren que enviemos algo para que respondan (ej. HTTP)
            if puerto == 80 or puerto == 443:
                s.send(b"HEAD / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")
            
            # Recibimos los primeros 1024 bytes de respuesta del servicio
            banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
            
            if banner:
                print(f"[+] Banner obtenido de {ip}:{puerto}:\n{banner}")
            else:
                print(f"[-] El puerto {puerto} en {ip} no devolvió ningún banner.")
                
    except socket.timeout:
        print(f"[-] Tiempo de espera agotado al conectar con {ip}:{puerto}")
    except Exception as e:
        print(f"[-] Error al intentar obtener el banner: {e}")

if __name__ == "__main__":
    # Probamos con una IP pública o local y un puerto común (ej. puerto 80 o 21)
    ip_objetivo = "scanme.nmap.org"  # O una IP local de prueba
    puerto_objetivo = 80
    
    print(f"Iniciando Banner Grabbing en {ip_objetivo}:{puerto_objetivo}...")
    obtener_banner(ip_objetivo, puerto_objetivo)