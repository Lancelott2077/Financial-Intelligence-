"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import {
  ArrowRight,
  TrendingUp,
  Loader2,
} from "lucide-react";
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import { useSimulation } from "@/hooks/useSimulation";
import { ScenarioBuilder } from "@/components/simulation/ScenarioBuilder";
import { formatCurrency } from "@/lib/utils";
import type { ScenarioChange } from "@/types/api";

interface LocalMetadata {
  income: number;
  savingsTarget: number;
  salaryDate: number;
  goal: string;
}

function formatMonthLabel(monthStr: string): string {
  try {
    const [year, month] = monthStr.split("-");
    const date = new Date(parseInt(year), parseInt(month) - 1, 1);
    return date.toLocaleDateString("en-US", { month: "short", year: "2-digit" });
  } catch {
    return monthStr;
  }
}

export default function SimulationPage({
  params,
}: {
  params: { sessionId: string };
}) {
  const { result, isRunning, error, run, reset } = useSimulation();
  const [metadata, setMetadata] = useState<LocalMetadata | null>(null);

  // Load localStorage financial context metadata
  useEffect(() => {
    try {
      const saved = localStorage.getItem(`fin_session_${params.sessionId}_meta`);
      if (saved) {
        setMetadata(JSON.parse(saved));
      }
    } catch {
      // Fail silently
    }
  }, [params.sessionId]);

  // Initial mock run on page load
  useEffect(() => {
    run({
      session_id: params.sessionId,
      scenario_changes: [{ category: "food_and_dining", change_percent: -30 }],
      horizon_months: 6,
    });
    return () => reset();
  }, [params.sessionId, run, reset]);

  const handleSimulate = (changes: ScenarioChange[], horizonMonths: number) => {
    run({
      session_id: params.sessionId,
      scenario_changes: changes,
      horizon_months: horizonMonths,
    });
  };

  // Compute cumulative chart data
  let cumulative = 0;
  const chartData = (result?.projected_months ?? []).map((m) => {
    cumulative += m.projected_savings;
    return {
      ...m,
      cumulativeSavings: cumulative,
    };
  });

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 animate-fade-in-up">
      {/* Header section */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-white/5 pb-6">
        <div className="space-y-1">
          <h1 className="text-3xl font-extrabold text-white tracking-tight flex items-center gap-2">
            Counterfactual Replay
          </h1>
          <p className="text-sm text-gray-400">
            Simulate adjustments and project cumulative savings over customizable horizons.
          </p>
        </div>

        <Link
          href={`/coach/${params.sessionId}`}
          className="inline-flex items-center gap-2 px-4 py-2 bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-400 border border-indigo-500/20 hover:border-indigo-500/30 rounded-xl text-sm font-medium transition-all group shrink-0"
        >
          <span>AI Coaching Report</span>
          <ArrowRight className="w-4 h-4 group-hover:translate-x-0.5 transition-transform" />
        </Link>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-5 gap-6">
        {/* Left: Configuration Sliders */}
        <div className="lg:col-span-2">
          <ScenarioBuilder onSimulate={handleSimulate} isSimulating={isRunning} />
        </div>

        {/* Right: Results Dashboard & Charts */}
        <div className="lg:col-span-3 space-y-6">
          {isRunning ? (
            <div className="glass rounded-2xl border border-white/5 bg-white/[0.01] h-[480px] flex flex-col items-center justify-center space-y-4">
              <Loader2 className="w-10 h-10 text-indigo-500 animate-spin" />
              <p className="text-xs text-gray-500 font-semibold uppercase tracking-wider">
                Recalculating projection models...
              </p>
            </div>
          ) : error ? (
            <div className="glass rounded-2xl border border-white/5 bg-white/[0.01] h-[480px] flex flex-col items-center justify-center p-6 text-center space-y-4">
              <AlertCircle className="w-10 h-10 text-rose-400" />
              <div className="space-y-1">
                <h3 className="text-sm font-bold text-white">Projection Failed</h3>
                <p className="text-xs text-gray-500">{error}</p>
              </div>
            </div>
          ) : result ? (
            <div className="space-y-6">
              {/* Savings Impact Hero Card */}
              <div className="glass rounded-2xl border border-emerald-500/10 bg-emerald-500/[0.01] p-6 flex flex-col md:flex-row md:items-center justify-between gap-4 relative overflow-hidden">
                <div className="absolute top-0 right-0 w-[150px] h-[150px] bg-emerald-500/5 rounded-full blur-[60px] pointer-events-none" />

                <div className="space-y-1.5">
                  <span className="text-[10px] font-bold text-gray-500 uppercase tracking-wider">
                    Total Projected Surplus
                  </span>
                  <div className="flex items-baseline gap-2">
                    <span className="text-3xl font-extrabold text-white">
                      {formatCurrency(result.total_projected_saving)}
                    </span>
                    <span className="text-xs text-emerald-400 font-bold uppercase">
                      over {result.projected_months.length} months
                    </span>
                  </div>
                  <p className="text-xs text-gray-400 font-medium">
                    {result.summary}
                  </p>
                </div>

                {metadata && (
                  <div className="p-4 rounded-xl bg-white/5 border border-white/5 text-xs space-y-2 shrink-0 md:text-right">
                    <span className="text-gray-500 font-semibold block uppercase text-[10px]">
                      Target Progress
                    </span>
                    <span className="text-white font-bold block">
                      {formatCurrency(result.total_projected_saving)} / {formatCurrency(metadata.savingsTarget * result.projected_months.length)}
                    </span>
                    <span className="text-indigo-400 font-semibold block text-[10px]">
                      {Math.round((result.total_projected_saving / (metadata.savingsTarget * result.projected_months.length)) * 100)}% of Goal Reached
                    </span>
                  </div>
                )}
              </div>

              {/* Accumulation Line Chart */}
              <div className="glass rounded-2xl border border-white/5 bg-white/[0.01] p-6 space-y-4">
                <div className="flex items-center justify-between border-b border-white/5 pb-3">
                  <div className="flex items-center gap-2">
                    <TrendingUp className="w-5 h-5 text-indigo-400" />
                    <h3 className="text-sm font-bold text-white tracking-tight">
                      Projected Cumulative Savings
                    </h3>
                  </div>
                  <span className="text-[10px] uppercase font-semibold text-indigo-400 bg-indigo-500/10 border border-indigo-500/20 px-2 py-0.5 rounded-full">
                    Growth Curve
                  </span>
                </div>

                <div className="w-full h-[280px]">
                  <ResponsiveContainer width="100%" height="100%">
                    <AreaChart
                      data={chartData}
                      margin={{ top: 10, right: 10, left: -20, bottom: 0 }}
                    >
                      <defs>
                        <linearGradient id="simGrad" x1="0" y1="0" x2="0" y2="1">
                          <stop offset="5%" stopColor="rgb(99, 102, 241)" stopOpacity={0.25} />
                          <stop offset="95%" stopColor="rgb(99, 102, 241)" stopOpacity={0.01} />
                        </linearGradient>
                      </defs>
                      <CartesianGrid
                        strokeDasharray="3 3"
                        vertical={false}
                        stroke="rgba(255, 255, 255, 0.05)"
                      />
                      <XAxis
                        dataKey="month"
                        tickFormatter={formatMonthLabel}
                        stroke="rgb(107, 114, 128)"
                        tickLine={false}
                        axisLine={false}
                        tick={{ fontSize: 11 }}
                        dy={8}
                      />
                      <YAxis
                        tickFormatter={(value) => `$${value}`}
                        stroke="rgb(107, 114, 128)"
                        tickLine={false}
                        axisLine={false}
                        tick={{ fontSize: 11 }}
                        dx={-8}
                      />
                      <Tooltip
                        content={({ active, payload }) => {
                          if (active && payload && payload.length) {
                            const val = payload[0].value as number;
                            const label = formatMonthLabel(payload[0].payload.month);
                            const perMonth = payload[0].payload.projected_savings;

                            return (
                              <div className="glass p-3 rounded-xl border border-white/10 text-xs space-y-1.5">
                                <p className="font-semibold text-white border-b border-white/5 pb-1">
                                  {label} Projection
                                </p>
                                <div className="flex justify-between gap-6">
                                  <span className="text-gray-400">Monthly Added Savings:</span>
                                  <span className="text-emerald-400 font-semibold">
                                    +{formatCurrency(perMonth)}
                                  </span>
                                </div>
                                <div className="flex justify-between gap-6 border-t border-white/5 pt-1">
                                  <span className="text-gray-400">Cumulative Savings:</span>
                                  <span className="text-indigo-400 font-bold">
                                    {formatCurrency(val)}
                                  </span>
                                </div>
                              </div>
                            );
                          }
                          return null;
                        }}
                      />
                      <Area
                        type="monotone"
                        dataKey="cumulativeSavings"
                        stroke="rgb(99, 102, 241)"
                        strokeWidth={2}
                        fillOpacity={1}
                        fill="url(#simGrad)"
                      />
                    </AreaChart>
                  </ResponsiveContainer>
                </div>
              </div>
            </div>
          ) : (
            <div className="glass rounded-2xl border border-white/5 bg-white/[0.01] h-[480px] flex items-center justify-center p-6 text-center text-gray-500">
              Please adjust sliders and run replay simulation.
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

// Alert icon wrapper
function AlertCircle(props: React.ComponentProps<"svg">) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
      {...props}
    >
      <circle cx="12" cy="12" r="10" />
      <line x1="12" y1="8" x2="12" y2="12" />
      <line x1="12" y1="16" x2="12.01" y2="16" />
    </svg>
  );
}
