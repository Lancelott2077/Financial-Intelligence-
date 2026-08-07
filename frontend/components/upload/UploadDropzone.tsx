"use client";

import { useState, useRef, DragEvent, ChangeEvent } from "react";
import { UploadCloud, FileSpreadsheet, X, AlertCircle } from "lucide-react";

export interface UploadMetadata {
  income: number;
  savingsTarget: number;
  salaryDate: number;
  goal: string;
}

interface UploadDropzoneProps {
  onStartUpload: (file: File, metadata: UploadMetadata) => void;
  isUploading: boolean;
}

export function UploadDropzone({ onStartUpload, isUploading }: UploadDropzoneProps) {
  const [file, setFile] = useState<File | null>(null);
  const [income, setIncome] = useState<string>("");
  const [savingsTarget, setSavingsTarget] = useState<string>("");
  const [salaryDate, setSalaryDate] = useState<string>("1");
  const [goal, setGoal] = useState<string>("emergency_fund");
  const [dragActive, setDragActive] = useState<boolean>(false);
  const [validationError, setValidationError] = useState<string | null>(null);

  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleDrag = (e: DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const handleDrop = (e: DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    setValidationError(null);

    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      const droppedFile = e.dataTransfer.files[0];
      if (droppedFile.name.endsWith(".csv")) {
        setFile(droppedFile);
      } else {
        setValidationError("Only CSV bank statements are supported.");
      }
    }
  };

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    setValidationError(null);
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  const removeFile = () => {
    setFile(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = "";
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setValidationError(null);

    if (!file) {
      setValidationError("Please select or drop a bank statement CSV file.");
      return;
    }

    const incomeNum = parseFloat(income);
    const savingsNum = parseFloat(savingsTarget);
    const salaryDateNum = parseInt(salaryDate);

    if (isNaN(incomeNum) || incomeNum <= 0) {
      setValidationError("Please enter a valid monthly income greater than 0.");
      return;
    }

    if (isNaN(savingsNum) || savingsNum < 0) {
      setValidationError("Please enter a valid monthly savings target.");
      return;
    }

    if (savingsNum > incomeNum) {
      setValidationError("Savings target cannot exceed monthly income.");
      return;
    }

    onStartUpload(file, {
      income: incomeNum,
      savingsTarget: savingsNum,
      salaryDate: salaryDateNum,
      goal,
    });
  };

  return (
    <form onSubmit={handleSubmit} className="grid grid-cols-1 lg:grid-cols-5 gap-6">
      {/* Left: Metadata form parameters */}
      <div className="lg:col-span-2 space-y-4 glass p-6 rounded-2xl border border-white/5 bg-white/[0.01]">
        <h3 className="text-sm font-semibold text-gray-300 uppercase tracking-wider border-b border-white/5 pb-2 mb-4">
          Financial Context
        </h3>

        {/* Monthly Income */}
        <div className="space-y-1.5">
          <label className="text-xs font-semibold text-gray-400">Monthly Income ($)</label>
          <input
            type="number"
            placeholder="e.g. 5000"
            value={income}
            onChange={(e) => setIncome(e.target.value)}
            disabled={isUploading}
            className="w-full bg-white/5 border border-white/10 rounded-xl px-3.5 py-2 text-sm text-white placeholder-gray-500 focus:outline-none focus:border-indigo-500/50 focus:ring-1 focus:ring-indigo-500/20 transition-all"
            required
          />
        </div>

        {/* Savings Target */}
        <div className="space-y-1.5">
          <label className="text-xs font-semibold text-gray-400">Monthly Savings Target ($)</label>
          <input
            type="number"
            placeholder="e.g. 1500"
            value={savingsTarget}
            onChange={(e) => setSavingsTarget(e.target.value)}
            disabled={isUploading}
            className="w-full bg-white/5 border border-white/10 rounded-xl px-3.5 py-2 text-sm text-white placeholder-gray-500 focus:outline-none focus:border-indigo-500/50 focus:ring-1 focus:ring-indigo-500/20 transition-all"
            required
          />
        </div>

        {/* Salary Credit Date */}
        <div className="space-y-1.5">
          <label className="text-xs font-semibold text-gray-400">Salary Credit Date</label>
          <select
            value={salaryDate}
            onChange={(e) => setSalaryDate(e.target.value)}
            disabled={isUploading}
            className="w-full bg-[#121215] border border-white/10 rounded-xl px-3.5 py-2 text-sm text-white focus:outline-none focus:border-indigo-500/50 transition-all cursor-pointer"
          >
            {[...Array(31)].map((_, i) => (
              <option key={i + 1} value={i + 1}>
                Day {i + 1}
              </option>
            ))}
          </select>
        </div>

        {/* Savings Goal Option */}
        <div className="space-y-1.5">
          <label className="text-xs font-semibold text-gray-400">Financial Goal</label>
          <select
            value={goal}
            onChange={(e) => setGoal(e.target.value)}
            disabled={isUploading}
            className="w-full bg-[#121215] border border-white/10 rounded-xl px-3.5 py-2 text-sm text-white focus:outline-none focus:border-indigo-500/50 transition-all cursor-pointer"
          >
            <option value="emergency_fund">Build Emergency Fund</option>
            <option value="debt_payoff">Pay Off Credit Cards/Debt</option>
            <option value="investment">Grow Investment Portfolio</option>
            <option value="purchase">Save for Major Purchase</option>
          </select>
        </div>
      </div>

      {/* Right: CSV dropzone upload area */}
      <div className="lg:col-span-3 space-y-4 flex flex-col justify-between">
        <div
          onDragEnter={handleDrag}
          onDragOver={handleDrag}
          onDragLeave={handleDrag}
          onDrop={handleDrop}
          onClick={() => fileInputRef.current?.click()}
          className={`flex-1 border-2 border-dashed rounded-2xl flex flex-col items-center justify-center p-8 text-center cursor-pointer transition-all duration-300 ${
            dragActive
              ? "border-indigo-500 bg-indigo-500/5 shadow-[0_0_20px_rgba(99,102,241,0.1)]"
              : file
              ? "border-emerald-500/40 bg-emerald-500/[0.02]"
              : "border-white/10 bg-white/[0.01] hover:border-indigo-500/30 hover:bg-white/[0.02]"
          }`}
        >
          <input
            type="file"
            ref={fileInputRef}
            onChange={handleFileChange}
            accept=".csv"
            className="hidden"
            disabled={isUploading}
          />

          {file ? (
            <div className="space-y-4 animate-fade-in-up">
              <div className="p-4 bg-emerald-500/10 rounded-full border border-emerald-500/20 text-emerald-400 inline-block">
                <FileSpreadsheet className="w-10 h-10" />
              </div>
              <div className="space-y-1">
                <p className="text-sm font-semibold text-white truncate max-w-[280px]">
                  {file.name}
                </p>
                <p className="text-xs text-gray-500">
                  {(file.size / 1024).toFixed(1)} KB — Ready to analyze
                </p>
              </div>
              <button
                type="button"
                onClick={(e) => {
                  e.stopPropagation();
                  removeFile();
                }}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-white/5 hover:bg-white/10 text-xs text-gray-400 hover:text-white transition-all"
              >
                <X className="w-3.5 h-3.5" />
                Change file
              </button>
            </div>
          ) : (
            <div className="space-y-4">
              <div className="p-4 bg-white/5 rounded-full border border-white/5 text-gray-400 inline-block group-hover:text-indigo-400 transition-colors">
                <UploadCloud className="w-10 h-10" />
              </div>
              <div className="space-y-1">
                <p className="text-sm font-semibold text-white">
                  Drag & drop bank statement CSV
                </p>
                <p className="text-xs text-gray-500 max-w-xs mx-auto leading-relaxed">
                  Support standard CSV layout (Date, Description, Amount). Maximum file size 10MB.
                </p>
              </div>
            </div>
          )}
        </div>

        {/* Validation warning */}
        {validationError && (
          <div className="flex items-start gap-2.5 p-3.5 rounded-xl bg-rose-500/10 border border-rose-500/20 text-rose-400 text-xs animate-fade-in-up">
            <AlertCircle className="w-4 h-4 shrink-0 mt-0.5" />
            <span>{validationError}</span>
          </div>
        )}

        {/* Submit */}
        <button
          type="submit"
          disabled={isUploading}
          className="w-full inline-flex items-center justify-center gap-2 px-4 py-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 text-white font-semibold shadow-lg hover:shadow-indigo-500/25 transition-all text-sm"
        >
          {isUploading ? "Uploading..." : "Start Behavior Analysis"}
        </button>
      </div>
    </form>
  );
}
