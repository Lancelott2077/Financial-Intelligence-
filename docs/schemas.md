# Data Schemas — Financial Intelligence Platform

> **Status:** Placeholder — update as models are finalised.

## Database Schemas

### upload_sessions

| Column     | Type        | Notes                              |
|-----------|-------------|-------------------------------------|
| id         | VARCHAR(36) | UUID primary key                   |
| filename   | VARCHAR(255)| Original CSV filename              |
| status     | VARCHAR(20) | pending/processing/completed/failed |
| created_at | DATETIME    |                                    |
| updated_at | DATETIME    |                                    |
| error_msg  | VARCHAR(1000)| Nullable                          |

### transactions

| Column      | Type         | Notes                      |
|-------------|--------------|----------------------------|
| id          | INTEGER      | Auto-increment PK          |
| session_id  | VARCHAR(36)  | FK → upload_sessions.id    |
| date        | DATE         |                            |
| description | VARCHAR(500) |                            |
| amount      | NUMERIC(12,2)| Negative = debit           |
| category    | VARCHAR(100) | Nullable                   |
| merchant    | VARCHAR(200) | Nullable                   |
| currency    | VARCHAR(3)   | Default: INR               |

### detected_behaviours

<!-- TODO: Add full schema. -->

### behaviour_evidence

<!-- TODO: Add full schema. -->

### action_plan_items

<!-- TODO: Add full schema. -->

---

## Pydantic Schemas

<!-- TODO: Reference app/schemas/ modules. -->

## Category Taxonomy

<!-- TODO: List all supported spending categories. -->

## Bias Type Registry

<!-- TODO: List all supported bias_type identifiers and their display names. -->
