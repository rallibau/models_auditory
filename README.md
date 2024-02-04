# Iniciar el entorno
### Constuir
make build
### INICIAR
make env-start


# Crear usuario administrador

### Conectarse al shell del contenedor
make bash
### Crear el usuario
python manage.py createsuperuser --username admin --email admin@example.com

# Reiniciar la base de datos
make reboot-database

# Urls del sitema:
### Documentación
http://localhost:8000/api/schema/swagger-ui/
### Incio
http://localhost:8000/