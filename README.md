```python
complete_readme = """# network-testing-toolkit 🛡️

> Proyecto obsesivo y enfermo de kit de herramientas de testeo de redes, ciberseguridad defensiva y ofensiva controlada, desarrollado en Python con interfaz gráfica modular (Tkinter).

---

## 📋 Tabla de Contenidos
1. [Características Principales](#características-principales)
2. [Estructura del Proyecto](#estructura-del-proyecto)
3. [Arquitectura e Integración](#arquitectura-e-integración)
4. [Catálogo Completo de Módulos](#catálogo-completo-de-módulos)
5. [Análisis Profundo de Cabeceras HTTP (http_headers)](#análisis-profundo-de-cabeceras-http-http_headers)
6. [Requisitos e Instalación](#requisitos-e-instalación)
7. [Instrucciones de Ejecución](#instrucciones-de-ejecución)

---

## 🚀 Características Principales
- **Interfaz Gráfica Modular (Tkinter):** Pestañas organizadas para un acceso rápido a cada herramienta.
- **Multihilos (Threading):** Ejecución asíncrona para evitar el bloqueo de la interfaz gráfica durante operaciones de red prolongadas.
- **Captura Estándar Dinámica:** Redirección automática de la salida (`sys.stdout`) hacia la consola integrada de la aplicación.
- **Estandarización de Módulos:** Todos los scripts individuales se comunican mediante una interfaz común basada en la función `run(param)`.

---

## 📂 Estructura de Directorios

```text
network-testing-toolkit/
│
├── tkinter_app.py           # Interfaz gráfica principal y gestor de hilos/consola
└── src/
    └── modules/
        ├── port_scanner.py      # 1. Escáner de Puertos
        ├── ping_sweep.py        # 2. Barrido Ping
        ├── banner_grabber.py    # 3. Captura de Banners
        ├── dir_buster.py        # 4. Búsqueda de Directorios
        ├── http_headers.py      # 5. Análisis de Cabeceras HTTP
        ├── password_checker.py  # 6. Validador de Contraseñas
        ├── dns_enum.py          # 7. Enumeración DNS
        ├── hash_checker.py      # 8. Verificador de Hash SHA-256
        ├── sniffer.py           # 9. Sniffer de Red (Scapy)
        ├── defense.py           # 10. Recomendaciones de Hardening
        ├── ssl_checker.py       # 11. Verificación de Certificados SSL
        ├── subdomain_scanner.py # 12. Escáner de Subdominios
        ├── traceroute.py        # 13. Trazado de Ruta
        └── utils_net.py         # 14. Utilidades de Red e IP

