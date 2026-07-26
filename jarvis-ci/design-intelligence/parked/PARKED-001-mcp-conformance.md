# PARKED-001 — MCP conformance for the adapter layer

| | |
|---|---|
| **Status** | 🅿️ **Parked — not rejected** |
| **Target stage** | 1 |
| **Current stage** | 0 |
| **Would have been** | RFC |
| **Priority if unparked** | P3 (1.19) |
| **Source** | capability:mcp-interop |
| **Confidence** | HIGH |

---

## Why parked

Stage discipline. Seven Stage-0 blocking exit criteria remain open, so a Stage-1
recommendation is inadmissible. `tools/route.py` withheld the RFC automatically —
no human judgement was applied and no override exists.

## Why it is preserved rather than dropped

The insight is sound and the evidence is HIGH confidence. MCP has consolidated as
the cross-vendor agent-to-tool standard under the Linux Foundation's AAIF, and
conforming early is materially cheaper than retrofitting. Discarding it would mean
rediscovering it later at higher cost.

Parking preserves the reasoning, the evidence and the date. Unparking is mechanical.

## Unpark trigger

**Stage 0 exit criteria complete** — specifically S0-E1, S0-E2, S0-E3, S0-E8, S0-E9.

Secondary trigger: RHINAL's own MCP server design completed (currently blocking
the integration from the other side).

## Preserved reasoning

The adapter pattern plus feature flags is already SDK-shaped — unplanned
optionality worth exploiting. Conforming to MCP would make JARVIS adapters
consumable by any MCP host, which is the cheapest available distribution.

Depends on: R-009 (pluggable-backends pattern), DEC-005 (interface stability).

> ⚠ Watch item: UNK-003 asks which layer standardises next. MCP erased bespoke
> tool-integration advantage in ~16 months. If the adapter interface layer is
> next, this parked item becomes urgent rather than optional.
