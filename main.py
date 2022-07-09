from PyPDF2 import PdfReader, PdfWriter

def read_first_scan(file_name):
    first_reader = PdfReader(file_name)
    for page in first_reader.pages:
        page.rotate(180)
    return first_reader

def read_second_scan(file_name):
	second_reader = PdfReader(file_name)
	for page in second_reader.pages:
		page.rotate(180)
	return second_reader

def zip_readers(scan_one, scan_two):
	pdf_writer = PdfWriter()
	for page_one, page_two in zip(range(0, len(scan_one.pages)), range(len(scan_two.pages)-1, -1, -1)):
		pdf_writer.add_page(scan_one.getPage(page_one))
		pdf_writer.add_page(scan_two.getPage(page_two))
	with open('final.pdf', mode='wb') as output_file:
		pdf_writer.write(output_file)

if __name__ == '__main__':
    scan_one = read_first_scan('first scan.pdf')
    scan_two = read_second_scan('second scan.pdf')
    zip_readers(scan_one, scan_two)
