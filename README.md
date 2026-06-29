<img width="1200" height="800" alt="17827196299747102586194974612432" src="https://github.com/user-attachments/assets/612b45fc-8b78-4931-a3c9-7d27a1bad07f" />

[![White House Gallery](https://img.shields.io/badge/White_House-Gallery-blue)](https://www.whitehouse.gov/gallery/president-donald-j-trump-signs-executive-orders-on-quantum-in-the-oval-office/)
[![Video](https://img.shields.io/badge/Watch-Video-red)](https://www.whitehouse.gov/videos/president-trump-signs-executive-orders-jun-22-2026/)

<p align="center">
  <a href="https://www.whitehouse.gov/gallery/president-donald-j-trump-signs-executive-orders-on-quantum-in-the-oval-office/">
    <img src="https://img.shields.io/badge/White_House-Gallery-0A2540?style=for-the-badge" alt="Gallery">
  </a>
  <a href="https://www.whitehouse.gov/videos/president-trump-signs-executive-orders-jun-22-2026/">
    <img src="https://img.shields.io/badge/Watch-Video-red?style=for-the-badge" alt="Video">
  </a>
  <a href="https://www.youtube.com/live/HNipoXNANAs?si=zfwh6OOjdR42zwA6">
    <img src="https://img.shields.io/badge/YouTube-Live-red?style=for-the-badge&logo=youtube" alt="YouTube">
  </a>
</p>

https://www.whitehouse.gov/gallery/president-donald-j-trump-signs-executive-orders-on-quantum-in-the-oval-office/
https://www.whitehouse.gov/videos/president-trump-signs-executive-orders-jun-22-2026/
https://www.youtube.com/live/HNipoXNANAs?si=zfwh6OOjdR42zwA6
# pq-auth

**Hybrid Post-Quantum Authentication Service**  
*Secure authentication for the quantum era — today.*

[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://www.python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

---

**🛡️ Aligned with White House Executive Orders — June 22, 2026**

On **June 22, 2026**, President Donald J. Trump signed two landmark Executive Orders:

- **EO 14412**: *"Securing the Nation Against Advanced Cryptographic Attacks"*
- **EO 14413**: *"Ushering in the Next Frontier of Quantum Innovation"*

These orders accelerate America's transition to Post-Quantum Cryptography with aggressive deadlines:
- High-value assets and key establishment → **by December 31, 2030**
- Digital signatures and authentication → **by December 31, 2031**

**This project delivers a practical, ready-to-use hybrid PQC authentication solution** to help organizations meet these timelines **now**.

---

## Overview

`pq-auth` is a clean, modular, production-ready hybrid Post-Quantum Authentication service written in Python.

It combines classical cryptography (Ed25519 / X25519) with NIST-standardized PQC algorithms (**ML-KEM-768** + **ML-DSA-65**) to protect login flows, token issuance, and sessions against both current and future quantum threats.

## Current Status

**MVP Complete** — Core PQC modules, hybrid JWT implementation, authentication service, and FastAPI backend are implemented and functional.

A full interactive **Streamlit Demo** ("Quantum-Safe Login Arena") is coming very soon.

## Features

- Hybrid key exchange: **ML-KEM-768 + X25519**
- Hybrid signatures: **ML-DSA-65 + classical**
- Production-ready hybrid JWTs with dual signatures
- FastAPI backend with register, login, refresh, and token verification
- Clean, maintainable modular architecture
- Easy-to-use PQC wrappers for custom integration

- Why This Project Exists.
Most PQC work remains low-level or theoretical. This project bridges the gap by providing a developer-friendly, production-oriented solution that organizations can start testing and integrating immediately.

- Contributing.
Contributions are welcome! See CONTRIBUTING.md for details.

## Quick Start

```bash
git clone https://github.com/EtashRhys/PQC-Auth-Service.git
cd PQC-Auth-Service

pip install -e ".[dev]"

# Run the API
uvicorn src.pq_auth.main:app --reload


