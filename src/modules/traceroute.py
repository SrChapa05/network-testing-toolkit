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

if __name__ == "__main__":
    # Objetivo de prueba (pueden cambiarlo por una IP o dominio)
    objetivo = "google.com"
    ejecutar_traceroute(objetivo)