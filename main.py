import sys
import io
import time
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Importar los módulos reales de la toolkit
from src.modules import (
    arp_scanner, banner_grabber, defense, dir_buster,
    http_headers, password_checker, ping_sweep, recon,
    scanner, security, sniffer, ssl_checker,
    subdomain_scanner, traceroute, utils_net
)

app = FastAPI(
    title="Network Testing Toolkit API",
    version="1.0.0",
    description="Backend FastAPI para el control y ejecución modular de herramientas de ciberseguridad."
)

# Configuración de CORS permitiendo peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O especifica ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro centralizado de módulos
MODULES_REGISTRY = {
    "arp-scanner": {"name": "ARP Scanner", "func": arp_scanner.run},
    "banner-grabber": {"name": "Banner Grabbing", "func": banner_grabber.run},
    "defense": {"name": "Defense / Hardening", "func": defense.run},
    "dir-buster": {"name": "Directory Buster", "func": dir_buster.run},
    "http-headers": {"name": "Cabeceras HTTP", "func": http_headers.run},
    "password-checker": {"name": "Validador de Contraseñas", "func": password_checker.run},
    "ping-sweep": {"name": "Barrido Ping", "func": ping_sweep.run},
    "recon": {"name": "Recon", "func": recon.run},
    "scanner": {"name": "Scanner", "func": scanner.run},
    "security": {"name": "Security", "func": security.run},
    "sniffer": {"name": "Sniffer de Red", "func": sniffer.run},
    "ssl-checker": {"name": "Verificador SSL", "func": ssl_checker.run},
    "subdomain-scanner": {"name": "Escáner de Subdominios", "func": subdomain_scanner.run},
    "traceroute": {"name": "Traceroute", "func": traceroute.run},
    "utils-net": {"name": "Utilidades de Red", "func": utils_net.run},
}

class ExecutionRequest(BaseModel):
    param: str = ""

@app.get("/")
def leer_raiz():
    """Ruta raíz para verificar el estado del servidor."""
    return {
        "estado": "activo",
        "mensaje": "Network Testing Toolkit API funcionando correctamente",
        "documentacion": "/docs",
        "total_modulos": len(MODULES_REGISTRY)
    }

@app.get("/api/modules")
def listar_modulos():
    """Devuelve la lista completa de módulos disponibles."""
    return {
        "modules": [
            {"id": key, "name": info["name"]} 
            for key, info in MODULES_REGISTRY.items()
        ]
    }
    
@app.post("/api/execute/{module_id}")
def ejecutar_modulo(module_id: str, request: ExecutionRequest):
    """Ejecuta un módulo específico y captura su salida estándar (prints)."""
    if module_id not in MODULES_REGISTRY:
        raise HTTPException(status_code=404, detail=f"El módulo '{module_id}' no existe.")

    mod_info = MODULES_REGISTRY[module_id]
    func = mod_info["func"]
    
    buffer_salida = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buffer_salida

    inicio = time.time()
    success = True

    try:
        # Ejecución del módulo con el parámetro provisto
        func(request.param)
        resultado = buffer_salida.getvalue()
    except Exception as e:
        success = False
        resultado = buffer_salida.getvalue() + f"\n[!] Error crítico ejecutando el módulo: {str(e)}"
    finally:
        sys.stdout = old_stdout

    duracion = round(time.time() - inicio, 3)

    return {
        "module_id": module_id,
        "module_name": mod_info["name"],
        "param": request.param,
        "success": success,
        "duration_seconds": duracion,
        "output": resultado if resultado else "[*] El módulo finalizó sin imprimir salidas en consola."
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)