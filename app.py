# Navigate to Google Images

import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
url = "https://www.google.com/imghp?hl=en"

browser.open(url)
print(browser.get_url())

# Type a search term and click "search"

#get HTML
browser.get_current_page()

#target the search input
browser.select_form()
browser.get_current_form().print_summary()

#search for a term
search_term = 'Uhuru'
browser["q"] = search_term 

#submit/"click" search
browser.launch_browser()
response = browser.submit_selected()

print('new url:', browser.get_url())
print('my response:\n', response.text[:500])

# Navigate to the new page and target all the images

#open new URL
new_url = browser.get_url()
browser.open(new_url)

#get HTML
page = browser.get_current_page()
all_images = page.find_all('img')

#target the source attribute
image_source = []
for image in all_images:
    image = image.get('src')
    image_source.append(image)
    
image_source[5:]

# Fix broken/incomplete image links

image_source = [image for image in image_source if image.startswith('https')]
image_source[5:]

# Create a new local directory on our computer

import os
import wget

path = os.getcwd()
path = os.path.join(path, search_term + "s")

#create the directory
os.mkdir(path)

path

# Download and save all the images

#download images
counter = 0
for image in image_source:
    save_as = os.path.join(path, search_term + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1



