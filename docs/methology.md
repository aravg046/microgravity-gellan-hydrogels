# Research Methodology

## 1. Overview

This investigation will use computational modelling to study the formation of low-acyl gellan gum hydrogels following sequential exposure to calcium ions under microgravity conditions.

The proposed experiment uses a three-chamber MixStix arrangement. A gellan gum solution is exposed to two equal doses of calcium chloride, introduced at different times. The main objective is to investigate whether the timing of calcium exposure influences the spatial distribution and development of the resulting hydrogel network.

The computational study will be developed alongside the proposed physical experiment. This will allow us to examine the expected behaviour of the system and identify the conditions under which the proposed arrangement is feasible.

## 2. Proposed experimental arrangement

The sample will occupy three separate chambers within a flexible, transparent tube.

| Chamber | Contents | Volume |
|---|---|---:|
| First | 10 mM calcium chloride | 2.0 mL |
| Middle | 0.60% w/v low-acyl gellan gum | 4.0 mL |
| Third | 10 mM calcium chloride | 2.0 mL |

The total proposed sample volume is 8.0 mL.

Two external pinch clamps separate the chambers. The first calcium dose is introduced by opening the first clamp, followed by the second dose after a selected interval.

Both calcium solutions have the same concentration and volume. The interval between their introduction will be treated as an important experimental variable.

## 3. Sequence of events

The proposed sequence is:

1. The three solutions are loaded into their respective chambers.
2. The first clamp is opened, allowing the first calcium solution to contact the gellan gum.
3. The sample is left for a predetermined interval.
4. The second clamp is opened, introducing the remaining calcium solution.
5. The sample is retained under the designated experimental conditions until the observation or analysis stage.

The exact loading, storage, clamp operation and handling procedures will be subject to the programme's approved hardware and safety requirements.

Opening a clamp will not be assumed to produce complete or instantaneous mixing.

## 4. Computational approach

The computational model will initially represent the tube as a one-dimensional system.

It will examine calcium transport through the sample, calcium interaction with the polymer and the development of the hydrogel network over time.

The first version will focus on diffusion. More complex effects, including fluid movement and changes in effective diffusivity during gelation, may be incorporated as the model develops and suitable data become available.

The two calcium releases will be represented as separate events, with the interval between them varied to examine its influence on the resulting concentration and gelation profiles.

## 5. Comparison between gravity conditions

A central part of the investigation is the comparison between gel formation under normal gravity and microgravity.

The flight sample is intended to experience microgravity conditions, while a corresponding ground sample will provide a reference for comparison.

The orientation of the ground-control tube has not yet been finalised. A vertical arrangement would align the tube's length with gravity, whereas a horizontal arrangement would place it perpendicular to gravity.

These arrangements may produce different patterns of fluid movement. The choice of orientation will therefore need to be justified before the comparison is finalised.

The initial computational model will distinguish between diffusion-dominated transport and transport potentially influenced by buoyancy-driven convection.

## 6. Variables under investigation

The principal variable will be the time interval between the two calcium releases.

Other parameters that may be examined include:

- Initial calcium concentration.
- Gellan gum concentration.
- Tube dimensions.
- Effective calcium diffusion coefficient.
- Temperature.
- Gravity condition.

Where possible, individual variables will be changed independently to understand their influence on the model's predictions.

## 7. Potential observations and analysis

The proposed investigation will focus on differences in the spatial distribution and development of the hydrogel.

Potential measurements include:

- Photographic documentation of the final gel.
- Continuity and uniformity of the gel along the tube.
- Differences between regions exposed to calcium at different times.
- Mechanical properties, where suitable testing equipment and sample geometry permit.
- Microscopic examination, if appropriate.

These measurements will be used to compare the experimental observations with the computational predictions.

Post-return measurements will describe the recovered sample. They cannot, by themselves, establish the exact time at which gelation occurred during the flight.

## 8. Limitations and experimental considerations

Several factors may influence the results independently of gravity.

These include differences in temperature history, sample preparation, storage, handling, clamp operation and the behaviour of the developing gel.

The actual internal geometry of the flight hardware also remains to be confirmed. Dimensions taken from older SSEP specifications will therefore be treated as provisional in the computational model.

A further limitation is that the first calcium dose may produce a developing gel network that changes the transport of the second dose. Whether this happens, and to what extent, remains an open research question.

The computational model will consequently be treated as an investigation of the proposed system rather than a complete prediction of flight behaviour.

## 9. Current unresolved decisions

The following points must be addressed as the project progresses:

- Final orientation of the Earth-control tube.
- Exact tube and chamber dimensions.
- Suitable delay intervals between calcium releases.
- Appropriate diffusion and gelation parameters from published research.
- Availability of suitable post-experiment measurements.
- The extent to which the physical experiment can be reproduced in the computational model.

These decisions will be documented as they are resolved, with assumptions kept separate from experimentally established information.
