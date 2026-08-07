"use client";

import { Check, Clock, Ban } from "lucide-react";
import { formatCurrency } from "@/lib/utils";
import type { PlanItem as PlanItemType } from "@/types/api";

interface PlanItemProps {
  item: PlanItemType;
  onToggleComplete: (id: number) => void;
  onToggleSkip: (id: number) => void;
}

export function PlanItem({ item, onToggleComplete, onToggleSkip }: PlanItemProps) {
  const isCompleted = item.status === "completed";
  const isSkipped = item.status === "skipped";

  // Priority color tags
  const priorityClasses = {
    high: "bg-rose-500/10 border-rose-500/20 text-rose-400",
    medium: "bg-amber-500/10 border-amber-500/20 text-amber-400",
    low: "bg-blue-500/10 border-blue-500/20 text-blue-400",
  }[item.priority] ?? "bg-gray-500/10 border-gray-500/20 text-gray-400";

  return (
    <div
      className={`glass rounded-xl p-4 border transition-all duration-200 flex items-start gap-4 ${
        isCompleted
          ? "border-emerald-500/20 bg-emerald-500/[0.005] opacity-60"
          : isSkipped
          ? "border-white/5 bg-white/[0.002] opacity-40"
          : "border-white/5 bg-white/[0.01] hover:border-white/10"
      }`}
    >
      {/* Checkbox circle trigger */}
      <button
        onClick={() => onToggleComplete(item.id)}
        disabled={isSkipped}
        className={`w-5 h-5 rounded-full border flex items-center justify-center shrink-0 mt-0.5 transition-all ${
          isCompleted
            ? "bg-emerald-500/15 border-emerald-500/40 text-emerald-400"
            : isSkipped
            ? "border-gray-800 bg-transparent text-transparent cursor-not-allowed"
            : "border-white/20 bg-white/5 hover:border-indigo-500/50 text-transparent"
        }`}
      >
        <Check className="w-3.5 h-3.5" />
      </button>

      {/* Task Details Info */}
      <div className="flex-1 min-w-0 space-y-1.5">
        <div className="flex flex-wrap items-center gap-2">
          <h4
            className={`text-sm font-bold text-white tracking-tight truncate max-w-[280px] md:max-w-md ${
              isCompleted ? "line-through text-gray-500 decoration-gray-700" : ""
            }`}
          >
            {item.title}
          </h4>
          <span className={`px-2 py-0.5 rounded-full text-[9px] font-semibold border uppercase tracking-wider ${priorityClasses}`}>
            {item.priority}
          </span>
        </div>

        <p
          className={`text-xs text-gray-400 leading-relaxed font-medium ${
            isCompleted ? "line-through text-gray-600 decoration-gray-800" : ""
          }`}
        >
          {item.description}
        </p>

        {/* Task Footer metadata */}
        <div className="flex items-center gap-4 pt-1 text-[10px] text-gray-500 font-semibold uppercase">
          <div className="flex items-center gap-1">
            <Clock className="w-3.5 h-3.5 text-indigo-400" />
            <span>
              Target:{" "}
              <strong className="text-gray-300">
                {item.target_date
                  ? new Date(item.target_date).toLocaleDateString("en-US", {
                      month: "short",
                      day: "numeric",
                    })
                  : "Asap"}
              </strong>
            </span>
          </div>

          <div className="flex items-center gap-1">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-500" />
            <span className="text-emerald-400">
              Est Saving: {formatCurrency(item.estimated_monthly_saving)}
            </span>
          </div>
        </div>
      </div>

      {/* Skip/Pause Actions */}
      <div className="shrink-0 self-center">
        <button
          onClick={() => onToggleSkip(item.id)}
          disabled={isCompleted}
          className={`p-1.5 border rounded-lg transition-all ${
            isSkipped
              ? "bg-amber-500/10 border-amber-500/20 text-amber-400"
              : "bg-white/5 border-white/5 text-gray-500 hover:text-white hover:bg-white/10"
          }`}
          title={isSkipped ? "Restore Task" : "Skip Task"}
        >
          <Ban className="w-3.5 h-3.5" />
        </button>
      </div>
    </div>
  );
}
