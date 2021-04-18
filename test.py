import fitz
import io
from PIL import Image
file = "PDF_Proof.PDF"
pdf_file = fitz.open(file)
for page_index in range(len(pdf_file)):
	page = pdf_file[page_index]
	image_list = page.getImageList()
	if image_list:
	    print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
	    for image_index, img in enumerate(page.getImageList(), start=1):
	        xref = img[0]
	        base_image = pdf_file.extractImage(xref)
	        image_bytes = base_image["image"]
	        image_ext = base_image["ext"]
	        print(f"[+][+] Image {xref} : {image_ext}")

 
