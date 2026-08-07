/**
 * types/session.ts — Upload session state types.
 *
 * TODO: Expand as session state management evolves.
 */

export interface SessionState {
  sessionId: string | null;
  status: "idle" | "uploading" | "processing" | "ready" | "error";
  errorMessage: string | null;
}
