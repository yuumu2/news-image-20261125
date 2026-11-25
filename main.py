import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    source = Path(__file__).resolve().with_name("entry_image.jpg")
    try:
        image = source.open("rb")
    except FileNotFoundError:
        print(f"Error: entry_image.jpg is missing ({source})", file=sys.stderr)
        return 1

    with image:
        output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
        output_dir.mkdir(parents=True, exist_ok=True)
        with (output_dir / "entry.png").open("wb") as output:
            shutil.copyfileobj(image, output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
