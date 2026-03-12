
# Measles Outbreak Modeling in Niamey, Niger

## 1. Introduction

Measles is a highly contagious viral disease that continues to cause outbreaks in regions with insufficient vaccination coverage. Due to its high transmissibility, measles epidemics can spread rapidly in populations with a large proportion of susceptible individuals. Mathematical models are widely used in epidemiology to understand transmission dynamics and estimate key parameters that characterize epidemic spread.

One of the most commonly used frameworks for modeling infectious disease transmission is the **Susceptible–Infectious–Recovered (SIR) model**. This model divides the population into compartments representing individuals who are susceptible, infectious, or recovered. By modeling transitions between these compartments, the SIR framework allows researchers to estimate parameters such as the **transmission rate** and the **basic reproduction number (R₀)**.

In this analysis, we examined **biweekly measles incidence data from Niamey, Niger**, covering three communities (A, B, and C). The objectives were to estimate the early epidemic growth rate, infer the basic reproduction number, implement a deterministic SIR model, and estimate transmission parameters using likelihood-based methods. Sensitivity and uncertainty analyses were also performed to assess the robustness of parameter estimates.

---

## 2. Data Description

The dataset contains **biweekly measles case counts** collected from three communities in Niamey.

Dataset characteristics:

- **Time unit:** biweeks (two-week intervals)
- **Communities:** A, B, C
- **Variables:**
  - `biweek`: time index
  - `community`: community identifier
  - `measles`: number of reported cases

Summary statistics:

- Number of observations: **48**
- Mean incidence: **232.5 cases**
- Maximum observed incidence: **1041 cases**
- Median incidence: **81 cases**

The observed data represent **biweekly incidence**, meaning the number of new measles cases occurring during each two-week period.

---

## 3. Early Outbreak Analysis

During the early phase of an epidemic, when most individuals are susceptible, disease incidence often grows approximately exponentially.

The exponential growth model can be written as:

\[
I(t) = I_0 e^{rt}
\]

where:

- \(I(t)\) = incidence at time \(t\)
- \(r\) = exponential growth rate

The estimated early outbreak growth rate was:

\[
r = 0.439
\]

with a **95% confidence interval**:

\[
0.374 \le r \le 0.504
\]

Using the relationship between the growth rate and the basic reproduction number:

\[
R_0 = \frac{\beta}{\gamma}
\]

and assuming an infectious period of approximately **2 weeks**, we set:

\[
\gamma = 1 \text{ per biweek}
\]

This produced an estimated reproduction number:

\[
R_0 \approx 1.44
\]

Analysis of different early outbreak windows indicated that the most stable estimates occurred for **biweeks 8–10**, where \(R_0\) values were approximately:

- 1.432
- 1.443
- 1.439

---

## 4. SIR Model

To describe epidemic dynamics mechanistically, a deterministic **SIR model** was implemented.

The model consists of three compartments:

- \(S(t)\): susceptible individuals
- \(I(t)\): infectious individuals
- \(R(t)\): recovered individuals

The governing equations are:

\[
\frac{dS}{dt} = -\beta \frac{SI}{N}
\]

\[
\frac{dI}{dt} = \beta \frac{SI}{N} - \gamma I
\]

\[
\frac{dR}{dt} = \gamma I
\]

where:

- \(N\) = population size
- \(\beta\) = transmission rate
- \(\gamma\) = recovery rate

### Mapping Model States to Observed Incidence

Because the data represent **new cases per biweek**, model incidence was reconstructed using an accumulator variable \(H(t)\):

\[
\frac{dH}{dt} = \beta \frac{SI}{N}
\]

Predicted incidence was calculated as:

\[
\Delta H(t) = H(t) - H(t-1)
\]

This represents the number of **new infections during each biweekly interval**.

---

## 5. Parameter Estimation

Two approaches were used to estimate model parameters.

### Nonlinear Least Squares

The model was first fit by minimizing the **sum of squared errors (SSE)** between observed and simulated incidence.

Sensitivity analysis of the transmission rate showed:

- Best transmission rate estimate:

