import type { Metadata } from "next";
import { PagePlaceholder } from "@/components/layout/PagePlaceholder";
import { MessageCircle } from "lucide-react";

export const metadata: Metadata = {
  title: "AI Financial Coach | Financial Intelligence",
  description: "Chat with your personalised Gemini-powered AI financial coach.",
};

/**
 * AI Financial Coach Page — Step 6 of the user journey.
 *
 * Conversational interface powered by Gemini, grounded in the
 * user's actual financial data and detected behaviours.
 *
 * TODO: Implement ChatWindow component with message bubbles.
 * TODO: Implement MessageInput component with send button.
 * TODO: Implement useCoach hook to POST /api/v1/coach/chat.
 * TODO: Maintain conversation history in local state.
 * TODO: Show loading skeleton while awaiting Gemini response.
 */
export default function CoachPage({
  params: _params,
}: {
  params: { sessionId: string };
}) {
  return (
    <PagePlaceholder
      icon={<MessageCircle className="w-12 h-12 text-indigo-400" />}
      title="AI Financial Coach"
      description="Ask me anything about your finances. I know your spending patterns and can guide you."
      pageName="AI Financial Coach"
      nextStep="Implement ChatWindow, MessageInput, and useCoach hook"
    />
  );
}
