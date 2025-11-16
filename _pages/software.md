---
permalink: /software/
title: "Software & Tools"
author_profile: true
---

I develop open-source software tools for multi-messenger astrophysics and transient astronomy. Below are my main contributions.

## Redback

**A Bayesian inference software package for electromagnetic transients**

[GitHub](https://github.com/nikhil-sarin/redback) | [Documentation](https://redback.readthedocs.io/) | [arXiv Paper](https://arxiv.org/abs/2308.12806)

Redback is a comprehensive Python package for fitting and interpreting electromagnetic transient observations. It provides:

- **Extensive model library**: 50+ models for kilonovae, GRB afterglows, supernovae, TDEs, and more
- **Flexible data handling**: Automatic data downloading from open-access catalogs
- **Bayesian inference**: Built on Bilby for robust parameter estimation
- **Simulation capabilities**: Forward modeling and population synthesis

### Key Features
- Joint fitting of multi-wavelength data
- Surrogate models for computationally expensive physics
- Easy extensibility for custom models
- Integration with major transient survey data

### Publications Using Redback
- [Redback: A Bayesian inference software package for electromagnetic transients](https://arxiv.org/abs/2308.12806) - Sarin et al. 2024, MNRAS
- Widely used in the community for fitting GRB afterglows, kilonovae, and other transients

### Installation
```bash
pip install redback
```

---

## Bilby

**Bayesian inference library for gravitational-wave astronomy**

[GitHub](https://git.ligo.org/lscsoft/bilby) | [Documentation](https://lscsoft.docs.ligo.org/bilby/)

I am a core contributor to Bilby, the primary Bayesian inference package used by the LIGO-Virgo-KAGRA Collaboration. Bilby provides a user-friendly interface for parameter estimation in gravitational-wave astronomy.

### Contributions
- Validation and testing frameworks
- Model implementations for electromagnetic counterparts
- Integration with Redback for joint GW-EM analysis

### Key Paper
- [Bayesian inference for compact binary coalescences with BILBY](https://arxiv.org/abs/2006.00714) - Romero-Shaw et al. 2020, MNRAS

---

## Other Tools & Contributions

### Surrogate Models for Type II Supernovae
Development of machine learning-based surrogate models for predicting supernova lightcurves and photosphere properties. These models enable rapid parameter estimation without expensive numerical simulations.
- [Surrogate models for lightcurves and photosphere properties of Type II supernovae](https://arxiv.org/abs/2506.02107) - Sarin et al. 2025

### Neutron Star Equation of State Inference
Tools for inferring nuclear physics from gravitational-wave and electromagnetic observations of neutron star mergers.
- [Measuring the nuclear equation of state with neutron star-black hole mergers](https://arxiv.org/abs/2311.05689) - Sarin et al. 2024, PRD

---

## Citation

If you use Redback in your research, please cite:

```bibtex
@article{sarin2024redback,
  title={Redback: A Bayesian inference software package for electromagnetic transients},
  author={Sarin, Nikhil and others},
  journal={Monthly Notices of the Royal Astronomical Society},
  year={2024}
}
```
