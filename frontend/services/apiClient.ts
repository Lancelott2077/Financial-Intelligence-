/**
 * services/apiClient.ts — Centralised HTTP client for backend API calls.
 *
 * All API requests must go through this client.
 * Handles base URL, default headers, and error normalisation.
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
 * Throws ApiError on non-2xx responses.
 */
async function request<T>(
  path: string,
  options?: RequestInit
): Promise<T> {
  const url = `${API_URL}${path}`;

  const defaultHeaders: HeadersInit = {};
  // Don't set Content-Type for FormData — the browser sets the boundary automatically.
  if (!(options?.body instanceof FormData)) {
    defaultHeaders["Content-Type"] = "application/json";
  }

  const response = await fetch(url, {
    ...options,
    headers: {
      ...defaultHeaders,
      ...options?.headers,
    },
  });

  if (!response.ok) {
    let detail: unknown;
    try {
      detail = await response.json();
    } catch {
      // Response body may not be JSON.
    }
    throw new ApiError(
      response.status,
      `API request failed: ${response.status} ${response.statusText}`,
      detail
    );
  }

  return response.json() as Promise<T>;
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
