"use client";

/**
 * hooks/useCoach.ts — AI financial coach conversation hook.
 *
 * Manages multi-turn conversation state and API calls.
 * Persists conversation history in local state.
 */

import { useState, useCallback } from "react";
import type { ChatMessage } from "@/types/api";
import { chatWithCoach } from "@/services/financialService";

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

  const send = useCallback(
    async (sessionId: string, message: string): Promise<void> => {
      const userMessage: ChatMessage = { role: "user", content: message };

      // Optimistically add user message to history.
      setHistory((prev) => [...prev, userMessage]);
      setIsThinking(true);
      setError(null);

      try {
        const response = await chatWithCoach({
          session_id: sessionId,
          message,
          history: [...history, userMessage],
        });

        const assistantMessage: ChatMessage = {
          role: "assistant",
          content: response.reply,
        };
        setHistory((prev) => [...prev, assistantMessage]);
      } catch (err) {
        setError(
          err instanceof Error ? err.message : "Coach is unavailable."
        );
      } finally {
        setIsThinking(false);
      }
    },
    [history]
  );

  const clearHistory = useCallback(() => {
    setHistory([]);
    setError(null);
  }, []);

  return { history, isThinking, error, send, clearHistory };
}
