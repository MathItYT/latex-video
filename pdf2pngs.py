from pathlib import Path

import pymupdf
from PIL import Image


if __name__ == "__main__":
    folder = Path("out")
    folder.mkdir(exist_ok=True)

    pdf_path = Path("latex-video.pdf")
    pdf = pymupdf.open(pdf_path)
    for i, page in enumerate(pdf):
        img_path = folder / f"page{i:03d}.png"
        img = page.get_pixmap(dpi=500)
        img.save(str(img_path))
        img = Image.open(img_path)
        img.resize((1080, 1920), Image.Resampling.BICUBIC).save(str(img_path), 'PNG')
        print(f"Saved {img_path}")

    print("Done")
