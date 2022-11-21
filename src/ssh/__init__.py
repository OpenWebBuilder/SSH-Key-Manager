from os import system
import uniKey
import vault.bluehost

def ssh_Bluehost(which="bluehost"):
    return f"ssh -i {uniKey.get_key_file(which)} {vault.bluehost.user}@{vault.bluehost.ip}"

def get_public_key(which="bluehost"):
    pubkey = f"{uniKey.get_key_file(which)}.pub"
    return system(f"cat {pubkey}")