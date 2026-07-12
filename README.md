# 🍷 Wine Not Backend

Backend de la aplicación **Wine Not**, un e-commerce de vinos desarrollado como proyecto Full Stack utilizando FastAPI y arquitectura hexagonal.

---

## Tecnologías

- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Pytest

---

## Arquitectura

El proyecto sigue una arquitectura hexagonal para separar la lógica de negocio de la infraestructura.

```
src
├── category
├── feedback
├── wine
└── shared
```

---

## Funcionalidades

- CRUD completo de vinos
- Gestión de categorías
- Gestión de opiniones
- Validación de datos
- Respuestas JSON
- Códigos HTTP apropiados
- Documentación automática con Swagger

---

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/Isbelita-dot/Wine-not-backend.git
```

### Entrar al proyecto

```bash
cd Wine-not-backend
```

### Crear entorno virtual

```bash
python -m venv venv
```

### Activar entorno virtual

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar la aplicación

```bash
uvicorn src.main:app --reload
```

---

## Documentación

Swagger

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# Documentación de la API

La API está documentada automáticamente mediante Swagger UI y ReDoc.

## Swagger

![Swagger](docs/swagger/swagger-home.png)

## Endpoints de Wines

![Wines](docs/swagger/swagger-wines.png)

## Endpoints de Categories

![Categories](docs/swagger/swagger-categories.png)

## Endpoints de Feedback

![Feedback](docs/swagger/swagger-feedback.png)

## Testing

```bash
pytest
```

---

## Base de datos

SQLite

```
wine.db
```

---

## Autores

Isbel Hernandez, Jordi Galea, Edgar Soriano.