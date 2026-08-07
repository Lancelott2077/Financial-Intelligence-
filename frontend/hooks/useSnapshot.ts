"use client";

/**
 * hooks/useSnapshot.ts — Financial snapshot data fetching hook.
 *
 * TODO: Implement using financialService.fetchSnapshot().
 * TODO: Add SWR or React Query for caching and revalidation.
 */

import { useState, useEffect } from "react";
import type { SnapshotResponse } from "@/types/api";

interface UseSnapshotReturn {
  data: SnapshotResponse | null;
  isLoading: boolean;
  error: string | null;
}

export function useSnapshot(sessionId: string | null): UseSnapshotReturn {
  const [data, setData] = useState<SnapshotResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!sessionId) return;
    // TODO: Call financialService.fetchSnapshot(sessionId).
    // TODO: Set data and handle errors.
  }, [sessionId]);

  return { data, isLoading, error };
}
