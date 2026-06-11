import argparse
import os
import sys
from pathlib import Path

from markitdown import MarkItDown


SUPPORTED_EXTS = {
    ".pdf", ".docx", ".pptx", ".xlsx", ".xls",
    ".html", ".htm", ".jpg", ".jpeg", ".png",
    ".bmp", ".gif", ".tiff", ".csv", ".json",
    ".xml", ".zip", ".epub", ".md", ".txt", ".rtf",
}


def convert_file(md: MarkItDown, path: Path, output: Path | None) -> str | None:
    result = md.convert_local(str(path))
    text = result.text_content
    if output:
        output.write_text(text, encoding="utf-8")
        print(f"[OK] {path.name} -> {output}")
        return None
    return text


def main():
    parser = argparse.ArgumentParser(
        description="Convert files to Markdown using Microsoft MarkItDown"
    )
    parser.add_argument("path", help="File or directory path")
    parser.add_argument("-o", "--output", help="Output file (for single file mode)")
    parser.add_argument("--all", action="store_true", help="Convert all supported files in directory")
    parser.add_argument("--clip", action="store_true", help="Copy result to clipboard (Windows)")
    args = parser.parse_args()

    path = Path(args.path)
    md = MarkItDown()

    if path.is_dir():
        if not args.all:
            print("Use --all to convert all supported files in directory")
            sys.exit(1)
        out_dir = Path(args.output) if args.output else path / "markitdown_output"
        out_dir.mkdir(exist_ok=True)
        for f in sorted(path.iterdir()):
            if f.suffix.lower() in SUPPORTED_EXTS:
                out_path = out_dir / f"{f.stem}.md"
                convert_file(md, f, out_path)
        print(f"[Done] Output directory: {out_dir}")
        return

    if not path.exists():
        print(f"[Error] File not found: {path}")
        sys.exit(1)

    text = convert_file(md, path, Path(args.output) if args.output else None)

    if args.clip and text:
        import subprocess
        subprocess.run(["clip"], input=text, text=True, encoding="utf-8")
        print("[Clip] Copied to clipboard")
    elif text:
        sys.stdout.write(text)


if __name__ == "__main__":
    main()
