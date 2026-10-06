# Smart File Organizer

A practical Python automation tool that organizes messy folders by file type,
handles duplicate filenames safely, and creates an activity log.

## Problem

Downloads and work folders often become cluttered with PDFs, images,
spreadsheets, documents, presentations, videos and code files.

Manually sorting hundreds of files is repetitive and error-prone.

## Solution

This tool:

- Detects file types by extension
- Creates category folders automatically
- Moves files into the appropriate category
- Prevents accidental overwrites
- Supports a safe `--dry-run` mode
- Records every action in a log
- Reports totals and errors

## Categories

PDF, Images, Excel, Word, PowerPoint, Videos, Audio, Text, Code,
Archives and Other.

## Usage

```bash
python file_organizer.py "path/to/folder"
```

### Safe preview

Before moving anything:

```bash
python file_organizer.py "path/to/folder" --dry-run
```

## Example

Before:

```text
Downloads/
├── resume.pdf
├── IMG_4837.jpg
├── sales_data.xlsx
├── assignment.docx
├── presentation.pptx
└── lecture.mp4
```

After:

```text
Downloads/
├── PDF/
├── Images/
├── Excel/
├── Word/
├── PowerPoint/
└── Videos/
```

## Duplicate handling

If `resume.pdf` already exists in the PDF folder, the program creates:

```text
resume_1.pdf
resume_2.pdf
...
```

instead of overwriting the existing file.

## Skills demonstrated

- Python
- pathlib
- File-system automation
- Exception handling
- CLI arguments
- Safe file operations
- Logging
- Practical problem solving

## Client use case

This can be adapted for:

- Downloads-folder organization
- Office document organization
- Photo/file sorting
- Automated archival workflows
- Custom company file-management rules

## Portfolio note

The included `sample_messy_folder` is synthetic and exists only to demonstrate
the automation safely.
