"use client";

/**
 * hooks/usePlan.ts — 30-day action plan data fetching hook.
 *
 * Fetches the generated action plan via the service layer.
 */

import { useState, useEffect, useCallback } from "react";
import type { PlanResponse } from "@/types/api";
import { fetchPlan } from "@/services/financialService";

interface UsePlanReturn {
  data: PlanResponse | null;
  isLoading: boolean;
  error: string | null;
  refetch: () => void;
}

export function usePlan(sessionId: string | null): UsePlanReturn {
  const [data, setData] = useState<PlanResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const load = useCallback(async (id: string, signal: AbortSignal) => {
    setIsLoading(true);
    setError(null);
    try {
      const result = await fetchPlan(id);
      if (!signal.aborted) {
        setData(result);
      }
    } catch (err) {
      if (!signal.aborted) {
        setError(
          err instanceof Error ? err.message : "Failed to load action plan."
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
