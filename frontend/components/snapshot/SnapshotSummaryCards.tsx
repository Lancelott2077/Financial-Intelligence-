"use client";

import { ArrowUpRight, ArrowDownRight, PiggyBank, Percent } from "lucide-react";
import { formatCurrency, formatPercent } from "@/lib/utils";

interface SnapshotSummaryCardsProps {
  totalIncome: number;
  totalExpenses: number;
  netSavings: number;
  savingsRate: number;
}

export function SnapshotSummaryCards({
  totalIncome,
  totalExpenses,
  netSavings,
  savingsRate,
}: SnapshotSummaryCardsProps) {
  const cards = [
    {
      title: "Total Income",
      value: formatCurrency(totalIncome),
      icon: <ArrowUpRight className="w-5 h-5 text-indigo-400" />,
      description: "Total earnings statement flow",
      glowClass: "group-hover:border-indigo-500/30 group-hover:shadow-[0_0_20px_rgba(99,102,241,0.15)]",
      textColor: "text-indigo-400",
    },
    {
      title: "Total Expenses",
      value: formatCurrency(totalExpenses),
      icon: <ArrowDownRight className="w-5 h-5 text-rose-400" />,
      description: "Debit transactions & transfers",
      glowClass: "group-hover:border-rose-500/30 group-hover:shadow-[0_0_20px_rgba(244,63,94,0.15)]",
      textColor: "text-rose-400",
    },
    {
      title: "Net Savings",
      value: formatCurrency(netSavings),
      icon: <PiggyBank className="w-5 h-5 text-emerald-400" />,
      description: "Remaining investable surplus",
      glowClass: "group-hover:border-emerald-500/30 group-hover:shadow-[0_0_20px_rgba(16,185,129,0.15)]",
      textColor: "text-emerald-400",
    },
    {
      title: "Savings Rate",
      value: formatPercent(savingsRate),
      icon: <Percent className="w-5 h-5 text-amber-400" />,
      description: "Efficiency score of spending",
      glowClass: "group-hover:border-amber-500/30 group-hover:shadow-[0_0_20px_rgba(245,158,11,0.15)]",
      textColor: "text-amber-400",
    },
  ];

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      {cards.map((card, idx) => (
        <div
          key={idx}
          className={`group glass rounded-xl p-5 border border-white/5 bg-white/[0.02] transition-all duration-300 ${card.glowClass}`}
        >
          <div className="flex items-center justify-between mb-3">
            <span className="text-sm font-medium text-gray-400 group-hover:text-gray-300 transition-colors">
              {card.title}
            </span>
            <div className="p-2 rounded-lg bg-white/5 border border-white/5 group-hover:bg-white/10 transition-all">
              {card.icon}
            </div>
          </div>

          <div className="flex flex-col">
            <span className="text-2xl font-bold tracking-tight text-white mb-1">
              {card.value}
            </span>
            <span className="text-xs text-gray-500 line-clamp-1">
              {card.description}
            </span>
          </div>
        </div>
      ))}
    </div>
  );
}
