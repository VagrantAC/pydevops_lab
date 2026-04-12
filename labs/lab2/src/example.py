import hashlib
import json
import os
import pathlib
import xml.etree.ElementTree as ET
from pprint import pprint
from typing import Any, Iterator

import yaml
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa


def read_file_len(file_path: str) -> int:
    open_file = open(file_path, "r")
    text = open_file.read()
    print("len(text)", len(text))
    print("file_handle", open_file)
    open_file.close()
    return len(text)


def read_file_lines(file_path: str) -> list[str]:
    open_file = open(file_path, "r")
    lines = open_file.readlines()
    print("count lines", len(lines))
    open_file.close()
    return lines


def read_file_with_context_manager(file_path: str) -> str:
    with open(file_path, "r") as open_file:
        text = open_file.read()
        print(f"len(text): {len(text)}")
        print(f"file_handle: {open_file}")
    print(f"file_handle is closed: {open_file.closed}")
    return text


def read_binary_file(file_path: str) -> bytes:
    with open(file_path, "rb") as open_file:
        btext = open_file.read()
        print(f"len(btext): {len(btext)}")
        print(f"file_handle: {open_file}")
    print(f"file_handle is closed: {open_file.closed}")
    return btext


def read_file_by_pathlib(file_path: str) -> str:
    path = pathlib.Path(file_path)
    text = path.read_text()
    print(f"len(text): {len(text)}")
    print(f"file_handle: {path}")
    return text


def read_file_lines_by_pathlib(file_path: str) -> list[str]:
    path = pathlib.Path(file_path)
    lines = path.read_text().splitlines()
    print(f"count lines: {len(lines)}")
    print(f"file_handle: {path}")
    return lines


def read_json_file(file_path: str) -> dict[Any, Any]:
    with open(file_path, "r") as open_file:
        policy: dict[Any, Any] = json.load(open_file)
        print(f"len(policy): {len(policy)}")
        print(f"file_handle: {open_file}")
    print(f"file_handle is closed: {open_file.closed}")
    pprint(policy)

    # update policy
    policy["Statement"]["Resource"] = "S3"
    pprint(policy)
    return policy


def read_yaml_file(file_path: str) -> dict[Any, Any]:
    with open(file_path, "r") as open_file:
        verify_apache: dict[Any, Any] = yaml.safe_load(open_file)
        print(f"len(verify_apache): {len(verify_apache)}")
        print(f"file_handle: {open_file}")
    print(f"file_handle is closed: {open_file.closed}")
    pprint(verify_apache)
    return verify_apache


def read_xml_file(file_path: str) -> ET.ElementTree:
    tree = ET.parse(file_path)
    root = tree.getroot()
    print(f"root.tag: {root.tag}")

    for child in root:
        print(f"child.tag: {child.tag} {child.attrib}")
    print(root)
    return tree


# process big file line by line


def line_reader(file_path: str) -> Iterator[str]:
    with open(file_path, "r") as open_file:
        for line in open_file:
            yield line


def use_hashlib(secret: str = "This is the password or document text") -> str:

    bsecret = secret.encode()
    m = hashlib.md5()
    m.update(bsecret)
    print(m.digest())
    print(m.hexdigest())
    return m.digest().hex()


def use_cryptography(
    message: bytes = b"This is the password or document text",
) -> None:
    key = Fernet.generate_key()
    print(key)

    f = Fernet(key)
    encrypted_message = f.encrypt(message)
    print(encrypted_message)

    decrypted_message = f.decrypt(encrypted_message)
    print(decrypted_message.decode())


def rsa_use_cryptography_hazma() -> None:
    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=4096, backend=default_backend()
    )
    print(private_key)

    public_key = private_key.public_key()
    print(public_key)

    message = b"This is the password or document text"
    oaef = padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    )
    encrypted = public_key.encrypt(message, oaef)
    print(encrypted)

    decrypted = private_key.decrypt(encrypted, oaef)
    print(decrypted.decode())


def use_os_path() -> None:
    cur_dir = os.getcwd()
    print(cur_dir)

    print(f"os.path.split: {os.path.split(cur_dir)}")

    print(f"os.path.dirname: {os.path.dirname(cur_dir)}")

    print(f"os.path.basename: {os.path.basename(cur_dir)}")

    print("========")
    while os.path.basename(cur_dir):
        cur_dir = os.path.dirname(cur_dir)
        print(f"os.path.basename: {os.path.basename(cur_dir)}")
    return None


def find_rc(rc_name: str = ".examplerc") -> str:
    # check path in environment variable
    var_name = "EXAMPLE_DIR"
    if var_name in os.environ:
        var_path = os.path.join(os.environ[var_name], rc_name)
        config_path = os.path.expandvars(var_path)
        print(f"Checking {config_path}")
        if os.path.exists(config_path):
            return config_path

    # check current directory
    config_path = os.path.join(os.getcwd(), rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    # check home directory
    home_dir = os.path.expanduser("~/")
    config_path = os.path.join(home_dir, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    # check current directory
    file_path = os.path.abspath(__file__)
    parent_path = os.path.dirname(file_path)
    config_path = os.path.join(parent_path, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    print(f"File {rc_name} has not been found")
    return ""


def find_rc_v2(rc_name: str = ".examplerc") -> str:
    # check path in environment variable
    var_name = "EXAMPLE_DIR"
    example_dir = os.environ.get(var_name)
    if example_dir:
        dir_path = pathlib.Path(example_dir)
        config_path = dir_path / rc_name
        print(f"Checking {config_path}")
        if config_path.exists():
            return config_path.as_posix()

    # check current directory
    config_path = pathlib.Path.cwd() / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_posix()

    # check home directory
    home_dir = pathlib.Path.home() / rc_name
    config_path = home_dir / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_posix()

    # check current directory
    file_path = pathlib.Path(__file__).resolve()
    parent_path = file_path.parent
    config_path = parent_path / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
        return config_path.as_posix()

    print(f"File {rc_name} has not been found")
    return ""


if __name__ == "__main__":
    # read_json_file("labs/lab2/src/service-policy.json")
    # read_yaml_file("labs/lab2/src/verify-apache.yml")
    # read_xml_file("labs/lab2/src/http_feeds.feedburner.com_oreilly_radar_atom.xml")

    # reader = line_reader(
    #     "labs/lab2/src/http_feeds.feedburner.com_oreilly_radar_atom.xml"
    # )
    # for line in reader:
    #     print(line, end="")

    # use_hashlib()
    # use_cryptography()
    # rsa_use_cryptography_hazma()
    # use_os_path()
    find_rc(".zshrc")
