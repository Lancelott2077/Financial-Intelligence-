# Data Schemas — Financial Intelligence Platform

> **Status:** Finalised (Milestone 1).

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
| category    | VARCHAR(100) | Nullable (Enum: SpendingCategory) |
| merchant    | VARCHAR(200) | Nullable                   |
| currency    | VARCHAR(3)   | Default: INR               |

### detected_behaviours

| Column      | Type         | Notes                      |
|-------------|--------------|----------------------------|
| id          | INTEGER      | Auto-increment PK          |
| session_id  | VARCHAR(36)  | FK → upload_sessions.id    |
| bias_type   | VARCHAR(100) | FK to BiasType registry    |
| confidence  | FLOAT        | 0.0 to 1.0                 |
| severity    | VARCHAR(20)  | low/medium/high            |
| summary     | TEXT         | Nullable                   |
| detected_at | DATETIME     |                            |

### behaviour_evidence

| Column      | Type         | Notes                      |
|-------------|--------------|----------------------------|
| id          | INTEGER      | Auto-increment PK          |
| behaviour_id| INTEGER      | FK → detected_behaviours.id|
| transaction_id| INTEGER    | FK → transactions.id       |
| explanation | TEXT         | Why this supports the bias |

### action_plan_items

| Column      | Type         | Notes                      |
|-------------|--------------|----------------------------|
| id          | INTEGER      | Auto-increment PK          |
| session_id  | VARCHAR(36)  | FK → upload_sessions.id    |
| title       | VARCHAR(255) |                            |
| description | TEXT         |                            |
| est_saving  | NUMERIC(12,2)| Monthly saving             |
| priority    | VARCHAR(20)  | low/medium/high            |
| target_date | DATE         | Nullable                   |
| status      | VARCHAR(20)  | pending/in_progress/etc    |
| behaviour_id| INTEGER      | Nullable FK → detected_behaviours.id |
| bias_type   | VARCHAR(100) | Nullable FK to BiasType registry |

---

## Pydantic Schemas

All Pydantic models are located in `backend/app/schemas/`. They inherit from a `BaseResponse` which sets `from_attributes=True` for seamless SQLAlchemy serialization.

- **common.py**: Contains all strictly typed enums (`SeverityLevel`, `ProcessingStatus`, `BiasType`, `PlanItemStatus`, `MessageRole`, `TransactionType`, `SpendingCategory`).
- **upload.py**: `UploadResponse`
- **snapshot.py**: `SnapshotResponse`, `CategoryBreakdown`, `MonthlyTrend`
- **behaviours.py**: `BehavioursResponse`, `BehaviourProfile`, `BehaviourDetail`, `EvidenceItem`
- **savings.py**: `SavingsResponse`, `SavingOpportunity`
- **simulation.py**: `SimulationRequest`, `SimulationResponse`, `ScenarioChange`, `ProjectedMonth`
- **coach.py**: `CoachRequest`, `CoachResponse`, `ChatMessage`
- **plan.py**: `PlanResponse`, `PlanItem`

## Category Taxonomy

*Mapped from `app.schemas.common.SpendingCategory`.*

1. `food_and_dining`
2. `groceries`
3. `transport`
4. `entertainment`
5. `utilities`
6. `healthcare`
7. `shopping`
8. `education`
9. `travel`
10. `income`
11. `transfer`
12. `other`

## Bias Type Registry

*Mapped from `app.schemas.common.BiasType`.*

1. `present_bias`: A tendency to overvalue immediate rewards.
2. `loss_aversion`: The psychological impact of losing money is perceived as twice as severe as gaining.
3. `anchoring`: Relying too heavily on the first piece of information encountered.
4. `mental_accounting`: Treating money differently depending on its source/use.
5. `status_quo_bias`: Preference for the current state of affairs.
