# GRC Lab Template Kit
This repository is a **GitHub Template Repository**.  
Click **“Use this template”** to create your own GRC or DevSecOps automation lab.


A baseline repo for **GRC Engineering** and **DevSecOps** labs with AWS focus (Lambda + CloudFormation) and a portable structure for other clouds.

## Features
- `src/lambda` with modular findings collectors (IAM, SCP, Access Analyzer, CloudTrail, Security Hub)
- Optional AI narrative (Bedrock-ready) and CSV reporting + SES email
- Makefile + scripts for deploy, report, and AWS credential checks
- PyTest unit tests, `flake8` lint, `pre-commit`, GitHub Actions CI
- Two CloudFormation templates: inline (for demos) and prod (separate Lambda artifact)
- Opinionated repo hygiene: CODEOWNERS, CONTRIBUTING, CI

## Quick Start
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pre-commit install
pytest -q
python -m src.lambda.index --report
./scripts/deploy.sh dev
./scripts/run_report.sh
```
