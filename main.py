"""Office-joke one-liner entry.

Reads entry.txt next to this file and copies it byte-identical to
$MAKEFUN_OUTPUT_DIR/entry.txt (mode 0644), with no temp file.
Stdlib only.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    try:
        with open(src, "rb") as f:
            data = f.read()
    except OSError as e:
        print(f"cannot read {src}: {e}", file=sys.stderr)
        return 1
    if not data.strip():
        print("entry.txt is empty or whitespace-only", file=sys.stderr)
        return 1
    try:
        os.makedirs(out_dir, exist_ok=True)
        dst = os.path.join(out_dir, "entry.txt")
        with open(dst, "wb") as f:
            f.write(data)
        os.chmod(dst, 0o644)
    except OSError as e:
        print(f"cannot write output: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
