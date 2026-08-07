"use client";

/**
 * hooks/useSavings.ts — Savings opportunities data fetching hook.
 *
 * Fetches ranked savings opportunities via the service layer.
 */

import { useState, useEffect, useCallback } from "react";
import type { SavingsResponse } from "@/types/api";
import { fetchSavings } from "@/services/financialService";

interface UseSavingsReturn {
  data: SavingsResponse | null;
  isLoading: boolean;
  error: string | null;
  refetch: () => void;
}

export function useSavings(sessionId: string | null): UseSavingsReturn {
  const [data, setData] = useState<SavingsResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const load = useCallback(async (id: string, signal: AbortSignal) => {
    setIsLoading(true);
    setError(null);
    try {
      const result = await fetchSavings(id);
      if (!signal.aborted) {
        setData(result);
      }
    } catch (err) {
      if (!signal.aborted) {
        setError(
          err instanceof Error ? err.message : "Failed to load savings."
        );
      }
    } finally {
      if (!signal.aborted) {
        setIsLoading(false);
      }
    }
  }, []);

  useEffect(() => {
    if (!sessionId) return;

    const controller = new AbortController();
    load(sessionId, controller.signal);

    return () => controller.abort();
  }, [sessionId, load]);

  const refetch = useCallback(() => {
    if (sessionId) {
      const controller = new AbortController();
      load(sessionId, controller.signal);
    }
  }, [sessionId, load]);

  return { data, isLoading, error, refetch };
}
