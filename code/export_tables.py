# -*- coding: utf-8 -*-
"""
Exports Table 1 (Evidence-Weighted Synthesis) and Table 2 (Falsifiable Research
Agenda) from the manuscript as machine-readable CSV/JSON, so the evidence base
and research agenda can be filtered, cited, or reused programmatically.
"""
import csv
import json
import os

OUTDIR = os.path.dirname(__file__)

TABLE1 = [
    {"claim": "Soluble Aβ oligomers facilitate NMDA-R/mGluR1-dependent hippocampal LTD, independent of plaque",
     "evidence": "Ex vivo hippocampal slices, primary neuron culture, AKAP150 knock-in mice [6-10,49]",
     "status": "Established",
     "remaining_uncertainty": "Human in vivo relevance at physiological concentrations"},
    {"claim": "ERβ/GPER1 signaling modulates hippocampal spine density and plasticity",
     "evidence": "Electrophysiology, receptor knockout mice, ex vivo morphology [11-17]",
     "status": "Established",
     "remaining_uncertainty": "Translation from acute slice effects to chronic in vivo state"},
    {"claim": "GPER1 effects on plasticity are uniformly anti-LTD/pro-LTP",
     "evidence": "Direct electrophysiological evidence of GPER1-dependent mGluR-LTD [16]",
     "status": "Refuted as stated; context-dependent",
     "remaining_uncertainty": "Which conditions favor GPER1's pro-LTP vs. pro-LTD action"},
    {"claim": "Allopregnanolone decline reduces tonic GABAergic inhibition via GABA-A δ-subunit receptors",
     "evidence": "Postpartum depression cohorts, brexanolone/zuranolone RCTs [18-23]",
     "status": "Established",
     "remaining_uncertainty": "Generalization from postpartum to perimenopausal population"},
    {"claim": "Perimenopausal transition increases depression risk",
     "evidence": "Epidemiological cohorts, meta-analyses [5,24,25]",
     "status": "Established",
     "remaining_uncertainty": "Whether fluctuation or deficiency is the operative variable (Section 3.3)"},
    {"claim": "Systemic hormone therapy protects cognition/reduces dementia risk",
     "evidence": "Multiple RCTs (KEEPS, ELITE, WHI) and meta-analyses, largely null-to-mixed [37-44]",
     "status": "Contested / largely null in RCTs",
     "remaining_uncertainty": "Whether any subgroup (surgical menopause, APOE4 status, timing) benefits"},
    {"claim": "Sex differences and APOE4 interact to elevate female Alzheimer's risk",
     "evidence": "Large cohort meta-analyses, mouse models [26-30]",
     "status": "Established",
     "remaining_uncertainty": "Precise mechanism linking APOE4-sex interaction to endocrine transition"},
    {"claim": "Perimenopausal HPA-axis dysregulation mediates depression risk increase",
     "evidence": "Mixed: some cohorts show cortisol rise; controlled Dex/CRH studies show normal reactivity [45-48]",
     "status": "Contested",
     "remaining_uncertainty": "Whether HPA-axis involvement is present in a subgroup"},
    {"claim": "Endocrine state and proteoform burden act on convergent synaptic machinery (same threshold, BCM framework)",
     "evidence": "Structural/mechanistic overlap (NMDA-R/glutamatergic signaling in shared circuits); no combined study",
     "status": "Structurally plausible / Proposed",
     "remaining_uncertainty": "No direct experimental test exists (Section 9 addresses this gap)"},
    {"claim": "Endocrine state and proteoform burden are reciprocally interacting (Model 5, Section 5.2) rather than independent (Model 1) or upstream-driven (Model 4)",
     "evidence": "No direct experimental test identified",
     "status": "Hypothesized (this review's central claim)",
     "remaining_uncertainty": "Requires the full research agenda in Section 9 to adjudicate among Models 1-5"},
]

