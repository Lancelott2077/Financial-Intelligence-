"use client";

import Link from "next/link";
import {
  Utensils,
  ShoppingBag,
  Car,
  Tv,
  Lightbulb,
  Activity,
  GraduationCap,
  Plane,
  ArrowRightLeft,
  HelpCircle,
  Sparkles,
} from "lucide-react";
import { formatCurrency } from "@/lib/utils";
import type { SavingOpportunity } from "@/types/api";

interface OpportunityCardProps {
  opportunity: SavingOpportunity;
  sessionId: string;
}

const CATEGORY_ICONS: Record<string, React.ComponentType<{ className?: string }>> = {
  food_and_dining: Utensils,
  shopping: ShoppingBag,
  transport: Car,
  entertainment: Tv,
  utilities: Lightbulb,
  healthcare: Activity,
  education: GraduationCap,
  travel: Plane,
  transfer: ArrowRightLeft,
  other: HelpCircle,
};

const CATEGORY_LABELS: Record<string, string> = {
  food_and_dining: "Food & Dining",
  shopping: "Shopping",
  transport: "Transport",
  entertainment: "Entertainment",
  utilities: "Utilities",
  healthcare: "Healthcare",
  education: "Education",
  travel: "Travel",
  transfer: "Transfer",
  other: "Other",
};

export function OpportunityCard({ opportunity, sessionId }: OpportunityCardProps) {
  const IconComponent = CATEGORY_ICONS[opportunity.category] ?? HelpCircle;

  // Difficulty badge colors
  const difficultyClasses = {
    high: "bg-rose-500/10 border-rose-500/20 text-rose-400",
    medium: "bg-amber-500/10 border-amber-500/20 text-amber-400",
    low: "bg-emerald-500/10 border-emerald-500/20 text-emerald-400",
  }[opportunity.difficulty] ?? "bg-gray-500/10 border-gray-500/20 text-gray-400";

  // Calculate percentage ratios for the spend comparison bar
  const maxSpend = Math.max(opportunity.current_monthly_spend, 1);
  const suggestedPercent = Math.min((opportunity.suggested_monthly_spend / maxSpend) * 100, 100);
  const savingPercent = 100 - suggestedPercent;

  return (
    <div className="glass rounded-xl p-5 border border-white/5 bg-white/[0.01] hover:border-white/10 transition-all duration-200 space-y-4">
      {/* Header Info */}
      <div className="flex items-start justify-between gap-4">
        <div className="flex items-center gap-3">
          <div className="p-2.5 rounded-lg bg-white/5 border border-white/5 text-indigo-400">
            <IconComponent className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-sm font-bold text-white tracking-tight">
              {opportunity.title}
            </h3>
            <span className="text-[10px] text-gray-500 font-semibold uppercase tracking-wider">
              {CATEGORY_LABELS[opportunity.category] ?? opportunity.category}
            </span>
          </div>
        </div>

        {/* Badges */}
        <div className="flex items-center gap-2">
          <span className={`px-2 py-0.5 rounded-full text-[10px] font-semibold border uppercase tracking-wider ${difficultyClasses}`}>
            {opportunity.difficulty} Effort
          </span>
        </div>
      </div>

      {/* Explanatory rationale */}
      <p className="text-xs text-gray-400 leading-relaxed font-medium">
        {opportunity.rationale}
      </p>

      {/* Spend comparison meters */}
      <div className="space-y-2 border-t border-white/5 pt-4">
        <div className="flex justify-between text-xs text-gray-400 font-medium">
          <span>Monthly Spend Comparison</span>
          <span className="text-emerald-400 font-bold">
            +{formatCurrency(opportunity.estimated_monthly_saving)}/mo potential savings
          </span>
        </div>

        {/* Custom progress comparison meter */}
        <div className="h-2 w-full bg-white/5 rounded-full overflow-hidden flex">
          {/* Suggested spend (solid indigo) */}
          <div
            className="h-full bg-indigo-500 transition-all duration-300"
            style={{ width: `${suggestedPercent}%` }}
          />
          {/* Saved spend (emerald striped or glow) */}
          <div
            className="h-full bg-emerald-500/40 transition-all duration-300 relative"
            style={{ width: `${savingPercent}%` }}
          />
        </div>

        {/* Spend tags */}
        <div className="flex justify-between text-[10px] text-gray-500 font-semibold">
          <div className="flex gap-4">
            <span>
              Current: <strong className="text-gray-300 font-bold">{formatCurrency(opportunity.current_monthly_spend)}</strong>
            </span>
            <span>
              Suggested: <strong className="text-indigo-400 font-bold">{formatCurrency(opportunity.suggested_monthly_spend)}</strong>
            </span>
          </div>
          <span className="text-emerald-400 font-bold">
            Cut by {Math.round(savingPercent)}%
          </span>
        </div>
      </div>

      {/* Action Footer */}
      <div className="flex justify-end pt-2 border-t border-white/5">
        <Link
          href={`/simulation/${sessionId}?opportunityId=${opportunity.id}&category=${opportunity.category}&change=${Math.round(
            ((opportunity.suggested_monthly_spend - opportunity.current_monthly_spend) / maxSpend) * 100
          )}`}
          className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-400 border border-indigo-500/20 hover:border-indigo-500/30 text-[10px] font-bold uppercase tracking-wider transition-all group"
        >
          <Sparkles className="w-3.5 h-3.5" />
          <span>Simulate this change</span>
        </Link>
      </div>
    </div>
  );
}