```

---

## ⚙️ Arquitectura e Integración

Cada módulo dentro de `src/modules/` implementa obligatoriamente la función estándar **`run(param)`**:

* **`param`**: El valor en cadena de texto introducido por el usuario en la caja de entrada de la interfaz gráfica.
* **Salida:** Emite los resultados operativos mediante la instrucción `print()`, la cual es interceptada de manera transparente por la GUI para mostrar el registro en tiempo real.

---

## 🛠️ Catálogo Completo de Módulos

| # | Módulo | Propósito y Uso | Parámetro de Entrada (`param`) | Información que Entrega |
| --- | --- | --- | --- | --- |
| 1 | **Port Scanner** | Detectar servicios expuestos en puertos TCP específicos. | IP u Host (ej. `127.0.0.1`) | Puertos abiertos, cerrados o filtrados y tiempo de respuesta. |
| 2 | **Ping Sweep** | Descubrir dispositivos activos dentro de una subred local. | Subred CIDR (ej. `192.168.1.0/24`) | Direcciones IP de los hosts que responden al protocolo ICMP. |
| 3 | **Banner Grabbing** | Identificar la versión exacta de un servicio de red. | `IP:PUERTO` (ej. `192.168.1.1:80`) | Cadena de texto o versión del software que expone el servicio. |
| 4 | **Directory Buster** | Localizar archivos y rutas ocultas en servidores web. | URL base (ej. `http://testphp.vulnweb.com`) | Rutas con códigos de estado HTTP válidos (200 OK, 403 Forbidden). |
| 5 | **HTTP Headers** | Auditar las políticas de seguridad perimetral web de OWASP. | URL o Dominio (ej. `google.com`) | Estado de cabeceras clave (HSTS, CSP, X-Frame-Options, etc.). |
| 6 | **Password Checker** | Evaluar la robusticidad de claves frente a ataques de fuerza bruta. | Cadena de texto (la contraseña a evaluar) | Puntuación de seguridad, nivel de fortaleza y sugerencias de mejora. |
| 7 | **DNS Enum** | Consultar registros de infraestructura de nombres de dominio. | Dominio objetivo (ej. `google.com`) | Direcciones IP asociadas (Registros A) y servidores de correo (MX). |
| 8 | **Hash Checker** | Validar la integridad de archivos mediante huellas criptográficas. | Ruta absoluta o relativa al archivo | Hash criptográfico calculado en formato SHA-256 hexadecimal. |
| 9 | **Sniffer** | Capturar y analizar tráfico de red en tiempo real. | Cantidad de paquetes (ej. `5`) | Resumen de tramas y protocolos de red interceptados. |
| 10 | **Defense (Hardening)** | Proveer directrices técnicas para mitigar vulnerabilidades. | *Opcional* (No requiere parámetros) | Buenas prácticas recomendadas contra vectores de ataque comunes. |
| 11 | **SSL Checker** | Comprobar la validez y vigencia de certificados digitales. | Dominio o URL (ej. `google.com`) | Entidad emisora, fecha de expiración y estado de cifrado TLS. |
| 12 | **Subdomain Scanner** | Descubrir subdominios expuestos de un objetivo corporativo. | Dominio raíz (ej. `google.com`) | Subdominios activos detectados en la red pública. |
| 13 | **Traceroute** | Mapear la ruta de saltos de red que realizan los paquetes IP. | Destino (ej. `google.com` o IP) | Secuencia de routers y latencias intermedias hasta el destino. |
| 14 | **Utils Net** | Validar formatos de red y obtener configuraciones locales. | Dirección IP a validar (ej. `192.168.1.1`) | Dirección IP local activa y booleano de validez del formato IP. |

---

## 🔍 Análisis Profundo de Cabeceras HTTP (`http_headers`)

El módulo de auditoría de cabeceras HTTP evalúa los siguientes controles de seguridad recomendados por OWASP:

* **Strict-Transport-Security (HSTS):**
* **Qué indica:** Si está ausente, el sitio web permite conexiones HTTP sin cifrar (o fuerza al usuario a pasar por un desvío inicial). Si está presente, obliga al navegador a usar siempre conexiones HTTPS seguras.


* **Content-Security-Policy (CSP):**
* **Qué indica:** Es una de las defensas más potentes. Controla desde qué dominios el navegador tiene permitido cargar recursos (scripts, imágenes, estilos). Su ausencia deja la puerta más abierta a ataques de tipo Inyección de Código (XSS).


* **X-Frame-Options:**
* **Qué indica:** Evita ataques de Clickjacking, impidiendo que la página web sea cargada dentro de un marco (`iframe`) malicioso en otro sitio para engañar al usuario y hacer clic sin saberlo.


* **X-Content-Type-Options:**
* **Qué indica:** Evita que el navegador interprete archivos con un formato distinto al declarado (previene que archivos maliciosos subidos por un atacante se ejecuten como código ejecutable por el navegador).


* **X-XSS-Protection:**
* **Qué indica:** Activa el filtro interno del navegador contra ataques de Cross-Site Scripting reflejado (aunque los navegadores modernos manejan esto de formas más avanzadas, sigue siendo una capa clásica).



---

## 📦 Requisitos e Instalación

1. **Clonar o descargar el repositorio.**
2. **Instalar las dependencias ejecutando:**
```bash
pip install -r requirements.txt

```


*(Nota: Herramientas de capa 2 como el Sniffer basado en Scapy pueden requerir privilegios de administrador/root en tu sistema operativo).*

---

## ▶️ Instrucciones de Ejecución

Para iniciar la aplicación gráfica completa con todas las herramientas integradas:

```bash
python tkinter_app.py

```

"""

with open("README.md", "w", encoding="utf-8") as f:
f.write(complete_readme)

print("Complete README.md successfully created.")

```

```text?code_stdout&code_event_index=1
Complete README.md successfully created.

