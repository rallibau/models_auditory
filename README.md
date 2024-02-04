# ARQUITECTURA
Para la realización de este ejercicio se ha optado por la implementación de una arquitectura limpia (hexagonal) que nos permita mantener aislada la implementación de los dos agregados de ejemplo (one, two), de la gestión de los datos pertenecientes a la auditoría.

# DESARROLLO
Este ejercicio se ha desarrollado mediante TDD. Los "happy paths" tienen pruebas "end to end", pero se ha optado por test unitarios para la mayoría de la cobertura. Ciertas partes del código, como las vistas, se dejan sin test por optimizar el tiempo.


En este ejemplo, la ejecución de cualquiera de los casos de uso que desembocan en la modificación de la persistencia, provaca la publicación de un evento. Como reacción a este evento, el módulo de auditoría persiste un registro con los datos anteriores y posteriores al cambio.


# EVOLUCIÓN FUTURA
Esta es una primera aproximación de la solución. En caso de llevar esta solución a producción en un entorno altamente demandante:
1. Lo primero sería el despliegue de un broker delegado de mensajería(rabbit,kafka...), y cambiar el bush en memoria por un bush que dialogue con este broker.
2. Elevar la gestión de auditoría a un servicio independiente, este servicio consume los eventos del módulo principal.
3. Persistir los datos de auditoría mediante una infra optimizada para ello. Dado que no son datos no relacionales podemos optar por mongo , elasticsearch, etc.

# COSAS QUE FALTAN
1. Falta la inyección de dependencias. Como es un ejemplo y su implementación es trivial, dejo de lado la implementación de la inyección de dependencias.
2. Paginación de las vistas. Se deja de lado por falta de tiempo.
3. Se toman atajos en el TDD para llegar a los objetivos propuestos.

# Iniciar el entorno
### Constuir
make build
### INICIAR
make env-start
### LANZAR TEST
make test


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