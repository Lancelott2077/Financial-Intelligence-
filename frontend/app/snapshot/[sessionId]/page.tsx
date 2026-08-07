"use client";

import Link from "next/link";
import { ArrowRight, AlertCircle, RefreshCw, BarChart3, TrendingUp } from "lucide-react";
import { useSnapshot } from "@/hooks/useSnapshot";
import { SnapshotSummaryCards } from "@/components/snapshot/SnapshotSummaryCards";
import { CategoryBreakdownChart } from "@/components/snapshot/CategoryBreakdownChart";
import { MonthlyTrendsChart } from "@/components/snapshot/MonthlyTrendsChart";

export default function SnapshotPage({
  params,
}: {
  params: { sessionId: string };
}) {
  const { data, isLoading, error, refetch } = useSnapshot(params.sessionId);

  // Format date strings helper
  const formatDate = (dateStr: string | null) => {
    if (!dateStr) return "";
    return new Date(dateStr).toLocaleDateString("en-US", {
      month: "short",
      day: "numeric",
      year: "numeric",
    });
  };

  // Loading skeleton state
  if (isLoading) {
    return (
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 animate-pulse">
        {/* Header Skeleton */}
        <div className="space-y-3">
          <div className="h-8 w-64 bg-white/5 rounded" />
          <div className="h-4 w-96 bg-white/5 rounded" />
        </div>

        {/* KPI Cards Skeletons */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {[...Array(4)].map((_, i) => (
            <div key={i} className="glass rounded-xl p-5 border border-white/5 bg-white/[0.01] h-[108px] space-y-4">
              <div className="flex justify-between">
                <div className="h-4 w-24 bg-white/5 rounded" />
                <div className="h-8 w-8 bg-white/5 rounded-lg" />
              </div>
              <div className="h-6 w-32 bg-white/5 rounded" />
            </div>
          ))}
        </div>

        {/* Charts Skeletons */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="glass rounded-xl p-6 border border-white/5 bg-white/[0.01] lg:col-span-2 h-[400px]">
            <div className="h-6 w-40 bg-white/5 rounded mb-6" />
            <div className="h-[300px] bg-white/[0.02] rounded-lg" />
          </div>
          <div className="glass rounded-xl p-6 border border-white/5 bg-white/[0.01] h-[400px]">
            <div className="h-6 w-40 bg-white/5 rounded mb-6" />
            <div className="h-[300px] bg-white/[0.02] rounded-lg" />
          </div>
        </div>
      </div>
    );
  }

  // Error boundary/retry state
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
            <h1 className="text-xl font-bold text-gray-100">Failed to load snapshot</h1>
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
  if (!data) {
    return (
      <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center p-8">
        <div className="glass rounded-2xl p-8 max-w-md w-full text-center space-y-6">
          <div className="flex justify-center">
            <div className="p-3 bg-white/5 rounded-full border border-white/10 text-indigo-400">
              <BarChart3 className="w-10 h-10" />
            </div>
          </div>
          <div className="space-y-2">
            <h1 className="text-xl font-bold text-gray-100">No snapshot data available</h1>
            <p className="text-sm text-gray-400 leading-relaxed">
              We couldn&apos;t find financial data for this session. Please return and upload a statement.
            </p>
          </div>
          <Link
            href="/upload"
            className="w-full inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-medium shadow-lg transition-all"
          >
            Go to Upload
          </Link>
        </div>
      </div>
    );
  }

  const {
    total_income,
    total_expenses,
    net_savings,
    savings_rate,
    date_range_start,
    date_range_end,
    category_breakdown,
    monthly_trends,
  } = data;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 animate-fade-in-up">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-white/5 pb-6">
        <div>
          <h1 className="text-3xl font-extrabold text-white tracking-tight">
            Financial Snapshot
          </h1>
          <p className="text-sm text-gray-400 mt-1">
            {date_range_start && date_range_end ? (
              <>
                Statement analysis period:{" "}
                <span className="text-indigo-400 font-semibold">
                  {formatDate(date_range_start)}
                </span>{" "}
                to{" "}
                <span className="text-indigo-400 font-semibold">
                  {formatDate(date_range_end)}
                </span>
              </>
            ) : (
              "Overview of income and expenses parsed from uploaded CSV."
            )}
          </p>
        </div>

        {/* CTA to Behaviour Report */}
        <Link
          href={`/behaviours/${params.sessionId}`}
          className="inline-flex items-center gap-2 px-4 py-2 bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-400 border border-indigo-500/20 hover:border-indigo-500/30 rounded-xl text-sm font-medium transition-all group"
        >
          <span>View Behaviour Report</span>
          <ArrowRight className="w-4 h-4 group-hover:translate-x-0.5 transition-transform" />
        </Link>
      </div>

      {/* KPI Cards section */}
      <SnapshotSummaryCards
        totalIncome={total_income}
        totalExpenses={total_expenses}
        netSavings={net_savings}
        savingsRate={savings_rate}
      />

      {/* Grid of charts */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Monthly Trends (Income vs Expenses) */}
        <div className="glass rounded-xl p-6 border border-white/5 bg-white/[0.01] lg:col-span-2 space-y-4 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between border-b border-white/5 pb-3">
              <div className="flex items-center gap-2">
                <TrendingUp className="w-5 h-5 text-indigo-400" />
                <h2 className="text-base font-bold text-white">Monthly Cash Flow Trends</h2>
              </div>
              <span className="text-[10px] uppercase font-semibold text-indigo-400 bg-indigo-500/10 border border-indigo-500/20 px-2 py-0.5 rounded-full">
                6-Month Outlook
              </span>
            </div>
            <p className="text-xs text-gray-500 mt-2">
              Monthly aggregate values for Income (Indigo) compared directly to Expenses (Rose).
            </p>
          </div>
          <MonthlyTrendsChart data={monthly_trends} />
        </div>

        {/* Category Breakdown (Donut) */}
        <div className="glass rounded-xl p-6 border border-white/5 bg-white/[0.01] space-y-4 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between border-b border-white/5 pb-3">
              <div className="flex items-center gap-2">
                <BarChart3 className="w-5 h-5 text-indigo-400" />
                <h2 className="text-base font-bold text-white">Spending by Category</h2>
              </div>
            </div>
            <p className="text-xs text-gray-500 mt-2">
              Breakdown of total debit transactions distributed by detected categories.
            </p>
          </div>
          <CategoryBreakdownChart data={category_breakdown} />
        </div>
      </div>
    </div>
  );
}
