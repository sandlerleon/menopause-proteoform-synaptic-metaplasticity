# -*- coding: utf-8 -*-
"""
Regenerates Figures 1-3 of:
Sandler, L. "Endocrine State and Soluble Proteoforms as Convergent Regulators of
Synaptic Plasticity: Implications for Menopause and Early Neurodegeneration."

These are conceptual/schematic diagrams (box-and-arrow flowcharts), not data plots:
no simulation or dataset underlies them. The script exists so the figures are
reproducible and version-controlled rather than static images.
"""
import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUTDIR = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUTDIR, exist_ok=True)


def box(ax, xy, w, h, text, facecolor, edgecolor, fontsize=12, fontweight='normal'):
    x, y = xy
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.02",
        facecolor=facecolor, edgecolor=edgecolor, linewidth=2,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha='center', va='center',
             fontsize=fontsize, fontweight=fontweight, wrap=True)
    return (x + w / 2, y), (x + w / 2, y + h), (x, y + h / 2), (x + w, y + h / 2)


def arrow(ax, start, end, connectionstyle="arc3,rad=0.0", color='#333333'):
    a = FancyArrowPatch(start, end, arrowstyle='-|>', mutation_scale=18,
                         connectionstyle=connectionstyle, color=color, linewidth=1.8)
    ax.add_patch(a)


def new_fig(width=11, height=7.5):
    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.axis('off')
    return fig, ax


ORANGE_FILL, ORANGE_EDGE = '#FDE8C8', '#D98B0A'
GREEN_FILL, GREEN_EDGE = '#E4F0DE', '#4C8C3C'
GREY_FILL, GREY_EDGE = '#EDEDED', '#555555'
PURPLE_FILL, PURPLE_EDGE = '#EDE7F6', '#6A4C93'
RED_FILL, RED_EDGE = '#FBE4E4', '#B33A3A'


def figure1():
    fig, ax = new_fig(11, 8.5)
    ax.set_title('Figure 1. Conceptual framework: proposed convergence of endocrine and\n'
                  'proteoform pathways on hippocampal/limbic synaptic plasticity', fontsize=13)

    b_endo = box(ax, (0.4, 6.7), 4.6, 1.3,
                 'Perimenopausal endocrine transition\n(↓ estradiol, ↓ allopregnanolone,\nhormonal variability)',
                 ORANGE_FILL, ORANGE_EDGE, fontweight='bold')
    b_prot = box(ax, (5.8, 6.7), 4.8, 1.3,
                 'Soluble Aβ (and, more provisionally,\ntau) oligomer accumulation\n(pre-plaque, early)',
                 GREEN_FILL, GREEN_EDGE, fontweight='bold')

    b_endo_r = box(ax, (0.4, 5.0), 4.6, 1.2,
                    'Receptor-level effects:\nERβ, GPER1, GABA-A δ-subunit\n(Section 2)',
                    ORANGE_FILL, ORANGE_EDGE)
    b_prot_r = box(ax, (5.8, 5.0), 4.8, 1.2,
                    'Receptor-level effects:\nNMDA-R/GluN2B, mGluR1,\nglutamate uptake (Section 3)',
                    GREEN_FILL, GREEN_EDGE)

    b_conv = box(ax, (2.6, 3.2), 5.8, 1.3,
                 'Convergent postsynaptic signaling:\ncalcineurin/AKAP150-dependent\nspine-elimination machinery',
                 GREY_FILL, GREY_EDGE, fontweight='bold')

    b_ltd = box(ax, (2.6, 1.7), 5.8, 1.1,
                'Shift in hippocampal/limbic\nLTD/LTP balance\n("LTD bias", Section 4)',
                PURPLE_FILL, PURPLE_EDGE, fontweight='bold')

    b_mood = box(ax, (0.4, 0.2), 4.2, 1.1,
                 'Mood / subjective cognitive\nsymptoms\n(clinically distinct entities, Section 6)',
                 RED_FILL, RED_EDGE)
    b_struct = box(ax, (5.8, 0.2), 4.8, 1.1,
                    'Structural change:\ndendritic spine loss,\ncircuit dysfunction',
                    RED_FILL, RED_EDGE)

    arrow(ax, (2.7, 6.7), (2.7, 6.2))
    arrow(ax, (8.2, 6.7), (8.2, 6.2))
    arrow(ax, (2.7, 5.0), (4.6, 4.5), connectionstyle="arc3,rad=-0.2")
    arrow(ax, (8.2, 5.0), (6.4, 4.5), connectionstyle="arc3,rad=0.2")
    ax.text(5.5, 4.75, 'proposed\nconvergence\n(Section 4)', ha='center', fontsize=9, style='italic', color='#444444')
    arrow(ax, (5.5, 3.2), (5.5, 2.8))
    arrow(ax, (3.5, 1.7), (2.5, 1.3), connectionstyle="arc3,rad=-0.2")
    arrow(ax, (7.5, 1.7), (8.2, 1.3), connectionstyle="arc3,rad=0.2")

    plt.tight_layout()
    fig.savefig(os.path.join(OUTDIR, 'figure1_convergence_framework.png'), dpi=150)
    plt.close(fig)


