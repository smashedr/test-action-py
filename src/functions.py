import subprocess  # nosec
from typing import Union


def check_output(cmd: Union[str, list], throw=False, silent=False) -> str:
    if isinstance(cmd, str):
        cmd = list(filter(None, cmd.split(" ")))
    try:
        out = subprocess.check_output(cmd).decode().strip()  # nosec
        if not silent:
            print(out)
        return out
    except Exception as error:
        if throw:
            raise error
        return ""
