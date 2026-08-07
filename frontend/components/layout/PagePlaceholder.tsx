/**
 * PagePlaceholder — Shared placeholder component for unimplemented pages.
 *
 * Displays a consistent placeholder UI with page name, description,
 * and a "next step" hint for future implementation.
 *
 * TODO: Remove this component once all pages are implemented.
 */

import { Construction } from "lucide-react";
import { ReactNode } from "react";

interface PagePlaceholderProps {
  icon?: ReactNode;
  title: string;
  description: string;
  pageName: string;
  nextStep?: string;
}

export function PagePlaceholder({
  icon,
  title,
  description,
  pageName,
  nextStep,
}: PagePlaceholderProps) {
  return (
    <div className="min-h-[calc(100vh-4rem)] flex items-center justify-center p-8">
      <div className="glass rounded-2xl p-10 max-w-lg w-full text-center animate-fade-in-up">
        {/* Icon */}
        <div className="flex justify-center mb-6">
          {icon ?? <Construction className="w-12 h-12 text-indigo-400" />}
        </div>

        {/* Badge */}
        <span className="inline-block px-3 py-1 rounded-full text-xs font-medium bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 mb-4">
          {pageName} — Placeholder
        </span>

        {/* Title */}
        <h1 className="text-2xl font-bold text-gray-100 mb-3">{title}</h1>

        {/* Description */}
        <p className="text-gray-400 leading-relaxed mb-6">{description}</p>

        {/* Next step hint */}
        {nextStep && (
          <div className="rounded-lg bg-amber-500/5 border border-amber-500/20 px-4 py-3">
            <p className="text-xs text-amber-400">
              <span className="font-semibold">Next step: </span>
              {nextStep}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
