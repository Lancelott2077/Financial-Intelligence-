import Link from "next/link";
import {
  Sparkles,
  BrainCircuit,
  PiggyBank,
  TrendingUp,
  Bot,
  CheckSquare,
  ArrowRight,
  Upload,
  Shield,
  Zap,
} from "lucide-react";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "FinBehaviour — AI-Powered Financial Intelligence",
  description:
    "Upload your bank statement and let AI detect cognitive spending biases, rank savings opportunities, and build a personalised 30-day action plan.",
};

const JOURNEY_STEPS = [
  {
    step: 1,
    icon: Upload,
    title: "Upload Statement",
    desc: "Drop your CSV bank export. We parse transactions instantly.",
    color: "text-indigo-400",
    bg: "bg-indigo-500/10 border-indigo-500/20",
  },
  {
    step: 2,
    icon: BrainCircuit,
    title: "Detect Biases",
    desc: "AI identifies cognitive patterns like Present Bias and Loss Aversion.",
    color: "text-rose-400",
    bg: "bg-rose-500/10 border-rose-500/20",
  },
  {
    step: 3,
    icon: PiggyBank,
    title: "Savings Opportunities",
    desc: "Get ranked, evidence-backed suggestions to reduce unnecessary spend.",
    color: "text-emerald-400",
    bg: "bg-emerald-500/10 border-emerald-500/20",
  },
  {
    step: 4,
    icon: TrendingUp,
    title: "Replay Simulations",
    desc: "Adjust sliders to see how behavioral changes compound over 12 months.",
    color: "text-amber-400",
    bg: "bg-amber-500/10 border-amber-500/20",
  },
  {
    step: 5,
    icon: Bot,
    title: "AI Coach Session",
    desc: "Chat with a Gemini-powered agent about your specific findings.",
    color: "text-violet-400",
    bg: "bg-violet-500/10 border-violet-500/20",
  },
  {
    step: 6,
    icon: CheckSquare,
    title: "30-Day Action Plan",
    desc: "A prioritised weekly checklist to change your financial habits.",
    color: "text-cyan-400",
    bg: "bg-cyan-500/10 border-cyan-500/20",
  },
];

const FEATURES = [
  {
    icon: Shield,
    title: "No Data Stored",
    desc: "Your transactions never leave your session. Zero persistence.",
  },
  {
    icon: Zap,
    title: "Instant Analysis",
    desc: "Deterministic engine returns results in under 2 seconds.",
  },
  {
    icon: Sparkles,
    title: "Gemini-Powered",
    desc: "Google Gemini API delivers personalised coaching narratives.",
  },
];

