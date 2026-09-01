import subprocess
import platform
import ipaddress

def ping_sweep(red):
    print(f"Iniciando Ping Sweep en la red: {red}\n")
    net = ipaddress.ip_network(red, strict=False)
    
    # Determinar el parámetro de conteo según el sistema operativo
    sistema = platform.system().lower()
    parametro_conteo = "-n" if sistema == "windows" else "-c"
    
    for ip in net.hosts():
        ip_str = str(ip)
        
        # Configurar comando de ping según Windows o Linux/macOS
        if sistema == "windows":
            comando = ["ping", parametro_conteo, "1", "-w", "1000", ip_str]
        else:
            comando = ["ping", parametro_conteo, "1", "-W", "1", ip_str]
        
        try:
            # Ejecutar el comando silenciosamente
            resultado = subprocess.run(
                comando, 
                stdout=subprocess.DEVNULL, 
                stderr=subprocess.DEVNULL
            )
            
            if resultado.returncode == 0:
                print(f"[+] Host activo encontrado: {ip_str}")
        except Exception:
            pass

def run(param):
    """Función estándar requerida para la integración en la interfaz Tkinter."""
    if not param:
        param = "192.168.1.0/24"
    ping_sweep(param)

if __name__ == "__main__":
    # Permite seguir ejecutando el script de forma independiente por consola
    run("192.168.1.0/24")