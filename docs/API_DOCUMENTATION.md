# API Documentation

## Base URL

```
http://127.0.0.1:8000
```

---

## Recursos

### Wines

| Método | Endpoint | Descripción |
|---------|----------|-------------|
| GET | /wines | Obtener todos los vinos |
| GET | /wines/{id} | Obtener un vino |
| POST | /wines | Crear vino |
| PUT | /wines/{id} | Actualizar vino |
| DELETE | /wines/{id} | Eliminar vino |

---

### Categories

| Método | Endpoint |
|---------|----------|
| GET | /categories |

---

### Feedback

| Método | Endpoint |
|---------|----------|
| GET | /feedback |
| POST | /feedback |

---

## Formato

Todas las respuestas utilizan JSON.

Ejemplo

```json
{
    "id":1,
    "name":"Rioja Reserva",
    "price":24.95
}
```

---

## Documentación interactiva

Swagger

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```