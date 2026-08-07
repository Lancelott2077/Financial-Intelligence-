import type { Metadata } from "next";
import { PagePlaceholder } from "@/components/layout/PagePlaceholder";
import { PiggyBank } from "lucide-react";

export const metadata: Metadata = {
  title: "Savings Opportunities | Financial Intelligence",
  description: "Discover personalised opportunities to reduce spending and grow your savings.",
};

/**
 * Savings Opportunities Page — Step 4 of the user journey.
 *
 * Displays ranked savings recommendations with estimated monthly impact
 * and difficulty ratings.
 *
 * TODO: Implement useSavings hook to fetch /api/v1/savings/{session_id}.
 * TODO: Implement SavingsCard component with projected saving and difficulty badge.
 * TODO: Implement SavingsImpactChart (Recharts bar chart) for visual comparison.
 * TODO: Add "Simulate this change" CTA linking to /simulation.
 */
export default function SavingsPage({
  params: _params,
}: {
  params: { sessionId: string };
}) {
  return (
    <PagePlaceholder
      icon={<PiggyBank className="w-12 h-12 text-indigo-400" />}
      title="Savings Opportunities"
      description="Here are the top changes you can make to meaningfully improve your finances."
      pageName="Savings Opportunities"
      nextStep="Implement useSavings, SavingsCard, and SavingsImpactChart"
    />
  );
}
