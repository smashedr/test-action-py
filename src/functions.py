import subprocess  # nosec
from typing import Optional


def check_output(*args, throw=False) -> Optional[str]:
    try:
        out = subprocess.check_output(*args).decode()  # nosec
        return out.strip()
    except Exception as error:
        if throw:
            raise error
        return None
