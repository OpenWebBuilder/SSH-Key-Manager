import os
import pathlib
import subprocess

# Protected Key-Vault
from vault.organization import keyFolder

this = "temp"


def get_key_dir(which):
    match which:
        case "azure":
            return f"{pathlib.Path.home()}/.ssh/{keyFolder}/azure"
        case "cloud":
            return f"{pathlib.Path.home()}/.ssh/{keyFolder}/cloud"
        case "git":
            return f"{pathlib.Path.home()}/.ssh/{keyFolder}/git"
        case "web":
            return f"{pathlib.Path.home()}/.ssh/{keyFolder}/web"
        case "bluehost":
            return f"{pathlib.Path.home()}/.ssh/{keyFolder}/web/bluehost"


def get_key_file(which):
    return f"{get_key_dir(which)}/id_rsa"


def generate_key(which):
    os.makedirs(get_key_dir(which), exist_ok=True)
    ssh_key_gen = f'ssh-keygen -f {get_key_file(which)} -N ""'
    if not key_exists(get_key_file(which)):
        subprocess.call(ssh_key_gen.split())
        print(f"Key Generated for {which}")
    else:
        print(f"{which} - Key exists")
    # Todo: Without Passphrase https://unix.stackexchange.com/questions/69314/automated-ssh-keygen-without-passphrase-how


def ssh_copy_id(which):
    # return f"ssh-copy-id -i {get_key_file(which)} {this.user}@{this.ip}"
    print(which)
    pass


def key_exists(key):
    return os.path.isfile(key)
