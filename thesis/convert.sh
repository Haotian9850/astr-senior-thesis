TEX_NAME=$1
pdflatex ${TEX_NAME}.tex
pdfcrop ${TEX_NAME}.pdf
pdftoppm ${TEX_NAME}-crop.pdf | pnmtopng > ${TEX_NAME}.png
