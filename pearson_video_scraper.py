""" Pearson Video Tutorials Scraper.

 Basically goes through this AMAZING SOURCE:
 view-source:https://media.pearsoncmg.com/curriculum/math/hsim2014/download_center/math1/index.html

Downloads each video, English AND Spanish, and then creates a nice little HTML
snippet for the website that labels headers for each section and gives video links.

HTML Example:

<h3>2-1 Lines and Angles</h3>
<a href="https://media.pearsoncmg.com/curriculum/math/hsim2014/download_center/math1/media/hvt_sp/shvt378_alg.mp4">Lesson 1-1 Spanish: Simplifying algebraic expressions with exponents</a>

HTML formant:
<h3>Section Header (more than one video for each section)</h3>
<a href="link" target="_blank">link text</a>

"""

import requests
import re

# Screw BS. Just need simple REs.
# Need an RE for each line with the link, and then an RE to get the link.


def grab_website(url):
	return requests.get(url).text


# Given the website text... grabs the spanish links and returns generated HTML.
def extract_spanish(website):

	spanish_html_blurb=""

	# Makes a list with all of the lines that contain the SPANISH links.
	list_with_links = re.findall(r'<a href.*Spanish.*</a>', website)

	# Cycle through each entry and extract link.
	for line in list_with_links:

		# Extract the link.
		try:
			link = re.findall(r'(?<=\").*?\.mp4(?=\")', line)[0]
		except IndexError:
			print("Skipping nonapplicable line")
			continue

		# Extract the text.
		try:
			text = re.findall(r'(?<=>).*?(?=<)', line)[0]
		except IndexError:
			print("Should never run...")

		# Update the html blurb.
		spanish_html_blurb = create_HTML_link(spanish_html_blurb, link, text)

	return spanish_html_blurb


# Given the website text... grabs the english links and returns generated HTML.
def extract_english(website):

	english_html_blurb=""

	# Makes a list with all of the lines that contain the SPANISH links.
	list_with_links = re.findall(r'<a href.*English.*</a>', website)

	# Cycle through each entry and extract link.
	for line in list_with_links:

		# Extract the link.
		try:
			link = re.findall(r'(?<=\").*?\.mp4(?=\")', line)[0]
		except IndexError:
			print("Skipping nonapplicable line")
			continue

		# Extract the text.
		try:
			text = re.findall(r'(?<=>).*?(?=<)', line)[0]
		except IndexError:
			print("Should never run...")

		# Update the html blurb.
		english_html_blurb = create_HTML_link(english_html_blurb, link, text)

	return english_html_blurb

# Creates an HTML section header in given file with given text.
def create_HTML_section_header(html_file, header_text):
	text = "<h3>" + header_text + "</h3><br>\n"
	html_file += text
	return html_file


# Creates an HTML link in given file with given link and display text.
def create_HTML_link(html_file, link, text):
	link_text = '<a href="{}" target="_blank">{}</a><br>\n'.format(link, text)
	html_file += link_text
	return html_file


def main():
	url = "https://media.pearsoncmg.com/curriculum/math/hsim2014/download_center/math3/index.html"
	website = grab_website(url)

	spanish_html_blurb = extract_spanish(website)
	print(spanish_html_blurb)

	#english_html_blurb = extract_english(website)
	#print(english_html_blurb)

main()
