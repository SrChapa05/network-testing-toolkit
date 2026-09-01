import urllib.request
import urllib.error

def buscar_subdominios(dominio, lista_subdominios):
    print(f"Iniciando búsqueda de subdominios para: {dominio}\n")
    
    for sub in lista_subdominios:
        sub_limpio = sub.strip()
        url = f"http://{sub_limpio}.{dominio}"
        
        try:
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'CyberSuite-MVP'}
            )
            # Intentamos realizar la petición con un timeout corto
            with urllib.request.urlopen(req, timeout=3) as respuesta:
                print(f"[+] Activo: {url} (Código: {respuesta.getcode()})")
                
        except urllib.error.HTTPError as e:
            # Si responde con un error HTTP (ej. 403 o 500), el subdominio existe
            print(f"[+] Activo (HTTP {e.code}): {url}")
        except urllib.error.URLError:
            # Si hay error de resolución DNS, el subdominio no existe o no es público
            pass
        except Exception:
            pass

def run(param):
    """Función estándar requerida para la integración en la interfaz Tkinter."""
    if not param:
        param = "google.com"
        
    # Limpiamos el dominio ingresado por si incluye protocolos o barras
    dominio = param.replace("https://", "").replace("http://", "").split("/")[0].strip()
    
    # Diccionario básico de subdominios comunes
    subdominios_prueba = [
        "www",
        "mail",
        "ftp",
        "admin",
        "test",
        "api",
        "dev",
        "portal",
        "shop",
        "vpn"
    ]
    
    buscar_subdominios(dominio, subdominios_prueba)

if __name__ == "__main__":
    # Permite seguir ejecutando el script de forma independiente por consola
    run("google.com")