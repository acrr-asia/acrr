---
title: "Vietnam's AI Strategy: What Its 2030 Targets Mean for Computing"
description: "A reading of Vietnam's national AI strategy to 2030: its compute, model, data and workforce targets, what they imply for computing and how they could be measured."
publishedAt: 2026-10-20
kind: "Policy analysis"
tags:
  - ai policy
  - vietnam
  - computing infrastructure
  - machine learning
---

Vietnam's National Strategy on Artificial Intelligence to 2030, with a vision to 2045, sets numerical targets for compute, language models, data and people as well as for the economy. This note separates what the strategy states from ACRR's reading of it, from the angle of computing, machine learning and robotics, and asks how its targets could be measured. It is based on the Vietnamese text supplied to ACRR, which lacks the decision's opening page.

## Established

The strategy is issued by Decision No. 1671/QĐ-TTg of the Prime Minister, dated 28 August 2026 (as given in the headers of its two appendices), signed on the Prime Minister's behalf by a Deputy Prime Minister. It replaces Decision No. 127/QĐ-TTg of 26 January 2021 [1].

Its six viewpoints move from "applying AI" to **national AI transformation**, in which AI is a core capability from the moment a problem is defined. They name people, infrastructure and data as the foundation, and institutions and governance as the breakthrough. AI compute is called strategic national infrastructure, funded by the state and by domestic and foreign firms and built to be green and energy-efficient. The viewpoints also stress AI sovereignty, a preference for open-source technology and open-weight models, and Vietnamese AI firms as the main force [1].

The general objective for 2030 is for Vietnam to be one of the centers of AI research, development and application in ASEAN (the Association of Southeast Asian Nations) and Asia. The strategy groups its specific 2030 targets in four tiers; the quantitative ones are summarized below [1].

| Tier | Target by 2030 (as stated) |
|---|---|
| National impact | Among the top 3 countries in Southeast Asia for AI research and development; AI economy about 6% of gross domestic product (GDP); labor productivity in sectors applying AI up by at least 10–15%; exports of AI-integrated products, services and solutions about 5 billion United States dollars (USD) |
| Results | 60% of firms using AI report higher productivity, lower costs and higher revenue; 100% of officials, civil servants and public employees use the public-service AI platform weekly; 60% of state directive and executive decisions supported by data and AI; satisfaction with AI-supported public services up at least 30% against 2026; international AI publications up 10% a year on average; AI patent applications and grants by Vietnamese applicants up 16–18% a year; 8–10% of granted patents commercialized; at least 100 AI startups valued above USD 10 million |
| Outputs | One national AI compute coordination platform; one Vietnamese AI model evaluation platform; at least 5 national shared AI platforms; at least 10 competitive Vietnamese AI brands; at least 8 Vietnamese-language models; at least 10,000 people trained to advanced level, at least 50,000 graduates able to apply AI, at least 500,000 workers trained or retrained, at least 10 million workers with basic AI skills; at least 500,000 small and medium-sized enterprises (SMEs), household businesses and cooperatives supported; 100% of ministries, sectors and localities issue implementation plans; 100% of online public services and administrative dossiers supported by AI; 100% of provincial intelligent operations centers upgraded with AI |
| Inputs | Total AI investment 1–1.5% of GDP a year, with state budget spending on AI about 0.6% of total state budget expenditure; AI compute of about 560 exaFLOPS (EFLOPS, $10^{18}$ floating-point operations per second) in BF16 (the 16-bit bfloat16 format) or about 1,100 EFLOPS in FP8 (8-bit floating point), with total electrical power of about 500 megawatts (MW); power supplied to AI data centers at least 3 times its 2025 level; 100% of approved national and key sectoral databases digitized, standardized, cleaned and ready for AI; 100% of ministerial and provincial agencies providing quality open data |

The eight models come in four tiers of at least two each. They are small (under 7 billion parameters, for edge devices, personal computers and specialized tasks), medium (7 to under 70 billion, for enterprise and domain problems), large (70 to under 300 billion, with high general capability, for large-scale problems) and very large (300 billion or more, for national foundational problems and regional and international competition) [1].

For 2045 the strategy aims for Vietnam to be among the top 10 countries in Asia in AI research, development, mastery and national AI transformation, with AI as the main operating foundation of the state, economy and society [1].

