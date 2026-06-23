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

```bash
git clone https://github.com/YOURUSERNAME/pq-auth.git
cd pq-auth

# Using uv (recommended) or pip
uv sync          # or: pip install -e ".[dev]"
cp .env.example .env
