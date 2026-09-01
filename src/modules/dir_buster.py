import urllib.request
import urllib.error

def buscar_directorios(url_base, lista_rutas):
    # Asegurarnos de que la URL termine en barra diagonal
    if not url_base.endswith("/"):
        url_base += "/"
        
    print(f"Iniciando búsqueda de directorios en: {url_base}\n")
    
    for ruta in lista_rutas:
        url_objetivo = url_base + ruta.strip()
        
        try:
            # Creamos la petición simulando ser un navegador
            req = urllib.request.Request(
                url_objetivo, 
                headers={'User-Agent': 'CyberSuite-MVP'}
            )
            
            # Intentamos abrir la URL
            with urllib.request.urlopen(req, timeout=3) as respuesta:
                codigo = respuesta.getcode()
                if codigo == 200:
                    print(f"[+] Encontrado (200 OK): /{ruta}")
                    
        except urllib.error.HTTPError as e:
            # Si el servidor responde con 403 (Prohibido), la ruta existe pero no tenemos permisos
            if e.code == 403:
                print(f"[!] Acceso Prohibido (403): /{ruta}")
            # Si es 404 (No encontrado), simplemente ignoramos o no mostramos nada
        except urllib.error.URLError:
            pass # Ignoramos errores de conexión de rutas inexistentes
        except Exception:
            pass

if __name__ == "__main__":
    # Una lista pequeña de directorios/archivos comunes para probar
    diccionario_prueba = [
        "admin",
        "login",
        "robots.txt",
        "backup.zip",
        "index.php",
        "dashboard",
        "config.json"
    ]
    
    # Podemos usar un sitio web público de pruebas (ej. http://testphp.vulnweb.com o un servidor local)
    url_objetivo = "http://testphp.vulnweb.com"
    
    buscar_directorios(url_objetivo, diccionario_prueba)