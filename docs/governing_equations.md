# Governing Equations

## 1. Model description

The first version of the model will describe calcium transport and gel formation along the length of the MixStix tube.

A one-dimensional model will be used initially, with position represented by \(x\) and time by \(t\).

The main variables are:

- \(c(x,t)\): concentration of free calcium ions.
- \(b(x,t)\): concentration of calcium bound to the polymer.
- \(g(x,t)\): local degree of gel formation, ranging from 0 to 1.
- \(D_{\mathrm{eff}}\): effective calcium diffusion coefficient.

The model will initially focus on diffusion. Bulk fluid movement will be considered in a later extension if sufficient information is available.

## 2. Calcium transport

The starting point is Fick's second law of diffusion:

\[
\frac{\partial c}{\partial t}
=
\frac{\partial}{\partial x}
\left(
D_{\mathrm{eff}}
\frac{\partial c}{\partial x}
\right)
\]

This equation describes how calcium concentration changes with time as a result of diffusion.

For a constant diffusion coefficient, it simplifies to:

\[
\frac{\partial c}{\partial t}
=
D_{\mathrm{eff}}
\frac{\partial^2 c}{\partial x^2}
\]

However, the diffusion coefficient may not remain constant as gelation progresses. The developing polymer network could affect calcium transport.

For this reason, the more general form will be retained in the model.

## 3. Calcium binding

Calcium ions do not simply diffuse through the solution without interacting with the polymer. They can associate with negatively charged regions of gellan gum.

To account for this, the model will distinguish between free calcium and calcium bound to the polymer.

A possible starting description of the binding process is:

\[
R_{\mathrm{bind}}
=
k_{\mathrm{on}}c(B_{\max}-b)
-
k_{\mathrm{off}}b
\]

Here:

- \(k_{\mathrm{on}}\) represents the binding rate constant.
- \(k_{\mathrm{off}}\) represents the dissociation rate constant.
- \(B_{\max}\) represents the available binding capacity.

The corresponding equations are:

\[
\frac{\partial c}{\partial t}
=
\frac{\partial}{\partial x}
\left(
D_{\mathrm{eff}}\frac{\partial c}{\partial x}
\right)
-
R_{\mathrm{bind}}
\]

\[
\frac{\partial b}{\partial t}
=
R_{\mathrm{bind}}
\]

This is a candidate representation, not yet a validated description of calcium binding in low-acyl gellan. Its suitability and parameters will need to be checked against experimental literature.

## 4. Gel formation

The local degree of gel formation will be represented by a variable \(g(x,t)\).

Its value will range from 0, representing an ungelled region, to 1, representing the chosen fully developed gel state.

A general kinetic equation can be written as:

\[
\frac{\partial g}{\partial t}
=
R_{\mathrm{gel}}(c,T,g)
\]

where \(R_{\mathrm{gel}}\) describes the local rate of gel development and \(T\) represents temperature.

The exact form of this function is not being fixed yet. It will depend on the available evidence about gellan gelation kinetics.

In particular, we should avoid assuming that gel formation is instantaneous or that it begins at one universal calcium concentration.

## 5. Coupling gel formation to diffusion

One of the central questions in this investigation is whether the developing gel changes the transport of calcium ions.

We can represent this possibility by allowing the effective diffusion coefficient to depend on the local gel state:

\[
D_{\mathrm{eff}}=D_{\mathrm{eff}}(g,T)
\]

The relationship between gel development and effective diffusivity will need to be established from published measurements or treated as an explicitly stated modelling assumption.

This coupling is important because it allows the model to investigate whether the first calcium dose changes the ability of the second dose to travel through the sample.

## 6. Initial conditions and clamp operation

Before either clamp is opened, the chambers contain the following solutions:

- First chamber: 10 mM calcium chloride.
- Middle chamber: 0.60% w/v low-acyl gellan gum.
- Third chamber: 10 mM calcium chloride.

The first clamp opens at \(t=0\), while the second remains closed until \(t=\Delta t\).

A closed clamp will initially be represented as an impermeable boundary, with no calcium flux across it:

\[
J_{\mathrm{Ca}}=0
\]

Once a clamp opens, the two neighbouring regions become connected. Concentration and calcium flux will then be treated as continuous across the newly opened interface.

The second clamp undergoes the same change at \(t=\Delta t\).

This is an idealised representation of the hardware. It does not assume that opening a clamp produces complete mixing or instantaneous bulk fluid movement.

## 7. Gravity conditions

The initial model will focus on diffusion under two different gravity conditions.

For the microgravity case, buoyancy-driven convection will be neglected in the first approximation.

For normal gravity, the eventual model may include a fluid velocity term:

\[
\frac{\partial c}{\partial t}
+
\frac{\partial (uc)}{\partial x}
=
\frac{\partial}{\partial x}
\left(
D_{\mathrm{eff}}\frac{\partial c}{\partial x}
\right)
-
R_{\mathrm{bind}}
\]

where \(u\) represents the fluid velocity.

The velocity cannot simply be assumed to be zero under normal gravity. However, it also cannot be calculated reliably without additional information about the tube orientation, temperature gradients and fluid properties.

The diffusion-only comparison will therefore be treated as a simplified baseline rather than a complete representation of both environments.

## 8. Main quantities to investigate

The equations should eventually allow us to calculate:

- Calcium concentration as a function of position and time.
- The distribution of bound calcium.
- The local degree of gel formation.
- Changes in effective diffusivity as the gel develops.
- The influence of the delay between the two calcium releases.
- Differences between normal-gravity and microgravity model conditions.

## 9. Outstanding questions

Several parts of the mathematical model still require investigation:

1. What diffusion coefficient is appropriate for calcium in the initial gellan solution?
2. How does calcium transport change as the gellan network develops?
3. Is a reversible binding model appropriate for this system?
4. What experimental relationship should be used to describe gel formation?
5. Can the clamp-release process reasonably be represented without explicitly modelling bulk fluid movement?

These questions will be addressed through the literature review and subsequent model development.

The equations presented here form the initial framework. They will be refined as the relevant material properties and experimental evidence become available.
