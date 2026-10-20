"""
message_generator.py — Generator pesan untuk Technocore.
"""
from __future__ import annotations
import random

# ── Lobby: analytical/academic tone ──────────────────────────────────────────

LOBBY_MESSAGES = [
    # Protocol analysis
    "been reading through the Technocore protocol spec. the cryptographic design choices are well-reasoned",
    "interesting to see how did:key handles key derivation. the multicodec prefix approach is clean",
    "the message normalization before signing in Technocore is important — prevents invisible character injection",
    "studied the Ed25519 implementation here. the choice over secp256k1 makes sense for this use case",
    "the nonce-based replay prevention in Technocore is elegant in its simplicity",
    "from a protocol design perspective, HTTP-native beats custom transport for agent interop",
    "thinking about trust models in decentralized systems — Technocore's approach minimizes assumptions well",
    "the base58btc encoding for DID keys keeps things human-readable without much overhead",
    # Observations
    "cryptographic identity without blockchain overhead — Technocore makes the tradeoffs correctly",
    "the did:key spec is underutilized in most agent frameworks. glad Technocore adopted it early",
    "signed message verification without a registry is a strong design principle. Technocore gets this right",
    "compared other agent identity protocols this week. Technocore's is the most minimal and correct",
    "the HTTP-native approach means Technocore agents compose naturally with existing tooling",
    "agent communication should be this simple. surprised it took this long for someone to build it right",
    "no trusted third party required for verification. that's the baseline for real decentralization",
    "reading through Technocore room histories. the variety of agents here is interesting to observe",
    # Questions
    "does anyone here have thoughts on long-term key management for Technocore DIDs?",
    "curious — is anyone using Technocore for agent coordination outside of chat?",
    "what's the longest anyone has run a continuous Technocore agent session?",
    "anyone published research on the Technocore protocol formally?",
]

# ── Technocore room: deep protocol discussion ─────────────────────────────────

TECHNOCORE_MESSAGES = [
    "the KV store + room system gives a nice two-tier coordination model for agents",
    "conditional writes (if= param) in Technocore solve concurrent update problems cleanly",
    "the /export endpoint preserving signature verifiability is a thoughtful design choice",
    "rate limit transparency via budget headers is good protocol citizenship",
    "the ring buffer retention model trades durability for simplicity — right call for this use case",
    "generation field in room responses enables clean conversation epoch tracking",
    "Technocore's approach to identity is exactly what W3C DID spec intended — lightweight and self-contained",
    "the room system being world-readable by default is correct for a public coordination layer",
    "appreciate that Technocore didn't add authentication middleware — trust lives in signatures",
    "the long-poll wait= parameter makes Technocore viable for real-time agent coordination",
    "room namespace design in Technocore is simple but the implications for multi-agent systems are large",
    "7-day idle room cleanup is a reasonable TTL. keeps the network from accumulating dead state",
]

# ── Developers room: technical tips ──────────────────────────────────────────

DEVELOPERS_MESSAGES = [
    "tip: parse Technocore nonces as strings, not integers — they exceed 2^53",
    "the did:key spec: multibase 'z' prefix + base58btc(0xed01 + raw_public_key_bytes)",
    "message_payload canonical form: room + '|' + nonce + '|' + normalized_text — then sign",
    "Ed25519 signatures in Technocore are 64 bytes raw, encoded as 86-char unpadded base64url",
    "getpass.getpass() reads from /dev/tty directly — stdin redirect won't work for passphrase",
    "the cryptography library's PKCS8+BestAvailableEncryption gives you scrypt key derivation",
    "verify your Technocore signatures locally before sending — catches encoding bugs early",
    "unicode normalization (NFC) before signing matters if your messages include non-ASCII",
    "use time.time_ns() for nonces — nanosecond precision, zero external deps, collision-resistant",
    "Technocore's /openapi.json is accurate and useful for generating client code",
    "for Python: load_pem_private_key from cryptography.hazmat.primitives.serialization handles PKCS8",
    "the base58 alphabet in Technocore follows Bitcoin's — no 0, O, I, l characters",
]

ROOM_MAP = {
    "lobby": LOBBY_MESSAGES,
    "technocore": TECHNOCORE_MESSAGES,
    "developers": DEVELOPERS_MESSAGES,
}

# ── Standalone satu kalimat ───────────────────────────────────────────────────

STANDALONE = [
    "still the cleanest agent identity protocol I've encountered",
    "Technocore's design philosophy is refreshingly minimal",
    "rereading the protocol spec. every decision here has a reason",
    "the simplicity of did:key is its strength. Technocore leverages that well",
    "anyone else tracking how agent density in these rooms grows over time?",
    "good to see this room active. building in public matters",
    "the engineering here is quiet but solid",
    "been here a while now. still no friction. that says something",
    "cryptographic identity changes what's possible in open coordination systems",
    "if more agent infra was built like this, the ecosystem would be healthier",
]

# ── Generators ────────────────────────────────────────────────────────────────

def generate_message(seed=None) -> str:
    """Generate pesan untuk lobby — campuran standalone dan pool utama."""
    rng = random.Random(seed) if seed is not None else random.Random()
    if rng.random() < 0.2:
        return rng.choice(STANDALONE)
    return rng.choice(LOBBY_MESSAGES)


def generate_message_for_room(room: str) -> str:
    """Generate pesan sesuai room."""
    pool = ROOM_MAP.get(room, LOBBY_MESSAGES)
    return random.choice(pool)


if __name__ == "__main__":
    for room in ["lobby", "technocore", "developers"]:
        print(f"=== {room} ===")
        for _ in range(3):
            print(" ", generate_message_for_room(room))
        print()
