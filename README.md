# Prueba Técnica Ridery

Implemetación de prueba técnica implementando una API que posteriormente es consumida por Odoo el cual se encarga de registrar vehículos asociados a contactos/conductores.

# Configuración

1. Tener docker y docker compose instalado.
2. Para configurar la contraseña de la base de datos debemos ubicar el archivo conf que se enecuentra en la ruta de [odoo/config/odoo.conf](https://github.com/VizMan0616/ridery-technical-test/blob/main/odoo/config/odoo.conf) allí debemos ubicar el parámetro `admin_passwd` y asignamos la contraseña que queramos para crear una base de datos al momento de levantar un ambiente de odoo.
3. Se debe crear un archivo `.env` con los mismos argumentos que contiene el [.env.example](https://github.com/VizMan0616/ridery-technical-test/blob/main/.env.example) y de esta forma asignar los puertos para cada uno de los servicios de docker.
4. Para poder levantar el ambiente de `odoo` junto a su base de datos y el API que registra los vehículos se debe ejecutar el siguiente comando:
    ```bash
    docker compose up -d
    ```
    _Se agrega el argumento `-d` (detach) para poder correr los 3 servicios de fondo._
5. Para poder visualizar los logs del servicio de la API y ver cómo se imprimen los vehículos cargados dentro del endpoint se debe ejecutar el siguiente comando:
    ```bash
    docker compose logs -f --tail 10 service
    ```
    _Esto permite que se puedan ver los logs del servicio de FastAPI y uvicorn, además para no mostrar todo el historial, solo se empiezan a visualizar a partir de los últimos 10 logs._

### Uso

El módulo principal de Gestión de Vehículos tiene como propósito poder registrar vehículos, las marcas de estos mismos y poder asociarlos a un conductor al momento de ser registrado dentro del sistema.

Adicional a esto existe un módulo auxiliar que permite guardar las respuestas obtenidas al momento de consumir una API o microservicio. El módulo de Gestión de Vehículos se conecta a este, para que cada vez que se envíen los vehículos correspondientes de cada conductor pueda llevar el control de las respuestas obtenidas al consumir la API.

  - __Configuración:__

    Para un uso adecuado se debe hacer lo siguiente:

    - Posterior a la instalación el módulo aparecerá unicamente para aquellos usuarios con permiso de administrador para poder gestionarlo. Para ello debemos ir a `[Ajustes] > [Usuarios y Compañías] > [Usuarios] > Escogemos usuario > [Gestión de Vehículos] > Administrador`. Esto permitirá poder acceder al módulo y tener la posibilidad de crear vehículos y marcas.
    - Para definir que un contacto es conductor y que pueda aparecer al momento de registrar un vehículo hay que ir a `[Contactos] > Escoger un contacto > [Es un Conductor]`
    - Se deben configurar las marcas de vehículos puesto que es un campo requerido, para ello vamos a `[Vehículos] > [Vehículos] > [Marcas]`.
  - Para poder enviar vehículos al API tenemos que ir a `[Vehículos] > [Vehículos] > [Conductores] > Escogemos un conductor > [Enviar Vehículos]`.
  - Para poder visualizar los vehículos asociados a un conductor tenemos que ir a `[Vehículos] > [Vehículos] > [Conductores] > Escogemos un conductor > [Vehículos]`. Adicionalmente el statbutton en la ficha del conductor nos mostrará la cantidad de vehículos asociados a este.

Video explicativo: [Video](https://komododecks.com/recordings/wqnxshWcLxPspIej33Hv)

# Herramientas utilizadas
  - [Docker](https://www.docker.com/)
  - [Git](https://git-scm.com/)
  - [Visual Studio Code](https://code.visualstudio.com/)