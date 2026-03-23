# PeachBot Medical Knowledge Graph (peachbot-medical-kg)

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-Active%20Development-orange)
![Architecture](https://img.shields.io/badge/architecture-Deterministic%20KG-green)
![Edge Ready](https://img.shields.io/badge/edge-compatible-brightgreen)
![Explainability](https://img.shields.io/badge/AI-Explainable-critical)

## Overview

This repository is a **Medical Knowledge Engineering System** designed to generate structured, evidence-backed clinical knowledge for PeachBot Core.

It acts as a **deterministic knowledge compiler**, transforming clinical reasoning into machine-readable JSON.

---

## Purpose

* Encode **clinical patterns**, not diagnoses
* Generate **edge-compatible structured knowledge**
* Provide **explainable and traceable medical reasoning**
* Support **evidence-backed signals with references**

---

## What This Repo Does

Input:

* Clinical patterns (symptoms, signs, investigations)

Output:

* Structured JSON knowledge for PeachBot Core

---

## What This Repo Does NOT Do

* No diagnosis
* No treatment recommendations
* No machine learning
* No real-time patient decision making

---

## Medical Disclaimer

This system is designed for **research and decision-support augmentation only**.

It does NOT:

* replace clinical judgment
* provide diagnosis
* recommend treatment

All outputs must be interpreted by a **qualified medical professional**.

---

## Architecture Role

peachbot-medical-kg → produces knowledge
PeachBot Core → consumes and reasons

---

## Structure

```bash
schema/  → clinical data models
sources/ → curated medical patterns
rules/   → rule definitions
builders/  → rule construction utilities
exporters/ → JSON generation
outputs/ → generated knowledge
scripts/ → execution scripts
```

---

## Quick Start (coming next)

Run:

```bash
python scripts/export_medai.py
```

---

## Status

⚠️ Early-stage knowledge engineering system (deterministic, rule-based)
