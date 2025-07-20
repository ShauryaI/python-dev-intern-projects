import pymupdf  # PyMuPDF
from PIL import Image
import pytesseract
from gtts import gTTS
from pydub import AudioSegment

# Path to your PDF file
pdf_path = "sample.pdf"

# Path to Tesseract executable (adjust as needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the PDF
doc = pymupdf.open(pdf_path)
extracted_text = ""
audio_segments = []

for page_num in range(len(doc)):
    page = doc.load_page(page_num)

    # Extract text directly from the page
    text = page.get_text()
    extracted_text += text + "\n"

    # Convert page to image for OCR (if images are present)
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Perform OCR on the image
    image_text = pytesseract.image_to_string(img)
    extracted_text += image_text + "\n"

    # Convert extracted text to speech
    if extracted_text.strip():  # Only convert if there's text
        tts = gTTS(text=extracted_text, lang='en')  # Adjust language as needed
        audio_file_path = f"page_{page_num}.mp3"
        tts.save(audio_file_path)
        audio_segments.append(AudioSegment.from_mp3(audio_file_path))
        extracted_text = ""  # Reset for next page

# Combine all audio segments (optional)
if audio_segments:
    combined_audio = sum(audio_segments)
    combined_audio.export("audiobook.mp3", format="mp3")