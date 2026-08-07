"use client";

/**
 * hooks/useSimulation.ts — Counterfactual simulation hook.
 *
 * TODO: Implement using financialService.runSimulation().
 */

import { useState } from "react";
import type { SimulationRequest, SimulationResponse } from "@/types/api";

interface UseSimulationReturn {
  result: SimulationResponse | null;
  isRunning: boolean;
  error: string | null;
  run: (request: SimulationRequest) => Promise<void>;
}

export function useSimulation(): UseSimulationReturn {
  const [result, setResult] = useState<SimulationResponse | null>(null);
  const [isRunning, setIsRunning] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const run = async (_request: SimulationRequest): Promise<void> => {
    // TODO: Set isRunning to true.
    // TODO: Call financialService.runSimulation(request).
    // TODO: Set result and handle errors.
    throw new Error("useSimulation.run not implemented.");
  };

  return { result, isRunning, error, run };
}
