# Ethereum Protocol Lab

Dual-track monorepo for **Execution-Layer (STEEL)** and **Consensus-Layer (LMD-GHOST + FFG)** experimentation with fully spec-linked tests and reproducible simulations.

## Getting Started

### Prerequisites
- Python 3.11
- [uv](https://astral.sh/uv/)
- Geth (optional, for RPC client testing)

### Environment Setup
```bash
# Clone the repo
git clone <your-repo-url>
cd ethereum-protocol-lab

# Initialize uv environment and install dependencies
uv sync

# Verify environment
make ci
```

### Basic Usage
- Run STEEL tests: `make test-steel` or `uv run pytest steel_tests/`
- Run consensus simulations: `make sim` or `uv run python consensus_sim/main.py`
- Generate artifacts (plots, logs): `make artifacts`

## Repo Structure
- `steel_tests/` — Spec-anchored EELS/EEST-style Python tests with Hypothesis property sweeps
- `consensus_sim/` — LMD-GHOST + FFG simulator with parameter sweeps, reorg/finality analysis
- `common/` — Shared utilities: JSON-RPC client, logging, plotting helpers
- `tests/` — Sanity tests for utilities
- `artifacts/` — Output logs, CSVs, and plots
- `docs/` — Optional documentation
- `Makefile` — Convenience commands for linting, testing, and simulation
- `.github/workflows/ci.yml` — GitHub Actions CI pipeline

## Testing & CI
```bash
make lint        # Run ruff and mypy
make test        # Run pytest
make ci          # Run lint + tests
```

Coverage and type checking are enforced to ensure reproducible, high-quality artifacts.

## Optional Geth Test
Start a local Geth node for RPC testing:
```bash
geth --dev --http --http.api eth,net,web3,debug --http.corsdomain="*" --allow-insecure-unlock
```
Then verify RPC client:
```python
from common.jsonrpc import JSONRPC
print(JSONRPC().call("web3_clientVersion"))
```

## Goals
This repo supports a 2-week sprint to generate high-signal artifacts for an Ethereum protocol developer portfolio:

- **Week 1:** Repo scaffolding, JSON-RPC client, first STEEL edge case, basic consensus skeleton, logging, and plotting.
- **Week 2:** Parameter sweeps, second STEEL edge case, adversarial consensus scenarios, timing/performance analysis, reproducibility scripts, and demo-ready artifacts.

All tests and scenarios are **spec-anchored**, reproducible, and produce reviewer-friendly artifacts (charts, tables, logs, videos).