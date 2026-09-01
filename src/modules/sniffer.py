from scapy.all import sniff

def procesar_paquete(paquete):
    # Aquí puedes procesar el paquete capturado según tus necesidades
    print(paquete.summary())
    
def iniciar_sniffer(cantidad_paquetes=5):
    print(f"Iniciando sniffer para capturar {cantidad_paquetes} paquetes...")
    sniff(count=cantidad_paquetes, prn=procesar_paquete)

if __name__ == "__main__":
    #Probar la función de sniffer con un número específico de paquetes
    iniciar_sniffer(10)