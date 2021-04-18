import fitz
import io
from PIL import Image
file = "PDF_Proof.PDF"
imgdir = "images"  # found images are stored in this subfolder

if not os.path.exists(imgdir):  # make subfolder if necessary
    os.mkdir(imgdir)

pdf_file = fitz.open(file)
