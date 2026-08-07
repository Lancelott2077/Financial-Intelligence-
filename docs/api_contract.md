# API Contract — Financial Intelligence Platform

> **Status:** Placeholder — update as endpoints are implemented.

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

<!-- TODO: Define authentication scheme (API key, JWT, etc.). -->
None for MVP.

---

## Endpoints

### POST /upload

Upload a bank transaction CSV file.

**Request:** `multipart/form-data`

| Field | Type   | Required | Description        |
|-------|--------|----------|--------------------|
| file  | File   | Yes      | Bank statement CSV |

**Response 202:** `UploadResponse`

```json
{
  "session_id": "uuid-string",
  "status": "pending",
  "message": "File uploaded successfully."
}
```

---

### GET /snapshot/{session_id}

Get aggregated financial snapshot.

**Response 200:** `SnapshotResponse`

<!-- TODO: Add full response schema. -->

---

### GET /behaviours/{session_id}

Get detected cognitive biases.

**Response 200:** `BehavioursResponse`

<!-- TODO: Add full response schema. -->

---

### GET /savings/{session_id}

Get ranked savings opportunities.

**Response 200:** `SavingsResponse`

<!-- TODO: Add full response schema. -->

---

### POST /simulation

Run a counterfactual simulation.

**Request body:** `SimulationRequest`

<!-- TODO: Add full request/response schema. -->

---

### POST /coach/chat

Send a message to the AI financial coach.

**Request body:** `CoachRequest`

<!-- TODO: Add full request/response schema. -->

---

### GET /plan/{session_id}

Get the personalised action plan.

**Response 200:** `PlanResponse`

<!-- TODO: Add full response schema. -->

---

## Error Responses

| Status | Meaning                        |
|--------|-------------------------------|
| 400    | Bad request / validation error |
| 404    | Session not found              |
| 501    | Endpoint not yet implemented   |
| 500    | Internal server error          |
