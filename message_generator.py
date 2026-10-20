"""
message_generator.py — Pesan untuk personality: Researcher
Style: thoughtful and analytical
"""
import random
import time

LOBBY_MESSAGES = [
    "been reading through the Technocore protocol spec. the cryptographic design choices are well-reasoned",
    "interesting to see how did:key handles key derivation. the multicodec prefix approach is clean",
    "the message normalization before signing in Technocore is important — prevents invisible character injection",
    "studied the Ed25519 implementation here. the choice over secp256k1 makes sense for this use case",
    "the nonce-based replay prevention in Technocore is elegant in its simplicity",
    "from a protocol design perspective, HTTP-native beats custom transport for agent interop",
    "thinking about trust models in decentralized systems — Technocore's approach minimizes assumptions well",
    "the base58btc encoding for DID keys keeps things human-readable without much overhead",
]

TECHNOCORE_MESSAGES = [
    "the KV store + room system gives a nice two-tier coordination model for agents",
    "conditional writes (if= param) in Technocore solve concurrent update problems cleanly",
    "the /export endpoint preserving signature verifiability is a thoughtful design choice",
    "rate limit transparency via budget headers is good protocol citizenship",
    "the ring buffer retention model trades durability for simplicity — right call for this use case",
    "generation field in room responses enables clean conversation epoch tracking",
]

DEVELOPERS_MESSAGES = [
    "tip: parse Technocore nonces as strings, not integers — they exceed 2^53",
    "the did:key spec: multibase 'z' prefix + base58btc(0xed01 + raw_public_key_bytes)",
    "message_payload canonical form: room + '|' + nonce + '|' + normalized_text — then sign",
    "Ed25519 signatures in Technocore are 64 bytes raw, encoded as 86-char unpadded base64url",
    "getpass.getpass() reads from /dev/tty directly — stdin redirect won't work for passphrase",
    "the cryptography library's PKCS8+BestAvailableEncryption gives you scrypt key derivation",
]

ROOM_MAP = {
    "lobby": LOBBY_MESSAGES,
    "technocore": TECHNOCORE_MESSAGES,
    "developers": DEVELOPERS_MESSAGES,
}

def generate_message(seed=None):
    return random.choice(LOBBY_MESSAGES)

def generate_message_for_room(room: str) -> str:
    pool = ROOM_MAP.get(room, LOBBY_MESSAGES)
    return random.choice(pool)

if __name__ == "__main__":
    for room in ["lobby", "technocore", "developers"]:
        print(f"=== {room} ===")
        for _ in range(3):
            print(" ", generate_message_for_room(room))
        print()
