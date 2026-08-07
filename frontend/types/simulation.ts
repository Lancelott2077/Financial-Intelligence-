/**
 * types/simulation.ts — Simulation client-side types.
 *
 * TODO: Add preset scenario template types.
 */

export interface ScenarioPreset {
  id: string;
  label: string;
  description: string;
  changes: Array<{ category: string; change_percent: number }>;
}

/**
 * Built-in scenario presets.
 * TODO: Define preset scenarios.
 */
export const SCENARIO_PRESETS: ScenarioPreset[] = [
  // TODO: Add preset scenarios.
];
