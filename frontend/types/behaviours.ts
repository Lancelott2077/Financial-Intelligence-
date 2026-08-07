/**
 * types/behaviours.ts — Client-side behaviour display types.
 *
 * TODO: Add bias display metadata (colour, icon, description).
 */

export interface BiasDisplayMeta {
  biasType: string;
  displayName: string;
  colour: string;
  iconName: string;
  explanation: string;
}

/**
 * Mapping of bias_type → display metadata.
 * TODO: Populate with all supported bias types.
 */
export const BIAS_DISPLAY_META: Record<string, BiasDisplayMeta> = {
  // TODO: Add entries for each bias type.
};
