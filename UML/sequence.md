```mermaid
sequenceDiagram
    participant User
    participant UI as Web UI
    participant BE as Backend
    participant API as Extension API
    participant DB as Extension DB

    User->>UI: Request Feature Extension
    UI->>BE: Process Request
    BE->>API: Call Extension Endpoint
    API->>DB: Query Extension Data
    DB-->>API: Return Results
    API-->>BE: Processed Data
    BE-->>UI: ResponsesequenceDiagram
    participant User
    participant UI as Web UI
    participant BE as Backend
    participant API as Extension API
    participant DB as Extension DB

    User->>UI: Request Feature Extension
    UI->>BE: Process Request
    BE->>API: Call Extension Endpoint
    API->>DB: Query Extension Data
    DB-->>API: Return Results
    API-->>BE: Processed Data
    BE-->>UI: Response
    UI-->>User: Display Results

    UI-->>User: Display Results



```