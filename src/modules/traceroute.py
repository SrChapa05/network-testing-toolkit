import subprocess
import platform

def ejecutar_traceroute(destino):
    print(f"Iniciando Traceroute hacia: {destino}\n")
    
    sistema = platform.system().lower()
    
    # Configurar comando según el sistema operativo
    if sistema == "windows":
        comando = ["tracert", destino]
    else:
        comando = ["traceroute", destino]
        
    try:
        # Ejecutar el comando y mostrar la salida en tiempo real
        proceso = subprocess.Popen(
            comando, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT, 
            text=True, 
            encoding='utf-8', 
            errors='ignore'
        )
        
        for linea in proceso.stdout:
            print(linea, end="")
            
        proceso.wait()
        print("\n[+] Traceroute completado.")
        
    except Exception as e:
        print(f"[-] Error al ejecutar traceroute: {e}")

def run(param):
    """Función estándar requerida para la integración en la interfaz Tkinter."""
    if not param:
        param = "google.com"
        
    # Limpiamos el objetivo por si el usuario introduce una URL completa con protocolo
    destino = param.replace("https://", "").replace("http://", "").split("/")[0].strip()
    ejecutar_traceroute(destino)

if __name__ == "__main__":
    # Permite seguir ejecutando el script de forma independiente por consola
    run("google.com")