def generar_recomendaciones():
    print("=" * 50)
    print("  GUÍA DE RECOMENDACIONES DE DEFENSAS (HARDENING)")
    print("=" * 50)
    
    recomendaciones = [
        "1. Desactiva servicios innecesarios (Telnet, FTP antiguo, SNMP v1/v2).",
        "2. Utiliza siempre cifrado moderno (TLS 1.3) para comunicaciones web.",
        "3. Implementa políticas estrictas de contraseñas (mínimo 12 caracteres y rotación).",
        "4. Mantén actualizado el sistema operativo y todas las librerías externas.",
        "5. Configura un Firewall perimetral para bloquear puertos no utilizados.",
        "6. Revisa periódicamente los registros de eventos (logs) en busca de anomalías."
    ]
    
    for rec in recomendaciones:
        print(f" [+] {rec}")
    print("=" * 50)

def run(param=""):
    """Función estándar requerida para la integración en la interfaz Tkinter."""
    generar_recomendaciones()

if __name__ == "__main__":
    # Permite ejecutar el script de forma independiente por consola
    run()