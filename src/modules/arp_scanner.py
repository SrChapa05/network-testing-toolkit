from scapy.all import ARP, Ether, srp

def escanear_arp(ip_rango):
    print(f"Escaneando la red en busca de dispositivos activos: {ip_rango}")
    
    # 1. Crear trama Ethernet de difusión (broadcast a toda la red física)
    paquete_ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # 2. Crear paquete ARP pidiendo el rango de IPs objetivo
    paquete_arp = ARP(pdst=ip_rango)
    
    # 3. Combinar ambas capas en un solo paquete
    paquete_final = paquete_ether / paquete_arp
    
    # 4. Enviar y recibir paquetes en la capa 2 (srp) con un timeout de 2 segundos
    respondidos, no_respondidos = srp(paquete_final, timeout=2, verbose=False)
    
    dispositivos = []
    for enviado, recibido in respondidos:
        # Guardamos la IP (psrc) y la dirección MAC física (hwsrc)
        dispositivos.append({'ip': recibido.psrc, 'mac': recibido.hwsrc})
        
    return dispositivos

if __name__ == "__main__":
    # Ajusten este rango según su red local (por ejemplo, "192.168.1.0/24")
    rango_red = "192.168.1.0/24"
    
    activos = escanear_arp(rango_red)
    
    print("\nDispositivos encontrados en la red:")
    print("IP" + " " * 16 + "MAC Address")
    print("-" * 35)
    for d in activos:
        print(f"{d['ip']:<18} {d['mac']}")