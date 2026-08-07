"use client";

/**
 * hooks/useBehaviours.ts — Detected behaviours data fetching hook.
 *
 * TODO: Implement using financialService.fetchBehaviours().
 */

import { useState, useEffect } from "react";
import type { BehavioursResponse } from "@/types/api";

interface UseBehavioursReturn {
  data: BehavioursResponse | null;
  isLoading: boolean;
  error: string | null;
}

export function useBehaviours(sessionId: string | null): UseBehavioursReturn {
  const [data, setData] = useState<BehavioursResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!sessionId) return;
    // TODO: Call financialService.fetchBehaviours(sessionId).
  }, [sessionId]);

  return { data, isLoading, error };
}
