"""
Convert PNG/JPG images to WebP format for web optimization.

Requirements:
    pip install pillow

Usage:
    python convert_to_webp.py
"""

import os
from pathlib import Path

from PIL import Image


def convert_image_to_webp(input_path, output_path=None, quality=85):
    """
    Convert an image to WebP format.

    Args:
        input_path: Path to input image (PNG, JPG, etc.)
        output_path: Path to output WebP file (optional)
        quality: WebP quality (1-100, default 85)
    """
    if output_path is None:
        output_path = Path(input_path).with_suffix(".webp")

    try:
        # Open image
        img = Image.open(input_path)

        # Convert RGBA to RGB if necessary
        if img.mode in ("RGBA", "LA"):
            background = Image.new("RGB", img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[-1])
            img = background

        # Save as WebP
        img.save(output_path, "webp", quality=quality, method=6)

        # Get file sizes
        input_size = os.path.getsize(input_path) / 1024  # KB
        output_size = os.path.getsize(output_path) / 1024  # KB
        savings = ((input_size - output_size) / input_size) * 100

        print(f"[OK] {os.path.basename(input_path)}")
        print(f"  {input_size:.1f} KB -> {output_size:.1f} KB ({savings:.1f}% smaller)")

        return True

    except Exception as e:
        print(f"[ERROR] Error converting {input_path}: {e}")
        return False


def convert_directory(directory, recursive=True):
    """
    Convert all images in a directory to WebP.

    Args:
        directory: Directory path
        recursive: Process subdirectories (default True)
    """
    image_extensions = {".png", ".jpg", ".jpeg", ".bmp", ".tiff"}
    converted_count = 0

    pattern = "**/*" if recursive else "*"

    for file_path in Path(directory).glob(pattern):
        if file_path.suffix.lower() in image_extensions and file_path.is_file():
            # Skip if WebP already exists
            webp_path = file_path.with_suffix(".webp")
            if webp_path.exists():
                print(f"[SKIP] {file_path.name} (WebP exists)")
                continue

            if convert_image_to_webp(file_path):
                converted_count += 1
                print()

    return converted_count


def main():
    """Convert all images in the images directory."""
    print("=" * 60)
    print("NanoSim Image Converter - WebP Optimization")
    print("=" * 60)
    print()

    # Check dependencies
    try:
        import importlib.util

        if importlib.util.find_spec("PIL") is None:
            raise ImportError("PIL module not found")
        print("[OK] Pillow found")
    except ImportError:
        print("[ERROR] Pillow not found")
        print()
        print("Please install: pip install pillow")
        print()
        return

    print()
    print("Converting images to WebP...")
    print("-" * 60)
    print()

    # Convert images in current directory and subdirectories
    current_dir = Path(".")
    converted_count = convert_directory(current_dir, recursive=True)

    print("-" * 60)
    print(f"[OK] Converted {converted_count} images to WebP format")
    print()
    print("Benefits of WebP:")
    print("  - ~30% smaller file size than PNG/JPG")
    print("  - Faster page loading")
    print("  - Better user experience")
    print()
    print("Next steps:")
    print("  1. Update HTML to use <picture> tags with WebP")
    print("  2. Keep original PNG/JPG as fallback")
    print("  3. Test loading speed with Google Lighthouse")
    print()


if __name__ == "__main__":
    main()
