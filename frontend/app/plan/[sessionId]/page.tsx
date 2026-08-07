"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { AlertCircle, RefreshCw, CheckSquare, Sparkles } from "lucide-react";
import { usePlan } from "@/hooks/usePlan";
import { PlanItem } from "@/components/plan/PlanItem";
import { formatCurrency } from "@/lib/utils";
import type { PlanItem as PlanItemType } from "@/types/api";

interface LocalMetadata {
  income: number;
  savingsTarget: number;
  salaryDate: number;
  goal: string;
}

const GOAL_LABELS: Record<string, string> = {
  emergency_fund: "Build Emergency Fund",
  debt_payoff: "Pay Off Debt",
  investment: "Grow Investment Portfolio",
  purchase: "Save for Major Purchase",
};

export default function ActionPlanPage({
  params,
}: {
  params: { sessionId: string };
}) {
  const { data, isLoading, error, refetch } = usePlan(params.sessionId);
  const [metadata, setMetadata] = useState<LocalMetadata | null>(null);

  // Local state to manage checkbox completions and skips for realistic demo interaction
  const [itemsState, setItemsState] = useState<PlanItemType[]>([]);

  // Load local metadata
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

  // Sync state when hook data loads
  useEffect(() => {
    if (data) {
      setItemsState(data.items);
    }
  }, [data]);

  const handleToggleComplete = (id: number) => {
    setItemsState((prev) =>
      prev.map((item) => {
        if (item.id === id) {
          const nextStatus = item.status === "completed" ? "pending" : "completed";
          return { ...item, status: nextStatus };
        }
        return item;
      })
    );
  };

  const handleToggleSkip = (id: number) => {
    setItemsState((prev) =>
      prev.map((item) => {
        if (item.id === id) {
          const nextStatus = item.status === "skipped" ? "pending" : "skipped";
          return { ...item, status: nextStatus };
        }
        return item;
      })
    );
  };

  // Loading skeleton state
  if (isLoading) {
    return (
      <div className="max-w-3xl mx-auto px-4 py-8 space-y-8 animate-pulse">
        {/* Header Skeleton */}
        <div className="space-y-3">
          <div className="h-8 w-64 bg-white/5 rounded" />
          <div className="h-4 w-96 bg-white/5 rounded" />
        </div>

        {/* Tracker Progress Skeleton */}
        <div className="glass rounded-2xl border border-white/5 bg-white/[0.01] h-[100px]" />

        {/* List Skeleton */}
        <div className="space-y-4">
          {[...Array(3)].map((_, i) => (
            <div key={i} className="glass rounded-xl p-5 border border-white/5 bg-white/[0.01] h-[90px]" />
          ))}
        </div>
      </div>
    );
  }

  // Error boundary state
  if (error) {
    return (
      <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center p-8">
        <div className="glass rounded-2xl p-8 max-w-md w-full text-center space-y-6 border-red-500/10">
          <div className="flex justify-center">
            <div className="p-3 bg-rose-500/10 rounded-full border border-rose-500/20 text-rose-400">
              <AlertCircle className="w-10 h-10" />
            </div>
          </div>
          <div className="space-y-2">
            <h1 className="text-xl font-bold text-gray-100">Failed to load action plan</h1>
            <p className="text-sm text-gray-400 leading-relaxed">{error}</p>
          </div>
          <button
            onClick={refetch}
            className="w-full inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-medium shadow-lg hover:shadow-indigo-500/25 transition-all"
          >
            <RefreshCw className="w-4 h-4" />
            Try Again
          </button>
        </div>
      </div>
    );
  }

  const hasNoData = itemsState.length === 0;

  if (hasNoData) {
    return (
      <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center p-8 animate-fade-in-up">
        <div className="glass rounded-2xl p-10 max-w-md w-full text-center space-y-6">
          <div className="flex justify-center">
            <div className="p-4 bg-white/5 rounded-full border border-white/10 text-indigo-400 inline-block">
              <CheckSquare className="w-12 h-12" />
            </div>
          </div>
          <div className="space-y-2">
            <h1 className="text-2xl font-bold text-white">No Action Items</h1>
            <p className="text-sm text-gray-400 leading-relaxed">
              There are no tasks currently generated for this statement period. Build your profile and upload a file first.
            </p>
          </div>
          <Link
            href="/upload"
            className="w-full inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold shadow-lg transition-all"
          >
            Go to Upload
          </Link>
        </div>
      </div>
    );
  }

  // Progress metrics calculation
  const totalCount = itemsState.length;
  const completedCount = itemsState.filter((item) => item.status === "completed").length;
  const completedPercent = Math.round((completedCount / totalCount) * 100);

  // Compute active monthly saving total for completed tasks
  const currentSavedValue = itemsState
    .filter((item) => item.status === "completed")
    .reduce((acc, item) => acc + item.estimated_monthly_saving, 0);

  return (
    <div className="max-w-3xl mx-auto px-4 py-8 space-y-8 animate-fade-in-up">
      {/* Header section */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-white/5 pb-5">
        <div className="space-y-1">
          <h1 className="text-3xl font-extrabold text-white tracking-tight flex items-center gap-2">
            30-Day Action Plan
          </h1>
          <p className="text-sm text-gray-400">
            {metadata ? (
              <>
                Targeting:{" "}
                <span className="text-indigo-400 font-semibold">
                  {GOAL_LABELS[metadata.goal] ?? metadata.goal}
                </span>
              </>
            ) : (
              "Structured checklist of weekly actions designed to mitigate behavioral spending trends."
            )}
          </p>
        </div>

        <Link
          href={`/snapshot/${params.sessionId}`}
          className="inline-flex items-center gap-2 px-4 py-2 bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-400 border border-indigo-500/20 hover:border-indigo-500/30 rounded-xl text-sm font-medium transition-all group shrink-0"
        >
          <span>Back to Dashboard</span>
        </Link>
      </div>

      {/* Progress tracker dashboard */}
      <div className="glass rounded-2xl border border-white/5 bg-white/[0.01] p-6 space-y-4">
        <div className="flex flex-col sm:flex-row justify-between sm:items-center gap-4">
          <div className="space-y-1">
            <span className="text-[10px] font-bold text-gray-500 uppercase tracking-wider">
              Monthly Savings Activated
            </span>
            <div className="flex items-baseline gap-2">
              <span className="text-2xl font-extrabold text-emerald-400">
                {formatCurrency(currentSavedValue)}
              </span>
              <span className="text-xs text-gray-500 font-medium">
                activated surplus of {formatCurrency(data?.total_estimated_monthly_saving ?? 0)} potential total
              </span>
            </div>
          </div>

          <div className="text-left sm:text-right space-y-1 shrink-0">
            <span className="text-[10px] font-bold text-gray-500 uppercase tracking-wider">
              Completion Rate
            </span>
            <div className="flex items-baseline gap-2 sm:justify-end">
              <span className="text-2xl font-extrabold text-white">
                {completedCount}/{totalCount}
              </span>
              <span className="text-xs text-indigo-400 font-bold uppercase">
                ({completedPercent}%)
              </span>
            </div>
          </div>
        </div>

        {/* Progress line */}
        <div className="h-1.5 w-full bg-white/5 rounded-full overflow-hidden">
          <div
            className="h-full bg-indigo-500 transition-all duration-300 ease-out"
            style={{ width: `${completedPercent}%` }}
          />
        </div>
      </div>

      {/* Checklist stack */}
      <div className="space-y-4">
        <h2 className="text-base font-bold text-white tracking-tight uppercase tracking-wider mb-2 flex items-center gap-2">
          <Sparkles className="w-4 h-4 text-indigo-400" />
          Plan Tasks
        </h2>

        <div className="space-y-3">
          {itemsState.map((item) => (
            <PlanItem
              key={item.id}
              item={item}
              onToggleComplete={handleToggleComplete}
              onToggleSkip={handleToggleSkip}
            />
          ))}
        </div>
      </div>
    </div>
  );
}
