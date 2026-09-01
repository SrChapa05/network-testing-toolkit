from scapy.all import sniff

def procesar_paquete(paquete):
    # Aquí puedes procesar el paquete capturado según tus necesidades
    print(paquete.summary())
    
def iniciar_sniffer(cantidad_paquetes=5):
    print(f"Iniciando sniffer para capturar {cantidad_paquetes} paquetes...")
    sniff(count=cantidad_paquetes, prn=procesar_paquete)

def run(param):
    """Función estándar requerida para la integración en la interfaz Tkinter."""
    try:
        # Intentamos convertir el parámetro de la interfaz a entero (número de paquetes)
        cantidad = int(param.strip()) if param and param.strip().isdigit() else 5
    except ValueError:
        cantidad = 5
        
    try:
        iniciar_sniffer(cantidad)
        print("[+] Sniffer finalizado con éxito.")
    except PermissionError:
        print("[!] Error: La captura de paquetes (Scapy) requiere privilegios de administrador/root.")
    except Exception as e:
        print(f"[!] Error inesperado en el sniffer: {e}")

if __name__ == "__main__":
    # Probar la función de sniffer de forma independiente por consola
    run("5")