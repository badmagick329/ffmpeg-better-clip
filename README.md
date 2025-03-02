# FFmpeg Better Clip

This Python script takes FFmpeg commands from your clipboard and “optimizes” them. It looks for specific patterns in your FFmpeg commands and rewrites them to improve efficiency when processing media files.

## What It Does

- **Optimize `-ss` and `-to` Usage:**  
  When both `-ss` (seek start) and `-to` (end time) are present, the script rewrites the command by:

  - Moving `-ss` to the beginning of the command.
  - Calculating the duration as `(to - ss)` and replacing `-to` with `-t` (duration).

  This approach prevents FFmpeg from reading the file from the very beginning up until the seek point, significantly speeding up processing.

- **Reorder `-ss`:**  
  If the command contains only `-ss`, it is simply moved to the start of the command. No duration is added.

- **Leave Unchanged:**  
  Commands that do not match the above patterns remain untouched.

## Why This Matters

FFmpeg’s efficiency can suffer when it has to read through a file up to a certain point before processing. By moving `-ss` to the front and using `-t` with a pre-calculated duration, the command avoids unnecessary file reading, resulting in faster processing times—especially beneficial for large media files.

## Requirements

- **Python 3.x**
- **Clipboard Library:**  
  [pyperclip](https://pypi.org/project/pyperclip/)
- **FFmpeg Installed:**  
  Ensure FFmpeg is installed and available in your system’s PATH if you want to test the optimized commands.

## Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/badmagick329/ffmpeg-better-clip.git
cd ffmpeg-better-clip
pip install -r requirements.txt
```

## Usage

1. **Copy FFmpeg Commands:**  
   Copy one or more FFmpeg commands to your clipboard.

2. **Run the Script:**  
   Execute the script with Python:

   ```bash
   python main.py
   ```

3. **Output:**  
   The script processes the clipboard content and outputs the optimized FFmpeg commands. You can then copy these commands for execution.

## How It Works

- **Clipboard Reading:**  
  The script fetches FFmpeg commands from your clipboard.
- **Command Parsing:**  
  It checks each command for the presence of `-ss` and `-to`.
- **Optimization:**
  - If both `-ss` and `-to` are found, it calculates the duration (`to - ss`), moves `-ss` to the start, and replaces `-to` with `-t` using the calculated duration.
  - If only `-ss` is present, it moves it to the beginning.
  - Otherwise, it leaves the command as is.
- **Result:**  
  The optimized commands are either printed out or re-copied to your clipboard, depending on your setup.

## Example

**Original Command:**

```bash
ffmpeg -i input.mp4 -ss 00:01:00 -to 00:02:30 -c copy output.mp4
```

**Optimized Command:**

```bash
ffmpeg -ss 00:01:00 -i input.mp4 -t 00:01:30 -c copy output.mp4
```

Here, `00:01:30` is the duration calculated as the difference between `00:02:30` and `00:01:00`.

## Contributing

If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
