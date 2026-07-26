# PRODUCT ARCHITECTURE DIAGRAM — FUNCTION HEALTH

```
┌─────────────────────────────────────────────────────────────────────┐
│                         PUBLIC WEBSITE                             │
│              https://www.functionhealth.com/                        │
│                                                                     │
│  Homepage → How It Works → What We Test → Lab Locations → FAQ      │
│  Journal → Press Releases → Signup (my.functionhealth.com/signup)   │
└─────────────────────────────┬───────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    MEMBER WEB APPLICATION                           │
│              https://my.functionhealth.com/                         │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │
│  │   SIGNUP     │  │   PROFILE    │  │  SCHEDULING  │              │
│  │ (Consent)    │  │ (User Data)  │  │ (Quest API)  │              │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘              │
│         │                 │                  │                       │
│         └─────────────────┼──────────────────┘                       │
│                           ↓                                          │
│  ┌─────────────────────────────────────────────────────────┐         │
│  │                   HEALTH HISTORY                       │         │
│  │         (Personalization → Clinician Context)           │         │
│  └──────────────────────────┬────────────────────────────┘         │
│                             ↓                                        │
│  ┌─────────────────────────────────────────────────────────┐         │
│  │              LAB TESTING WORKFLOW                      │         │
│  │   Annual (~100+ markers) + Mid-Year (~60+ markers)     │         │
│  │   1-3 Visits → Quest Processes → Batch Results (~2 wks)  │         │
│  └──────────────────────────┬────────────────────────────┘         │
│                             ↓                                        │
│  ┌─────────────────────────────────────────────────────────┐         │
│  │              RESULTS & CLINICAL REVIEW                 │         │
│  │   /results-report → /recommendations → /notes         │         │
│  │   Clinician Reviews → AI Protocol Generation           │         │
│  └──────────────────────────┬────────────────────────────┘         │
│                             ↓                                        │
│  ┌─────────────────────────────────────────────────────────┐         │
│  │              ADVANCED FEATURES                         │         │
│  │   MRI/CT (Ezra) → Upload Health Records → AI Chat      │         │
│  │   Protocols → Supplement Intelligence (SuppCo)         │         │
│  └─────────────────────────────────────────────────────────┘         │
└─────────────────────────────────────────────────────────────────────┘

BACKEND INFRASTRUCTURE:
Google Cloud Run (REST API v1) → Firebase Auth → Firestore/Cloud SQL →
Quest Integration → Ezra Imaging → SuppCo Database → AI Inference (LLM)

MOBILE / WEARABLE (Future):
Native App (iOS/Android) → Apple Health / Google Health Connect →
Real-Time Notifications → Wearable Integration (Oura, Whoop, Garmin)

INTERNATIONAL (Future):
Global Lab Partners → GDPR Compliance → Multilingual →
Cross-Border Health Data Portability
