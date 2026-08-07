import type { Metadata } from "next";
import { PagePlaceholder } from "@/components/layout/PagePlaceholder";
import { UploadCloud } from "lucide-react";

export const metadata: Metadata = {
  title: "Upload Statement | Financial Intelligence",
  description: "Upload your bank transaction CSV to begin AI-powered financial analysis.",
};

/**
 * Upload Page — Step 1 of the user journey.
 *
 * Allows the user to upload a bank statement CSV file.
 * Displays upload progress and navigates to /snapshot on completion.
 *
 * TODO: Implement UploadDropzone component.
 * TODO: Implement useUpload hook for API integration.
 * TODO: Show progress bar during upload and processing.
 * TODO: Navigate to /snapshot/{session_id} on success.
 */
export default function UploadPage() {
  return (
    <PagePlaceholder
      icon={<UploadCloud className="w-12 h-12 text-indigo-400" />}
      title="Upload Your Bank Statement"
      description="Drop your CSV file here to begin. We support most major bank export formats."
      pageName="Upload"
      nextStep="Implement UploadDropzone and useUpload hook"
    />
  );
}
