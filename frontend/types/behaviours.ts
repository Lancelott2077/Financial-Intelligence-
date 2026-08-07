/**
 * types/behaviours.ts — Client-side behaviour display types.
 */

import { BiasType } from "./api";

export interface BiasDisplayMeta {
  biasType: BiasType;
  displayName: string;
  colour: string;
  iconName: string;
  explanation: string;
}

/**
 * Mapping of bias_type → display metadata.
 */
export const BIAS_DISPLAY_META: Record<BiasType, BiasDisplayMeta> = {
  present_bias: {
    biasType: "present_bias",
    displayName: "Present Bias",
    colour: "bg-orange-500",
    iconName: "Clock",
    explanation: "A tendency to overvalue immediate rewards at the expense of long-term goals.",
  },
  loss_aversion: {
    biasType: "loss_aversion",
    displayName: "Loss Aversion",
    colour: "bg-red-500",
    iconName: "TrendingDown",
    explanation: "The psychological impact of losing money is twice as severe as the joy of gaining the same amount.",
  },
  anchoring: {
    biasType: "anchoring",
    displayName: "Anchoring Effect",
    colour: "bg-blue-500",
    iconName: "Anchor",
    explanation: "Relying too heavily on the first piece of information encountered when making decisions.",
  },
  mental_accounting: {
    biasType: "mental_accounting",
    displayName: "Mental Accounting",
    colour: "bg-purple-500",
    iconName: "Wallet",
    explanation: "Treating money differently depending on its source or intended use.",
  },
  status_quo_bias: {
    biasType: "status_quo_bias",
    displayName: "Status Quo Bias",
    colour: "bg-slate-500",
    iconName: "PauseCircle",
    explanation: "A preference for the current state of affairs, resisting changes that could be beneficial.",
  },
};
