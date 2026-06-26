"""
PQC Signatures Module - ML-DSA only
Clean digital signature operations.
"""

import oqs
from typing import Tuple, Optional

class MLDSA:
    """Simple wrapper for ML-DSA (FIPS 204) signatures."""
    
    DEFAULT_ALG = "ML-DSA-65"  # Security level 3 - recommended for most uses
    
    def __init__(self, algorithm: str = DEFAULT_ALG):
        if not algorithm.startswith("ML-DSA-"):
            raise ValueError("Only ML-DSA algorithms are supported in this module")
        self.algorithm = algorithm
        self._sig = oqs.Signature(algorithm)
    
    def generate_keypair(self) -> Tuple[bytes, bytes]:
        """Generate signing keypair (public, secret)."""
        public_key = self._sig.generate_keypair()
        secret_key = self._sig.export_secret_key()
        return public_key, secret_key
    
    def sign(self, message: bytes, secret_key: bytes) -> bytes:
        """Sign a message."""
        sig = oqs.Signature(self.algorithm)
        sig.import_secret_key(secret_key)
        signature = sig.sign(message)
        return signature
    
    def verify(self, message: bytes, signature: bytes, public_key: bytes) -> bool:
        """Verify a signature."""
        sig = oqs.Signature(self.algorithm)
        return sig.verify(message, signature, public_key)
    
    def get_signature_length(self) -> int:
        """Return expected signature length."""
        return self._sig.get_signature_length()


# Convenience instance
default_dsa = MLDSA()
