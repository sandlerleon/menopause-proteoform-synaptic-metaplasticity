# Does Endocrine State Gate Proteoform-Induced Synaptic Vulnerability?

Leon Sandler, Independent Researcher — sandler.leon@gmail.com

Code and manuscript for "Does Endocrine State Gate Proteoform-Induced Synaptic
Vulnerability? A Metaplasticity Framework for Menopause and Early
Neurodegeneration," prepared for submission to *Neuroscience & Biobehavioral
Reviews* (Elsevier) as a hypothesis-driven conceptual review.

## Summary

This is a hypothesis-driven conceptual review (not a systematic review or
meta-analysis — see manuscript Section 1.3) synthesizing two literatures
usually studied separately — neuroendocrine regulation of hippocampal synaptic
plasticity across the menopause transition, and soluble amyloid-β (Aβ)
oligomer-driven synaptotoxicity in early neurodegeneration — around a shared
formal question posed in the language of Bienenstock-Cooper-Munro (BCM)
metaplasticity theory: does endocrine state alter susceptibility to
proteoform-driven synaptic metaplasticity? The review distinguishes
perimenopausal mood symptoms, cognitive complaints, and Alzheimer's
pathophysiology as clinically separate entities, weighs the central
convergence hypothesis against four competing explanatory models, and
presents a structured, falsifiable research agenda. It reports no new
clinical or preclinical data.

## Contents

- `manuscript/` — manuscript (Word), CC BY 4.0.
- `code/` — Python (Matplotlib/pandas), MIT license:
  - `generate_figures.py` — regenerates Figures 1-3 (conceptual box-and-arrow
    diagrams illustrating the proposed convergence framework, the
    estrogen/allopregnanolone receptor pathways, and the Aβ-oligomer LTD
    mechanism). These are schematic, not data plots — no simulation or
    dataset underlies them; the script exists so the figures are
    reproducible and version-controlled rather than static images.
  - `export_tables.py` — exports Table 1 (Evidence-Weighted Synthesis, 10
    claims) and Table 2 (Falsifiable Research Agenda, 6 proposed experiments)
    as machine-readable CSV/JSON, so the evidence base and research agenda
    can be filtered, cited, or reused programmatically.
  - `figure1_convergence_framework.png`, `figure2_estrogen_allopregnanolone_pathways.png`,
    `figure3_ab_oligomer_ltd_mechanism.png` — regenerated figures from the above script.
  - `table1_evidence_weighted_synthesis.{csv,json}`, `table2_falsifiable_research_agenda.{csv,json}`
    — regenerated tables from the above script.

Run with `python generate_figures.py` and `python export_tables.py`
(requires `matplotlib`; no other dependencies).

## License

Code: MIT (see `LICENSE` at repo root — the top-level `LICENSE` file
applies to `code/`). Manuscript: CC BY 4.0 (see `manuscript/LICENSE`).
