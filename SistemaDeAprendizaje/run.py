"""
Punto de Entrada de la Aplicación - LogicWeb UTA
Inicializa la factoría del servidor web y expone el servicio en el puerto 5000.
"""

import os
from app import create_app

app = create_app()
app.config["ROOT_DIR"] = os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    import os
    # Render asignará un puerto dinámico mediante la variable de entorno PORT.
    # Si no existe (como en tu computadora), usará por defecto el puerto 5000.
    port = int(os.environ.get("PORT", 5000))
    
    # Importante: host="0.0.0.0" permite que el servidor escuche peticiones externas en Render.
    # debug=False se recomienda en producción, pero puedes mantenerlo en True si lo deseas.
    app.run(host="0.0.0.0", port=port, debug=False)