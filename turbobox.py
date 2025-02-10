import os
import zipfile
import argparse


def compress_files(input_paths, output_path):
    """Compress files into a zip archive."""
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in input_paths:
            if os.path.isfile(file):
                zipf.write(file, os.path.basename(file))
                print(f"Compressed: {file}")
            else:
                print(f"Skipped (not a file): {file}")


def main():
    parser = argparse.ArgumentParser(description="TurboBox: Efficiently archive and compress files.")
    parser.add_argument(
        'input', nargs='+', help="Path(s) of the file(s) to compress.")
    parser.add_argument(
        '-o', '--output', required=True, help="Output path for the compressed archive.")
    
    args = parser.parse_args()

    compress_files(args.input, args.output)


if __name__ == "__main__":
    main()