TABLE2 = [
    {"question": "Do endocrine state and oligomer burden interact (additively/synergistically) on LTD induction?",
     "model_intervention": "Ovariectomized vs. sham mice ± acute soluble Aβ oligomer infusion",
     "measurement": "Hippocampal LTD magnitude (field EPSP slope depression)",
     "predicted_outcome_model5": "LTD magnitude in OVX+oligomer exceeds the sum of single-factor effects",
     "interpretation_if_not_observed": "Equal to sum: additive, not synergistic (still consistent with Model 5, weaker form). No greater than larger single effect: supports Model 1 (independent pathways) for this readout"},
    {"question": "Is the interaction receptor-specific as proposed (ERβ, GABA-A δ-subunit)?",
     "model_intervention": "OVX mice + oligomer, ± ERβ-selective agonist or zuranolone-class GABA-A δ-PAM",
     "measurement": "LTD magnitude, spine density (Golgi/2-photon imaging)",
     "predicted_outcome_model5": "Partial normalization of LTD/spine loss by either agonist",
     "interpretation_if_not_observed": "No normalization: falsifies the specific receptor pathways proposed, even if a general endocrine-oligomer interaction holds via another route"},
    {"question": "Does GPER1 activation help or worsen oligomer-facilitated LTD, given its distinct LTD-promoting role (Section 3.1)?",
     "model_intervention": "OVX mice + oligomer + GPER1 agonist (G1)",
     "measurement": "LTD magnitude",
     "predicted_outcome_model5": "Direction not assumed; test is diagnostic, not confirmatory",
     "interpretation_if_not_observed": "If GPER1 agonism worsens LTD, the simplified \"estrogen restoration helps\" framing must be replaced with a pathway-specific model (Section 3.1)"},
    {"question": "Does peripheral, non-CNS-penetrating oligomer clearance reduce LTD/spine loss in oligomer-exposed, ovariectomized animals?",
     "model_intervention": "OVX mice + oligomer ± peripheral sequestration (as in Section 7.2)",
     "measurement": "LTD magnitude, spine density, peripheral vs. CNS oligomer concentration",
     "predicted_outcome_model5": "Reduced LTD/spine loss with clearance",
     "interpretation_if_not_observed": "No effect: the peripheral-sink logic (Section 7.2) does not extend to this synaptotoxic oligomer species/context"},
    {"question": "Does combined endocrine restoration + peripheral clearance outperform either alone?",
     "model_intervention": "Four-arm design: vehicle / endocrine only / clearance only / combined",
     "measurement": "LTD magnitude; if extended, mood/cognition-relevant behavioral measures",
     "predicted_outcome_model5": "Combined arm shows greatest normalization",
     "interpretation_if_not_observed": "No combined advantage over the better single arm: falsifies the additivity/synergy claim even if each single-target effect independently replicates"},
    {"question": "Are endocrine decline and proteoform burden consequences of a shared upstream driver (Model 4) rather than directly interacting?",
     "model_intervention": "Aged (not ovariectomized) mice with independently manipulated inflammatory/vascular status",
     "measurement": "LTD magnitude, correlation structure between endocrine markers, oligomer burden, and inflammatory/vascular markers",
     "predicted_outcome_model5": "Direct endocrine-oligomer interaction persists after controlling for shared aging/inflammatory covariates",
     "interpretation_if_not_observed": "If the interaction disappears after controlling for a shared covariate, Model 4 is favored over Model 5"},
]


def write_csv(rows, path):
    if not rows:
        return
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    write_csv(TABLE1, os.path.join(OUTDIR, 'table1_evidence_weighted_synthesis.csv'))
    write_csv(TABLE2, os.path.join(OUTDIR, 'table2_falsifiable_research_agenda.csv'))
    with open(os.path.join(OUTDIR, 'table1_evidence_weighted_synthesis.json'), 'w', encoding='utf-8') as f:
        json.dump(TABLE1, f, ensure_ascii=False, indent=2)
    with open(os.path.join(OUTDIR, 'table2_falsifiable_research_agenda.json'), 'w', encoding='utf-8') as f:
        json.dump(TABLE2, f, ensure_ascii=False, indent=2)
    print('wrote', len(TABLE1), 'rows to table1 and', len(TABLE2), 'rows to table2 (CSV + JSON)')
