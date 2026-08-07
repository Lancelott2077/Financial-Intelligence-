"use client";

import { useState } from "react";
import Link from "next/link";
import { ArrowRight, Send, Trash2 } from "lucide-react";
import { useCoach } from "@/hooks/useCoach";
import { ChatWindow } from "@/components/coach/ChatWindow";

const SUGGESTION_CHIPS = [
  "Explain my Present Bias details.",
  "How do I cut food & dining expenses?",
  "Suggest tips to save on shopping.",
];

export default function CoachPage({
  params,
}: {
  params: { sessionId: string };
}) {
  const { history, isThinking, error, send, clearHistory } = useCoach();
  const [input, setInput] = useState("");

  const handleSend = async (messageText: string) => {
    if (!messageText.trim() || isThinking) return;
    setInput("");
    await send(params.sessionId, messageText);
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    handleSend(input);
  };

  return (
    <div className="max-w-3xl mx-auto px-4 py-8 space-y-6 animate-fade-in-up">
      {/* Header section */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-white/5 pb-5">
        <div className="space-y-1">
          <h1 className="text-3xl font-extrabold text-white tracking-tight flex items-center gap-2">
            AI Financial Coach
          </h1>
          <p className="text-sm text-gray-400">
            Discuss your behavior report analysis and action items with a Gemini-powered agent.
          </p>
        </div>

        <div className="flex items-center gap-2">
          {history.length > 0 && (
            <button
              onClick={clearHistory}
              disabled={isThinking}
              className="p-2 bg-white/5 hover:bg-white/10 border border-white/5 hover:border-white/10 text-gray-400 hover:text-white rounded-xl transition-all"
              title="Clear conversation history"
            >
              <Trash2 className="w-4 h-4" />
            </button>
          )}
          <Link
            href={`/plan/${params.sessionId}`}
            className="inline-flex items-center gap-2 px-4 py-2 bg-indigo-500/10 hover:bg-indigo-500/20 text-indigo-400 border border-indigo-500/20 hover:border-indigo-500/30 rounded-xl text-sm font-medium transition-all group shrink-0"
          >
            <span>Action Plan</span>
            <ArrowRight className="w-4 h-4 group-hover:translate-x-0.5 transition-transform" />
          </Link>
        </div>
      </div>

      {/* Main chat window container */}
      <div className="glass rounded-2xl border border-white/5 bg-white/[0.01] overflow-hidden flex flex-col justify-between h-[520px]">
        {/* Chat Header info */}
        <div className="px-5 py-3 border-b border-white/5 bg-white/[0.005] flex items-center justify-between">
          <div className="flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            <span className="text-[10px] font-bold text-gray-400 uppercase tracking-wider">
              Gemini Coach Active
            </span>
          </div>
        </div>

        {/* Message logs */}
        <ChatWindow history={history} isThinking={isThinking} />

        {/* Suggestion Chips */}
        {history.length === 0 && (
          <div className="px-5 pb-2">
            <div className="flex flex-wrap gap-2 justify-center">
              {SUGGESTION_CHIPS.map((chip, idx) => (
                <button
                  key={idx}
                  onClick={() => handleSend(chip)}
                  disabled={isThinking}
                  className="px-3 py-1.5 rounded-full bg-white/5 hover:bg-white/10 text-[10px] text-gray-400 hover:text-white border border-white/5 transition-all font-semibold"
                >
                  {chip}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Form message input */}
        <form
          onSubmit={handleSubmit}
          className="p-4 border-t border-white/5 bg-[#09090b]/80 flex gap-2"
        >
          <input
            type="text"
            placeholder="Ask a question about your finances..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            disabled={isThinking}
            className="flex-1 bg-white/5 border border-white/10 rounded-xl px-4 py-2.5 text-xs text-white placeholder-gray-500 focus:outline-none focus:border-indigo-500/50 transition-all"
          />
          <button
            type="submit"
            disabled={!input.trim() || isThinking}
            className="p-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 text-white shadow-lg transition-all"
          >
            <Send className="w-4 h-4" />
          </button>
        </form>
      </div>

      {error && (
        <div className="p-3 rounded-xl bg-rose-500/10 border border-rose-500/20 text-rose-400 text-xs text-center font-medium">
          {error}
        </div>
      )}
    </div>
  );
}
