# CellAgent Replicator 🧬

This project is a simplified implementation inspired by the paper:

📄 **CellAgent: An LLM-driven Multi-Agent Framework for Automated Single-cell Data Analysis**  
[arXiv:2407.09811](https://arxiv.org/abs/2407.09811)

---

## Overview

The goal of this project is to replicate the core logic of **CellAgent**, a framework that automates scRNA-seq (single-cell RNA sequencing) data analysis using a **multi-agent system powered by Large Language Models (LLMs)**.

The system simulates how a human expert would plan, code, and evaluate an analysis task—entirely through LLM interaction and prompt engineering.

---

## Implemented Components

This implementation includes the following core agents:

- **Planner**: Receives a natural language task description and breaks it into structured step-by-step instructions.
- **Executor**: Generates executable Python code for each step using available tools.
- **Evaluator**: Compares multiple code solutions and selects the best one based on the task objective.

In addition, two auxiliary modules have been implemented:

- **Memory Control**: Passes contextual code between steps to maintain consistency.
- **Tool Retriever**: Supplies brief documentation about available tools to help the Executor make informed decisions.

