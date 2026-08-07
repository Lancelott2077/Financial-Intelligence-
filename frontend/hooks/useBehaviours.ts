"use client";

/**
 * hooks/useBehaviours.ts — Detected behaviours data fetching hook.
 *
 * Fetches behaviour intelligence data via the service layer.
 */

import { useState, useEffect, useCallback } from "react";
import type { BehavioursResponse } from "@/types/api";
import { fetchBehaviours } from "@/services/financialService";

interface UseBehavioursReturn {
  data: BehavioursResponse | null;
  isLoading: boolean;
  error: string | null;
  refetch: () => void;
}

export function useBehaviours(sessionId: string | null): UseBehavioursReturn {
  const [data, setData] = useState<BehavioursResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const load = useCallback(async (id: string, signal: AbortSignal) => {
    setIsLoading(true);
    setError(null);
    try {
      const result = await fetchBehaviours(id);
      if (!signal.aborted) {
        setData(result);
      }
    } catch (err) {
      if (!signal.aborted) {
        setError(
          err instanceof Error ? err.message : "Failed to load behaviours."
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
