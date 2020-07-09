import pyttsx3
import PyPDF2

pdf_book = open('object_oriented_python_tutorial.pdf', 'rb')

# reading the pdf file
pdf_reader = PyPDF2.PdfFileReader(pdf_book)

# getting total pages
book_pages = pdf_reader.numPages

print(book_pages)

engine = pyttsx3.init()

voices = engine.getProperty('voices')

# male voice pass voices[0].id
# female voice pass voices[1].id
engine.setProperty('voice', voices[1].id)
# read specific page
# getting the specific page from pdf for listen
page = pdf_reader.getPage(7)
# converting page to text
text = page.extractText()
# reading text
engine.say(text)
engine.runAndWait()


# read specific range of pages
# start_page = 7
# end_page = 15
# for num in range(start_page, end_page):
#     page = pdf_reader.getPage(num)
#     # converting page to text
#     text = page.extractText()
#     # reading text
#     engine.say(text)
#     engine.runAndWait()
