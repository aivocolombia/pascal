# Pascal AI - Asistente Inmobiliario Digital

## Descripción General
Pascal AI es un asistente inmobiliario digital implementado en n8n que ayuda a los usuarios a encontrar propiedades en Colombia para compra o arriendo. El sistema está diseñado para interactuar a través de Telegram y proporcionar una experiencia personalizada en la búsqueda de inmuebles incluyendo agentamiento de citas y guardando los datos del lead.

## Características Principales
- Búsqueda personalizada de propiedades
- Agendamiento automático de citas
- Gestión de leads
- Integración con Telegram
- Sistema de memoria conversacional
- Validación de disponibilidad horaria

## Requisitos Técnicos
- n8n (versión recomendada: última estable)
- Cuenta de OpenAI API
- Bot de Telegram
- Base de datos PostgreSQL

## Estructura del Sistema
```
pascal/
├── Pascal_Ai.json         # Flujo principal de n8n
├── README.md             # Documentación principal
├── ARCHITECTURE.md       # Documentación de arquitectura
└── MANUAL.md            # Manual de implementación
```

## Componentes Principales
1. **OpenAI Model**: Motor de procesamiento de lenguaje natural
2. **AI Agent**: Agente conversacional principal
3. **Simple Memory**: Sistema de memoria conversacional
4. **Telegram Trigger**: Manejador de eventos de Telegram
5. **Database Integration**: Sistema de gestión de leads

## Configuración Inicial
1. Importar el flujo `Pascal_Ai.json` en n8n
2. Configurar las credenciales necesarias:
   - OpenAI API
   - Telegram Bot Token
   - Credenciales de base de datos
3. Activar el workflow

## Documentación Adicional
- Ver [ARCHITECTURE.md](./ARCHITECTURE.md) para detalles técnicos
- Ver [MANUAL.md](./MANUAL.md) para guía de implementación


## Licencia
Derechos reservados - Pascal AI 