# PQC-Auth-Service
A hybrid quantum authorization service made with a Python base

# pq-auth

**Hybrid Post-Quantum Authentication Service**  
Secure, modern authentication built for the quantum era.

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

A practical, hybrid Post-Quantum Cryptography (PQC) authentication service using **NIST FIPS 203 (ML-KEM)** for key encapsulation and **FIPS 204 (ML-DSA)** for digital signatures. It combines these with classical algorithms (X25519 + ML-KEM, ECDSA + ML-DSA) to maintain security during the transition to quantum-resistant systems.

## Why This Project?

Quantum computers threaten current public-key cryptography ("store now, decrypt later" risk). This service provides a **production-oriented reference implementation** of hybrid PQC authentication — ready for evaluation, prototyping, and integration.

**Key Goals:**
- Demonstrate secure hybrid constructions
- Provide measurable performance benchmarks
- Offer easy deployment and extensibility
- Encourage community review and contributions in the PQC space

## Features

- **Hybrid PQC Core**
  - ML-KEM (Kyber) + X25519 for key exchange/encapsulation
  - ML-DSA (Dilithium) + ECDSA for signatures
  - Custom hybrid combiners and key derivation
- **Full Authentication Service**
  - User registration, login, token refresh (JWT)
  - Session management with SQLAlchemy + Alembic migrations
  - Rate limiting, audit logging, and security headers
- **Developer Experience**
  - FastAPI REST endpoints with OpenAPI docs
  - Typer CLI for admin tasks, key generation, and benchmarks
  - Comprehensive test suite (unit, integration, PQC-specific, performance)
  - Docker + Docker Compose support
  - MkDocs documentation site
- **Observability & Ops**
  - Structured logging, configuration via Pydantic
  - CI/CD workflows, pre-commit hooks, Makefile

## Quick Start

### 1. Clone & Setup

bash

# Run the API
uv run fastapi dev src/pq_auth/main.py
# or: make run

Visit http://localhost:8000/docs for interactive API docs.CLI examples:bash

uv run pq-auth keygen --hybrid
uv run pq-auth bench

DocumentationArchitecture & Design Decisions (docs/architecture.md)
Benchmarks (docs/benchmarks.md)
API Reference (docs/api.md) (or via /docs when running)

Security & DisclaimerThis is for research, evaluation, and non-production use until independently audited.See SECURITY.md for responsible disclosure and security policy.We strongly recommend professional cryptographic review before production use.ContributingContributions welcome! See CONTRIBUTING.md.Security issues should be reported privately via the Security tab.LicenseApache License 2.0 — see LICENSE file.Built with respect for future quantum threats.

