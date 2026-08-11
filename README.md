# 📋 Task Manager API — FastAPI

¡Bienvenido/a! Este proyecto es una API REST completa para la gestión de tareas, construida con **FastAPI** como parte de mi proceso de aprendizaje del framework, siguiendo el libro *"Primeros pasos con FastAPI"* de Andrés Cruz y ampliando sobre esa base con mis propias implementaciones.

La idea de este repo es mostrar un recorrido real: desde los fundamentos del framework hasta un backend con base de datos relacional, autenticación, testing y renderizado de vistas.

## 🚀 ¿Qué encontrarás en este proyecto?

### API REST completa (CRUD de tareas)
- Rutas `GET`, `POST`, `PUT`, `DELETE` para gestionar tareas, con validaciones de path (`Path()`) y de cuerpo (`Body()`)
- Creación de tareas tanto vía **JSON** como vía **formulario HTML** (`Form()`)
- Paginación de resultados
- Sistema de **tags** para asociar etiquetas a las tareas (relación muchos a muchos)

### Base de datos relacional
- Conexión a **MySQL** mediante **SQLAlchemy**
- Modelos con relaciones `One to Many` (Usuario → Tareas, Categoría → Tareas) y `Many to Many` (Tareas ↔ Tags)
- Inyección de la sesión de base de datos como dependencia en cada endpoint

### Validación de datos con Pydantic
- Esquemas separados para lectura y escritura (`Task`, `TaskRead`, `TaskWrite`)
- Validadores personalizados por campo (por ejemplo, nombres alfanuméricos)
- Ejemplos precargados en la documentación interactiva (Swagger) para facilitar las pruebas

### Autenticación
- Registro de usuarios con contraseñas hasheadas (`passlib` + `bcrypt`)
- Login con generación de token de acceso (`OAuth2PasswordBearer`)
- Rutas protegidas mediante dependencias de autenticación
- Logout con invalidación del token

### Manejo de archivos
- Distintas estrategias para subir archivos: como `bytes`, como `UploadFile`, y en lote (múltiples archivos)

### Vistas con Jinja2
- Renderizado de HTML del lado del servidor con herencia de templates
- Listado de tareas con formularios de creación y edición, tanto por envío tradicional como por `fetch()` en JavaScript

### Dependencias personalizadas
- Ejemplos de dependencias reutilizables (paginación)
- Protección de rutas a nivel de decorador con `dependencies=[Depends(...)]`
- Uso del patrón de dependencias como variable con `Annotated`

### Testing
- Suite de tests con `pytest` sobre los endpoints principales (usuarios y tareas)
- Uso de `TestClient` de FastAPI para probar la API sin necesidad de levantar el servidor

## 🛠️ Stack tecnológico

| Tecnología | Uso |
|---|---|
| **FastAPI** | Framework principal de la API |
| **SQLAlchemy** | ORM para la base de datos |
| **MySQL** | Base de datos relacional |
| **Pydantic** | Validación y serialización de datos |
| **Passlib (bcrypt)** | Hasheo seguro de contraseñas |
| **Jinja2** | Motor de plantillas para vistas HTML |
| **Uvicorn** | Servidor ASGI |
| **Pytest** | Testing automatizado |

## 📦 Cómo levantar el proyecto localmente

```bash
# 1. Clonar el repositorio
git clone https://github.com/Ivan-Porcari/fastapi_vtasks.git
cd fastapi_vtasks

# 2. Crear y activar el ambiente virtual
python -m venv venv
source venv/Scripts/activate    # Windows (Git Bash)
# o venv\Scripts\Activate.ps1   # Windows (PowerShell)
# o source venv/bin/activate    # Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar la conexión a la base de datos
# Editar la variable DATABASE_URL en database.py con tus credenciales de MySQL

# 5. Levantar el servidor
uvicorn api:app --reload
```

La documentación interactiva queda disponible en:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## 🧪 Correr los tests

```bash
pytest
```

## 📚 Sobre este proyecto

Este repositorio documenta mi proceso de aprendizaje de FastAPI, partiendo de una guía estructurada y expandiendo cada capítulo con implementaciones propias, resolución de errores reales y buenas prácticas de organización de código (separación en módulos, routers, esquemas y modelos). Lo mantengo como parte de mi portfolio para mostrar tanto el dominio técnico del framework como la capacidad de estructurar un proyecto backend de punta a punta.

---

📫 ¿Preguntas o sugerencias? No dudes en abrir un issue o contactarme.
