# Report E — Product Architecture Diagram

```mermaid
flowchart TB
 W[Web commerce and education] --> A[Account and identity]
 A --> M[Mobile app]
 M --> B[Bluetooth / device SDKs]
 B --> R[Ring data]
 M --> H[Health-platform connectors]
 H --> X[External wearable data]
 C[CGM / M1] --> I[Ingestion layer]
 L[Blood Vision / laboratory] --> I
 R --> I
 X --> I
 I --> Q[Quality and provenance]
 Q --> N[Normalized time-series and event model]
 N --> S[Scoring and feature services]
 S --> T[Timeline / dashboards]
 S --> P[PowerPlugs / recommendations]
 S --> Z[Notifications]
 I --> O[Analytics and support diagnostics]
 A --> G[Commerce, warranty and entitlements]
```

- **🟢 Confirmed.** Ring, CGM, blood and optional product surfaces are publicly described. [R2](https://www.ultrahuman.com/global/ring/) [R3](https://www.nature.com/articles/s41598-024-56933-2) [R4](https://www.ultrahuman.com/blood-vision/buy/us/)
- **🟡 Strong Inference.** The internal services in the diagram are required by the product behaviour but are not an official Ultrahuman architecture disclosure.
- **🔴 Speculation.** Exact language, framework, deployment topology, queues, databases and model vendors are unknown.

---
