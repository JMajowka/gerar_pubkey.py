import ecdsa
from ecdsa import SigningKey, SECP256k1
import sys

def main(): # ← Linha 5 (aqui começa o erro)
        # ---> TUDO DENTRO DA FUNÇÃO PRECISA ESTAR INDENTADO (4 espaços ou tab)
        priv_key_hex = "6123ae9541852265204a116b4c203d514e436cfe4439370c61ebf4f28234228f"

        try:
            if not all(c in '0123456789abcdef' for c in priv_key_hex):
                raise ValueError("Chave contém caracteres inválidos")
            if len(priv_key_hex) != 64:
                raise ValueError("Chave deve ter 64 caracteres hexadecimais")

            priv_key = bytes.fromhex(priv_key_hex)
            sk = SigningKey.from_string(priv_key, curve=SECP256k1)
            vk = sk.get_verifying_key()

            print(f"Chave Pública (comprimida): {vk.to_string('compressed').hex()}")
            print(f"Chave Pública (não comprimida): {vk.to_string('uncompressed').hex()}")

        except Exception as e:
            print(f"ERRO CRÍTICO: {str(e)}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
main("gerar_pubkey.py") # ← Chamada da função (sem indentação aqui)
