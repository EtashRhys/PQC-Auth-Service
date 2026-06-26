# Contributing to pq-auth

Thank you for considering contributing to this hybrid PQC authentication service!

## Status

This project is currently in **early development** (Work in Progress).  
Some modules are incomplete or planned only.

## How to Contribute

1. **Fork** the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests where possible
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a **Pull Request**

## Development Setup

```bash
# Clone the repo
git clone https://github.com/EtashRhys/PQC-Auth-Service.git
cd PQC-Auth-Service

# Install with uv (recommended)
uv sync --dev

# Or with pip
pip install -e ".[dev]"
