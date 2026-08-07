"use client";

/**
 * hooks/useSimulation.ts — Counterfactual simulation hook.
 *
 * Manages simulation request/response state via the service layer.
 */

import { useState, useCallback } from "react";
import type { SimulationRequest, SimulationResponse } from "@/types/api";
import { runSimulation } from "@/services/financialService";

interface UseSimulationReturn {
  result: SimulationResponse | null;
  isRunning: boolean;
  error: string | null;
  run: (request: SimulationRequest) => Promise<void>;
  reset: () => void;
}

export function useSimulation(): UseSimulationReturn {
  const [result, setResult] = useState<SimulationResponse | null>(null);
  const [isRunning, setIsRunning] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const run = useCallback(async (request: SimulationRequest): Promise<void> => {
    setIsRunning(true);
    setError(null);
    try {
      const response = await runSimulation(request);
      setResult(response);
    } catch (err) {
      setError(
        err instanceof Error ? err.message : "Simulation failed."
      );
    } finally {
      setIsRunning(false);
    }
  }, []);

  const reset = useCallback(() => {
    setResult(null);
    setError(null);
  }, []);

  return { result, isRunning, error, run, reset };
}
