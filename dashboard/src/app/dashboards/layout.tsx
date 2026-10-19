// Copyright 2026 VERA contributors
// SPDX-License-Identifier: Apache-2.0
import { DashboardShell } from "@/components/DashboardShell";

export default function DashboardsLayout({ children }: { children: React.ReactNode }) {
  return <DashboardShell>{children}</DashboardShell>;
}
