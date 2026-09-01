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

def run(param):
    """Función estándar para la integración en la interfaz gráfica."""
    if not param:
        param = "scanme.nmap.org:80"
    
    try:
        # Permite aceptar formato IP:PUERTO o solo IP (asumiendo puerto 80)
        if ":" in param:
            ip, puerto_str = param.split(":", 1)
            ip = ip.strip()
            puerto = int(puerto_str.strip())
        else:
            ip = param.strip()
            puerto = 80
            
        print(f"Iniciando Banner Grabbing en {ip}:{puerto}...")
        obtener_banner(ip, puerto)
        
    except ValueError:
        print("[!] Formato incorrecto. Usa IP:PUERTO (ej: 192.168.1.1:80)")
    except Exception as e:
        print(f"[!] Error inesperado: {e}")

if __name__ == "__main__":
    # Permite seguir ejecutando el script de forma independiente por consola
    run("scanme.nmap.org:80")