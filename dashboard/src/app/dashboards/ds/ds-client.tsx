// Copyright 2026 VERA contributors
// SPDX-License-Identifier: Apache-2.0
"use client";

import { AuthGuard } from "@/components/AuthGuard";
import { RunSummaryView } from "@/components/RunSummaryView";
import { ROUTE_ROLES } from "@/lib/auth";

export function DsClient({ e2eRole }: { e2eRole?: string }) {
  return (
    <AuthGuard roles={ROUTE_ROLES["/dashboards/ds"]} simulateRole={e2eRole}>
      <RunSummaryView lens="ds" />
    </AuthGuard>
  );
}
