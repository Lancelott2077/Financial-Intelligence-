import { PagePlaceholder } from "@/components/layout/PagePlaceholder";
import { UploadIcon } from "lucide-react";

/**
 * Home page — redirects to the Upload page.
 * TODO: Implement redirect to /upload or show landing hero.
 */
export default function HomePage() {
  return (
    <PagePlaceholder
      icon={<UploadIcon className="w-12 h-12 text-indigo-400" />}
      title="Welcome to Financial Intelligence"
      description="Upload your bank statement CSV to get started. Your AI-powered financial coach is ready."
      pageName="Landing / Home"
      nextStep="Navigate to /upload to begin"
    />
  );
}
