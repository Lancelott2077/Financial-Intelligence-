import type { Metadata } from "next";
import { PagePlaceholder } from "@/components/layout/PagePlaceholder";
import { Play } from "lucide-react";

export const metadata: Metadata = {
  title: "Counterfactual Replay | Financial Intelligence",
  description: "See how your finances could look if you changed specific spending behaviours.",
};

/**
 * Counterfactual Replay Page — Step 5 of the user journey.
 *
 * Allows the user to configure hypothetical spending changes and
 * visualise projected financial outcomes over a time horizon.
 *
 * TODO: Implement ScenarioBuilder component with sliders per category.
 * TODO: Implement useSimulation hook to POST /api/v1/simulation.
 * TODO: Implement ProjectionChart (Recharts line chart) showing before/after.
 * TODO: Show total projected saving over 12 months.
 */
export default function SimulationPage({
  params: _params,
}: {
  params: { sessionId: string };
}) {
  return (
    <PagePlaceholder
      icon={<Play className="w-12 h-12 text-indigo-400" />}
      title="Counterfactual Replay"
      description="What if you cut dining by 20%? See how your savings would change over 12 months."
      pageName="Counterfactual Replay"
      nextStep="Implement ScenarioBuilder, useSimulation hook, and ProjectionChart"
    />
  );
}
