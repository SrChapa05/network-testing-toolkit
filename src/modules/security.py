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

if __name__ == "__main__":
    archivo_prueba = __file__  # Analiza este mismo script de ejemplo
    print(f"Calculando hash SHA-256 para: {archivo_prueba}")
    hash_resultado = calcular_hash_archivo(archivo_prueba)
    if hash_resultado:
        print(f"[+] Hash SHA-256: {hash_resultado}")