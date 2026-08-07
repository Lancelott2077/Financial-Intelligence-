"use client";

import { useState } from "react";
import {
  Clock,
  TrendingDown,
  Anchor,
  Wallet,
  Pause,
  HelpCircle,
  ChevronDown,
  ChevronUp,
  AlertTriangle,
} from "lucide-react";
import { formatCurrency } from "@/lib/utils";
import { BIAS_DISPLAY_META } from "@/types/behaviours";
import type { BehaviourDetail } from "@/types/api";

interface BiasCardProps {
  bias: BehaviourDetail;
}

// Icon mapper for the dynamic lucide string names
const iconMap: Record<string, React.ComponentType<{ className?: string }>> = {
  Clock,
  TrendingDown,
  Anchor,
  Wallet,
  PauseCircle: Pause, // Map PauseCircle to Pause or similar
};

export function BiasCard({ bias }: BiasCardProps) {
  const [isOpen, setIsOpen] = useState(false);
  const meta = BIAS_DISPLAY_META[bias.bias_type];
  
  const IconComponent = meta ? iconMap[meta.iconName] : HelpCircle;
  const colorClass = meta ? meta.colour : "bg-gray-500";

  // Severity color classes
  const severityClasses = {
    high: "bg-rose-500/10 border-rose-500/20 text-rose-400",
    medium: "bg-amber-500/10 border-amber-500/20 text-amber-400",
    low: "bg-blue-500/10 border-blue-500/20 text-blue-400",
  }[bias.severity] ?? "bg-gray-500/10 border-gray-500/20 text-gray-400";

  return (
    <div className="glass rounded-xl border border-white/5 bg-white/[0.01] overflow-hidden transition-all duration-200">
      {/* Top Header Card */}
      <div
        onClick={() => setIsOpen(!isOpen)}
        className="p-5 flex items-start gap-4 cursor-pointer hover:bg-white/[0.02] transition-colors select-none"
      >
        {/* Dynamic Bias Icon */}
        <div className={`p-3 rounded-xl shrink-0 text-white ${colorClass}`}>
          <IconComponent className="w-5 h-5" />
        </div>

        {/* Info Grid */}
        <div className="flex-1 min-w-0 space-y-1.5">
          <div className="flex flex-wrap items-center gap-2">
            <h3 className="text-base font-bold text-white tracking-tight">
              {bias.display_name}
            </h3>
            <span className={`px-2 py-0.5 rounded-full text-[10px] font-semibold border uppercase tracking-wider ${severityClasses}`}>
              {bias.severity} Severity
            </span>
          </div>

          <p className="text-sm text-gray-400 leading-relaxed font-medium">
            {bias.summary}
          </p>

          {/* Subtext and confidence indicators */}
          <div className="flex items-center gap-4 pt-1 text-xs text-gray-500">
            <div className="flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-indigo-500" />
              <span>Confidence: <strong className="text-gray-300 font-semibold">{Math.round(bias.confidence * 100)}%</strong></span>
            </div>
            {bias.evidence.length > 0 && (
              <div className="flex items-center gap-1.5">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-500" />
                <span>Evidence Count: <strong className="text-gray-300 font-semibold">{bias.evidence.length}</strong></span>
              </div>
            )}
          </div>
        </div>

        {/* Toggle Chevron */}
        <div className="p-1.5 rounded-lg bg-white/5 border border-white/5 text-gray-400 shrink-0">
          {isOpen ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
        </div>
      </div>

      {/* Expandable Evidence Drawer */}
      {isOpen && (
        <div className="border-t border-white/5 bg-white/[0.005] p-5 space-y-4 animate-fade-in-up">
          <div className="flex items-center gap-2 text-xs font-semibold text-gray-400 uppercase tracking-wider">
            <AlertTriangle className="w-4 h-4 text-indigo-400" />
            <span>Transaction Evidence and Analysis</span>
          </div>

          {bias.evidence.length === 0 ? (
            <p className="text-xs text-gray-500 italic">No direct transaction evidence recorded.</p>
          ) : (
            <div className="space-y-3">
              {bias.evidence.map((item, idx) => {
                const isDebit = item.amount < 0;
                return (
                  <div
                    key={idx}
                    className="p-3.5 rounded-xl border border-white/5 bg-white/[0.01] flex flex-col md:flex-row md:items-start justify-between gap-3 text-xs"
                  >
                    {/* Left: Date, category and detail explanations */}
                    <div className="space-y-1.5 max-w-xl">
                      <div className="flex items-center gap-2">
                        <span className="text-[10px] text-gray-500 font-medium">
                          {new Date(item.date).toLocaleDateString("en-US", {
                            month: "short",
                            day: "numeric",
                            year: "numeric",
                          })}
                        </span>
                        <span className="w-1 h-1 rounded-full bg-gray-700" />
                        <span className="text-gray-300 font-semibold truncate max-w-[200px]">
                          {item.description}
                        </span>
                        <span className="text-[10px] bg-white/5 border border-white/5 px-2 py-0.5 rounded text-gray-400 uppercase font-medium">
                          {item.category.replace(/_/g, " ")}
                        </span>
                      </div>
                      <p className="text-gray-400 leading-relaxed font-medium">
                        {item.explanation}
                      </p>
                    </div>

                    {/* Right: Currency flow */}
                    <div className="md:text-right shrink-0">
                      <span className={`font-bold text-sm ${isDebit ? "text-rose-400" : "text-emerald-400"}`}>
                        {formatCurrency(item.amount)}
                      </span>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
