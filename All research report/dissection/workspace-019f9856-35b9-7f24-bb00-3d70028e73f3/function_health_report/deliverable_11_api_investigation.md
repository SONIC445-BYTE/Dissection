# DELIVERABLE 11 — API INVESTIGATION
## FUNCTION HEALTH — REST API, ENDPOINTS, AUTHENTICATION, SCHEMAS, AND DEVELOPER EXPERIENCE
*Evidence from reverse-engineered documentation (github.com/daveremy/function-health-mcp). Not officially documented by Function Health.*

---

## 11.1 API OVERVIEW

### Confirmed 🟢
- **Status:** Undocumented (not officially published by Function Health)
- **Base URL:** `https://production-member-app-mid-lhuqotpy2a-ue.a.run.app/api/v1`
- **Protocol:** REST (JSON)
- **Authentication:** Firebase JWT (`idToken` in Authorization header)
- **Rate Limiting:** Not explicitly documented; aggressive requests trigger errors; recommended 250ms spacing between requests
- **Versioning:** `/api/v1` — implies future versioning possible
- **Source:** Reverse-engineered by open-source community (github.com/daveremy/function-health-mcp; credit to daveremy and Inigo Beitia Arevalo)

---

## 11.2 AUTHENTICATION

### Confirmed 🟢

**Login Endpoint:**
```
POST /login
Content-Type: application/json
{
  "email": "user@example.com",
  "password": "..."
}
```
**Response:**
```
{
  "idToken": "eyJhbGciOi...",
  "refreshToken": "AMf-vBx...",
  "expiresIn": "3600",
  "localId": "abc123",
  "email": "user@example.com"
}
```

**Token Refresh:**
```
POST https://securetoken.googleapis.com/v1/token?key=REDACTED_GOOGLE_API_KEY
Content-Type: application/json
{
  "grant_type": "refresh_token",
  "refresh_token": "AMf-vBx..."
}
```

**Response:**
```
{
  "access_token": "eyJhbGciOi...",
  "expires_in": "3600",
  "refresh_token": "AMf-vBx..."
}
```

**Request Headers (All Endpoints):**
```
Authorization: Bearer <idToken>
Content-Type: application/json
Accept: application/json, text/plain, */*
User-Agent: Mozilla/5.0 ...
fe-app-version: 0.84.0
x-backend-skip-cache: true
referer: https://my.functionhealth.com/
```

---

## 11.3 ENDPOINTS

### Confirmed 🟢

| Endpoint | Method | Description | Key Fields |
|----------|--------|-------------|-----------|
| `/user` | GET | User profile | `id`, `patientIdentifier`, `fname`, `lname`, `biologicalSex`, `dob`, `patientContactInfo`, `dateJoined`, `intake_status`, `patientMembership` |
| `/biomarkers` | GET | Biomarker definitions (metadata only) | `id`, `name`, `questBiomarkerCode`, `categories`, `sexDetails` (`optimalRangeLow`, `optimalRangeHigh`, `questRefRangeLow`, `questRefRangeHigh`), `status` |
| `/categories` | GET | Biomarker categories with nested biomarkers | `id`, `categoryName`, `description`, `biomarkers` (full biomarker objects) |
| `/results-report` | GET | Structured biomarker results (primary data source) | `data` → `biomarkerResultsRecord` (array) → `biomarker` (metadata) + `currentResult` (`id`, `dateOfService`, `calculatedResult`, `displayResult`, `inRange`, `requisitionId`) + `outOfRangeType` + `units` + `optimalRange` + `rangeString` |
| `/recommendations` | GET | Personalized health recommendations | Array: `id`, `category` (e.g., Nutrition), `title`, `description` |
| `/biological-calculations/biological-age` | GET | Biological age calculation | `biologicalAge`, `chronologicalAge` |
| `/biological-calculations/bmi` | GET | BMI data | `bmi`, `weight`, `height` |
| `/notes` | GET | Clinician notes | Array: `id`, `content`, `createdAt` |
| `/requisitions?pending=true` | GET | Pending (in-progress) test rounds | Array: `id`, `status`, `dateOfService` |
| `/requisitions?pending=false` | GET | Completed test rounds | Used for change detection (count comparison) |
| `/pending-schedules` | GET | Upcoming scheduled visits | Array: `id`, `scheduledDate` |

---

## 11.4 DATA MODEL DETAILS

### Confirmed 🟢

**Biomarker Metadata (`/biomarkers`):**
- Each biomarker has `questBiomarkerCode` (Quest Diagnostics lab code)
- `categories` array (biomarker can belong to multiple categories)
- `sexDetails` array: `sex` ("All"/"Male"/"Female"), `oneLineDescription`, `optimalRangeHigh`, `optimalRangeLow`, `questRefRangeHigh`, `questRefRangeLow`
- `status`: null or active status

**Results (`/results-report`):**
- `biomarkerResultsRecord` array — each item contains:
  - `biomarker`: Full biomarker metadata (name, description, optimal/reference ranges, sex details)
  - `currentResult`: The latest result value with `id`, `dateOfService`, `calculatedResult`, `displayResult`, `inRange`, `requisitionId`
  - `outOfRangeType`: "HIGH", "LOW", or empty string
  - `units`: Measurement units
  - `optimalRange`: Function's recommended range string (e.g., "40-80")
  - `rangeString`: Quest reference range string (e.g., "30-100")

**Test Rounds (`requisitionId`):**
- Annual test: ~100+ biomarkers, 1-3 visits over 2-4 weeks
- Mid-year test: ~60+ biomarkers, 1-3 visits
- All visits for one test share `requisitionId`
- Results arrive in batches as each visit is processed

---

## 11.5 SCHEMA LIMITATIONS

### Confirmed 🟢
- **No Official Documentation:** Function Health does not publish API docs, OpenAPI spec, or developer guides
- **No SDK:** Only reverse-engineered open-source project exists
- **No Webhooks:** Not documented; notifications likely delivered via email/app notification, not webhook
- **No GraphQL:** REST only
- **No Sandbox:** No public sandbox environment for testing
- **No Rate Limit Headers:** No explicit rate limit documentation
- **No Pagination:** Not confirmed for large result sets
- **No Filtering:** Endpoints accept basic query parameters (`pending=true/false`) but no complex filtering, sorting, or search

---

*Source: https://github.com/daveremy/function-health-mcp/blob/main/docs/api-reference.md (reverse-engineered by daveremy; original reverse-engineering by Inigo Beitia Arevalo — https://github.com/bogini/function-health-exporter)*
