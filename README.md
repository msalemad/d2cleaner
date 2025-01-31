# 🌟 Destiny 2 Cleaner 🌟

Destiny 2 Cleaner es una aplicación que permite gestionar el inventario de tus personajes en Destiny 2, moviendo objetos a la bóveda de manera automática.

## ✨ Características

- 📋 Obtener los IDs de los personajes.
- 📦 Mover objetos del inventario a la bóveda.
- 🛡️ Desequipar armas, armaduras o todos los objetos de un personaje.

## 🛠️ Requisitos

- 🐍 Python 3.x
- 📦 Biblioteca `requests`

## 🚀 Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tu_usuario/d2cleaner.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd d2cleaner
    ```
3. Instala las dependencias:
    ```bash
    pip install requests
    ```

## ⚙️ Configuración

1. Obtén tu API Key de Bungie y reemplaza `'your_api_key_here'` en el archivo `d2cleaner.py`:
    ```python
    API_KEY = 'your_api_key_here'
    ```
2. Reemplaza `'your_membership_id_here'` con tu ID de membresía en el archivo `d2cleaner.py`:
    ```python
    membership_id = 'your_membership_id_here'
    ```

## 📚 Uso

1. Ejecuta el script:
    ```bash
    python d2cleaner.py
    ```
2. Sigue las instrucciones en pantalla para seleccionar la clase del personaje y la operación a realizar.

## 🖥️ Compatibilidad

### Windows

Para ejecutar Destiny 2 Cleaner en Windows, asegúrate de tener Python instalado y sigue los pasos de instalación y configuración mencionados anteriormente.

### Android

Puedes ejecutar Destiny 2 Cleaner en Android utilizando Termux o Pydroid:

#### Termux

1. Instala Termux desde la Play Store.
2. Abre Termux y actualiza los paquetes:
    ```bash
    pkg update && pkg upgrade
    ```
3. Instala Python:
    ```bash
    pkg install python
    ```
4. Clona el repositorio y navega al directorio del proyecto:
    ```bash
    git clone https://github.com/tu_usuario/d2cleaner.git
    cd d2cleaner
    ```
5. Instala las dependencias:
    ```bash
    pip install requests
    ```
6. Configura y ejecuta el script como se describe en la sección de configuración y uso.

#### Pydroid

1. Instala Pydroid desde la Play Store.
2. Abre Pydroid y abre el archivo `d2cleaner.py`.
3. Instala las dependencias desde el terminal de Pydroid:
    ```bash
    pip install requests
    ```
4. Configura y ejecuta el script como se describe en la sección de configuración y uso.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## 📧 Contacto

Para cualquier consulta, puedes contactarme en [tu_email@example.com](mailto:tu_email@example.com).