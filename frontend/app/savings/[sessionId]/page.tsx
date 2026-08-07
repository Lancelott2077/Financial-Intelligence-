"use client";

import { useEffect, useState } from "react";
import NextLink from "next/link";
import { ArrowRight, AlertCircle, RefreshCw, PiggyBank, Sparkles, TrendingUp } from "lucide-react";
import { useSavings } from "@/hooks/useSavings";
import { OpportunityCard } from "@/components/savings/OpportunityCard";
import { formatCurrency } from "@/lib/utils";

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

export default function SavingsPage({
  params,
}: {
  params: { sessionId: string };
}) {
  const { data, isLoading, error, refetch } = useSavings(params.sessionId);
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

  // Loading skeleton state
  if (isLoading) {
    return (
      <div className="max-w-3xl mx-auto px-4 py-8 space-y-8 animate-pulse">
        {/* Header Skeleton */}
        <div className="space-y-3">
          <div className="h-8 w-64 bg-white/5 rounded" />
          <div className="h-4 w-96 bg-white/5 rounded" />
        </div>

        {/* Hero Card Skeleton */}
        <div className="glass rounded-2xl border border-white/5 bg-white/[0.01] h-[140px]" />

        {/* List Skeleton */}
        <div className="space-y-4">
          {[...Array(2)].map((_, i) => (
            <div key={i} className="glass rounded-xl p-5 border border-white/5 bg-white/[0.01] h-[160px]" />
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
            <h1 className="text-xl font-bold text-gray-100">Failed to load savings plan</h1>
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

  // Empty State / Fallback
  const hasNoData = !data || data.opportunities.length === 0;

  if (hasNoData) {
    return (
      <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center p-8 animate-fade-in-up">
        <div className="glass rounded-2xl p-10 max-w-md w-full text-center space-y-6">
          <div className="flex justify-center">
            <div className="p-4 bg-emerald-500/10 rounded-full border border-emerald-500/20 text-emerald-400 inline-block">
              <PiggyBank className="w-12 h-12" />
            </div>
          </div>
          <div className="space-y-2">
            <h1 className="text-2xl font-bold text-white">No Savings Opportunities Found</h1>
            <p className="text-sm text-gray-400 leading-relaxed">
              We couldn&apos;t identify any immediate opportunities for spend adjustments in this statement period. Keep monitoring transactions!
            </p>
          </div>
          <NextLink
            href={`/snapshot/${params.sessionId}`}
            className="w-full inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold shadow-lg transition-all"
          >
            Back to Snapshot
          </NextLink>
        </div>
      </div>
    );
  }

  // Calculate projected goal indicators
  const annualSavings = data.total_potential_monthly_saving * 12;

  return (
    <div className="max-w-3xl mx-auto px-4 py-8 space-y-8 animate-fade-in-up">
      {/* Header section */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-white/5 pb-6">
        <div className="space-y-1">
          <h1 className="text-3xl font-extrabold text-white tracking-tight flex items-center gap-2">
            Savings Opportunities
          </h1>
          <p className="text-sm text-gray-400">
            {metadata ? (
              <>
                Targeting savings for:{" "}
                <span className="text-indigo-400 font-semibold">
                  {GOAL_LABELS[metadata.goal] ?? metadata.goal}
                </span>{" "}
                (${metadata.savingsTarget}/mo target)
              </>
            ) : (
              "Ranked lists of actionable adjustment options based on behavioral trends."
            )}
          </p>
        </div>

        <NextLink
          href={`/simulation/${params.sessionId}`}
          className="inline-flex items-center gap-2 px-4 py-2 bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-400 border border-indigo-500/20 hover:border-indigo-500/30 rounded-xl text-sm font-medium transition-all group shrink-0"
        >
          <span>Run Simulation</span>
          <ArrowRight className="w-4 h-4 group-hover:translate-x-0.5 transition-transform" />
        </NextLink>
      </div>

      {/* Top Impact Banner Card */}
      <div className="relative overflow-hidden glass rounded-2xl border border-emerald-500/10 bg-emerald-500/[0.01] p-6 space-y-4">
        {/* Glow */}
        <div className="absolute top-0 right-0 w-[200px] h-[200px] bg-emerald-500/5 rounded-full blur-[80px] pointer-events-none" />

        <div className="flex items-start gap-4">
          <div className="p-3 bg-emerald-500/10 rounded-xl border border-emerald-500/20 text-emerald-400 shrink-0">
            <PiggyBank className="w-6 h-6" />
          </div>
          <div className="space-y-1">
            <span className="text-xs font-semibold text-gray-400 uppercase tracking-wider">
              Total Potential Savings Impact
            </span>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-white">
                {formatCurrency(data.total_potential_monthly_saving)}
              </span>
              <span className="text-xs text-emerald-400 font-semibold uppercase">
                per month
              </span>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 border-t border-white/5 pt-4 text-xs text-gray-400">
          <div className="flex items-center gap-2">
            <TrendingUp className="w-4 h-4 text-emerald-400" />
            <span>
              Projected annual impact:{" "}
              <strong className="text-white font-bold">{formatCurrency(annualSavings)}</strong>
            </span>
          </div>
          {metadata && (
            <div className="flex items-center gap-2">
              <Sparkles className="w-4 h-4 text-indigo-400" />
              <span>
                Reaches{" "}
                <strong className="text-white font-bold">
                  {Math.round((data.total_potential_monthly_saving / metadata.savingsTarget) * 100)}%
                </strong>{" "}
                of your monthly target savings
              </span>
            </div>
          )}
        </div>
      </div>

      {/* Ranked list of opportunities */}
      <div className="space-y-4">
        <h2 className="text-base font-bold text-white tracking-tight uppercase tracking-wider mb-2">
          Ranked Recommendations
        </h2>

        {data.opportunities.map((item) => (
          <OpportunityCard
            key={item.id}
            opportunity={item}
            sessionId={params.sessionId}
          />
        ))}
      </div>
    </div>
  );
}
