# Base de Datos

La aplicación utiliza SQLite mediante SQLAlchemy como ORM.

---

## Tabla Wines

| Campo | Tipo |
|--------|------|
| id | Integer |
| name | String |
| winery | String |
| country | String |
| category_id | Integer |
| description | String |
| price | Float |
| stock | Integer |
| image_url | String |

---

## Tabla Categories

| Campo | Tipo |
|--------|------|
| id | Integer |
| name | String |

---

## Tabla Feedback

| Campo | Tipo |
|--------|------|
| id | Integer |
| name | String |
| rating | Integer |
| comment | String |

---

## Relaciones

```
Category
    │
    └───────────< Wine

Wine
    │
    └─────────── Feedback
```

---

## ORM

El acceso a los datos se realiza mediante SQLAlchemy.

La inicialización de la base de datos se realiza utilizando:

```
Base.metadata.create_all(bind=engine)
```

---

## Persistencia

Motor de base de datos:

```
SQLite
```

Archivo:

```
wine.db
```