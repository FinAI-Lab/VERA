// Copyright 2026 VERA contributors
// SPDX-License-Identifier: Apache-2.0
import { DsClient } from "./ds-client";

export default function DsPage({
  searchParams,
}: {
  searchParams: { e2e_role?: string };
}) {
  return <DsClient e2eRole={searchParams.e2e_role} />;
}
