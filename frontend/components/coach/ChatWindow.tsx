"use client";

import { useEffect, useRef } from "react";
import { Brain, User, Loader2 } from "lucide-react";
import type { ChatMessage } from "@/types/api";

interface ChatWindowProps {
  history: ChatMessage[];
  isThinking: boolean;
}

export function ChatWindow({ history, isThinking }: ChatWindowProps) {
  const bottomRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom of chat
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [history, isThinking]);

  return (
    <div className="flex-1 overflow-y-auto p-4 space-y-4 min-h-[360px] max-h-[480px] scrollbar-thin">
      {history.length === 0 && (
        <div className="flex flex-col items-center justify-center h-full min-h-[300px] text-center space-y-3">
          <div className="p-3 bg-indigo-500/10 rounded-2xl border border-indigo-500/20 text-indigo-400">
            <Brain className="w-8 h-8 animate-pulse" />
          </div>
          <div className="space-y-1 max-w-xs">
            <h4 className="text-sm font-bold text-white">AI Financial Coach</h4>
            <p className="text-xs text-gray-500 leading-relaxed font-medium">
              Ask me anything about your behavioral report, savings opportunities, or counterfactual simulations.
            </p>
          </div>
        </div>
      )}

      {history.map((msg, idx) => {
        const isUser = msg.role === "user";
        return (
          <div
            key={idx}
            className={`flex items-start gap-3 text-xs ${isUser ? "justify-end" : "justify-start"}`}
          >
            {/* Coach Icon */}
            {!isUser && (
              <div className="p-2 bg-indigo-500/10 rounded-xl border border-indigo-500/20 text-indigo-400 shrink-0">
                <Brain className="w-4 h-4" />
              </div>
            )}

            {/* Bubble */}
            <div
              className={`max-w-[80%] rounded-2xl px-4 py-3 border leading-relaxed font-medium ${
                isUser
                  ? "bg-indigo-600 border-indigo-500 text-white rounded-tr-none"
                  : "glass border-white/5 bg-white/[0.02] text-gray-200 rounded-tl-none"
              }`}
            >
              <p className="whitespace-pre-line">{msg.content}</p>
            </div>

            {/* User Icon */}
            {isUser && (
              <div className="p-2 bg-white/5 rounded-xl border border-white/5 text-gray-400 shrink-0">
                <User className="w-4 h-4" />
              </div>
            )}
          </div>
        );
      })}

      {/* Typing loader */}
      {isThinking && (
        <div className="flex items-start gap-3 text-xs justify-start">
          <div className="p-2 bg-indigo-500/10 rounded-xl border border-indigo-500/20 text-indigo-400 shrink-0">
            <Brain className="w-4 h-4" />
          </div>
          <div className="glass border-white/5 bg-white/[0.02] rounded-2xl rounded-tl-none px-4 py-3 flex items-center gap-2">
            <Loader2 className="w-3.5 h-3.5 text-indigo-400 animate-spin" />
            <span className="text-gray-500 font-semibold uppercase tracking-wider text-[10px]">
              Coach is compiling analysis...
            </span>
          </div>
        </div>
      )}

      <div ref={bottomRef} />
    </div>
  );
}
