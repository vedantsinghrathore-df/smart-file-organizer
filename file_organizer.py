"""
Smart File Organizer
--------------------
Organizes files in a folder by extension, safely handles duplicates,
and creates a timestamped activity log.

Usage:
    python file_organizer.py "path/to/folder"

Optional:
    python file_organizer.py "path/to/folder" --dry-run
"""

from pathlib import Path
from datetime import datetime
import argparse
import shutil

CATEGORY_MAP = {
    "PDF": {".pdf"},
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "Excel": {".xlsx", ".xls", ".csv"},
    "Word": {".docx", ".doc"},
    "PowerPoint": {".pptx", ".ppt"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi", ".webm"},
    "Audio": {".mp3", ".wav", ".aac", ".flac"},
    "Text": {".txt", ".md"},
    "Code": {".py", ".cpp", ".c", ".java", ".js", ".html", ".css", ".sql"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
}

def get_category(extension: str) -> str:
    extension = extension.lower()
    for category, extensions in CATEGORY_MAP.items():
        if extension in extensions:
            return category
    return "Other"

def unique_destination(destination: Path) -> Path:
    """Return a non-conflicting path without overwriting an existing file."""
    if not destination.exists():
        return destination

    stem = destination.stem
    suffix = destination.suffix
    counter = 1

    while True:
        candidate = destination.with_name(f"{stem}_{counter}{suffix}")
        if not candidate.exists():
            return candidate
        counter += 1

def organize_folder(folder: Path, dry_run: bool = False):
    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"Folder does not exist: {folder}")

    log_dir = folder / "_organizer_logs"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"organizer_{timestamp}.txt"

    stats = {
        "processed": 0,
        "organized": 0,
        "skipped": 0,
        "errors": 0,
        "categories": {},
    }

    log_lines = [
        "SMART FILE ORGANIZER",
        f"Folder: {folder}",
        f"Started: {datetime.now():%Y-%m-%d %H:%M:%S}",
        f"Dry run: {dry_run}",
        "-" * 60,
    ]

    # Only inspect files directly inside the selected folder.
    # This prevents the program from accidentally reorganizing nested folders.
    for source in sorted(folder.iterdir()):
        if not source.is_file():
            continue
        if source.name.startswith("."):
            continue

        stats["processed"] += 1
        category = get_category(source.suffix)
        target_dir = folder / category
        destination = unique_destination(target_dir / source.name)

        try:
            if not dry_run:
                target_dir.mkdir(exist_ok=True)
                shutil.move(str(source), str(destination))

            stats["organized"] += 1
            stats["categories"][category] = stats["categories"].get(category, 0) + 1

            action = "WOULD MOVE" if dry_run else "MOVED"
            log_lines.append(
                f"{action}: {source.name} -> {category}/{destination.name}"
            )

        except Exception as exc:
            stats["errors"] += 1
            log_lines.append(f"ERROR: {source.name} -> {exc}")

    # Don't create a log folder during a dry run unless there are actual logs to save.
    if not dry_run:
        log_dir.mkdir(exist_ok=True)
        log_lines.extend([
            "-" * 60,
            f"Files processed: {stats['processed']}",
            f"Files organized: {stats['organized']}",
            f"Errors: {stats['errors']}",
            "",
            "BY CATEGORY:",
        ])
        for category, count in sorted(stats["categories"].items()):
            log_lines.append(f"{category}: {count}")

        log_file.write_text("\n".join(log_lines), encoding="utf-8")

    return stats, log_file if not dry_run else None

def main():
    parser = argparse.ArgumentParser(
        description="Organize files into folders based on file type."
    )
    parser.add_argument("folder", help="Folder to organize")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would happen without moving files"
    )
    args = parser.parse_args()

    try:
        stats, log_file = organize_folder(Path(args.folder), args.dry_run)

        print("\nSMART FILE ORGANIZER")
        print("=" * 35)
        print(f"Files processed : {stats['processed']}")
        print(f"Files organized : {stats['organized']}")
        print(f"Errors          : {stats['errors']}")

        if stats["categories"]:
            print("\nBy category:")
            for category, count in sorted(stats["categories"].items()):
                print(f"  {category:<12} {count}")

        if log_file:
            print(f"\nLog saved to: {log_file}")

    except Exception as exc:
        print(f"Error: {exc}")

if __name__ == "__main__":
    main()
