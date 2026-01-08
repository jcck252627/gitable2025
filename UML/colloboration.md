```mermaid

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




```flowchart TB
    %% ============================
    %% Developer Layer
    %% ============================
    Dev["Developer Workstation<br/>VS Code / Git"] 

    %% ============================
    %% Azure DevOps Platform
    %% ============================
    subgraph AzureDevOps["Azure DevOps Services"]
        Repos["Azure Repos<br/>Git Repository"]
        Pipelines["Azure Pipelines<br/>CI/CD Engine"]
        Artifacts["Azure Artifacts<br/>Package Feeds"]
    end

    %% ============================
    %% Azure Cloud Services
    %% ============================
    subgraph AzureCloud["Azure Cloud"]
        ACR["Azure Container Registry (ACR)"]
        AKS["Azure Kubernetes Service (AKS)"]
        AppSvc["Azure App Service"]
        SQL["Azure SQL Database"]
        KV["Azure Key Vault"]
        Log["Log Analytics Workspace"]
        Mon["Azure Monitor"]
    end

    %% Developer interactions
    Dev --> Repos

    %% CI Pipeline interactions
    Repos --> Pipelines
    Pipelines --> ACR
    Pipelines --> Artifacts

    %% CD Deployment
    Pipelines --> AKS
    Pipelines --> AppSvc

    %% Runtime interactions
    AKS --> KV
    AppSvc --> KV
    AKS --> SQL
    AppSvc --> SQL

    %% Monitoring & Logging
    AKS --> Log
    AppSvc --> Log
    Log --> Mon
    Mon --> Dev
