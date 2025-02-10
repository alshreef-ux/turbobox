# TurboBox

TurboBox is a Python-based tool designed to efficiently archive and compress files on Windows systems. It helps save space and improve load times by creating compressed zip archives of the specified files.

## Features

- Compress multiple files into a single zip archive.
- Easy to use command-line interface.
- Outputs compressed files with a reduced size for storage efficiency.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the `turbobox.py` file to your local system.

```bash
git clone https://github.com/yourusername/turbobox.git
```

2. Navigate to the directory containing `turbobox.py`.

```bash
cd turbobox
```

## Usage

To use TurboBox, run the script with the paths of the files you want to compress and specify the output path for the archive.

```bash
python turbobox.py <input_file1> <input_file2> ... -o <output_archive.zip>
```

### Example

Compress `file1.txt` and `file2.txt` into an archive named `archive.zip`:

```bash
python turbobox.py file1.txt file2.txt -o archive.zip
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.