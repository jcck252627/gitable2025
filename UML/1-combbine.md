```mermaid
%% CAN NOT COMBINE THEM !!!!!!


%% ==========================
%% 1. Component Diagram - Extensible Web App
%% ==========================
flowchart TB
    %% Extensible Web App Component Model
    Client["Web Client"]
    UI["Web App UI\n(Front-End Layer)"]
    Backend["Web App Backend\n(Core Services)"]

    CoreAPI["Core API Service\n(Primary Endpoints)"]
    ExtAPI["Extension API\n«extensible component»"]

    CoreDB[("Core Database")]
    AddDB[("Additional Database\n«extension»")]

    Client --> UI
    UI --> Backend

    Backend --> CoreAPI
    Backend --> ExtAPI

    CoreAPI --> CoreDB
    ExtAPI --> AddDB


%% ==========================
%% 2. Use Case Diagram (Simulated)
%% ==========================
flowchart TB
    %% Actors and Use Cases
    User([User])
    Admin([Admin])

    UC1((Access Web App))
    UC2((Use Core API))
    UC3((Use Extension API))
    UC4((Query Core Database))
    UC5((Query Extension Database))

    User --> UC1
    UC1 --> UC2
    UC1 --> UC3

    UC2 --> UC4
    UC3 --> UC5

    Admin --> UC2
    Admin --> UC3


%% ==========================
%% 3. Sequence Diagram
%% ==========================
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
    BE-->>UI: Response
    UI-->>User: Display Results


%% ==========================
%% 4. Collaboration Diagram (Class Diagram Simulation)
%% ==========================
classDiagram
    class WebUI
    class Backend
    class ExtensionAPI
    class ExtensionDB

    WebUI --> Backend : request()
    Backend --> ExtensionAPI : callExtension()
    ExtensionAPI --> ExtensionDB : query()
    ExtensionDB --> ExtensionAPI : result()
    ExtensionAPI --> Backend : return()
    Backend --> WebUI : response()


%% ==========================
%% 5. Statechart Diagram - Extension API Module
%% ==========================
stateDiagram-v2
    [*] --> Initialized
    Initialized --> Waiting : registers routes
    Waiting --> Processing : receives request
    Processing --> Waiting : response sent
    Processing --> Error : exception raised
    Error --> Waiting : recover and reset


%% ==========================
%% 6. Activity Diagram - Extended Feature Flow
%% ==========================
flowchart TD
    Start([Start]) --> Trigger{Feature Extension Requested?}

    Trigger -->|Yes| Process[Process Request]
    Trigger -->|No| End1([End])

    Process --> CallAPI[Call Extension API]
    CallAPI --> QueryDB[Query Extension Database]
    QueryDB --> BuildResponse[Build Response]
    BuildResponse --> End([End])


```