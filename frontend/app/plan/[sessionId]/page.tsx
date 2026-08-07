import type { Metadata } from "next";
import { PagePlaceholder } from "@/components/layout/PagePlaceholder";
import { CheckSquare } from "lucide-react";

export const metadata: Metadata = {
  title: "Action Plan | Financial Intelligence",
  description: "Your personalised financial action plan — prioritised steps to improve your finances.",
};

/**
 * Action Plan Page — Step 7 of the user journey.
 *
 * Displays a prioritised, time-bound list of financial actions
 * derived from detected behaviours and savings opportunities.
 *
 * TODO: Implement usePlan hook to fetch /api/v1/plan/{session_id}.
 * TODO: Implement PlanItem component with priority badge, target date, and status toggle.
 * TODO: Implement PlanProgressBar showing completion percentage.
 * TODO: Add "Mark Complete" and "Skip" actions for each item.
 */
export default function ActionPlanPage({
  params: _params,
}: {
  params: { sessionId: string };
}) {
  return (
    <PagePlaceholder
      icon={<CheckSquare className="w-12 h-12 text-indigo-400" />}
      title="Your Action Plan"
      description="A prioritised list of steps to transform your financial habits — one action at a time."
      pageName="Action Plan"
      nextStep="Implement usePlan hook, PlanItem component, and PlanProgressBar"
    />
  );
}