export default function HomePage() {
  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative overflow-hidden flex flex-col items-center justify-center text-center px-4 pt-24 pb-20">
        {/* Background glow */}
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[700px] h-[400px] bg-indigo-600/10 rounded-full blur-[120px] pointer-events-none" />

        <div className="relative z-10 max-w-3xl mx-auto space-y-6 animate-fade-in-up">
          <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full border border-indigo-500/25 bg-indigo-500/10 text-indigo-400 text-xs font-semibold uppercase tracking-widest mb-2">
            <Sparkles className="w-3.5 h-3.5 animate-pulse" />
            AI-Based Smart Spending Recommendation System
          </div>

          <h1 className="text-4xl sm:text-5xl md:text-6xl font-black text-white leading-tight tracking-tight">
            Your Money.{" "}
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-violet-400 to-rose-400">
              Understood.
            </span>
          </h1>

          <p className="text-base sm:text-lg text-gray-400 max-w-xl mx-auto leading-relaxed font-medium">
            FinBehaviour analyses your bank statement to detect cognitive spending biases, surface savings opportunities, and give you a personalised 30-day action plan — powered by Gemini AI.
          </p>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-4 pt-2">
            <Link
              href="/upload"
              className="w-full sm:w-auto inline-flex items-center justify-center gap-2.5 px-8 py-3.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold shadow-lg shadow-indigo-500/20 hover:shadow-indigo-500/30 transition-all text-sm group"
            >
              <Upload className="w-4 h-4" />
              <span>Upload Bank Statement</span>
              <ArrowRight className="w-4 h-4 group-hover:translate-x-0.5 transition-transform" />
            </Link>

            <Link
              href="/snapshot/demo"
              className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl border border-white/10 hover:border-white/20 bg-white/5 hover:bg-white/10 text-gray-300 font-semibold text-sm transition-all"
            >
              <BrainCircuit className="w-4 h-4 text-indigo-400" />
              View Demo Report
            </Link>
          </div>

          <p className="text-[11px] text-gray-600 font-medium mt-2">
            Supports standard bank CSV exports · No account required
          </p>
        </div>
      </section>

      {/* Features Row */}
      <section className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pb-12">
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          {FEATURES.map((f, idx) => {
            const Icon = f.icon;
            return (
              <div
                key={idx}
                className="glass rounded-xl p-5 border border-white/5 bg-white/[0.01] flex items-start gap-3"
              >
                <div className="p-2 rounded-lg bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 shrink-0">
                  <Icon className="w-4 h-4" />
                </div>
                <div>
                  <h3 className="text-xs font-bold text-white mb-1">{f.title}</h3>
                  <p className="text-[11px] text-gray-500 leading-relaxed font-medium">{f.desc}</p>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {/* Journey Steps Grid */}
      <section className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pb-20 space-y-6">
        <div className="text-center space-y-2">
          <h2 className="text-2xl font-extrabold text-white tracking-tight">
            Your 6-Step Intelligence Journey
          </h2>
          <p className="text-sm text-gray-500 font-medium">
            From raw transactions to actionable behavioral change in minutes.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {JOURNEY_STEPS.map((s) => {
            const Icon = s.icon;
            return (
              <div
                key={s.step}
                className="glass rounded-xl p-5 border border-white/5 bg-white/[0.01] hover:border-white/10 transition-all space-y-3 group"
              >
                <div className="flex items-center gap-3">
                  <div className={`p-2.5 rounded-xl border ${s.bg} ${s.color} shrink-0`}>
                    <Icon className="w-5 h-5" />
                  </div>
                  <span className="text-[10px] font-black text-gray-600 uppercase tracking-widest">
                    Step {s.step}
                  </span>
                </div>
                <div>
                  <h3 className="text-sm font-bold text-white mb-1">{s.title}</h3>
                  <p className="text-xs text-gray-500 leading-relaxed font-medium">{s.desc}</p>
                </div>
              </div>
            );
          })}
        </div>

        {/* Bottom CTA */}
        <div className="glass rounded-2xl border border-indigo-500/10 bg-indigo-500/[0.01] p-8 flex flex-col md:flex-row items-center justify-between gap-6 relative overflow-hidden">
          <div className="absolute top-0 right-0 w-[250px] h-[200px] bg-indigo-500/5 rounded-full blur-[80px] pointer-events-none" />

          <div className="space-y-2 relative">
            <h3 className="text-lg font-bold text-white tracking-tight">
              Ready to understand your spending?
            </h3>
            <p className="text-xs text-gray-400 max-w-sm leading-relaxed font-medium">
              Upload any standard bank CSV export and get your full Financial Intelligence Report in seconds.
            </p>
          </div>

          <Link
            href="/upload"
            className="w-full md:w-auto inline-flex items-center justify-center gap-2 px-6 py-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold shadow-lg hover:shadow-indigo-500/25 transition-all text-sm shrink-0 group"
          >
            <Sparkles className="w-4 h-4" />
            <span>Start Analysis</span>
            <ArrowRight className="w-4 h-4 group-hover:translate-x-0.5 transition-transform" />
          </Link>
        </div>
      </section>
    </div>
  );
}
