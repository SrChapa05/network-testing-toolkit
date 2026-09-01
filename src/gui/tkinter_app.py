import tkinter as tk
from tkinter import ttk, scrolledtext
import sys
import os
import threading
import io
import contextlib

# Asegurar acceso a los módulos de la carpeta src
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.abspath(os.path.join(current_dir, '..'))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Importar los 14 módulos de manera segura
try:
    from modules import (
        scanner, ping_sweep, ssl_checker, traceroute,
        arp_scanner, http_headers, banner_grabber, dir_buster,
        password_checker, subdomain_scanner, sniffer, 
        security, defense, utils_net
    )
except ImportError as e:
    print(f"[Aviso] Algunos módulos faltan o tienen otro nombre: {e}")

def ejecutar_capturando_salida(func_modulo, *args, **kwargs):
    """Captura automáticamente todos los print() de la función del módulo."""
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        try:
            func_modulo(*args, **kwargs)
        except Exception as e:
            print(f"\n[Error de ejecución] {e}")
    return buffer.getvalue()

class NetworkToolkitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("All-in-One Network Security Toolkit (14 Módulos)")
        self.root.geometry("1100x750")

        style = ttk.Style()
        style.theme_use('clam')

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Mapeo completo de los 14 módulos del toolkit
        self.tools_config = [
            {
                "title": "Escáner de Puertos",
                "label": "Objetivo (IP o Dominio):",
                "module_func": getattr(scanner, 'run', None)
            },
            {
                "title": "Ping / ARP Sweep",
                "label": "Subred (ej. 192.168.1.0/24):",
                "module_func": getattr(ping_sweep, 'run', None)
            },
            {
                "title": "Seguridad SSL",
                "label": "URL Objetivo (ej. https://example.com):",
                "module_func": getattr(ssl_checker, 'run', None)
            },
            {
                "title": "Traceroute",
                "label": "Host o Dominio:",
                "module_func": getattr(traceroute, 'run', None)
            },
            {
                "title": "ARP Scanner",
                "label": "Interfaz o Red (ej. eth0 / 192.168.1.0/24):",
                "module_func": getattr(arp_scanner, 'run', None)
            },
            {
                "title": "Cabeceras HTTP",
                "label": "URL Objetivo (ej. https://example.com):",
                "module_func": getattr(http_headers, 'run', None)
            },
            {
                "title": "Banner Grabber",
                "label": "IP y Puerto (ej. 192.168.1.1:80):",
                "module_func": getattr(banner_grabber, 'run', None)
            },
            {
                "title": "Buscador de Directorios",
                "label": "URL Base (ej. http://example.com):",
                "module_func": getattr(dir_buster, 'run', None)
            },
            {
                "title": "Validador de Contraseñas",
                "label": "Archivo o Credencial:",
                "module_func": getattr(password_checker, 'run', None)
            },
            {
                "title": "Escáner de Subdominios",
                "label": "Dominio principal (ej. example.com):",
                "module_func": getattr(subdomain_scanner, 'run', None)
            },
            {
                "title": "Sniffer de Red",
                "label": "Interfaz de red (ej. Wi-Fi / eth0):",
                "module_func": getattr(sniffer, 'run', None)
            },
            {
                "title": "Análisis de Seguridad",
                "label": "Objetivo (IP o Host):",
                "module_func": getattr(security, 'run', None)
            },
            {
                "title": "Módulo de Defensa",
                "label": "Parámetro o Regla:",
                "module_func": getattr(defense, 'run', None)
            },
            {
                "title": "Utilidades de Red",
                "label": "Host o Parámetro:",
                "module_func": getattr(utils_net, 'run', None)
            }
        ]

        self.init_dynamic_tabs()

    def init_dynamic_tabs(self):
        for tool in self.tools_config:
            tab = ttk.Frame(self.notebook)
            self.notebook.add(tab, text=tool["title"])

            lbl = ttk.Label(tab, text=tool["label"], font=("Arial", 10, "bold"))
            lbl.pack(anchor="w", padx=15, pady=5)

            entry = ttk.Entry(tab, width=50)
            entry.pack(anchor="w", padx=15, pady=5)

            output = scrolledtext.ScrolledText(tab, wrap=tk.WORD, width=115, height=22, bg="#1e1e1e", fg="#00ff00", insertbackground="white")
            output.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

            btn = ttk.Button(
                tab, 
                text=f"Ejecutar {tool['title']}", 
                command=lambda e=entry, o=output, f=tool["module_func"], t=tool["title"]: self.execute_task(f, e, o, t)
            )
            btn.pack(anchor="w", padx=15, pady=5, before=output)

    def run_in_thread(self, target_func, *args):
        thread = threading.Thread(target=target_func, args=args)
        thread.daemon = True
        thread.start()

    def execute_task(self, module_func, entry, output, tool_name):
        param = entry.get().strip()
        if not param:
            output.insert(tk.END, "[!] Introduce un parámetro válido.\n")
            return
        
        output.delete(1.0, tk.END)
        output.insert(tk.END, f"[*] Ejecutando [{tool_name}] con objetivo: {param}...\n\n")
        
        def task():
            if module_func is None:
                resultado = "[!] Advertencia: La función 'run' no está definida en este módulo o el archivo no se encontró."
            else:
                resultado = ejecutar_capturando_salida(module_func, param)
            
            output.after(0, lambda: output.insert(tk.END, f"{resultado}\n[+] [{tool_name}] Finalizado.\n"))

        self.run_in_thread(task)

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkToolkitApp(root)
    root.mainloop()