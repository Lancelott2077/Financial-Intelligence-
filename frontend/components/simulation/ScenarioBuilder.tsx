"use client";

import { useState } from "react";
import { Sliders, Sparkles } from "lucide-react";
import { SCENARIO_PRESETS } from "@/types/simulation";
import type { SpendingCategory, ScenarioChange } from "@/types/api";

interface ScenarioBuilderProps {
  onSimulate: (changes: ScenarioChange[], horizonMonths: number) => void;
  isSimulating: boolean;
}

const CATEGORY_SLIDERS: Array<{ key: SpendingCategory; label: string }> = [
  { key: "food_and_dining", label: "Food & Dining" },
  { key: "shopping", label: "Shopping" },
  { key: "entertainment", label: "Entertainment" },
  { key: "utilities", label: "Utilities" },
];

export function ScenarioBuilder({ onSimulate, isSimulating }: ScenarioBuilderProps) {
  const [sliderVals, setSliderVals] = useState<Record<SpendingCategory, number>>({
    food_and_dining: 0,
    shopping: 0,
    entertainment: 0,
    utilities: 0,
    groceries: 0,
    transport: 0,
    healthcare: 0,
    education: 0,
    travel: 0,
    income: 0,
    transfer: 0,
    other: 0,
  });

  const [horizon, setHorizon] = useState<number>(6);

  const handleSliderChange = (category: SpendingCategory, value: number) => {
    setSliderVals((prev) => ({ ...prev, [category]: value }));
  };

  const applyPreset = (presetId: string) => {
    const preset = SCENARIO_PRESETS.find((p) => p.id === presetId);
    if (!preset) return;

    // Reset all sliders first
    const resetVals = { ...sliderVals };
    Object.keys(resetVals).forEach((k) => {
      resetVals[k as SpendingCategory] = 0;
    });

    // Apply preset changes
    preset.changes.forEach((c) => {
      resetVals[c.category] = c.change_percent;
    });

    setSliderVals(resetVals);
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    // Map active changes (only non-zero value sliders)
    const activeChanges: ScenarioChange[] = CATEGORY_SLIDERS.map((c) => ({
      category: c.key,
      change_percent: sliderVals[c.key],
    })).filter((c) => c.change_percent !== 0);

    onSimulate(activeChanges, horizon);
  };

  return (
    <form onSubmit={handleSubmit} className="glass p-6 rounded-2xl border border-white/5 bg-white/[0.01] space-y-6">
      <div>
        <h3 className="text-sm font-bold text-white tracking-tight flex items-center gap-2 uppercase tracking-wider mb-1">
          <Sliders className="w-4 h-4 text-indigo-400" />
          Scenario Configurator
        </h3>
        <p className="text-xs text-gray-500">
          Configure spending adjustments or choose a preset profile.
        </p>
      </div>

      {/* Preset selection chips */}
      <div className="space-y-2">
        <label className="text-[10px] font-bold text-gray-400 uppercase tracking-wider">
          Presets Profiles
        </label>
        <div className="flex flex-wrap gap-2">
          {SCENARIO_PRESETS.map((p) => (
            <button
              key={p.id}
              type="button"
              onClick={() => applyPreset(p.id)}
              disabled={isSimulating}
              className="px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 text-xs text-gray-300 border border-white/5 hover:border-white/10 transition-all font-semibold"
            >
              {p.label}
            </button>
          ))}
        </div>
      </div>

      {/* Slider inputs stack */}
      <div className="space-y-4 border-t border-white/5 pt-4">
        {CATEGORY_SLIDERS.map((c) => (
          <div key={c.key} className="space-y-1.5">
            <div className="flex justify-between text-xs font-semibold">
              <span className="text-gray-300">{c.label}</span>
              <span
                className={
                  sliderVals[c.key] < 0 ? "text-rose-400 font-bold" : "text-gray-500 font-bold"
                }
              >
                {sliderVals[c.key]}%
              </span>
            </div>
            <input
              type="range"
              min="-100"
              max="0"
              value={sliderVals[c.key]}
              onChange={(e) => handleSliderChange(c.key, parseInt(e.target.value))}
              disabled={isSimulating}
              className="w-full h-1 bg-white/5 rounded-lg appearance-none cursor-pointer accent-indigo-500 focus:outline-none"
            />
          </div>
        ))}
      </div>

      {/* Select Horizon months dropdown */}
      <div className="space-y-1.5 border-t border-white/5 pt-4">
        <label className="text-xs font-semibold text-gray-400">Projection Horizon</label>
        <select
          value={horizon}
          onChange={(e) => setHorizon(parseInt(e.target.value))}
          disabled={isSimulating}
          className="w-full bg-[#121215] border border-white/10 rounded-xl px-3.5 py-2 text-sm text-white focus:outline-none focus:border-indigo-500/50 transition-all cursor-pointer"
        >
          <option value={3}>3 Months Projection</option>
          <option value={6}>6 Months Projection</option>
          <option value={12}>12 Months Projection</option>
        </select>
      </div>

      {/* Trigger submit */}
      <button
        type="submit"
        disabled={isSimulating}
        className="w-full inline-flex items-center justify-center gap-2 px-4 py-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 text-white font-semibold shadow-lg hover:shadow-indigo-500/25 transition-all text-xs uppercase tracking-wider"
      >
        <Sparkles className="w-4 h-4" />
        {isSimulating ? "Recalculating..." : "Run Replay Projection"}
      </button>
    </form>
  );
}
