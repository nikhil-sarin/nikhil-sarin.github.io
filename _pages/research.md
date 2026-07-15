---
permalink: /research/
title: "Research"
author_profile: true
---

My research sits at the intersection of theoretical astrophysics, observational data, and statistical inference.
I build models for the lightcurves and spectra of explosive transients — supernovae, gamma-ray bursts, kilonovae, tidal disruption events, among others — and develop Bayesian and machine-learning methods to confront those models with data, individually and at population scale.
A common thread is the question: *what can the light and/or gravitational waves tell us about the physics of high energy transient phenomena, neutron stars, and massive stars more generally?*

---

## Gravitational-wave Astrophysics & Neutron Star Physics

A large strand of my research concerns what gravitational waves and multi-messenger observations can tell us about neutron star physics, and vice versa.

I have contributed to **gravitational-wave parameter estimation** since my PhD, including as one of the developers of [Bilby](https://arxiv.org/abs/2006.00714) — the Bayesian inference library that became the standard PE software for the LIGO Scientific Collaboration. My contributions included implementing the reduced-order quadrature likelihood for compact binary coalescences and Monte-Carlo noise realisations. I was on the writing team for the **LIGO-Virgo search for post-merger gravitational waves from GW170817** ([Abbott et al. 2019](https://arxiv.org/abs/1810.02581)), contributing to the astrophysical interpretation and calculating detection thresholds for third-generation detectors. I have also served on the parameter estimation rota for events in the LVK catalog.

On the **neutron star equation of state**, I developed a framework to **measure the nuclear EOS directly from NS-BH gravitational-wave mergers** ([Sarin et al. 2024](https://arxiv.org/abs/2311.05689)), and contributed to work on **jointly inferring cosmology and the EOS** from GW mergers ([Magnall, Goode, Sarin et al. 2024](https://arxiv.org/abs/2410.07754)). I also studied **what the fate of the post-merger remnant reveals about the EOS** — whether a neutron star survives or collapses — through modelling of X-ray afterglows and GW signatures ([Sarin et al. 2020](https://arxiv.org/abs/2001.06102), [Sarin & Lasky 2021](https://arxiv.org/abs/2012.08172)).

I pioneered **X-ray guided gravitational-wave searches** for binary neutron star merger remnants ([Sarin et al. 2018](https://arxiv.org/abs/1805.01481)), using EM observations to define targeted GW search windows. I have also argued for **continual single-observatory GW coverage** to avoid missing multimessenger events like GRB 211211A ([Sarin et al. 2023](https://arxiv.org/abs/2210.14938)), and studied the **coincidence of GW events with fast radio bursts** from NS-BH mergers ([Clarke, Sarin et al. 2025](https://arxiv.org/abs/2408.02534)).

On the **neutron star population**, I developed a framework using **inverse cascades** to confront neutron star spin-down models with the observed pulsar population ([Sarin et al. 2023](https://arxiv.org/abs/2305.14347)). Inverse cascades — the transfer of magnetic energy from small to large scales — can dramatically alter the spin-down and magnetic field evolution of young neutron stars, and I showed that accounting for this physics changes the inferred birth spin and magnetic field distributions of the pulsar population, with implications for the engine energetics of magnetar-driven transients. I also wrote an **invited review** on the evolution of binary NS post-merger remnants ([Sarin & Lasky 2021](https://arxiv.org/abs/2012.08172)) and made the science case for a **dedicated kHz gravitational-wave observatory** ([Sarin & Lasky 2022](https://arxiv.org/abs/2110.10892), Editor's Pick 2022).

---

## Neutron Star Mergers & Multi-messenger Astrophysics

Binary neutron star mergers are unique laboratories — they produce gravitational waves, short GRBs, and kilonovae simultaneously, and are the primary confirmed site of r-process nucleosynthesis.

I contributed to the astrophysical interpretation and multi-wavelength modelling for the **JWST discovery of heavy elements** in a neutron star merger ([Levan et al. 2023](https://www.nature.com/articles/s41586-023-06759-1)). I have modelled the diversity of **magnetar-driven kilonovae** ([Sarin et al. 2022](https://arxiv.org/abs/2205.14159)), studied **fast dynamic ejecta** in NS mergers ([Rosswog, Sarin et al. 2025](https://arxiv.org/abs/2411.18813)), and examined **heating-rate prescriptions** and their effect on kilonova light curves ([Sarin & Rosswog 2024](https://arxiv.org/abs/2404.07271)). I developed detailed strategies for **joint afterglow and kilonova fitting** of GRB observations, including working out how to handle afterglow contamination ([Wallace & Sarin 2025](https://arxiv.org/abs/2504.08887)).

I also developed a **hierarchical Bayesian framework linking the merger rates of NS binaries to the observed short GRB rate** ([Sarin et al. 2022](https://arxiv.org/abs/2201.08491)), marginalising over the beaming fraction, luminosity function, and detector sensitivity to jointly constrain the local BNS merger rate and the fraction that produce detectable sGRBs — providing a self-consistent picture connecting GW detections, GRB observations, and population synthesis models.

A growing focus is the new class of **Einstein Probe fast X-ray transients** — an observational window on jet-driven explosions, shock breakouts, and off-axis events — where I have contributed lightcurve modelling and theoretical interpretation across multiple discovery papers.

---

## Electromagnetic Transients & Lightcurve Modelling

The lightcurves and spectra of supernovae, GRBs, kilonovae, and TDEs encode the physics of the explosion, the progenitor, and the surrounding environment. A large part of my research involves building physical models that are accurate enough to be informative and fast enough for Bayesian inference — and then using them to interpret observations across a wide range of transient classes.

On **supernovae**, I developed a **generalised framework for circumstellar-matter interaction** ([Sarin & Hirai 2026](https://arxiv.org/abs/2605.19571)) that unifies a wide class of interaction-powered transients — from Type IIn to stripped-envelope events — under a single formalism built on arbitrary mass-loss histories and ejecta profiles. I studied how **$^{56}$Ni mixing and neutron-rich ejecta** fundamentally shape supernova lightcurves ([Sarin 2026](https://arxiv.org/abs/2606.23780)), demonstrating that fast bright rises are not by themselves evidence for low ejecta mass or engine power, and that one-zone fits to mixed lightcurves return systematically biased parameters — results with direct implications for how we interpret stripped-envelope supernovae and GRB-SNe as r-process targets. I led the lightcurve modelling for the **Nature paper revealing a new cosmic formation site of silicon and sulphur** in an extremely stripped supernova ([Schulze et al. 2025](https://arxiv.org/abs/2409.02054)), have modelled Type Ic-BL supernovae, superluminous supernovae, Type IIP supernovae and Type Ia supernovae across large observational campaigns, and contributed to numerous discovery papers on individual events.

On **gamma-ray bursts and afterglows**, I built models for X-ray plateau emission powered by millisecond magnetars and studied what they imply for the post-merger remnant ([Sarin et al. 2019](https://arxiv.org/abs/1812.08176), [Sarin et al. 2020](https://arxiv.org/abs/2008.05745)). I studied **low-efficiency long GRBs** ([Sarin et al. 2022](https://arxiv.org/abs/2106.01556)) and developed strategies for jointly fitting afterglow and kilonova emission — including how to handle afterglow contamination ([Wallace & Sarin 2025](https://arxiv.org/abs/2504.08887)). I also identified **CDF-S XT1 as a structured jet viewed off-axis at z=2.23** ([Sarin et al. 2023](https://arxiv.org/abs/2105.10108)) — one of the most distant off-axis GRB afterglows known — by combining Bayesian structured-jet modelling with X-ray and multi-wavelength data, demonstrating that apparently anomalous X-ray transients can be explained as the off-axis afterglows of ordinary short GRBs seen from an unfavourable viewing angle.

On **tidal disruption events**, I extended the **cooling envelope model** as a unified framework for TDE lightcurves ([Sarin & Metzger 2024](https://arxiv.org/abs/2307.15121)) and have applied it to individual events and population studies including testing whether TDE models can reliably measure black hole masses.

---

## Inference at Scale & Statistical Methods

Modern transient surveys — ZTF, Rubin/LSST, Einstein Probe — deliver data faster than traditional case-by-case analysis can keep up. A major focus of my work is developing the statistical and computational infrastructure to do rigorous physical inference on thousands of events simultaneously.

The central tool is [**Redback**](https://github.com/nikhil-sarin/redback) ([Sarin et al. 2024](https://arxiv.org/abs/2308.12806)), the end-to-end modelling, simulation, and inference package I built for electromagnetic transients. Redback handles everything from data ingestion and processing through a large library of physical models — magnetar engines, kilonova, GRB afterglows, supernovae, TDEs, CSM interaction, and more — to full Bayesian parameter estimation and population analysis. It now underpins inference across dozens of published studies and is the primary analysis tool used by my group. The model library has recently been extended with Fortran-based CSM interaction physics via [**Redback-CSM**](https://github.com/nikhil-sarin/redback-csm).

Fitting thousands of lightcurves with expensive physical models requires fast approximations. I develop **surrogate and emulator models** that reproduce physical model outputs at a fraction of the computational cost. I built surrogates for **Type II supernova lightcurves and photosphere evolution** ([Sarin et al. 2025](https://arxiv.org/abs/2506.02107)), enabling fast Bayesian inference on individual events and samples that would otherwise require expensive radiation-hydrodynamics calculations. Separately, I led the **lightcurve modelling of 2,205 ZTF DR2 Type Ia supernovae** ([Sarin et al. 2026](https://arxiv.org/abs/2602.02677)) — one of the largest such analyses to date — fitting physical models to the full sample to extract population-level constraints on SN Ia physics and cosmological implications. GPU-accelerated inference for even larger samples is in development via [**Redback-JAX**](https://github.com/nikhil-sarin/redback-jax).

Beyond lightcurve fitting, I develop **Bayesian hierarchical and simulation-based inference** frameworks for transient populations — linking progenitor populations to observed rates, and building decision-aware pipelines for real-time classification and follow-up prioritisation in the Rubin era.
