"use client";

/**
 * hooks/useUpload.ts — CSV upload state management hook.
 *
 * Manages file selection, upload progress, and session creation.
 *
 * TODO: Implement upload logic using financialService.uploadStatement().
 * TODO: Poll session status until processing is complete.
 * TODO: Navigate to /snapshot/{session_id} on completion.
 */

import { useState } from "react";
import type { SessionState } from "@/types/session";

interface UseUploadReturn {
  state: SessionState;
  upload: (file: File) => Promise<void>;
  reset: () => void;
}

export function useUpload(): UseUploadReturn {
  const [state, setState] = useState<SessionState>({
    sessionId: null,
    status: "idle",
    errorMessage: null,
  });

  const upload = async (_file: File): Promise<void> => {
    // TODO: Set status to 'uploading'.
    // TODO: Call financialService.uploadStatement(file).
    // TODO: Set sessionId and status to 'processing'.
    // TODO: Poll /api/v1/session/{session_id}/status until 'completed'.
    // TODO: Set status to 'ready' and navigate to snapshot page.
    throw new Error("useUpload.upload not implemented.");
  };

  const reset = (): void => {
    setState({ sessionId: null, status: "idle", errorMessage: null });
  };

  return { state, upload, reset };
}
