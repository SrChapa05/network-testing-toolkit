import dns.resolver

# Consulta registros DNS para un dominio específico
def consultar_dns(dominio, tipo_registro="A"):
    try:
        respuestas = dns.resolver.resolve(dominio, tipo_registro)
        registros = [str(r) for r in respuestas]
        return registros
    except Exception as e:
        print(f"[-] Error al consultar DNS ({tipo_registro}) para {dominio}: {e}")
        return []

def run(param):
    """Función estándar requerida para la integración en la interfaz Tkinter."""
    if not param:
        param = "google.com"
        
    dominio_objetivo = param.strip()
    
    print(f"--- Consultando registros A (IPs) para {dominio_objetivo} ---")
    ips = consultar_dns(dominio_objetivo, "A")
    if ips:
        for ip in ips:
            print(f"  [+] IP: {ip}")
    
    print(f"\n--- Consultando servidores de correo (MX) para {dominio_objetivo} ---")
    servidores_correo = consultar_dns(dominio_objetivo, "MX")
    if servidores_correo:
        for mx in servidores_correo:
            print(f"  [+] MX: {mx}")

if __name__ == "__main__":
    # Permite seguir ejecutando el script de forma independiente por consola
    run("google.com")