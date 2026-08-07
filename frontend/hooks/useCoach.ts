"use client";

/**
 * hooks/useCoach.ts — AI financial coach conversation hook.
 *
 * Manages multi-turn conversation state and API calls.
 *
 * TODO: Implement using financialService.chatWithCoach().
 * TODO: Persist conversation history in local state.
 * TODO: Scroll chat window to bottom on new message.
 */

import { useState } from "react";
import type { ChatMessage, CoachResponse } from "@/types/api";

interface UseCoachReturn {
  history: ChatMessage[];
  isThinking: boolean;
  error: string | null;
  send: (sessionId: string, message: string) => Promise<void>;
  clearHistory: () => void;
}

export function useCoach(): UseCoachReturn {
  const [history, setHistory] = useState<ChatMessage[]>([]);
  const [isThinking, setIsThinking] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const send = async (
    _sessionId: string,
    _message: string
  ): Promise<void> => {
    // TODO: Append user message to history.
    // TODO: Set isThinking to true.
    // TODO: Call financialService.chatWithCoach({ session_id, message, history }).
    // TODO: Append assistant reply to history.
    // TODO: Handle errors.
    throw new Error("useCoach.send not implemented.");
  };

  const clearHistory = () => setHistory([]);

  return { history, isThinking, error, send, clearHistory };
}
