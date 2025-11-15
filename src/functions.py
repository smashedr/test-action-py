import subprocess  # nosec


def check_output(*args, throw=False, silent=True) -> str:
    try:
        out = subprocess.check_output(*args).decode().strip()  # nosec
        if not silent:
            print(out)
        return out
    except Exception as error:
        if throw:
            raise error
        return ""
