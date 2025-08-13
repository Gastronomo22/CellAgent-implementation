# CellAgent Replicator 🧬

This project is an implementation inspired by the paper:

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

---

## Example Usage

The file `annotate_pbmc.py` contains a minimal working example that demonstrates how to use the pipeline on a real dataset (`pbmc.h5ad`) within a Google Colab environment.  
It shows how to:

- Load a single-cell dataset using Scanpy  
- Configure the OpenAI API via Colab secrets  
- Define the analysis task and available tools  
- Run the multi-step pipeline using `run_cellagent_task`  
- Print the selected code and justification for each analysis step  

This script is intended as a simple entry point for users to test and extend the pipeline on their own data.


