import sys
import os

# Configurar la ruta absoluta para reconocer el paquete 'src'
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

import tkinter as tk
from gui.tkinter_app import NetworkToolkitApp

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkToolkitApp(root)
    root.mainloop()