# app
Configuración

Requisitos

1-. Instalar Python 3.10 como mínimo.

    sudo apt update
    sudo apt install python3.11
    python3 --version

2-. Descargar el proyecto.

3-. Con pip se debe ejecutar el siguiente comando
(en el caso de no tener pip ver el siguiente link https://pip.pypa.io/en/stable/installation/)

4-. Con este comando se instalaran las librerías que usa la aplicación. 

    pip install -r requirements.txt
    
5-. instalar postgresql

# Instalación de Git

    sudo apt update
    sudo apt install git
    git --version

# Instalación de Samba  (paso opcional)

    sudo apt-get install samba
    sudo systemctl status nmbd

> Configuración del servidor de samba

    sudo mkdir /samba
    sudo nano /etc/samba/smb.conf

> Compartir carpeta

    [html]
    comment = Carpeta apache
    path = /var/www/html
    guest ok = yes
    writable = yes
    browsable = yes
    create mask = 0666
    directory mask = 0777
    public = yes

# Instalar y configurar virtualenv (opcional)

> Se debe instalar, para eso ir al siguiente link: https://pypi.org/project/virtualenv/
> Se debe copiar
    pip install virtualenv
    
  Luego pegarlo en el terminal, de esa forma se instala la libreria de virtualenv (entorno virtual)

> Ir a la raiz del proyecto desde la terminal y escribir lo siguiente:

    virtualenv venv
    
  Esto creara una carpeta con un entorno virtual el cual se debe activar de la siguiente manera:
    
    cd /path/raiz/proyecto/venv/bin/
    source activate
  
  (buscar comandos para windows)
  
# Instalar y configurar django, PostgreSQL en servidor Ubuntu Server
        
> Actualizar la lista de paquetes de Ubuntu e instalar los paquetes necesarios:
    
    sudo apt-get update
    sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
        
> Crea un entorno virtual utilizando venv:
    
    sudo apt-get install python3-venv
    python3 -m venv myenv
    source myenv/bin/activate
    
> Instala Django dentro del entorno virtual:

    pip install django
    
> Instala Django dentro del entorno virtual:

    sudo -u postgres psql
    CREATE DATABASE myproject;
    CREATE USER myuser WITH PASSWORD 'mypassword';
    ALTER ROLE myuser SET client_encoding TO 'utf8';
    ALTER ROLE myuser SET default_transaction_isolation TO 'read committed';
    ALTER ROLE myuser SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE myproject TO myuser;

> Instala Django dentro del entorno virtual:

    django-admin startproject myproject

> Instala Django dentro del entorno virtual:

    python manage.py runserver 127.0.0.1:8000
    
Ahora se deberías poder acceder al proyecto Django desde cualquier navegador visitando http://127.0.0.1:8000


