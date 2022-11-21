import ssh
import uniKey


if __name__ == '__main__':
    uniKey.generate_key("bluehost")

    uniKey.generate_key("azure")

    print(ssh.ssh_Bluehost())

    # print(ssh.get_public_key())