\[
\beta \approx 1.72
\]

with minimum SSE:

\[
SSE \approx 532103
\]

---

### Poisson Likelihood

Because incidence data represent **counts**, a Poisson observation model was used:

\[
Y_t \sim Poisson(p \cdot \lambda_t)
\]

where:

- \(Y_t\) = observed incidence
- \(\lambda_t\) = model-predicted incidence
- \(p\) = reporting probability

Parameter estimation using maximum likelihood produced the following estimates:

- **Population size (N):** 9999.99  
- **Transmission rate (β):** 1.741  
- **Initial infections (I₀):** 3.61  
- **Immune fraction:** 0.044  
- **Reporting probability (p):** 0.992  

Final negative log-likelihood:

\[
-31882.91
\]

---

## 6. Results

Estimated parameters:

| Parameter | Estimate |
|----------|----------|
| β | 1.741 |
| R₀ | 1.741 |
| N | 9999.99 |
| I₀ | 3.61 |
| immune_fraction | 0.044 |
| reporting probability p | 0.992 |

### Early outbreak growth rate

\[
r = 0.439
\]

### Key observations from epidemic curves

- The outbreak exhibits a **rapid early exponential growth phase**.
- The SIR model reproduces the **general shape of the epidemic curve**.
- The peak incidence occurs around the **middle of the observation period**.

---

## 7. Sensitivity Analysis

Sensitivity analyses were performed to evaluate how model outputs change under different assumptions.

Two main analyses were conducted:

### Early outbreak window sensitivity

Estimates of \(R_0\) were computed using different early time windows. The most stable estimates were observed for **biweeks 8–10**, suggesting that the exponential growth assumption holds best during this period.

### Transmission rate sensitivity

The sum of squared errors was evaluated across different values of β. The SSE curve displayed a clear minimum near:

\[
\beta \approx 1.72
\]

This indicates that the observed data strongly constrain the transmission rate.

---

## 8. Uncertainty Analysis

Parameter uncertainty was assessed using **profile likelihood analysis** for β.

In this analysis:

- β was fixed across a range of values
- Remaining parameters were re-estimated
- The resulting negative log-likelihood was recorded

The profile likelihood indicated a best estimate of:

\[
\beta \approx 1.83
\]

with optimized parameters:

- \(N = 9999.86\)
- \(I_0 = 3.26\)
- immune_fraction = 0.088
- \(p = 0.9999\)

The profile likelihood curve exhibited a clear minimum, indicating that β is **well identified by the data**.

---

## 9. Comparison Between Communities

Although the primary analysis focused on **Community A**, the same modeling framework can be applied to **Communities B and C**.

Comparing parameter estimates across communities could reveal differences in:

- transmission rates
- epidemic timing
- attack rates
- population immunity levels

Such comparisons can provide insight into how local population characteristics influence outbreak dynamics.

---

## 10. Limitations

Several limitations should be considered when interpreting these results:

- The deterministic SIR model ignores stochastic variation in transmission.
- The population is assumed to be **closed**, with no migration or births.
- The infectious period is assumed constant.
- Age structure and vaccination history are not explicitly modeled.
- Reporting probability is assumed constant over time.

These simplifying assumptions may influence parameter estimates and model predictions.

---

## 11. Conclusion

This analysis demonstrates how mechanistic epidemic models can be used to interpret infectious disease outbreak data. Using biweekly measles incidence data from Niamey, we estimated the early growth rate of the epidemic, inferred the basic reproduction number, and fitted a deterministic SIR model to observed incidence data.

The estimated transmission rate was approximately **β ≈ 1.7–1.8**, corresponding to a reproduction number near **R₀ ≈ 1.7–1.8** under the assumed recovery rate. Sensitivity and profile likelihood analyses indicated that the transmission parameter is well constrained by the available data.

Overall, the modeling framework illustrates how combining mechanistic models with likelihood-based inference can provide valuable insights into epidemic dynamics. Furthermore, AI-assisted workflows can accelerate epidemiological analysis by helping researchers rapidly implement models, perform inference, and interpret results..
