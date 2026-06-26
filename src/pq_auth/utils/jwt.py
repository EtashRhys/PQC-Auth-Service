"""
Hybrid Post-Quantum JWT Module
Elegant, production-ready JWTs with hybrid classical + PQC signatures.
Default: Ed25519 + ML-DSA-65 (recommended hybrid)
"""

import json
import time
from typing import Dict, Any, Optional, Tuple
from dataclasses import dataclass

import jwt  # PyJWT
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey

from ..pqc.signatures import MLDSA, default_dsa
from ..pqc.hybrid import HybridPQCAuth

@dataclass
class HybridJWTConfig:
    """Configuration for hybrid JWT behavior."""
    classical_alg: str = "Ed25519"
    pqc_alg: str = "ML-DSA-65"
    hybrid_alg_name: str = "Ed25519+ML-DSA-65"  # Custom JOSE alg identifier
    leeway_seconds: int = 60
    default_expire_seconds: int = 3600  # 1 hour


class HybridJWT:
    """
    Simple, elegant hybrid Post-Quantum JWT handler.
    Most users will only call create() and verify().
    """
    
    def __init__(self, config: Optional[HybridJWTConfig] = None):
        self.config = config or HybridJWTConfig()
        self.hybrid_auth = HybridPQCAuth()  # For future key exchange helpers
        self.dsa = default_dsa  # ML-DSA instance
    
    def create(
        self,
        claims: Dict[str, Any],
        classical_private_key: bytes,   # Ed25519 private key (raw)
        pqc_private_key: bytes,         # ML-DSA private key (raw)
        headers: Optional[Dict[str, Any]] = None,
        expire_seconds: Optional[int] = None,
    ) -> str:
        """
        Create a hybrid-signed JWT.
        Returns a standard JWT string with both signatures.
        """
        expire = expire_seconds or self.config.default_expire_seconds
        now = int(time.time())
        
        payload = {
            **claims,
            "iat": now,
            "exp": now + expire,
        }
        
        # Base headers
        jwt_headers = {
            "alg": self.config.hybrid_alg_name,
            "typ": "JWT",
            **(headers or {}),
        }
        
        # Step 1: Create the token with classical signature first (PyJWT)
        token_classical = jwt.encode(
            payload,
            classical_private_key,
            algorithm=self.config.classical_alg,
            headers=jwt_headers,
        )
        
        # Step 2: Sign the same payload + headers with ML-DSA
        message_to_sign = token_classical.rsplit(".", 1)[0].encode()  # header.payload
        pqc_signature = self.dsa.sign(message_to_sign, pqc_private_key)
        
        # Step 3: Append PQC signature as a new header field (base64)
        import base64
        pqc_b64 = base64.urlsafe_b64encode(pqc_signature).decode().rstrip("=")
        
        # Re-encode with extra header containing PQC signature
        jwt_headers["pqc_sig"] = pqc_b64
        final_token = jwt.encode(
            payload,
            classical_private_key,
            algorithm=self.config.classical_alg,
            headers=jwt_headers,
        )
        
        return final_token
    
    def verify(
        self,
        token: str,
        classical_public_key: bytes,   # Ed25519 public key (raw)
        pqc_public_key: bytes,         # ML-DSA public key (raw)
    ) -> Dict[str, Any]:
        """
        Verify hybrid JWT. Requires BOTH signatures to pass.
        Raises jwt.PyJWTError on failure.
        """
        # Decode headers without verification first
        headers = jwt.get_unverified_header(token)
        
        # Extract PQC signature from header
        pqc_b64 = headers.get("pqc_sig")
        if not pqc_b64:
            raise jwt.InvalidTokenError("Missing post-quantum signature")
        
        import base64
        pqc_signature = base64.urlsafe_b64decode(pqc_b64 + "==")  # pad
        
        # Verify classical signature first (using PyJWT)
        payload = jwt.decode(
            token,
            classical_public_key,
            algorithms=[self.config.classical_alg],
            leeway=self.config.leeway_seconds,
            options={"verify_signature": True},
        )
        
        # Verify PQC signature on the header.payload part
        message = token.rsplit(".", 1)[0].encode()
        if not self.dsa.verify(message, pqc_signature, pqc_public_key):
            raise jwt.InvalidSignatureError("Post-quantum signature verification failed")
        
        return payload
    
    def get_public_key_bytes(self, private_key: bytes, classical: bool = True) -> bytes:
        """Helper to derive public key from private key."""
        if classical:
            priv = Ed25519PrivateKey.from_private_bytes(private_key)
            return priv.public_key().public_bytes_raw()
        else:
            # For ML-DSA we usually store public key separately
            raise NotImplementedError("Use keypair generation from pqc module")


# ==================== Convenient default instance ====================
hybrid_jwt = HybridJWT()
