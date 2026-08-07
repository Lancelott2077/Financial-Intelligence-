# API Contract — Financial Intelligence Platform

> **Status:** Finalised (Milestone 1).

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

None for MVP.

---

## Endpoints

### 1. Upload CSV
`POST /upload`
Upload a bank transaction CSV file to initiate an analysis session.

**Request:** `multipart/form-data`
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `file` | File | Yes | Bank statement CSV |

**Response (202 Accepted):** `UploadResponse`
```json
{
  "session_id": "c1f7b7f2-6c84-486a-86a0-53bcaf32cda4",
  "status": "pending",
  "message": "File uploaded successfully. Processing will begin shortly."
}
```

---

### 2. Get Financial Snapshot
`GET /snapshot/{session_id}`
Retrieve the aggregated financial snapshot for the session.

**Request Params:**
- `session_id` (UUID)

**Response (200 OK):** `SnapshotResponse`
```json
{
  "session_id": "c1f7b7f2-6c84-486a-86a0-53bcaf32cda4",
  "total_income": 4500.0,
  "total_expenses": 3200.0,
  "net_savings": 1300.0,
  "savings_rate": 28.8,
  "transaction_count": 84,
  "date_range_start": "2024-01-01",
  "date_range_end": "2024-03-31",
  "category_breakdown": [
    {
      "category": "food_and_dining",
      "total": 800.0,
      "percentage": 25.0,
      "transaction_count": 22
    }
  ],
  "monthly_trends": [
    {
      "month": "2024-01",
      "income": 1500.0,
      "expenses": 1000.0,
      "net": 500.0
    }
  ]
}
```

---

### 3. Get Detected Behaviours
`GET /behaviours/{session_id}`
Retrieve all identified cognitive/behavioural biases.

**Request Params:**
- `session_id` (UUID)

**Response (200 OK):** `BehavioursResponse`
```json
{
  "session_id": "c1f7b7f2-6c84-486a-86a0-53bcaf32cda4",
  "total_count": 1,
  "behaviours": [
    {
      "id": 101,
      "bias_type": "present_bias",
      "display_name": "Present Bias",
      "confidence": 0.88,
      "severity": "medium",
      "detected": true,
      "summary": "Frequent small impulse purchases affecting long-term saving.",
      "evidence": [
        {
          "transaction_id": 45,
          "date": "2024-03-12",
          "description": "Starbucks",
          "amount": -5.50,
          "category": "food_and_dining",
          "explanation": "High frequency coffee purchase."
        }
      ]
    }
  ]
}
```

---

### 4. Get Savings Opportunities
`GET /savings/{session_id}`
Retrieve ranked savings opportunities based on past behaviour.

**Request Params:**
- `session_id` (UUID)

**Response (200 OK):** `SavingsResponse`
```json
{
  "session_id": "c1f7b7f2-6c84-486a-86a0-53bcaf32cda4",
  "total_potential_monthly_saving": 250.0,
  "opportunities": [
    {
      "id": 1,
      "title": "Reduce Dining Out",
      "category": "food_and_dining",
      "current_monthly_spend": 800.0,
      "suggested_monthly_spend": 550.0,
      "estimated_monthly_saving": 250.0,
      "difficulty": "medium",
      "rationale": "Your dining expenses are 25% above average."
    }
  ]
}
```

---

### 5. Run Counterfactual Simulation
`POST /simulation`
Run a 'what-if' scenario to project future savings based on behavioural changes.

**Request Body:** `SimulationRequest`
```json
{
  "session_id": "c1f7b7f2-6c84-486a-86a0-53bcaf32cda4",
  "behaviour_id": 101,
  "scenario_changes": [
    {
      "category": "food_and_dining",
      "change_percent": -30.0
    }
  ],
  "horizon_months": 6
}
```

**Response (200 OK):** `SimulationResponse`
```json
{
  "session_id": "c1f7b7f2-6c84-486a-86a0-53bcaf32cda4",
  "scenario_id": "sim-8f92a3",
  "total_projected_saving": 1500.0,
  "summary": "Cutting dining out by 30% yields $1500 over 6 months.",
  "projected_months": [
    {
      "month": "2024-04",
      "projected_income": 1500.0,
      "projected_expenses": 750.0,
      "projected_savings": 750.0
    }
  ]
}
```

---

### 6. AI Coach Chat
`POST /coach/chat`
Send a message to the AI financial coach (context-aware of the session).

**Request Body:** `CoachRequest`
```json
{
  "session_id": "c1f7b7f2-6c84-486a-86a0-53bcaf32cda4",
  "message": "How do I stop spending so much on food?",
  "history": [
    {
      "role": "assistant",
      "content": "Hi, I'm your financial coach. How can I help today?"
    }
  ]
}
```

**Response (200 OK):** `CoachResponse`
```json
{
  "session_id": "c1f7b7f2-6c84-486a-86a0-53bcaf32cda4",
  "reply": "I see you have a tendency towards present bias regarding dining out. Consider meal prepping.",
  "references": ["present_bias", "plan-item-12"]
}
```

---

### 7. Get Action Plan
`GET /plan/{session_id}`
Retrieve a generated 30-day behavioural action plan.

**Request Params:**
- `session_id` (UUID)

**Response (200 OK):** `PlanResponse`
```json
{
  "session_id": "c1f7b7f2-6c84-486a-86a0-53bcaf32cda4",
  "total_estimated_monthly_saving": 250.0,
  "items": [
    {
      "id": 12,
      "title": "Set a weekly coffee limit",
      "description": "Limit yourself to two coffees out per week.",
      "estimated_monthly_saving": 80.0,
      "priority": "high",
      "target_date": "2024-04-15",
      "status": "pending",
      "linked_behaviour_id": 101,
      "linked_bias_type": "present_bias"
    }
  ]
}
```

---

## Error Responses (Standard Format)

| HTTP Status | Meaning | Scenario |
|-------------|---------|----------|
| **400 Bad Request** | Validation failed | Missing required fields; change_percent out of bounds (-100 to 100). |
| **404 Not Found** | Resource missing | `session_id` does not exist or has no processed data. |
| **422 Unprocessable Entity** | Schema error | Pydantic validation failure (e.g. invalid enum value provided). |
| **500 Internal Error** | Server fault | Unhandled exception during processing or simulation. |
| **501 Not Implemented** | Stub endpoint | API endpoint exists but logic is not yet implemented. |
