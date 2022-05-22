# importing libraries
from bs4 import BeautifulSoup
import requests

def main(URL):
	# opening our output file in append mode
	File = open("out.csv", "a")

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}


	# Making the HTTP Request
	webpage = requests.get(URL, headers=HEADERS)

	# Creating the Soup Object containing all data
	soup = BeautifulSoup(webpage.content, "lxml")

	# retrieving product title
	try:
		# Outer Tag Object
		title = soup.find("span",
						attrs={"id": 'productTitle'})

		# Inner NavigableString Object
		title_value = title.string

		# Title as a string value
		title_string = title_value.strip().replace(',', '')

	except AttributeError:
		title_string = "NA"
	print("product Title = ", title_string)

	# saving the title in the file
	File.write(f"{title_string},")

	# retrieving price
	try:
		price = soup.find(
			"span", attrs={'id': 'priceblock_ourprice'})
								.string.strip().replace(',', '')
		# we are omitting unnecessary spaces
		# and commas form our string
	except AttributeError:
		price = "NA"
	print("Products price = ", price)

	# saving
	File.write(f"{price},")

	try:
		review_count = soup.find(
			"span", attrs={'id': 'acrCustomerReviewText'})
								.string.strip().replace(',', '')

	except AttributeError:
		review_count = "NA"
	print("Total reviews = ", review_count)
	File.write(f"{review_count},")


if __name__ == '__main__':
# opening our url file to access URLs
	file = open("url.txt", "r")

	# iterating over the urls
	for links in file.readlines():
		main(links)