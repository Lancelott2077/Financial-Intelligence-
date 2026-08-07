"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { ArrowRight, AlertCircle, RefreshCw, Brain, Sparkles, ShieldAlert, Award } from "lucide-react";
import { useBehaviours } from "@/hooks/useBehaviours";
import { BiasCard } from "@/components/behaviours/BiasCard";
import type { SeverityLevel } from "@/types/api";

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

export default function BehaviourReportPage({
  params,
}: {
  params: { sessionId: string };
}) {
  const { data, isLoading, error, refetch } = useBehaviours(params.sessionId);
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
      <div className="max-w-4xl mx-auto px-4 py-8 space-y-8 animate-pulse">
        {/* Header Skeleton */}
        <div className="space-y-3">
          <div className="h-8 w-64 bg-white/5 rounded" />
          <div className="h-4 w-96 bg-white/5 rounded" />
        </div>

        {/* Dashboard Cards Skeleton */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {[...Array(3)].map((_, i) => (
            <div key={i} className="glass rounded-xl p-5 border border-white/5 bg-white/[0.01] h-[100px]" />
          ))}
        </div>

        {/* List Skeleton */}
        <div className="space-y-4">
          {[...Array(2)].map((_, i) => (
            <div key={i} className="glass rounded-xl p-5 border border-white/5 bg-white/[0.01] h-[80px]" />
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
            <h1 className="text-xl font-bold text-gray-100">Failed to load behaviours</h1>
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

  // Empty state / Fallback when no biases are detected
  const hasNoData = !data || data.behaviours.length === 0;

  if (hasNoData) {
    return (
      <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center p-8 animate-fade-in-up">
        <div className="glass rounded-2xl p-10 max-w-md w-full text-center space-y-6">
          <div className="flex justify-center">
            <div className="p-4 bg-emerald-500/10 rounded-full border border-emerald-500/20 text-emerald-400 inline-block">
              <Award className="w-12 h-12" />
            </div>
          </div>
          <div className="space-y-2">
            <h1 className="text-2xl font-bold text-white">No Biases Detected</h1>
            <p className="text-sm text-gray-400 leading-relaxed">
              Congratulations! Our AI analysis detected no cognitive biases in your bank statement. You are spending rationally relative to your parameters.
            </p>
          </div>
          <Link
            href={`/savings/${params.sessionId}`}
            className="w-full inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold shadow-lg transition-all"
          >
            Go to Savings Plan
          </Link>
        </div>
      </div>
    );
  }

  // Compute Overall Risk score level
  const hasHigh = data.behaviours.some((b) => b.severity === "high");
  const hasMedium = data.behaviours.some((b) => b.severity === "medium");
  const overallRisk: SeverityLevel = hasHigh ? "high" : hasMedium ? "medium" : "low";

  // Find dominant bias (highest confidence score)
  const dominantBias = [...data.behaviours].sort((a, b) => b.confidence - a.confidence)[0];

  const riskLabelColors = {
    high: "text-rose-400 bg-rose-500/10 border-rose-500/25",
    medium: "text-amber-400 bg-amber-500/10 border-amber-500/25",
    low: "text-blue-400 bg-blue-500/10 border-blue-500/25",
  }[overallRisk];

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 space-y-8 animate-fade-in-up">
      {/* Header section */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-white/5 pb-6">
        <div className="space-y-1">
          <h1 className="text-3xl font-extrabold text-white tracking-tight flex items-center gap-2">
            Behaviour Intelligence
          </h1>
          <p className="text-sm text-gray-400">
            {metadata ? (
              <>
                Custom analysis aligned to your goal:{" "}
                <span className="text-indigo-400 font-semibold">
                  {GOAL_LABELS[metadata.goal] ?? metadata.goal}
                </span>
              </>
            ) : (
              "Detailed report on identified behavioral biases and financial tendencies."
            )}
          </p>
        </div>

        <Link
          href={`/savings/${params.sessionId}`}
          className="inline-flex items-center gap-2 px-4 py-2 bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-400 border border-indigo-500/20 hover:border-indigo-500/30 rounded-xl text-sm font-medium transition-all group shrink-0"
        >
          <span>Savings Opportunities</span>
          <ArrowRight className="w-4 h-4 group-hover:translate-x-0.5 transition-transform" />
        </Link>
      </div>

      {/* Intelligence Dashboard Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {/* Card 1: Active Biases */}
        <div className="glass rounded-xl p-5 border border-white/5 bg-white/[0.01] flex flex-col justify-between">
          <span className="text-xs font-semibold text-gray-500 uppercase tracking-wider">
            Detected Tendencies
          </span>
          <div className="flex items-baseline gap-1.5 mt-2">
            <span className="text-3xl font-extrabold text-white">
              {data.behaviours.length}
            </span>
            <span className="text-xs text-gray-400">active biases</span>
          </div>
        </div>

        {/* Card 2: Dominant Bias */}
        <div className="glass rounded-xl p-5 border border-white/5 bg-white/[0.01] flex flex-col justify-between">
          <span className="text-xs font-semibold text-gray-500 uppercase tracking-wider">
            Dominant Bias
          </span>
          <div className="flex items-center gap-2 mt-2">
            <Brain className="w-5 h-5 text-indigo-400" />
            <span className="text-sm font-bold text-white truncate">
              {dominantBias.display_name}
            </span>
          </div>
        </div>

        {/* Card 3: Overall Risk Level */}
        <div className="glass rounded-xl p-5 border border-white/5 bg-white/[0.01] flex flex-col justify-between">
          <span className="text-xs font-semibold text-gray-500 uppercase tracking-wider">
            Risk Profile
          </span>
          <div className="mt-2">
            <span className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold border uppercase tracking-wider ${riskLabelColors}`}>
              <ShieldAlert className="w-3.5 h-3.5" />
              {overallRisk} Risk
            </span>
          </div>
        </div>
      </div>

      {/* Biases Stack */}
      <div className="space-y-4">
        <h2 className="text-lg font-bold text-white tracking-tight flex items-center gap-2 mb-2">
          <Sparkles className="w-4 h-4 text-indigo-400" />
          Bias Breakdown
        </h2>

        {data.behaviours.map((bias) => (
          <BiasCard key={bias.id} bias={bias} />
        ))}
      </div>

      {/* Bottom actionable CTA */}
      <div className="glass rounded-2xl p-6 border border-indigo-500/10 bg-indigo-500/[0.01] flex flex-col md:flex-row items-center justify-between gap-4">
        <div className="space-y-1">
          <h3 className="text-sm font-bold text-white">Ready to tackle these behaviors?</h3>
          <p className="text-xs text-gray-400">
            View ranked saving recommendations mapped directly to your financial profile.
          </p>
        </div>
        <Link
          href={`/savings/${params.sessionId}`}
          className="w-full md:w-auto inline-flex items-center justify-center gap-2 px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow-lg hover:shadow-indigo-500/25 transition-all shrink-0"
        >
          <span>Develop Savings Strategy</span>
          <ArrowRight className="w-4 h-4" />
        </Link>
      </div>
    </div>
  );
}
