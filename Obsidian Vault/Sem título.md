```mermaid
graph TD
    A[1. CLARUS MVP] --> B[1.1 Planejamento & UX/UI]
    A --> C[1.2 Infraestrutura & Ingestão]
    A --> D[1.3 Integração de IA]
    A --> E[1.4 Notificações & Painel]
    A --> F[1.5 Testes & Deploy]

    B --> B1[1.1.1 Requisitos e Negócio]
    B --> B2[1.1.2 Arquitetura de Prompts]
    B --> B3[1.1.3 UI Design - Painel]

    C --> C1[1.2.1 Setup Cloud & DB]
    C --> C2[1.2.2 Webhook Ingestão]
    C --> C3[1.2.3 Upload CSV]

    D --> D1[1.3.1 Integração API Gemini]
    D --> D2[1.3.2 Engenharia de Prompts]
    D --> D3[1.3.3 Algoritmo de Anomalias]

    E --> E1[1.4.1 Conexão MS Teams]
    E --> E2[1.4.2 Cards de Alerta Teams]
    E --> E3[1.4.3 Tela Config. Web]

    F --> F1[1.5.1 Testes e Custo de API]
    F --> F2[1.5.2 Deploy Produção]
    F --> F3[1.5.3 Piloto & Onboarding]
    
    