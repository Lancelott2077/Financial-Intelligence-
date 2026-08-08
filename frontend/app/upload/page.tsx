"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { Sparkles, BrainCircuit, Check, Loader2 } from "lucide-react";
import { useUpload } from "@/hooks/useUpload";
import { UploadDropzone, UploadMetadata } from "@/components/upload/UploadDropzone";

export default function UploadPage() {
  const router = useRouter();
  const { state, upload, reset } = useUpload();
  const [currentStep, setCurrentStep] = useState<number>(0);
  const [progressVal, setProgressVal] = useState<number>(0);

  const steps = [
    { label: "Uploading statement CSV file", targetProgress: 25 },
    { label: "Categorizing transaction descriptions", targetProgress: 50 },
    { label: "Detecting behavioral cognitive biases", targetProgress: 75 },
    { label: "Constructing 30-day action plan", targetProgress: 100 },
  ];

  // Triggered when file and metadata are submitted and validated
  const handleStartUpload = async (file: File, metadata: UploadMetadata) => {
    try {
      localStorage.setItem("fin_temp_upload_meta", JSON.stringify(metadata));
      const sessionId = await upload(file);
      if (sessionId) {
        const savedMetaStr = localStorage.getItem("fin_temp_upload_meta");
        if (savedMetaStr) {
          localStorage.setItem(
            `fin_session_${sessionId}_meta`,
            savedMetaStr
          );
          localStorage.removeItem("fin_temp_upload_meta");
        }
        router.push(`/snapshot/${sessionId}`);
      }
    } catch {
      // Handled by hook state
    }
  };

  // Stepper progress simulation when uploading/processing
  useEffect(() => {
    let timer: NodeJS.Timeout;
    if (state.status === "uploading") {
      setCurrentStep(0);
      setProgressVal(10);
    } else if (state.status === "processing") {
      setCurrentStep(1);
      setProgressVal(35);

      // Simulate progressing steps since backend calculation occurs quickly
      const interval = 250; // ms
      timer = setInterval(() => {
        setProgressVal((prev) => {
          if (prev < 95) {
            const nextVal = prev + 5;
            if (nextVal >= 85) setCurrentStep(3);
            else if (nextVal >= 60) setCurrentStep(2);
            return nextVal;
          }
          return prev;
        });
      }, interval);
    } else if (state.status === "ready") {
      setProgressVal(100);
      setCurrentStep(4);
    } else if (state.status === "error" || state.status === "idle") {
      setProgressVal(0);
      setCurrentStep(0);
    }

    return () => {
      if (timer) clearInterval(timer);
    };
  }, [state.status, state.sessionId, router]);

  const isWorking = state.status === "uploading" || state.status === "processing" || state.status === "ready";

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 min-h-[calc(100vh-4rem)] flex items-center justify-center">
      <div className="w-full max-w-4xl space-y-8 animate-fade-in-up">
        {/* Loader Screen */}
        {isWorking ? (
          <div className="glass rounded-2xl p-8 max-w-md mx-auto text-center border-indigo-500/10 space-y-6">
            <div className="flex justify-center relative">
              <div className="absolute inset-0 flex items-center justify-center animate-pulse">
                <BrainCircuit className="w-8 h-8 text-indigo-400" />
              </div>
              <Loader2 className="w-16 h-16 text-indigo-500/30 animate-spin" />
            </div>

            <div className="space-y-1">
              <h2 className="text-xl font-bold text-white tracking-tight">
                {state.status === "ready" ? "Analysis Ready!" : "AI is analyzing statement..."}
              </h2>
              <p className="text-xs text-gray-500">
                Please wait while we run our financial models.
              </p>
            </div>

            {/* Stepper Display */}
            <div className="space-y-3.5 text-left border-t border-white/5 pt-5">
              {steps.map((step, idx) => {
                const isDone = currentStep > idx || state.status === "ready";
                const isCurrent = currentStep === idx && state.status !== "ready";
                return (
                  <div key={idx} className="flex items-center gap-3 text-xs">
                    <div
                      className={`w-5 h-5 rounded-full flex items-center justify-center border transition-all ${
                        isDone
                          ? "bg-emerald-500/10 border-emerald-500/30 text-emerald-400"
                          : isCurrent
                          ? "bg-indigo-500/10 border-indigo-500/30 text-indigo-400 animate-pulse"
                          : "border-white/5 text-gray-600 bg-white/[0.01]"
                      }`}
                    >
                      {isDone ? (
                        <Check className="w-3 h-3" />
                      ) : isCurrent ? (
                        <Loader2 className="w-3 h-3 animate-spin" />
                      ) : (
                        idx + 1
                      )}
                    </div>
                    <span
                      className={`font-medium transition-colors ${
                        isDone
                          ? "text-gray-300 line-through decoration-gray-700 decoration-1"
                          : isCurrent
                          ? "text-indigo-400 font-semibold"
                          : "text-gray-600"
                      }`}
                    >
                      {step.label}
                    </span>
                  </div>
                );
              })}
            </div>

            {/* Progress line */}
            <div className="space-y-1.5 pt-2">
              <div className="h-1 w-full bg-white/5 rounded-full overflow-hidden">
                <div
                  className="h-full bg-indigo-500 transition-all duration-300 ease-out"
                  style={{ width: `${progressVal}%` }}
                />
              </div>
              <div className="flex justify-between text-[10px] text-gray-500 font-medium">
                <span>ANALYZING STATEMENT</span>
                <span>{progressVal}%</span>
              </div>
            </div>
          </div>
        ) : (
          /* Normal Form Upload View */
          <div className="space-y-6">
            {/* Header */}
            <div className="text-center space-y-2">
              <div className="inline-flex items-center justify-center p-2 rounded-xl bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 mb-2">
                <Sparkles className="w-5 h-5 animate-pulse" />
              </div>
              <h1 className="text-3xl font-extrabold tracking-tight text-white sm:text-4xl">
                Activate Your Financial Intelligence
              </h1>
              <p className="text-sm text-gray-400 max-w-xl mx-auto leading-relaxed">
                Upload your transaction statement. Our engine will map spending categories, extract behavioural biases, and compile your coaching plan.
              </p>
            </div>

            {/* Hook Error Display */}
            {state.errorMessage && (
              <div className="p-4 rounded-xl bg-rose-500/10 border border-rose-500/20 max-w-md mx-auto text-center text-xs text-rose-400 font-medium animate-fade-in-up">
                {state.errorMessage}
                <button
                  onClick={reset}
                  className="block mt-2 mx-auto underline hover:text-rose-300"
                >
                  Clear error & try again
                </button>
              </div>
            )}

            {/* Dropzone Card */}
            <div className="glass rounded-3xl p-6 border border-white/5 bg-white/[0.01]">
              <UploadDropzone
                onStartUpload={handleStartUpload}
                isUploading={state.status === "uploading"}
              />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
