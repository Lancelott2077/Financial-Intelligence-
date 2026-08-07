import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Navigation } from "@/components/layout/Navigation";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Financial Intelligence — Behavioural Finance AI",
  description:
    "AI-powered personal finance platform that detects cognitive biases, " +
    "analyses spending patterns, and delivers personalised financial coaching.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <body className={`${inter.className} bg-gray-950 text-gray-100 min-h-screen`}>
        <Navigation />
        <main className="pt-16">{children}</main>
      </body>
    </html>
  );
}
