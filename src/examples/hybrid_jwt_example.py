from pq_auth.pqc.hybrid import hybrid_auth
from pq_auth.utils.jwt import hybrid_jwt

# Generate keys once
keys = hybrid_auth.generate_hybrid_keypair()

token = hybrid_jwt.create(
    claims={"user_id": 123, "role": "admin"},
    classical_private_key=keys["x25519_private"],   # or proper Ed25519
    pqc_private_key=keys["dsa_private"],
)

user = hybrid_jwt.verify(token, keys["x25519_public"], keys["dsa_public"])
print("Verified!", user)
