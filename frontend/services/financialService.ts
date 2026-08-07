/**
 * services/financialService.ts — API service layer for all backend endpoints.
 *
 * Each function wraps one API endpoint call using apiClient.
 * Components and hooks should use this service, not apiClient directly.
 *
 * TODO: Implement all service functions once apiClient is complete.
 */

import { apiClient } from "./apiClient";
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
  // TODO: Build FormData with file and call apiClient.postForm("/upload").
  throw new Error("uploadStatement not implemented.");
}

/** Fetch financial snapshot for a session. */
export async function fetchSnapshot(sessionId: string): Promise<SnapshotResponse> {
  // TODO: return apiClient.get(`/snapshot/${sessionId}`);
  throw new Error("fetchSnapshot not implemented.");
}

/** Fetch detected behaviours for a session. */
export async function fetchBehaviours(sessionId: string): Promise<BehavioursResponse> {
  // TODO: return apiClient.get(`/behaviours/${sessionId}`);
  throw new Error("fetchBehaviours not implemented.");
}

/** Fetch savings opportunities for a session. */
export async function fetchSavings(sessionId: string): Promise<SavingsResponse> {
  // TODO: return apiClient.get(`/savings/${sessionId}`);
  throw new Error("fetchSavings not implemented.");
}

/** Run a counterfactual simulation. */
export async function runSimulation(
  request: SimulationRequest
): Promise<SimulationResponse> {
  // TODO: return apiClient.post("/simulation", request);
  throw new Error("runSimulation not implemented.");
}

/** Send a message to the AI financial coach. */
export async function chatWithCoach(request: CoachRequest): Promise<CoachResponse> {
  // TODO: return apiClient.post("/coach/chat", request);
  throw new Error("chatWithCoach not implemented.");
}

/** Fetch the action plan for a session. */
export async function fetchPlan(sessionId: string): Promise<PlanResponse> {
  // TODO: return apiClient.get(`/plan/${sessionId}`);
  throw new Error("fetchPlan not implemented.");
}
