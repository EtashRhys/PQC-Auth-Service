"""
PQC KEM Module - ML-KEM only
Simple, universal key encapsulation.
"""

import oqs
from typing import Tuple, Optional
import secrets

class MLKEM:
    """Simple wrapper for ML-KEM (FIPS 203) key encapsulation."""
    
    DEFAULT_ALG = "ML-KEM-768"  # Security level 3 - recommended balance
    
    def __init__(self, algorithm: str = DEFAULT_ALG):
        if not algorithm.startswith("ML-KEM-"):
            raise ValueError("Only ML-KEM algorithms are supported in this module")
        self.algorithm = algorithm
        self._kem = oqs.KeyEncapsulation(algorithm)
    
    def generate_keypair(self) -> Tuple[bytes, bytes]:
        """Generate public + private keypair."""
        public_key = self._kem.generate_keypair()
        secret_key = self._kem.export_secret_key()  # or handle carefully
        return public_key, secret_key
    
    def encapsulate(self, peer_public_key: bytes) -> Tuple[bytes, bytes]:
        """Encapsulate a shared secret for the peer."""
        ciphertext, shared_secret = self._kem.encap_secret(peer_public_key)
        return ciphertext, shared_secret
    
    def decapsulate(self, ciphertext: bytes, secret_key: bytes) -> bytes:
        """Decapsulate to recover the shared secret."""
        # In practice, re-init with secret key or use proper session handling
        kem = oqs.KeyEncapsulation(self.algorithm)
        kem.import_secret_key(secret_key)  # Check exact API if needed
        shared_secret = kem.decap_secret(ciphertext)
        return shared_secret
    
    def get_key_length(self) -> int:
        """Return shared secret length in bytes."""
        return self._kem.get_shared_secret_length()


# Convenience instance
default_kem = MLKEM()
