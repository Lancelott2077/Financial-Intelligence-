"use client";

/**
 * hooks/useUpload.ts — CSV upload state management hook.
 *
 * Manages file selection, upload progress, and session creation.
 * On success, returns the session ID for downstream navigation.
 */

import { useState, useCallback } from "react";
import type { SessionState } from "@/types/session";
import { uploadStatement } from "@/services/financialService";

interface UseUploadReturn {
  state: SessionState;
  upload: (file: File) => Promise<string | null>;
  reset: () => void;
}

export function useUpload(): UseUploadReturn {
  const [state, setState] = useState<SessionState>({
    sessionId: null,
    status: "idle",
    errorMessage: null,
  });

  const upload = useCallback(async (file: File): Promise<string | null> => {
    setState({ sessionId: null, status: "uploading", errorMessage: null });

    try {
      const response = await uploadStatement(file);
      setState({
        sessionId: response.session_id,
        status: "ready",
        errorMessage: null,
      });
      return response.session_id;
    } catch (err) {
      setState({
        sessionId: null,
        status: "error",
        errorMessage:
          err instanceof Error ? err.message : "Upload failed. Please try again.",
      });
      return null;
    }
  }, []);

  const reset = useCallback((): void => {
    setState({ sessionId: null, status: "idle", errorMessage: null });
  }, []);

  return { state, upload, reset };
}