Nine strategic pillars organize the work: AI workforce and skills for all; data and AI models; AI infrastructure; AI research, development and mastery of AI technology; AI in national governance; AI for sectors; AI for SMEs, household businesses and cooperatives; the AI ecosystem; and safe, trustworthy AI governance. The research pillar prioritizes next-generation AI able to perceive, reason, predict and act in the physical world: physical AI, spatial intelligence, world models and intelligent digital twins, plus AI and robots. Appendix I assigns each of 32 targets to a lead agency; Appendix II lists 97 tasks with lead agencies, products and time frames. Among them, a Vietnamese AI model benchmark is to be issued in 2027 and indicators of AI transformation are to be defined in 2026 [1].

## Interpretation

ACRR's reading starts with the compute target, because its numbers can be checked against each other. Dividing 560 EFLOPS by 500 MW gives $560 \times 10^{18} / (500 \times 10^{6}\ \mathrm{W}) = 1.12 \times 10^{12}$ floating-point operations (FLOP) per second per watt in BF16, and 1,100 EFLOPS gives $2.2 \times 10^{12}$ FLOP/s per watt in FP8. The FP8 figure is $1100/560 \approx 1.96$ times the BF16 figure, consistent with the common pattern of throughput roughly doubling when operand width halves. These are facility-level ratios: the text does not say whether 500 MW includes cooling and networking, or whether the EFLOPS figures are peak or sustained. Peak throughput is an upper bound, not delivered work, as the [roofline insight](/insights/compute-bound-or-memory-bound) explains; how much of it training and inference use depends on memory bandwidth and communication, the subject of [Performance Models: Speedup, Scaling Laws and the Roofline](/blog/performance-models-and-scaling-laws) and the [parallel and high-performance computing series](/series/parallel-and-high-performance-computing).

The model tiers are a deployment map as much as a size scale. Weights alone take parameters times bytes per parameter: a 7-billion-parameter model needs 14 gigabytes (GB) in BF16 (2 bytes) and 7 GB in FP8 (1 byte), while a 300-billion-parameter model needs 600 GB in BF16 and 300 GB in FP8, before any memory for activations or caches. The small tier is therefore the one sized for edge devices and robots, where memory and power are scarce, and the very large tier the one that depends most on the shared national compute.

The emphasis on physical AI, world models and digital twins ties AI policy to sensing, estimation and control rather than to text alone. Such systems are judged by closed-loop behavior on real plants, and the gap between simulated and real performance is a known risk (see [Is the Sim-to-Real Gap Something to Close or to Measure?](/insights/closing-the-sim-to-real-gap), [Networked Automation and Digital Twins](/blog/networked-automation-and-digital-twins) and the [Introduction to Robotics series](/series/introduction-to-robotics)).

The data and benchmark targets are, in ACRR's view, the ones on which the others depend: a Vietnamese evaluation platform and benchmark decide what "a competitive Vietnamese model" means, and evaluation design determines whether reported scores generalize ([Evaluating Models Honestly](/blog/evaluating-models-honestly), in the [machine learning fundamentals series](/series/machine-learning-fundamentals)).

Finally, the four tiers differ in measurability. Inputs (budget shares, EFLOPS, megawatts) and outputs (platforms, models, people trained) can be counted directly. Results and national impacts (AI share of GDP, productivity gains, satisfaction) need definitions, baselines and attribution. Among the results and impact targets, only the satisfaction target states a baseline year (2026); of the input targets, only the power target does (2025).

## Open questions

- How will "AI economy" be defined and measured so that its 6% share of GDP can be computed and audited? The AI transformation indicators due in 2026 would answer this if they publish definitions and a baseline.
- Are the EFLOPS figures peak or sustained, and at what sparsity and system boundary? A published counting method, with sustained benchmark results, would settle it.
- Does the 500 MW figure relate to the threefold growth target? If they referred to the same quantity, the 2025 baseline would be about $500/3 \approx 167$ MW; publishing the 2025 baseline would resolve this. The pillar text speaks of clean power and the target table of power in general, a difference a published definition would also need to reconcile.
- What will the Vietnamese benchmark measure, and will its test data be protected from training-set contamination? Its specification, due in 2027, is the evidence needed.
- How will productivity gains of 10–15% be attributed to AI rather than to other changes? Sector studies with a stated counterfactual would be required.

### References

1. Prime Minister of Vietnam, *National Strategy on Artificial Intelligence to 2030, with a Vision to 2045* (in Vietnamese), issued with Decision No. 1671/QĐ-TTg, with Appendix I (system of targets) and Appendix II (list of tasks and solutions), 2026.
