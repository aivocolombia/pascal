# Arquitectura de Pascal AI

## Visión General del Sistema
Pascal AI implementa una arquitectura basada en eventos y microservicios, utilizando n8n como plataforma principal de orquestación. El sistema está diseñado para manejar interacciones en tiempo real con usuarios a través de Telegram, procesando lenguaje natural y gestionando datos de propiedades inmobiliarias.

## Componentes del Sistema

### 1. Capa de Interfaz de Usuario
- **Telegram Bot**
  - Punto de entrada principal para interacciones con usuarios
  - Manejo de mensajes entrantes y salientes
  - Formato de respuestas personalizado

### 2. Capa de Procesamiento
- **OpenAI Model**
  - Modelo: GPT
  - Procesamiento de lenguaje natural
  - Interpretación de intenciones del usuario
  - Generación de respuestas contextuales

- **AI Agent**
  - Gestión de flujo conversacional
  - Lógica de negocio inmobiliaria
  - Sistema de toma de decisiones
  - Validación de datos

### 3. Capa de Memoria y Estado
- **Simple Memory**
  - Almacenamiento de contexto conversacional
  - Gestión de sesiones por usuario
  - Buffer de ventana deslizante
  - Persistencia temporal de datos

### 4. Capa de Datos
- **Base de Datos PostgreSQL**
  - Tabla de leads
  - Historial de interacciones
  - Datos de propiedades
  - Registros de citas

## Flujos de Datos

1. **Flujo de Mensajes**
```
Usuario -> Telegram -> n8n Trigger -> AI Agent -> Procesamiento -> Respuesta -> Usuario
```

2. **Flujo de Gestión de Leads**
```
Datos Usuario -> AI Agent -> Validación -> Base de Datos -> Actualización Estado
```

3. **Flujo de Agendamiento**
```
Solicitud -> Validación Disponibilidad -> Creación Evento -> Confirmación
```

## Integraciones Principales

### 1. OpenAI API
- Endpoint: API de OpenAI
- Autenticación: Token API
- Uso: Procesamiento de lenguaje natural

### 2. Telegram Bot API
- Webhook configurado para n8n
- Manejo de actualizaciones en tiempo real
- Procesamiento de comandos específicos

### 3. Base de Datos
- Conexión PostgreSQL
- Esquemas principales:
  - leads
  - properties
  - appointments

## Consideraciones de Seguridad

1. **Autenticación**
   - Tokens seguros para APIs
   - Credenciales encriptadas en n8n

2. **Datos Sensibles**
   - Encriptación de información personal
   - Manejo seguro de credenciales
   - Logs sanitizados

3. **Rate Limiting**
   - Control de solicitudes a APIs
   - Protección contra spam
   - Gestión de cuotas

## Monitoreo y Logging

- Registro de interacciones
- Métricas de rendimiento
- Alertas de errores
- Seguimiento de uso de API

## Escalabilidad

El sistema está diseñado para escalar horizontalmente:
- Múltiples instancias de n8n
- Balanceo de carga
- Caché distribuido
- Particionamiento de base de datos 