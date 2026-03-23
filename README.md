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

## License

This project is licensed under the **Apache License 2.0**.

You are free to:

- Use commercially  
- Modify and extend  
- Distribute  

Under the terms of the license.

### Key Points

- Includes **patent grant protection**
- Requires **preservation of license and notices**
- Contributions are licensed under Apache 2.0 unless stated otherwise

See:

- [`LICENSE`](./LICENSE)
- [`NOTICE`](./NOTICE)

## 🤝 Contributions

Contributions are welcome under the **Apache 2.0 License**.

### Contribution Guidelines

Please ensure all contributions:

- Follow the **clinical knowledge unit structure**
- Are **medically meaningful (pattern-based, not diagnostic claims)**
- Include **clear explanations**
- Preferably include **supporting evidence or references**
- Maintain **deterministic and explainable logic**

### Do NOT contribute:

- Diagnosis statements  
- Treatment recommendations  
- Unverified medical claims  
- Black-box logic  

### Workflow

1. Fork the repository  
2. Create a feature branch  
3. Add or update rules / schema  
4. Submit a pull request with clear description  

---

### Review Criteria

All contributions will be reviewed for:

- Clinical correctness  
- Structural consistency  
- Explainability  
- Safety and compliance  

---

## Citation

If you use this work in research, publications, or products, please cite:

**Plain Text Citation:**

Swapin Vidya. *PeachBot Medical Knowledge Graph (peachbot-medical-kg):  
A Deterministic Clinical Knowledge Compiler for Edge AI Systems.* 2026.

---

### BibTeX

```bibtex
@software{peachbot_medkg_2026,
  author       = {Swapin Vidya},
  title        = {PeachBot Medical Knowledge Graph (peachbot-medical-kg)},
  year         = {2026},
  publisher    = {GitHub},
  url          = {https://github.com/peachbotAI/peachbot-medical-kg},
  note         = {Deterministic clinical knowledge compiler for edge AI systems}
}
```

By contributing, you agree that your contributions will be licensed under Apache 2.0.

## Status

⚠️ Early-stage knowledge engineering system (deterministic, rule-based)
