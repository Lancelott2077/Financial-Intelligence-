import type { Metadata } from "next";
import { PagePlaceholder } from "@/components/layout/PagePlaceholder";
import { BarChart3 } from "lucide-react";

export const metadata: Metadata = {
  title: "Financial Snapshot | Financial Intelligence",
  description: "See an overview of your income, expenses, and savings from your uploaded statement.",
};

/**
 * Financial Snapshot Page — Step 2 of the user journey.
 *
 * Displays aggregated financial data: totals, category breakdown,
 * and monthly trends visualised with Recharts.
 *
 * TODO: Implement useSnapshot hook to fetch /api/v1/snapshot/{session_id}.
 * TODO: Implement SnapshotSummaryCards component (income, expenses, savings).
 * TODO: Implement CategoryBreakdownChart (pie / donut chart with Recharts).
 * TODO: Implement MonthlyTrendsChart (bar chart with Recharts).
 */
export default function SnapshotPage({
  params,
}: {
  params: { sessionId: string };
}) {
  return (
    <PagePlaceholder
      icon={<BarChart3 className="w-12 h-12 text-indigo-400" />}
      title="Your Financial Snapshot"
      description="Income, expenses, savings rate, and spending breakdown — all in one view."
      pageName="Financial Snapshot"
      nextStep="Implement useSnapshot, SnapshotSummaryCards, and chart components"
    />
  );
}
