"use client";

/**
 * Navigation — Top navigation bar.
 *
 * Displays the brand logo and links to all main pages.
 * Highlights the active route.
 *
 * TODO: Implement active route detection using usePathname().
 * TODO: Add session_id context to navigation links.
 * TODO: Add mobile hamburger menu for small screens.
 */

import Link from "next/link";
import { usePathname } from "next/navigation";
import { BrainCircuit } from "lucide-react";

const NAV_LINKS = [
  { href: "/upload", label: "Upload" },
  { href: "/snapshot", label: "Snapshot" },
  { href: "/behaviours", label: "Behaviours" },
  { href: "/savings", label: "Savings" },
  { href: "/simulation", label: "Simulation" },
  { href: "/coach", label: "AI Coach" },
  { href: "/plan", label: "Action Plan" },
] as const;

const SESSION_ROUTES = new Set([
  "snapshot",
  "behaviours",
  "savings",
  "simulation",
  "coach",
  "plan",
]);

function extractSessionId(pathname: string): string | null {
  const segments = pathname.split("/").filter(Boolean);
  if (segments.length === 2 && SESSION_ROUTES.has(segments[0])) {
    return segments[1];
  }
  return null;
}

export function Navigation() {
  const pathname = usePathname();
  const sessionId = extractSessionId(pathname);

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 glass border-b border-white/8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        {/* Brand */}
        <Link href="/" className="flex items-center gap-2 group">
          <BrainCircuit className="w-7 h-7 text-indigo-400 group-hover:text-indigo-300 transition-colors" />
          <span className="font-semibold text-lg gradient-text">
            Financial Intelligence
          </span>
        </Link>

        {/* Links */}
        <div className="hidden md:flex items-center gap-1">
          {NAV_LINKS.map((link) => {
            const path =
              sessionId && link.href !== "/upload"
                ? `${link.href}/${sessionId}`
                : link.href;
            return (
              <Link
                key={link.href}
                href={path}
                className="px-3 py-1.5 rounded-md text-sm text-gray-400 hover:text-gray-100 hover:bg-white/5 transition-all duration-150"
              >
                {link.label}
              </Link>
            );
          })}
        </div>
      </div>
    </nav>
  );
}
