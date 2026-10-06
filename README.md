# Smart File Organizer

A practical Python automation tool that organizes messy folders by file type, handles duplicate filenames safely, supports dry-run mode, and creates an activity log.

## Features

- Automatically detects file types
- Creates category folders
- Moves files into the correct folders
- Prevents filename overwrites
- Handles duplicate filenames safely
- Dry-run mode to preview changes
- Activity logging
- Command-line interface
- Error handling

## Categories

The organizer can automatically sort files such as:

- Documents
- Images
- Videos
- Audio
- Spreadsheets
- Presentations
- Archives
- Code files
- Other files

## Example

Before:

Downloads/
- report.pdf
- photo.jpg
- presentation.pptx
- script.py
- video.mp4

After:

Downloads/
├── Documents/
├── Images/
├── Presentations/
├── Code/
└── Videos/

## Technologies

- Python
- Python Standard Library
- File System Automation
- Command-Line Interface

## Usage

Run the organizer:

```bash
python file_organizer.py "path/to/folder"
