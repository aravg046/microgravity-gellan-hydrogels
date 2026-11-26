# Parameter Sheet and Initial Assumptions

This document brings together the values and assumptions we will use while developing the computational model of sequential gellan gum gelation in microgravity. Some values come directly from our proposed experiment, while others are estimates taken from published hardware specifications. We will update this document as the literature review progresses.

## 1. Tube and chamber specifications

Our proposed experiment uses a three-chamber MixStix arrangement, with the chambers separated by two external pinch clamps.

| Parameter | Current value | Notes |
|---|---:|---|
| Maximum tube capacity | 10 mL | Published MixStix specification |
| Total sample volume | 8.0 mL | Proposed experiment |
| Tube length | 170 mm | Taken from an older SSEP specification |
| Internal diameter | 9.5 mm | Taken from an older SSEP specification |
| Outer diameter | 13 mm | Taken from an older SSEP specification |
| Number of chambers | 3 | Proposed arrangement |
| Number of clamps | 2 | Proposed arrangement |

The tube dimensions need some caution. The measurements come from an older SSEP document and have not been confirmed for the exact hardware used in our programme. For now, we will use them as starting estimates and allow the dimensions to be changed in the simulation.

## 2. Materials and solution composition

The proposed formulation uses low-acyl gellan gum and calcium chloride. Both calcium solutions have the same concentration and volume.

| Component | Concentration | Volume |
|---|---:|---:|
| Low-acyl gellan gum stock | 0.60% w/v | 4.0 mL |
| First calcium chloride solution | 10 mM | 2.0 mL |
| Second calcium chloride solution | 10 mM | 2.0 mL |

The total sample volume is therefore 8.0 mL.

## 3. Values calculated from the formulation

A few useful quantities can be worked out directly from the proposed composition:

- The gellan gum stock contains 24 mg of polymer.
- Each calcium chloride dose contains 20 µmol of calcium chloride.
- Both doses together contain 40 µmol.
- If the entire sample eventually mixes uniformly, the average gellan concentration will be 0.30% w/v.
- Under the same assumption, the final average calcium chloride concentration will be 5.0 mM.

These final concentrations are useful for mass-balance calculations. They do not mean that the sample will actually become uniform during the experiment.

## 4. How the experiment begins

Before either clamp is opened, the three chambers contain:

- Chamber 1: 2.0 mL of 10 mM calcium chloride solution.
- Chamber 2: 4.0 mL of 0.60% w/v low-acyl gellan gum solution.
- Chamber 3: 2.0 mL of 10 mM calcium chloride solution.

The first clamp is opened at the beginning of the experiment. After a selected waiting period, the second clamp is opened, introducing the remaining calcium solution.

The interval between the two releases will be an important variable in the model.

## 5. Initial approach to modelling

We will initially represent the tube as a one-dimensional system, following changes in calcium concentration and gel formation along its length.

For the first version, opening a clamp will be represented as a sudden release. This is a simplifying assumption rather than a claim that the actual fluid movement is instantaneous.

We also need to account for an important possibility: the first calcium dose may cause gelation near the initial contact region. If this happens, the developing gel could affect how readily the second dose travels through the tube.

The model should therefore allow spatial differences in calcium concentration and gel formation rather than assuming that everything mixes uniformly.

## 6. Properties we still need to establish

The following values cannot yet be assigned confidently. We will look for suitable experimental measurements in the literature before using them.

| Property | Current status |
|---|---|
| Calcium-ion diffusion coefficient | Literature review pending |
| Calcium transport through developing gellan gel | Unknown |
| Gellan gelation kinetics | Literature review pending |
| Effect of temperature on gelation | Literature review pending |
| Rheological properties of the selected gellan grade | Literature review pending |
| Actual temperature history | To be established |
| Exact internal chamber geometry | Not confirmed |

## 7. Keeping track of uncertainty

Throughout the project, we will distinguish between values taken from the proposed experiment, values reported in published research, quantities calculated from existing values, and assumptions introduced for modelling.

This distinction matters because the purpose of the simulation is to investigate the behaviour of the proposed system, not to make uncertain hardware specifications or material properties appear established.

As more reliable information becomes available, the assumptions and parameter values will be revised accordingly.
