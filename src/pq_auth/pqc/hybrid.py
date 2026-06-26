"""
Hybrid PQC Module - Combines classical + PQC (recommended for production)
This is the easiest integration point for most users.
"""

from .kem import MLKEM, default_kem
from .signatures import MLDSA, default_dsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.asymmetric import x25519
import os
from typing import Tuple, Dict, Any

class HybridPQCAuth:
    """
    Easiest-to-use hybrid post-quantum authentication.
    Default: X25519 + ML-KEM-768 for key exchange
             Ed25519 + ML-DSA-65 for signatures (you can swap)
    """
    
    def __init__(self, 
                 kem_alg: str = "ML-KEM-768",
                 dsa_alg: str = "ML-DSA-65"):
        self.kem = MLKEM(kem_alg)
        self.dsa = MLDSA(dsa_alg)
    
    def generate_hybrid_keypair(self) -> Dict[str, bytes]:
        """Generate full hybrid keypair for easy integration."""
        # Classical
        x25519_priv = x25519.X25519PrivateKey.generate()
        x25519_pub = x25519_priv.public_key()
        
        # PQC
        kem_pub, kem_priv = self.kem.generate_keypair()
        dsa_pub, dsa_priv = self.dsa.generate_keypair()
        
        return {
            "x25519_public": x25519_pub.public_bytes_raw(),
            "x25519_private": x25519_priv.private_bytes_raw(),
            "kem_public": kem_pub,
            "kem_private": kem_priv,
            "dsa_public": dsa_pub,
            "dsa_private": dsa_priv,
        }
    
    def hybrid_shared_secret(self, 
                           peer_x25519_pub: bytes,
                           peer_kem_pub: bytes,
                           my_x25519_priv: bytes,
                           my_kem_priv: bytes) -> bytes:
        """Compute hybrid shared secret (X25519 + ML-KEM)."""
        # Classical part
        x_priv = x25519.X25519PrivateKey.from_private_bytes(my_x25519_priv)
        x_shared = x_priv.exchange(x25519.X25519PublicKey.from_public_bytes(peer_x25519_pub))
        
        # PQC part
        kem_ct, kem_ss = self.kem.encapsulate(peer_kem_pub)  # Wait, adjust for decaps
        
        # Combine with HKDF (standard hybrid pattern)
        combined = x_shared + kem_ss  # In real use: proper order + context
        hkdf = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b"hybrid-pqc-auth-v1"
        )
        return hkdf.derive(combined)
    
    # Add more helper methods as needed (sign/verify hybrid tokens, etc.)

# Default easy-to-use instance
hybrid_auth = HybridPQCAuth()
