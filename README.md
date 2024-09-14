# Animación hecha en LaTeX

Este es un ejemplo de cómo hacer una animación en LaTeX. Para ello, se necesita hacer varias páginas en PDF, que serán nuestros frames, y luego los convertimos con PyMuPDF a PNGs, para finalmente concatenarlos con FFmpeg.

## Requisitos

- Instalar las librearías necesarias con `pip install -r requirements.txt`
- Tener instalado FFmpeg y LaTeX.

## Uso
```bash
pdflatex -shell-escape latex-video.tex
python3 pdf2pngs.py
ffmpeg -y -r 60 -i out/page%03d.png -vcodec libx264 -pix_fmt yuv420p -r 60 "LaTeX animation.mp4"
```
