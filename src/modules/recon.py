import dns.resolver

#Consulta registros DNS para un dominio específico
def consultar_dns(dominio, tipo_registro="A"):
    try:
        respuestas = dns.resolver.resolve(dominio, tipo_registro)
        registros = [str(r) for r in respuestas]
        return registros
    except Exception as e:
        print(f"Error al consultar DNS para {dominio} con tipo de registro {tipo_registro}: {e}")
        return []
    
    
if __name__ == "__main__":
    # Definimos un dominio de prueba seguro (por ejemplo, google.com o example.com)
    dominio_objetivo = "google.com"
    
    print(f"--- Consultando registros A (IPs) para {dominio_objetivo} ---")
    ips = consultar_dns(dominio_objetivo, "A")
    print(ips)
    
    print(f"\n--- Consultando servidores de correo (MX) para {dominio_objetivo} ---")
    servidores_correo = consultar_dns(dominio_objetivo, "MX")
    print(servidores_correo)