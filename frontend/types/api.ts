/**
 * types/api.ts — API response type definitions.
 *
 * These must mirror the Pydantic schemas defined in backend/app/schemas/.
 * Update both sides whenever the API contract changes.
 */

// ── Shared Enums ──────────────────────────────────────────────────────────────

export type SeverityLevel = "low" | "medium" | "high";
export type ProcessingStatus = "pending" | "processing" | "completed" | "failed";
export type PlanItemStatus = "pending" | "in_progress" | "completed" | "skipped";
export type MessageRole = "user" | "assistant";
export type TransactionType = "debit" | "credit";

export type BiasType =
  | "present_bias"
  | "loss_aversion"
  | "anchoring"
  | "mental_accounting"
  | "status_quo_bias";

export type SpendingCategory =
  | "food_and_dining"
  | "groceries"
  | "transport"
  | "entertainment"
  | "utilities"
  | "healthcare"
  | "shopping"
  | "education"
  | "travel"
  | "income"
  | "transfer"
  | "other";

// ── Upload ────────────────────────────────────────────────────────────────────

export interface UploadResponse {
  session_id: string;
  status: ProcessingStatus;
  message: string;
}

// ── Snapshot ──────────────────────────────────────────────────────────────────

export interface CategoryBreakdown {
  category: string;
  total: number;
  percentage: number;
  transaction_count: number;
}

export interface MonthlyTrend {
  month: string;
  income: number;
  expenses: number;
  net: number;
}

export interface SnapshotResponse {
  session_id: string;
  total_income: number;
  total_expenses: number;
  net_savings: number;
  savings_rate: number;
  transaction_count: number;
  date_range_start: string | null;
  date_range_end: string | null;
  category_breakdown: CategoryBreakdown[];
  monthly_trends: MonthlyTrend[];
}

// ── Behaviours ────────────────────────────────────────────────────────────────

export interface EvidenceItem {
  transaction_id: number;
  date: string;
  description: string;
  amount: number;
  category: string;
  explanation: string;
}

export interface BehaviourDetail {
  id: number;
  bias_type: BiasType;
  display_name: string;
  confidence: number;
  severity: SeverityLevel;
  detected: boolean;
  summary: string;
  evidence: EvidenceItem[];
}

export interface BehaviourProfile {
  session_id: string;
  dominant_bias: BiasType | null;
  all_biases: BehaviourDetail[];
  overall_risk_level: SeverityLevel;
}

export interface BehavioursResponse {
  session_id: string;
  behaviours: BehaviourDetail[];
  total_count: number;
}

// ── Savings ───────────────────────────────────────────────────────────────────

export interface SavingOpportunity {
  id: number;
  title: string;
  category: SpendingCategory;
  current_monthly_spend: number;
  suggested_monthly_spend: number;
  estimated_monthly_saving: number;
  difficulty: SeverityLevel;
  rationale: string;
}

export interface SavingsResponse {
  session_id: string;
  total_potential_monthly_saving: number;
  opportunities: SavingOpportunity[];
}

// ── Simulation ────────────────────────────────────────────────────────────────

export interface ScenarioChange {
  category: SpendingCategory;
  change_percent: number;
}

export interface SimulationRequest {
  session_id: string;
  behaviour_id?: number | null;
  scenario_changes: ScenarioChange[];
  horizon_months: number;
}

export interface ProjectedMonth {
  month: string;
  projected_income: number;
  projected_expenses: number;
  projected_savings: number;
}

export interface SimulationResponse {
  session_id: string;
  scenario_id: string;
  total_projected_saving: number;
  projected_months: ProjectedMonth[];
  summary: string;
}

// ── Coach ─────────────────────────────────────────────────────────────────────

export interface ChatMessage {
  role: MessageRole;
  content: string;
}

export interface CoachRequest {
  session_id: string;
  message: string;
  history: ChatMessage[];
}

export interface CoachResponse {
  session_id: string;
  reply: string;
  references: string[];
}

// ── Plan ──────────────────────────────────────────────────────────────────────

export interface PlanItem {
  id: number;
  title: string;
  description: string;
  estimated_monthly_saving: number;
  priority: SeverityLevel;
  target_date: string | null;
  status: PlanItemStatus;
  linked_behaviour_id: number | null;
  linked_bias_type: BiasType | null;
}

export interface PlanResponse {
  session_id: string;
  items: PlanItem[];
  total_estimated_monthly_saving: number;
}
