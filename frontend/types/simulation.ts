/**
 * types/simulation.ts — Simulation client-side types.
 */

import { SpendingCategory } from "./api";

export interface ScenarioPreset {
  id: string;
  label: string;
  description: string;
  changes: Array<{ category: SpendingCategory; change_percent: number }>;
}

/**
 * Built-in scenario presets.
 */
export const SCENARIO_PRESETS: ScenarioPreset[] = [
  {
    id: "cut_dining",
    label: "Cut Dining Out",
    description: "Reduce dining and food delivery expenses by 30%.",
    changes: [{ category: "food_and_dining", change_percent: -30 }],
  },
  {
    id: "reduce_entertainment",
    label: "Frugal Entertainment",
    description: "Cut entertainment expenses in half.",
    changes: [{ category: "entertainment", change_percent: -50 }],
  },
  {
    id: "frugal_month",
    label: "Frugal Month",
    description: "Reduce dining, entertainment, and shopping by 25%.",
    changes: [
      { category: "food_and_dining", change_percent: -25 },
      { category: "entertainment", change_percent: -25 },
      { category: "shopping", change_percent: -25 },
    ],
  },
];
