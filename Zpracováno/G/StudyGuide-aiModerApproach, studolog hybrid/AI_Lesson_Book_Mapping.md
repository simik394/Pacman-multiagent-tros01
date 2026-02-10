# 4IZ431 AI 1: Mapping Lesson Notes to Textbook
**Textbook:** *Artificial Intelligence: A Modern Approach (3rd Edition)*

This document analyzes the coverage of the textbook content within the course lesson notes (`4IZ431-AI_1.PŘ.pdf`).

## 1. Omitted Content
The following chapters from the textbook appear to be **completely omitted** or skipped in the provided lesson notes. These topics were likely not covered in depth during the lectures.

### Logic & Inference
*   **Chapter 8: First-Order Logic**
    *   *Details:* The notes mention Predicate Logic exists (Lesson 08), but skip the syntax, semantics, and engineering of knowledge bases found here.
*   **Chapter 9: Inference in First-Order Logic**
    *   *Details:* Algorithms like Unification, Forward/Backward Chaining, and Resolution for FOL are absent.

### Probabilistic Reasoning (Major Omission)
*   **Chapter 13: Quantifying Uncertainty**
    *   *Details:* Probability axioms, Bayes' Rule, and independence.
*   **Chapter 14: Probabilistic Reasoning**
    *   *Details:* **Bayesian Networks** (a core AI topic) are not in the notes.
*   **Chapter 15: Probabilistic Reasoning over Time**
    *   *Details:* Hidden Markov Models (HMMs), Kalman Filters, Dynamic Bayesian Networks.
*   **Chapter 20: Learning Probabilistic Models**
    *   *Details:* Bayesian Learning, EM Algorithm.

### Natural Language Processing (NLP)
*   **Chapter 22: Natural Language Processing**
    *   *Details:* Language models, text classification, information retrieval.
*   **Chapter 23: Natural Language for Communication**
    *   *Details:* Grammar, parsing, machine translation.

---

## 2. Mapping: Lesson Notes to Textbook Chapters
The following table maps the specific lesson notes to the corresponding chapters in the textbook that serve as their theoretical basis.

| Lesson Note | Topic (CZ) | Corresponding Textbook Chapters | Key Concepts Covered in Notes |
| :--- | :--- | :--- | :--- |
| **01** | Úvod, historie | **Ch 1: Introduction**<br>**Ch 26: Philosophical Foundations** | • Turing Test<br>• Chinese Room Argument<br>• Strong vs. Weak AI |
| **02** | Vyhodnocování inteligence | **Ch 2: Intelligent Agents**<br>**Ch 26: Philosophical Foundations** | • Rationality<br>• Thinking vs. Acting<br>• Measuring Intelligence |
| **03** | Řešení úloh ve stavovém prostoru | **Ch 3: Solving Problems by Searching**<br>**Ch 4: Beyond Classical Search** | • **Uninformed:** BFS, DFS, Iterative Deepening<br>• **Informed:** A*, Heuristics<br>• **Local:** Hill-climbing |
| **04** | Splňování podmínek | **Ch 6: Constraint Satisfaction Problems**<br>**Ch 7: Logical Agents** | • CSP definition (Map coloring, N-Queens)<br>• SAT Solving (DPLL algorithm)<br>• Propositional Logic |
| **05** | Teorie her | **Ch 5: Adversarial Search** | • Minimax Algorithm<br>• Alpha-Beta Pruning<br>• Zero-sum games |
| **06** | Plánování (a rozvrhování) | **Ch 10: Classical Planning**<br>**Ch 4: Beyond Classical Search** | • STRIPS<br>• State-space planning<br>• **Simulated Annealing** (Optimization) |
| **07** | Strojové učení | **Ch 18: Learning from Examples** | • Supervised Learning<br>• Overfitting/Underfitting<br>• Neural Networks (Perceptrons) |
| **08** | Použití znalostí v učení | **Ch 19: Knowledge in Learning**<br>**Ch 12: Knowledge Representation** | • **Explanation-Based Learning**<br>• Case-Based Reasoning<br>• Semantic Networks & Frames |
| **09** | Zpětnovazební učení | **Ch 21: Reinforcement Learning**<br>**Ch 17: Making Complex Decisions** | • **Markov Decision Processes (MDPs)**<br>• Active/Passive RL<br>• Reward functions |
| **10** | Počítačové vidění | **Ch 24: Perception** | • Edge Detection<br>• Convolution<br>• CNNs (Convolutional Neural Networks) |
| **11** | Agenti a roboti | **Ch 25: Robotics**<br>**Ch 2: Intelligent Agents** | • Sensors & Actuators<br>• Subsumption Architecture<br>• Reactive vs. Deliberative Agents |

### Notes on Lesson 08 (Knowledge in Learning)
While mapped to **Chapter 19**, the notes focus heavily on **Knowledge Representation** (Chapter 12 concepts like Frames and Ontologies) as a prerequisite for learning. The advanced logical induction algorithms (FOIL, ILP) found in Chapter 19 are simplified in the course to concepts like "Case-Based Reasoning" and "Explanation-Based Learning".
