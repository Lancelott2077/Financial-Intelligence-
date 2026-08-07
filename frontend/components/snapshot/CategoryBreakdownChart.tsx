"use client";

import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer } from "recharts";
import { formatCurrency, formatPercent } from "@/lib/utils";
import type { CategoryBreakdown } from "@/types/api";

interface CategoryBreakdownChartProps {
  data: CategoryBreakdown[];
}

const CATEGORY_COLORS: Record<string, string> = {
  food_and_dining: "#818cf8", // indigo
  shopping: "#ec4899",        // pink
  transport: "#3b82f6",       // blue
  entertainment: "#f59e0b",   // amber
  utilities: "#10b981",       // emerald
  groceries: "#a855f7",       // purple
  healthcare: "#ef4444",      // red
  education: "#06b6d4",       // cyan
  travel: "#14b8a6",          // teal
  transfer: "#6b7280",        // gray
  other: "#9ca3af",           // light gray
};

const CATEGORY_LABELS: Record<string, string> = {
  food_and_dining: "Food & Dining",
  shopping: "Shopping",
  transport: "Transport",
  entertainment: "Entertainment",
  utilities: "Utilities",
  groceries: "Groceries",
  healthcare: "Healthcare",
  education: "Education",
  travel: "Travel",
  transfer: "Transfer",
  other: "Other Spends",
};

export function CategoryBreakdownChart({ data }: CategoryBreakdownChartProps) {
  // Sort by total descending
  const sortedData = [...data].sort((a, b) => b.total - a.total);

  return (
    <div className="flex flex-col h-full justify-between">
      {/* Chart Visual */}
      <div className="relative w-full h-[240px] flex items-center justify-center">
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie
              data={sortedData}
              cx="50%"
              cy="50%"
              innerRadius={65}
              outerRadius={85}
              paddingAngle={4}
              dataKey="total"
              nameKey="category"
            >
              {sortedData.map((entry, index) => (
                <Cell
                  key={`cell-${index}`}
                  fill={CATEGORY_COLORS[entry.category] ?? CATEGORY_COLORS.other}
                  className="stroke-gray-950 stroke-[3px]"
                />
              ))}
            </Pie>
            <Tooltip
              content={({ active, payload }) => {
                if (active && payload && payload.length) {
                  const entry = payload[0].payload as CategoryBreakdown;
                  return (
                    <div className="glass px-3 py-2 rounded-lg border border-white/10 text-xs">
                      <p className="font-semibold text-white mb-0.5">
                        {CATEGORY_LABELS[entry.category] ?? entry.category}
                      </p>
                      <div className="flex gap-4 text-gray-400">
                        <span>{formatCurrency(entry.total)}</span>
                        <span className="text-indigo-400 font-medium">
                          {formatPercent(entry.percentage)}
                        </span>
                      </div>
                    </div>
                  );
                }
                return null;
              }}
            />
          </PieChart>
        </ResponsiveContainer>

        {/* Center overlay label */}
        <div className="absolute inset-0 flex flex-col items-center justify-center pointer-events-none">
          <span className="text-xs text-gray-500 font-medium uppercase tracking-wider">
            Top Category
          </span>
          <span className="text-lg font-bold text-white mt-0.5">
            {sortedData[0]
              ? CATEGORY_LABELS[sortedData[0].category] ?? sortedData[0].category
              : "N/A"}
          </span>
        </div>
      </div>

      {/* Legend list */}
      <div className="mt-4 space-y-2 max-h-[160px] overflow-y-auto pr-1">
        {sortedData.map((item, idx) => {
          const color = CATEGORY_COLORS[item.category] ?? CATEGORY_COLORS.other;
          return (
            <div key={idx} className="flex items-center justify-between text-xs">
              <div className="flex items-center gap-2">
                <span
                  className="w-2.5 h-2.5 rounded-full shrink-0"
                  style={{ backgroundColor: color }}
                />
                <span className="text-gray-400 font-medium truncate max-w-[120px]">
                  {CATEGORY_LABELS[item.category] ?? item.category}
                </span>
              </div>
              <div className="flex items-center gap-3">
                <span className="text-gray-300 font-semibold">
                  {formatCurrency(item.total)}
                </span>
                <span className="text-gray-500 w-8 text-right font-medium">
                  {formatPercent(item.percentage)}
                </span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
