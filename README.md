# websena
Web Bienestar al aprendiz - SENA CTMA
Abre una terminal o línea de comandos en tu sistema operativo.

Navega hasta la carpeta de tu proyecto Django utilizando el comando cd. Por ejemplo, si tu proyecto se encuentra en la carpeta ~/misitio, puedes navegar a esa carpeta escribiendo:

bash
Copy code
cd ~/misitio
Crea un entorno virtual de Python utilizando el siguiente comando:
Copy code
python -m venv venv
Este comando creará un nuevo directorio llamado venv en tu proyecto, donde se almacenarán todos los archivos y librerías del entorno virtual.

Activa el entorno virtual utilizando el siguiente comando:
En sistemas operativos Windows:
Copy code
venv\Scripts\activate
En sistemas operativos Linux o macOS:
bash
Copy code
source venv/bin/activate
Una vez que hayas activado el entorno virtual, verás el nombre del entorno virtual aparecer al principio de tu línea de comandos, lo que indica que estás trabajando en ese entorno aislado. Por ejemplo, si llamaste a tu entorno virtual venv, deberías ver algo así:

mathematica
Copy code
(venv) C:\Users\usuario\misitio>
Ahora puedes instalar las librerías especificadas en tu archivo requirements.txt utilizando el comando pip que mencioné anteriormente:
Copy code
pip install -r requirements.txt
Una vez que hayas completado la instalación de las librerías, estarás listo para trabajar en tu proyecto Django dentro de tu entorno virtual aislado.

Cuando hayas terminado de trabajar en tu proyecto y quieras salir del entorno virtual, simplemente escribe el siguiente comando en la línea de comandos:
Copy code
deactivate
