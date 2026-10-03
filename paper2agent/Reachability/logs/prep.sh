#!/usr/bin/env bash
# Mechanical preparation only: snapshot -> extract -> review-aid. One paper at a time (host has ~2 GB free RAM).
export PATH="$HOME/.local/bin:$PATH"
SK=$HOME/.claude/skills/paper2agent/paper2skill
R=$HOME/AI_agents/paper2agent/Reachability
prep() { # bibkey title
  local id="$1-paper" w="$R/paper-review/$1-paper"
  if [ -f "$w/review-aid/review-queue.json" ]; then echo "[skip] $id"; return; fi
  echo "[$(date +%T)] prepare $id"
  uv run $SK/scripts/paper_bundle.py prepare "$R/papers/$1.pdf" --work "$w" --name "$id" --title "$2" --main "$R/papers/$1.pdf" 2>&1 | tail -2
  uv run $SK/scripts/paper_bundle.py extract --work "$w" 2>&1 | tail -2
  uv run $SK/scripts/paper_bundle.py review-aid --work "$w" 2>&1 | tail -2
  echo "[$(date +%T)] done $id"
}
if [ $# -gt 0 ]; then prep "$1" "$2"; exit; fi
prep devonport2021data "Data-Driven Reachability Analysis with Christoffel Functions"
prep liebenwein2018sampling "Sampling-Based Approximation Algorithms for Reachability Analysis with Provable Guarantees"
prep devonport2023data "Data-Driven Reachability and Support Estimation with Christoffel Functions"
prep lew2021sampling "Sampling-based Reachability Analysis: A Random Set Theory Approach with Adversarial Sampling"
prep lew2022simple "A Simple and Efficient Sampling-based Algorithm for General Reachability Analysis"
prep devonport2020estimating "Estimating Reachable Sets with Scenario Optimization"
prep dietrich2025data "Data-Driven Reachability with Scenario Optimization and the Holdout Method"
prep dietrich2024nonconvex "Nonconvex Scenario Optimization for Data-Driven Reachability"
prep sartipizadeh2019voronoi "Voronoi Partition-based Scenario Reduction for Fast Sampling-based Stochastic Reachability Computation of Linear Systems"
prep fan2017dryvr "DryVR: Data-Driven Verification and Compositional Reasoning for Automotive Systems"
prep gruenbacher2022gotube "GoTube: Scalable Statistical Verification of Continuous-Depth Models"
prep tebjou2023data "Data-driven Reachability using Christoffel Functions and Conformal Prediction"
prep lin2024verification "Verification of Neural Reachable Tubes via Scenario Optimization and Conformal Prediction"
prep hashemi2023data "Data-Driven Reachability Analysis of Stochastic Dynamical Systems with Conformal Inference"
prep hashemi2025pca "PCA-DDReach: Efficient Statistical Reachability Analysis of Stochastic Dynamical Systems via Principal Component Analysis"
prep selim2022safe "Safe Reinforcement Learning Using Black-Box Reachability Analysis"
prep ganai2023iterative "Iterative Reachability Estimation for Safe Reinforcement Learning"
prep liu2025recurrent "Recurrent Control Barrier Functions: A Path Towards Nonparametric Safety Verification"
prep ouyang2026symplectic "Symplectic Inductive Bias for Data-Driven Target Reachability in Hamiltonian Systems"
echo ALL_PREP_DONE
