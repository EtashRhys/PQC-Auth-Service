# pq-auth

**Hybrid Post-Quantum Authentication Service** (Work in Progress)  
Secure, modern authentication built for the quantum era.

[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

A practical hybrid Post-Quantum Cryptography (PQC) authentication service using **NIST FIPS 203 (ML-KEM)** for key encapsulation and **FIPS 204 (ML-DSA)** for digital signatures. It combines these with classical algorithms (X25519 + ML-KEM, ECDSA + ML-DSA).

## Status: Work in Progress

This repository contains the project structure and source code for a hybrid PQC auth service.  
**Not all parts are fully integrated or end-to-end tested yet.** The code is modular by design — feel free to explore, copy individual modules, and adapt them for your own needs.

## Why This Project?

Quantum computers pose a "store now, decrypt later" threat to current public-key cryptography. This aims to be a practical reference implementation of hybrid PQC authentication for evaluation and prototyping.

## Features

- **Hybrid PQC Core** (planned)
  - ML-KEM (Kyber) + X25519 for key exchange/encapsulation
  - ML-DSA (Dilithium) + ECDSA for signatures
  - Custom hybrid combiners and key derivation
- **FastAPI Service**
  - Basic FastAPI entrypoint with health checks
  - Planned: User registration, login, JWT refresh, sessions
- **Developer Experience**
  - Modular structure for easy cherry-picking
  - Planned: Typer CLI, tests, Docker support, benchmarks

## Current Project Structure

```bash
src/
└── pq_auth/
    ├── main.py
    ├── pqc/           # ← Core PQC modules will go here
    ├── auth/
    ├── utils/
    └── config.py
