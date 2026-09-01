import socket
import ssl
from datetime import datetime

def verificar_ssl(dominio):
    # Creamos un contexto SSL seguro predeterminado
    contexto = ssl.create_default_context()
    
    try:
        # Nos conectamos por TCP al puerto 443 (HTTPS)
        with socket.create_connection((dominio, 443), timeout=5) as sock:
            # Envolvemos el socket con la capa SSL/TLS
            with contexto.wrap_socket(sock, server_hostname=dominio) as conexion:
                # Extraemos la información del certificado en formato diccionario
                info_cert = conexion.getpeercert()
                
                # Obtenemos la fecha de expiración ('notAfter')
                fecha_expiracion = info_cert.get('notAfter')
                emisor = info_cert.get('issuer')
                
                print(f"[+] Dominio seguro: {dominio}")
                print(f"    - Emisor: {emisor}")
                print(f"    - Caduca el: {fecha_expiracion}")
                return info_cert
                
    except Exception as e:
        print(f"[-] Error al verificar SSL para {dominio}: {e}")
        return None

if __name__ == "__main__":
    # Probamos con un dominio seguro conocido
    verificar_ssl("google.com")