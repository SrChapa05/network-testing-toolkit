import urllib.request
import urllib.error

def revisar_cabeceras(url):
    # Asegurarnos de que la URL tenga el protocolo correcto
    if not url.startswith("http"):
        url = "https://" + url
        
    print(f"Analizando cabeceras de seguridad para: {url}")
    
    # Cabeceras de seguridad clave recomendadas por OWASP
    cabeceras_importantes = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "X-XSS-Protection"
    ]
    
    try:
        # Realizamos la petición HTTP simulando un navegador
        req = urllib.request.Request(url, headers={'User-Agent': 'CyberSuite-MVP'})
        with urllib.request.urlopen(req, timeout=5) as respuesta:
            cabeceras = respuesta.headers
            
            print("\n[+] Estado de las cabeceras de seguridad:")
            for header in cabeceras_importantes:
                if header in cabeceras:
                    print(f"    [+] {header}: Presente")
                else:
                    print(f"    [-] {header}: Ausente (Riesgo potencial)")
                    
    except urllib.error.URLError as e:
        print(f"[-] Error de conexión con {url}: {e.reason}")
    except Exception as e:
        print(f"[-] Ocurrió un error inesperado: {e}")

def run(param):
    """Función estándar requerida para la integración en la interfaz Tkinter."""
    if not param:
        param = "google.com"
    revisar_cabeceras(param)

if __name__ == "__main__":
    # Permite ejecutar el script de forma independiente por consola
    run("google.com")