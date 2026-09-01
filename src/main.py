import sys
import os

# Asegurar que la carpeta src esté en el path de Python para importar los módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Importar funciones de los módulos (asegúrate de que __init__.py exista en src/modules/)
try:
    from modules.scanner import escanear_puertos
    from modules.recon import consultar_dns
    from modules.ssl_checker import verificar_ssl
    from modules.arp_scanner import escanear_arp
    from modules.ping_sweep import ping_sweep
    from modules.traceroute import ejecutar_traceroute
    from modules.subdomain_scanner import buscar_subdominios
    from modules.dir_buster import buscar_directorios
    from modules.banner_grabber import obtener_banner
    from modules.http_headers import revisar_cabeceras
    from modules.password_checker import verificar_fortaleza_password
    from modules.security import calcular_hash_archivo
    from modules.defense import generar_recomendaciones
    from modules.utils_net import obtener_ip_local
except ImportError as e:
    # Fallback o aviso si se ejecuta desde otra ruta
    pass

def mostrar_banner():
    print("=" * 60)
    print("      NETWORK TESTING TOOLKIT - CYBERSUITE MVP")
    print("      Monitoreo, Auditoría y Defensa de Redes")
    print("=" * 60)

def menu_principal():
    while True:
        print("\n[ PANEL DE CONTROL PRINCIPAL ]")
        print("--- Reconocimiento y Red ---")
        print(" 1. Escáner de Puertos TCP")
        print(" 2. Escáner ARP Local")
        print(" 3. Barrido de Pings (Ping Sweep)")
        print(" 4. Traceroute de Red")
        print(" 5. Consulta y Resolución DNS")
        print(" 6. Buscador de Subdominios")
        
        print("\n--- Auditoría Web y Servicios ---")
        print(" 7. Validador de Certificados SSL/TLS")
        print(" 8. Auditor de Cabeceras HTTP")
        print(" 9. Captura de Banners (Banner Grabbing)")
        print("10. Buscador de Directorios Web (Dir Buster)")
        
        print("\n--- Seguridad y Utilidades ---")
        print("11. Verificador de Fortaleza de Contraseñas")
        print("12. Verificador de Integridad de Archivos (SHA-256)")
        print("13. Guía de Endurecimiento (Hardening & Defense)")
        print("14. Mostrar IP Local Actual")
        
        print("\n 0. Salir de la Suite")
        
        opcion = input("\nSeleccione una opción (0-14): ").strip()
        
        if opcion == "1":
            objetivo = input("Ingrese la IP o dominio objetivo: ").strip()
            puertos = [21, 22, 80, 443, 8080] # Ejemplo de puertos base
            escanear_puertos(objetivo, puertos)
            
        elif opcion == "2":
            red = input("Ingrese la red local (ej. 192.168.1.0/24): ").strip()
            escanear_arp(red)
            
        elif opcion == "3":
            red = input("Ingrese la red para Ping Sweep (ej. 192.168.1.0/24): ").strip()
            ping_sweep(red)
            
        elif opcion == "4":
            objetivo = input("Ingrese la IP o dominio destino: ").strip()
            ejecutar_traceroute(objetivo)
            
        elif opcion == "5":
            dominio = input("Ingrese el dominio a consultar: ").strip()
            consultar_dns(dominio)
            
        elif opcion == "6":
            dominio = input("Ingrese el dominio principal: ").strip()
            subs = ["www", "mail", "ftp", "admin", "test", "api", "dev"]
            buscar_subdominios(dominio, subs)
            
        elif opcion == "7":
            dominio = input("Ingrese el dominio/IP HTTPS a verificar: ").strip()
            verificar_ssl(dominio)
            
        elif opcion == "8":
            url = input("Ingrese la URL a auditar: ").strip()
            revisar_cabeceras(url)
            
        elif opcion == "9":
            ip = input("Ingrese la IP objetivo: ").strip()
            puerto = int(input("Ingrese el puerto (ej. 80 o 22): ").strip())
            obtener_banner(ip, puerto)
            
        elif opcion == "10":
            url = input("Ingrese la URL base: ").strip()
            rutas = ["admin", "login", "robots.txt", "backup.zip", "index.php"]
            buscar_directorios(url, rutas)
            
        elif opcion == "11":
            pwd = input("Ingrese la contraseña a evaluar: ").strip()
            verificar_fortaleza_password(pwd)
            
        elif opcion == "12":
            ruta = input("Ingrese la ruta absoluta o relativa del archivo: ").strip()
            hash_val = calcular_hash_archivo(ruta)
            if hash_val:
                print(f"[+] Hash SHA-256: {hash_val}")
                
        elif opcion == "13":
            generar_recomendaciones()
            
        elif opcion == "14":
            print(f"\n[+] Su IP Local activa es: {obtener_ip_local()}")
            
        elif opcion == "0":
            print("\nSaliendo de la CyberSuite. ¡Hasta pronto!")
            break
        else:
            print("\n[-] Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    mostrar_banner()
    menu_principal()