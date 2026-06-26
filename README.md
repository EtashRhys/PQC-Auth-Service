# pq-auth

**Hybrid Post-Quantum Authentication Service** (Work in Progress)  
Secure, modern authentication built for the quantum era.

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

A practical hybrid Post-Quantum Cryptography (PQC) authentication service using **NIST FIPS 203 (ML-KEM)** for key encapsulation and **FIPS 204 (ML-DSA)** for digital signatures. It combines these with classical algorithms (X25519 + ML-KEM, ECDSA + ML-DSA).

## Status: Work in Progress

This repository contains the project structure and source code for a hybrid PQC auth service.  
**Not all parts are fully integrated or end-to-end tested yet.** The code is modular by design — feel free to explore, copy individual modules (especially the PQC wrappers in `src/pq_auth/pqc/`), and adapt them for your own needs.

## Why This Project?

Quantum computers pose a "store now, decrypt later" threat to current public-key cryptography. This aims to be a **practical reference implementation** of hybrid PQC authentication.

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
  - Structured logging, Pydantic configuration
  - CI/CD workflows, pre-commit hooks, Makefile

## Project Structure

```bash
pq-auth/
├── src/pq_auth/           # Main package
│   ├── pqc/               # ← Core: ML-KEM, ML-DSA, hybrid logic
│   ├── auth/              # Authentication logic & API
│   ├── core/              # Config, security, database
│   └── ...
├── tests/
├── docs/
├── docker/
├── pyproject.toml
└── ...
