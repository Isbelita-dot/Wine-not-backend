# Wine Not - Project Context

## Objetivo

Desarrollar un e-commerce de vinos para la asignatura Full Stack.

## Tecnologías

Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pytest

Frontend
- HTML
- CSS
- JavaScript
- Axios

## Arquitectura Backend

app/
    api/
    core/
    crud/
    db/
    models/
    schemas/
    services/

## Recursos

Category

Wine

Feedback

## Relaciones

Category 1:N Wine

Wine 1:N Feedback

## Convenciones

Modelos -> PascalCase

Schemas -> PascalCase

Archivos -> snake_case

Endpoints -> plural

CRUD separado de Services

Toda lógica de negocio va en Services.

No escribir consultas SQL en los endpoints.

Los endpoints solo reciben la petición y llaman al Service.

## Gitflow

main

develop

feature/*