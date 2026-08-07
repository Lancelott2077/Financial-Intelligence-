import type { Metadata } from "next";
import { PagePlaceholder } from "@/components/layout/PagePlaceholder";
import { Brain } from "lucide-react";

export const metadata: Metadata = {
  title: "Behaviour Report | Financial Intelligence",
  description: "Discover the cognitive biases shaping your financial decisions.",
};

/**
 * Behaviour Report Page — Step 3 of the user journey.
 *
 * Displays detected cognitive biases with confidence scores,
 * severity indicators, and supporting transaction evidence.
 *
 * TODO: Implement useBehaviours hook to fetch /api/v1/behaviours/{session_id}.
 * TODO: Implement BiasCard component showing bias name, severity badge, and confidence.
 * TODO: Implement EvidenceTable component listing supporting transactions.
 * TODO: Implement BiasRadarChart (Recharts radar chart) for bias overview.
 */
export default function BehaviourReportPage({
  params,
}: {
  params: { sessionId: string };
}) {
  return (
    <PagePlaceholder
      icon={<Brain className="w-12 h-12 text-indigo-400" />}
      title="Your Behaviour Report"
      description="AI has identified cognitive biases in your spending. Here is the evidence."
      pageName="Behaviour Report"
      nextStep="Implement useBehaviours, BiasCard, and EvidenceTable components"
    />
  );
}
