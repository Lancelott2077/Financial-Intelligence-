/**
 * services/apiClient.ts — Centralised HTTP client for backend API calls.
 *
 * All API requests must go through this client.
 * Handles base URL, default headers, and error normalisation.
 *
 * TODO: Implement request/response interceptors.
 * TODO: Add retry logic for transient failures.
 * TODO: Add request cancellation support (AbortController).
 */

import { API_URL } from "@/lib/constants";

/** Standardised API error thrown by all service functions. */
export class ApiError extends Error {
  constructor(
    public statusCode: number,
    message: string,
    public detail?: unknown
  ) {
    super(message);
    this.name = "ApiError";
  }
}

/**
 * Base fetch wrapper with JSON handling and error normalisation.
 *
 * TODO: Implement full request/response cycle.
 * TODO: Throw ApiError on non-2xx responses.
 */
async function request<T>(
  path: string,
  options?: RequestInit
): Promise<T> {
  // TODO: Construct full URL from API_URL + path.
  // TODO: Set default headers (Content-Type: application/json).
  // TODO: Call fetch() and handle response.
  // TODO: Throw ApiError on non-2xx status.
  throw new Error(`apiClient.request not implemented. Would call: ${API_URL}${path}`);
}

export const apiClient = {
  get: <T>(path: string) => request<T>(path, { method: "GET" }),
  post: <T>(path: string, body: unknown) =>
    request<T>(path, {
      method: "POST",
      body: JSON.stringify(body),
      headers: { "Content-Type": "application/json" },
    }),
  postForm: <T>(path: string, formData: FormData) =>
    request<T>(path, { method: "POST", body: formData }),
};
