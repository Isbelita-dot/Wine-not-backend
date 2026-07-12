# Arquitectura

El proyecto utiliza una arquitectura hexagonal para mantener una separación clara entre la lógica de negocio y la infraestructura.

```
src
│
├── category
│   ├── application
│   ├── domain
│   └── infrastructure
│
├── feedback
│   ├── application
│   ├── domain
│   └── infrastructure
│
├── wine
│   ├── application
│   ├── domain
│   └── infrastructure
│
└── shared
    ├── config
    └── infrastructure
```

---

## Capas

### Domain

- Entidades
- Interfaces
- Reglas de negocio

### Application

- Casos de uso
- Servicios

### Infrastructure

- Base de datos
- Repositorios
- API REST
- Modelos ORM

### Shared

- Configuración
- Conexión con la base de datos
- Utilidades comunes

---

## Ventajas

- Bajo acoplamiento
- Alta cohesión
- Fácil mantenimiento
- Escalabilidad
- Código reutilizable
- Separación de responsabilidades