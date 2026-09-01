# network-testing-toolkit
proyecto obsesivo y enfermo de kit de herremientas de testeo de redes

"pip install -r requirements.txt" para instalar las librerias


http_headers:
Strict-Transport-Security (HSTS):

Qué indica: Si está ausente, el sitio web permite conexiones HTTP sin cifrar (o fuerza al usuario a pasar por un desvío inicial). Si está presente, obliga al navegador a usar siempre conexiones HTTPS seguras.

Content-Security-Policy (CSP):

Qué indica: Es una de las defensas más potentes. Controla desde qué dominios el navegador tiene permitido cargar recursos (scripts, imágenes, estilos). Su ausencia deja la puerta más abierta a ataques de tipo Inyección de Código (XSS).

X-Frame-Options:

Qué indica: (Apareció como Presente en Google). Evita ataques de Clickjacking, impidiendo que la página web sea cargada dentro de un marco (iframe) malicioso en otro sitio para engañar al usuario y hacer clic sin saberlo.

X-Content-Type-Options:

Qué indica: Evita que el navegador interprete archivos con un formato distinto al declarado (previene que archivos maliciosos subidos por un atacante se ejecuten como código ejecutable por el navegador).

X-XSS-Protection:

Qué indica: (Apareció como Presente). Activa el filtro interno del navegador contra ataques de Cross-Site Scripting reflejado (aunque los navegadores modernos manejan esto de formas más avanzadas, sigue siendo una capa clásica).