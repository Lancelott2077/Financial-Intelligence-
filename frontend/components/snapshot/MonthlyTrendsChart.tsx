"use client";

import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Legend,
} from "recharts";
import { formatCurrency } from "@/lib/utils";
import type { MonthlyTrend } from "@/types/api";

interface MonthlyTrendsChartProps {
  data: MonthlyTrend[];
}

/** Format month string e.g. "2024-01" to "Jan" or "Jan 24" */
function formatMonthLabel(monthStr: string): string {
  try {
    const [year, month] = monthStr.split("-");
    const date = new Date(parseInt(year), parseInt(month) - 1, 1);
    return date.toLocaleDateString("en-US", { month: "short", year: "2-digit" });
  } catch {
    return monthStr;
  }
}

export function MonthlyTrendsChart({ data }: MonthlyTrendsChartProps) {
  return (
    <div className="w-full h-[320px] min-h-[300px]">
      <ResponsiveContainer width="100%" height="100%">
        <AreaChart
          data={data}
          margin={{ top: 10, right: 10, left: -20, bottom: 0 }}
        >
          <defs>
            {/* Income Gradient */}
            <linearGradient id="incomeGrad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="rgb(99, 102, 241)" stopOpacity={0.25} />
              <stop offset="95%" stopColor="rgb(99, 102, 241)" stopOpacity={0.01} />
            </linearGradient>
            {/* Expenses Gradient */}
            <linearGradient id="expenseGrad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="rgb(244, 63, 94)" stopOpacity={0.2} />
              <stop offset="95%" stopColor="rgb(244, 63, 94)" stopOpacity={0.01} />
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
              if (active && payload && payload.length === 2) {
                const inc = payload[0].value as number;
                const exp = payload[1].value as number;
                const net = inc - exp;
                const dateLabel = formatMonthLabel(payload[0].payload.month);

                return (
                  <div className="glass p-3 rounded-xl border border-white/10 text-xs space-y-2">
                    <p className="font-semibold text-white border-b border-white/5 pb-1">
                      {dateLabel} Summary
                    </p>
                    <div className="space-y-1">
                      <div className="flex justify-between gap-6">
                        <span className="text-gray-400">Total Income:</span>
                        <span className="text-indigo-400 font-semibold">
                          {formatCurrency(inc)}
                        </span>
                      </div>
                      <div className="flex justify-between gap-6">
                        <span className="text-gray-400">Total Expenses:</span>
                        <span className="text-rose-400 font-semibold">
                          {formatCurrency(exp)}
                        </span>
                      </div>
                      <div className="flex justify-between gap-6 border-t border-white/5 pt-1">
                        <span className="text-gray-400">Net Surplus:</span>
                        <span
                          className={`font-bold ${
                            net >= 0 ? "text-emerald-400" : "text-rose-400"
                          }`}
                        >
                          {formatCurrency(net)}
                        </span>
                      </div>
                    </div>
                  </div>
                );
              }
              return null;
            }}
          />

          <Legend
            verticalAlign="top"
            height={36}
            iconType="circle"
            iconSize={8}
            content={({ payload }) => (
              <div className="flex justify-end gap-6 text-xs text-gray-400 mb-2">
                {payload?.map((entry, index) => (
                  <div key={`legend-${index}`} className="flex items-center gap-2">
                    <span
                      className="w-2 h-2 rounded-full shrink-0"
                      style={{
                        backgroundColor:
                          entry.value === "Income"
                            ? "rgb(99, 102, 241)"
                            : "rgb(244, 63, 94)",
                      }}
                    />
                    <span className="font-medium text-gray-300">
                      {entry.value}
                    </span>
                  </div>
                ))}
              </div>
            )}
          />

          <Area
            name="Income"
            type="monotone"
            dataKey="income"
            stroke="rgb(99, 102, 241)"
            strokeWidth={2}
            fillOpacity={1}
            fill="url(#incomeGrad)"
          />

          <Area
            name="Expenses"
            type="monotone"
            dataKey="expenses"
            stroke="rgb(244, 63, 94)"
            strokeWidth={2}
            fillOpacity={1}
            fill="url(#expenseGrad)"
          />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
}
