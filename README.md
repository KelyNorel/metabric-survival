# Breast Cancer Survival Analysis — METABRIC

Survival analysis of breast cancer patients using the METABRIC dataset.

## Overview

METABRIC (Molecular Taxonomy of Breast Cancer International Consortium) is a 
landmark breast cancer study integrating clinical and molecular data from 
~2,000 patients with long-term follow-up. This project analyzes overall survival 
and recurrence-free survival across clinical and molecular subtypes.

## Dataset

**Source:** [cBioPortal — METABRIC](https://www.cbioportal.org/study/summary?id=brca_metabric)  
**Patients:** 496 with complete survival data  
**Median follow-up:** 93.9 months (~7.8 years)  
**OS event rate:** 41.9% | **RFS event rate:** 33.7%  
No PHI involved — all data publicly available.

## Questions Explored

1. Overall survival — Kaplan-Meier curves
2. Survival by molecular subtype (LumA, LumB, HER2, Basal, claudin-low, Normal)
3. Survival by ER/HER2 status and treatment (hormone therapy, chemotherapy)
4. Cox PH model — which clinical features are independently prognostic?
5. ML-based prediction of 5-year survival

## Stack

- Python, pandas — data ingestion and processing
- lifelines — Kaplan-Meier, Cox PH, log-rank tests
- scikit-learn — ML survival prediction
- Matplotlib, seaborn — visualizations
- Jupyter — documented EDA notebook

## Project Structure
metabric-survival/
├── data/
│   ├── raw/          # cBioPortal source files (not tracked in git)
│   └── processed/    # cleaned datasets (not tracked in git)
├── notebooks/
│   └── figures/      # saved plots
├── src/
│   └── ingest.py     # data ingestion and cleaning
└── README.md

## Status
🔄 In progress — EDA and KM curves next