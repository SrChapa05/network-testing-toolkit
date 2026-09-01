import hashlib
import os

def calcular_hash_archivo(ruta_archivo):
    sha256_hash = hashlib.sha256()
    try:
        if not os.path.exists(ruta_archivo):
            print(f"[-] El archivo {ruta_archivo} no existe.")
            return None
            
        with open(ruta_archivo, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
                
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"[-] Error al calcular el hash: {e}")
        return None

def run(param):
    """Función estándar requerida para la integración en la interfaz Tkinter."""
    if not param:
        param = __file__  # Si está vacío, analiza este mismo archivo como demostración
        
    print(f"Calculando hash SHA-256 para: {param}")
    hash_resultado = calcular_hash_archivo(param)
    if hash_resultado:
        print(f"[+] Hash SHA-256: {hash_resultado}")

if __name__ == "__main__":
    # Permite seguir ejecutando el script de forma independiente por consola
    run(__file__)