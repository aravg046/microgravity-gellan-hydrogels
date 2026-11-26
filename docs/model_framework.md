# Model Framework

## 1. Introduction

The purpose of this model is to investigate how sequential calcium-ion exposure affects the formation of low-acyl gellan gum hydrogels under microgravity conditions.

Gellan gum forms hydrogels in the presence of suitable cations, including calcium ions. The interaction between the polymer and these ions contributes to the formation of a three-dimensional network. However, the resulting gel structure depends on several factors, including polymer concentration, ion concentration, temperature and the conditions under which gelation takes place.

In our proposed experiment, calcium chloride is introduced into the gellan gum solution in two separate stages. This provides an opportunity to investigate whether the timing of calcium exposure influences the distribution and development of the resulting gel.

The computational model will focus on the transport of calcium ions, their interaction with the polymer and the development of the hydrogel network over time.

## 2. Calcium-ion transport

When the first calcium chloride solution comes into contact with the gellan gum solution, calcium ions begin to move through the system.

The primary mechanism considered in the initial model will be molecular diffusion. This process occurs because of differences in concentration, with ions moving from regions of higher concentration towards regions of lower concentration.

Under normal gravity, fluid movement can also be influenced by buoyancy-driven convection. Temperature and concentration differences may contribute to this movement, depending on the properties of the solution.

In microgravity, buoyancy-driven convection is greatly reduced. However, diffusion does not disappear. Other effects, including surface tension, capillary forces, wall interactions and residual acceleration, may still influence transport.

An important objective of the investigation is to determine whether the reduced influence of buoyancy changes the spatial distribution of calcium ions during gel formation.

## 3. Interaction between calcium ions and gellan gum

Low-acyl gellan gum is an anionic polysaccharide. Calcium ions interact with negatively charged regions of the polymer and help form junction zones within the developing network.

As these interactions develop, the solution gradually acquires the properties of a hydrogel.

This process is not necessarily uniform throughout the sample. Regions receiving calcium ions earlier or at higher local concentrations may begin forming a network before other regions.

For the computational model, gel formation will therefore be treated as a process that can vary with both position and time.

The relationship between local calcium concentration and the extent of gel formation will need to be established using experimental literature. We should not assume that gelation occurs at one universal calcium concentration or follows a simple instantaneous reaction.

## 4. Sequential calcium exposure

The proposed MixStix arrangement contains three chambers:

- The first chamber contains 2.0 mL of 10 mM calcium chloride solution.
- The middle chamber contains 4.0 mL of 0.60% w/v low-acyl gellan gum solution.
- The third chamber contains another 2.0 mL of 10 mM calcium chloride solution.

The first calcium dose is introduced when the first clamp is opened. Following a selected delay, the second clamp is opened to introduce the remaining calcium solution.

Both doses have the same concentration and volume.

The interval between the two releases is an important variable in the investigation. During this period, the first calcium dose may diffuse through the gellan solution and initiate gel formation.

One possibility is that the developing network changes the transport of calcium ions through the initially exposed region. If this occurs, it could influence the distribution of the second dose.

However, this effect cannot be assumed in advance. The first dose may produce a local gel barrier, a gradual change in transport properties, or no significant restriction at all. Determining which behaviour is most realistic is one of the central questions the model should address.

## 5. Coupling transport and gel formation

The model will need to consider calcium transport and gel development together rather than as completely independent processes.

Initially, calcium ions move through the liquid gellan solution. As the polymer network develops, the environment through which the ions move changes.

This raises the possibility that the effective rate of calcium transport may depend on the local state of gel formation.

A later version of the model may therefore account for changes in effective diffusivity as the gel network develops.

The exact relationship between gel formation and ion transport will require suitable experimental data. Until then, it should be treated as a modelling hypothesis rather than an established material property.

## 6. Representing microgravity

The main comparison of interest is between gel formation under normal gravity and under microgravity.

The initial model will focus on the difference in buoyancy-driven transport between these conditions. Molecular diffusion will remain present in both cases.

A one-dimensional representation of the tube will be used initially. This will allow us to study how calcium concentration and gel formation vary along the tube's length without introducing unnecessary geometric complexity at the beginning.

This is a simplification. Actual transport may also depend on the tube walls, its cross-section, the position of the clamps and the presence of bubbles.

The model will be expanded only if the available information and computational approach justify a more detailed representation.

## 7. Variables and outputs

The model should eventually allow us to examine:

- Calcium-ion concentration at different positions along the tube.
- Changes in calcium distribution over time.
- The time and location at which gel formation begins.
- The spatial distribution of the developing gel network.
- The influence of the delay between the two calcium releases.
- Differences between normal-gravity and microgravity conditions.

These outputs will help us determine whether sequential calcium exposure produces a different gelation pattern from a more immediate exposure.

## 8. Scope and limitations

The first version of the model will use simplified geometry and a limited number of physical processes. It will not attempt to reproduce every aspect of the MixStix experiment.

In particular, opening a clamp will initially be represented as a sudden release. This does not imply that the contents mix instantaneously or that the released solution travels through the tube in a predictable manner.

The model will also require literature-derived values for diffusion, gelation kinetics and the properties of the selected gellan gum grade. These values will be documented separately in the parameter sheet.

The purpose of this framework is to establish a physical basis for the simulation. Its assumptions will be revised as more reliable experimental data and literature become available.

Ultimately, the model should help us investigate whether sequential calcium exposure can produce distinguishable spatial patterns of hydrogel formation under microgravity, and whether reduced buoyancy-driven transport contributes to those differences.



## Computational dimensionality

The investigation will use a two-dimensional computational model, with one coordinate representing the length of the tube and the other representing its vertical cross-sectional direction.

This approach will allow us to investigate spatial variations in calcium transport and gel formation, while also considering the influence of gravity on fluid movement.

The model will initially use a simplified two-dimensional representation of the cylindrical tube. It will not fully reproduce three-dimensional flow or all effects associated with the tube walls.

The model will be developed in stages, beginning with diffusion and calcium binding, followed by gel-dependent transport and, where sufficient physical data are available, fluid flow under different gravity conditions.

## Numerical method

The computational model will use the Finite Element Method (FEM) to solve the governing equations in two spatial dimensions.

FEM was selected because it provides flexibility when representing the tube geometry, applying boundary conditions and extending the model to include coupled transport processes.

The initial implementation will use Python, with scikit-fem as the preferred FEM library. NumPy and SciPy will support numerical calculations, while Matplotlib will be used to visualise the results.

The choice of library and solver will be tested through a small prototype before the complete model is developed.
