/**
 * services/financialService.ts — API service layer for all backend endpoints.
 *
 * Each function wraps one API endpoint call using apiClient.
 * When USE_MOCK_DATA is true, functions read from local JSON fixtures instead.
 * Components and hooks should use this service, not apiClient directly.
 */

import { apiClient } from "./apiClient";
import { USE_MOCK_DATA } from "@/lib/constants";
import { mockDelay } from "@/lib/utils";
import type {
  UploadResponse,
  SnapshotResponse,
  BehavioursResponse,
  SavingsResponse,
  SimulationRequest,
  SimulationResponse,
  CoachRequest,
  CoachResponse,
  PlanResponse,
} from "@/types/api";

/** Upload a CSV file and return a session ID. */
export async function uploadStatement(file: File): Promise<UploadResponse> {
  if (USE_MOCK_DATA) {
    await mockDelay(1200);
    return {
      session_id: "c1f7b7f2-6c84-486a-86a0-53bcaf32cda4",
      status: "completed",
      message: `File "${file.name}" uploaded successfully. Processing complete.`,
    };
  }
  const formData = new FormData();
  formData.append("file", file);
  return apiClient.postForm<UploadResponse>("/upload", formData);
}

/** Fetch financial snapshot for a session. */
export async function fetchSnapshot(
  sessionId: string
): Promise<SnapshotResponse> {
  if (USE_MOCK_DATA) {
    await mockDelay();
    const data = await import("@/mock-data/snapshot_mock.json");
    return data.default as SnapshotResponse;
  }
  return apiClient.get<SnapshotResponse>(`/snapshot/${sessionId}`);
}

/** Fetch detected behaviours for a session. */
export async function fetchBehaviours(
  sessionId: string
): Promise<BehavioursResponse> {
  if (USE_MOCK_DATA) {
    await mockDelay();
    const data = await import("@/mock-data/behaviours_mock.json");
    return data.default as BehavioursResponse;
  }
  return apiClient.get<BehavioursResponse>(`/behaviours/${sessionId}`);
}

/** Fetch savings opportunities for a session. */
export async function fetchSavings(
  sessionId: string
): Promise<SavingsResponse> {
  if (USE_MOCK_DATA) {
    await mockDelay();
    const data = await import("@/mock-data/savings_mock.json");
    return data.default as SavingsResponse;
  }
  return apiClient.get<SavingsResponse>(`/savings/${sessionId}`);
}

/** Run a counterfactual simulation. */
export async function runSimulation(
  request: SimulationRequest
): Promise<SimulationResponse> {
  if (USE_MOCK_DATA) {
    await mockDelay(800);
    const data = await import("@/mock-data/simulation_mock.json");
    return data.default as SimulationResponse;
  }
  return apiClient.post<SimulationResponse>("/simulation", request);
}

/** Send a message to the AI financial coach. */
export async function chatWithCoach(
  request: CoachRequest
): Promise<CoachResponse> {
  if (USE_MOCK_DATA) {
    await mockDelay(1000);
    const data = await import("@/mock-data/coach_mock.json");
    return data.default as CoachResponse;
  }
  return apiClient.post<CoachResponse>("/coach/chat", request);
}

/** Fetch the action plan for a session. */
export async function fetchPlan(sessionId: string): Promise<PlanResponse> {
  if (USE_MOCK_DATA) {
    await mockDelay();
    const data = await import("@/mock-data/plan_mock.json");
    return data.default as PlanResponse;
  }
  return apiClient.get<PlanResponse>(`/plan/${sessionId}`);
}
