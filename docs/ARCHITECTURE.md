# Architecture — PeachBot Medical Knowledge Graph

## Overview

This repository implements a **deterministic medical knowledge compiler** that transforms structured clinical reasoning into JSON for downstream inference systems.

---

## Core Concept

```text
Clinical Knowledge → Structured Units → Validation → Export → JSON
```

---

## Knowledge Unit Model

Each unit follows:

```text
INPUT → CONTEXT → SIGNAL → META → EVIDENCE
```

### Components

* **Inputs**: symptoms, signs, investigations
* **Context**: severity, duration, system (ICD-aligned)
* **Signal**: clinical interpretation (non-diagnostic)
* **Meta**: weight, confidence, explanation
* **Evidence**: source-backed justification

---

## Pipeline

```text
sources/        → pattern definitions
        ↓
builders/       → construct rules
        ↓
schema/         → enforce structure
        ↓
validators/     → enforce correctness + evidence
        ↓
rules/          → wrap into exportable format
        ↓
registry        → collect rules
        ↓
exporters/      → generate JSON
```

---

## Design Principles

* **Deterministic** — no probabilistic inference
* **Explainable** — every output traceable
* **Evidence-Gated** — no rule without reference
* **Modular** — domain extensible
* **Edge-Compatible** — lightweight and fast

---

## Separation of Responsibilities

| Component     | Responsibility                  |
| ------------- | ------------------------------- |
| Medical KG    | Define clinical knowledge       |
| PeachBot Core | Perform reasoning and inference |

---

## Output Contract

The system produces structured JSON:

* Conditions
* Signals
* Metadata
* Evidence

This output is consumed by **PeachBot Core**.

---

## Future Extensions

* Versioned knowledge packs
* ICD code-level mapping
* Conflict resolution between rules
* Expanded evidence hierarchy

---

## Summary

This system does not perform diagnosis.

It encodes:

> Structured, evidence-backed clinical reasoning for edge systems.
