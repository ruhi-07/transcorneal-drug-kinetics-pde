# Transcorneal Bio-Transport: Transient Drug Penetration Kinetics

A computational finite-difference framework solving a time-dependent **Partial Differential Equation (PDE)** to simulate how topically applied ophthalmic solutions penetrate the multi-layered physical matrix of the human cornea.

This model allows researchers to predict transient drug saturation intervals before therapeutic molecules cross into the aqueous humor of the anterior chamber.

## The Mathematical Framework

The transient migration front of localized drug concentrations (\(C\)) across corneal space (\(x\)) over temporal progress (\(t\)) is governed by a non-steady-state **Diffusion-Reaction Partial Differential Equation**:

\[\frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2} - k_{el}C\]

### Biomechanical Dynamics Analyzed:
* **\(D \frac{\partial^2 C}{\partial x^2}\) (Fickian Diffusion Tensor):** Maps spatial transport mechanics across the tightly bound collagen lamellae framework of the corneal stroma.
* **\(k_{el}C\) (Physiological Clearance Rate):** Incorporates metabolic loss, nasolacrimal drainage vectors, and parallel cellular clearance mechanics within the anterior structures.

## Boundary Configurations Applied
The boundary constraints mimic exact anterior anatomy:
1. **Epithelial Interface (\(x = 0\)):** Continuous drug reservoir saturation representing topical drop application:  
   \[C(0, t) = C_{tear\_film}\]
2. **Endothelial Partition (\(x = L\)):** Zero-flux interface modeling downstream boundary resistance before aqueous humor transition:  
   \[\frac{\partial C}{\partial x} \Big\vert{}_{x=L} = 0\]

## Biomechanical Baseline Parameter Index

| Parameter Symbol | Definition / Biological Metric | Applied Model Value | Metric Units |
| :--- | :--- | :--- | :--- |
| **L** | Central thickness profile of a standard human cornea | `0.05` | cm (500 μm) |
| **D** | Diffusion coefficient of molecular drops inside stroma matrix | `3.2e-6` | cm² / s |
| **\(k_{el}\)** | Elimination and baseline systemic clearance constant | `1.5e-4` | s⁻¹ |
