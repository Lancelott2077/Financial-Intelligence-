import { redirect } from "next/navigation";

/** Redirect bare /snapshot → /upload so users land somewhere useful */
export default function SnapshotIndexPage() {
  redirect("/upload");
}