def figure2():
    fig, ax = new_fig(11, 7)
    ax.set_title('Figure 2. Estrogen and allopregnanolone act through multiple, not uniformly\n'
                  'pro-LTP, receptor pathways on hippocampal plasticity', fontsize=13)

    b_e2 = box(ax, (0.4, 5.4), 3.5, 1.2, '17β-estradiol\n(E2)', ORANGE_FILL, ORANGE_EDGE, fontweight='bold')
    b_allo = box(ax, (4.3, 5.4), 4.0, 1.2, 'Allopregnanolone\n(progesterone-derived)', ORANGE_FILL, ORANGE_EDGE, fontweight='bold')

    b_era = box(ax, (0.2, 3.7), 1.9, 1.1, 'ERα', '#FFF4E0', ORANGE_EDGE)
    b_erb = box(ax, (2.2, 3.7), 1.9, 1.1, 'ERβ', '#FFF4E0', ORANGE_EDGE)
    b_gper = box(ax, (4.3, 3.7), 2.3, 1.1, 'GPER1\n(membrane)', '#FFF4E0', ORANGE_EDGE)
    b_gaba = box(ax, (6.8, 3.7), 2.8, 1.1, 'GABA-A δ-subunit\n(extrasynaptic)', '#FFF4E0', ORANGE_EDGE)

    b_pro = box(ax, (0.2, 1.7), 4.0, 1.2,
                '↑ PSD-95, GluR1,\ndendritic branching\n(pro-LTP, Section 2.1)', GREEN_FILL, GREEN_EDGE)
    b_ctx = box(ax, (4.4, 1.7), 2.3, 1.2,
                'Context-dependent:\nboth pro-LTP AND a\ndistinct mGluR-LTD form', RED_FILL, RED_EDGE, fontweight='bold')
    b_tonic = box(ax, (7.0, 1.7), 2.9, 1.2,
                  '↓ tonic inhibition when\nallopregnanolone falls\n(postpartum/perimenopausal)', GREEN_FILL, GREEN_EDGE)

    arrow(ax, (1.5, 5.4), (1.15, 4.8), connectionstyle="arc3,rad=0.1")
    arrow(ax, (2.1, 5.4), (3.1, 4.8), connectionstyle="arc3,rad=-0.2")
    arrow(ax, (6.0, 5.4), (5.4, 4.8), connectionstyle="arc3,rad=0.2")
    arrow(ax, (7.6, 5.4), (8.2, 4.8), connectionstyle="arc3,rad=-0.15")

    arrow(ax, (1.15, 3.7), (2.2, 2.9), connectionstyle="arc3,rad=-0.15")
    arrow(ax, (3.15, 3.7), (2.6, 2.9), connectionstyle="arc3,rad=0.15")
    arrow(ax, (5.45, 3.7), (5.55, 2.9))
    arrow(ax, (8.2, 3.7), (8.45, 2.9))

    plt.tight_layout()
    fig.savefig(os.path.join(OUTDIR, 'figure2_estrogen_allopregnanolone_pathways.png'), dpi=150)
    plt.close(fig)


def figure3():
    fig, ax = new_fig(11, 7)
    ax.set_title('Figure 3. Soluble Aβ oligomers facilitate hippocampal LTD via convergent\n'
                  'NMDA-receptor/mGluR1/calcineurin signaling, independent of plaque', fontsize=13)

    b_ab = box(ax, (0.3, 5.3), 4.2, 1.2,
               'Soluble Aβ oligomers\n(dimers/trimers, not monomers)', GREEN_FILL, GREEN_EDGE, fontweight='bold')
    b_uptake = box(ax, (4.8, 5.3), 3.2, 1.2, '↓ Neuronal glutamate\nuptake', '#EEF6EA', GREEN_EDGE)
    b_glu = box(ax, (8.3, 5.3), 2.6, 1.2, '↑ Extracellular\nglutamate', '#EEF6EA', GREEN_EDGE)

    b_nmda = box(ax, (0.7, 3.3), 4.5, 1.2,
                 'Excessive extrasynaptic\nGluN2B-NMDAR activation', ORANGE_FILL, ORANGE_EDGE)
    b_mglur = box(ax, (5.7, 3.3), 4.2, 1.2,
                  'mGluR1 activation\n(acute co-engagement)', ORANGE_FILL, ORANGE_EDGE)

    b_can = box(ax, (2.2, 1.2), 6.5, 1.3,
                'AKAP150-anchored calcineurin (CaN)\nsignaling → spine shrinkage/elimination',
                GREY_FILL, GREY_EDGE, fontweight='bold')

    arrow(ax, (2.4, 5.3), (2.9, 4.5), connectionstyle="arc3,rad=-0.15")
    arrow(ax, (4.8, 6.0), (7.0, 6.0), connectionstyle="arc3,rad=-0.3")
    arrow(ax, (6.3, 5.3), (7.5, 4.5), connectionstyle="arc3,rad=0.15")
    arrow(ax, (9.6, 5.3), (8.2, 4.5), connectionstyle="arc3,rad=0.25")

    arrow(ax, (3.0, 3.3), (4.5, 2.5), connectionstyle="arc3,rad=-0.15")
    arrow(ax, (7.8, 3.3), (6.5, 2.5), connectionstyle="arc3,rad=0.15")

    plt.tight_layout()
    fig.savefig(os.path.join(OUTDIR, 'figure3_ab_oligomer_ltd_mechanism.png'), dpi=150)
    plt.close(fig)


if __name__ == '__main__':
    figure1()
    figure2()
    figure3()
    print('wrote 3 figures to', OUTDIR)
