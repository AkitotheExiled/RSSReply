from bs4 import BeautifulSoup
from markdownify import markdownify as md

def get_links_titles_guuids(text):
    soup = BeautifulSoup(text, "lxml-xml")
    data = {"data": []}
    count = 0
    count2 = 0
    try:
        items = soup.find_all("item")
        for item in items:
            guid = item.guid.text
            if guid == "":
                guid = item.link.text
            data["data"].append({"id": guid})
            data["data"][count2]["title"] = item.title.text
            data["data"][count2]["link"] = item.link.text
            if contains_html(item.description.text):
                cdata_removed = item.description.text.lstrip("<![CDATA[").rstrip("]]>")
                data["data"][count2]["desc"] = md(cdata_removed)
            else:
                data["data"][count2]["desc"] = item.description.text
            data["data"][count2]["images"] = get_images_from_text(item.description.text)
            count2 += 1
        return data
    except Exception as e:
        print(e)

def get_images_from_text(text):
    images = BeautifulSoup(text, "html.parser").find_all('img')
    img_srcs = []
    for img in images:
        img_srcs.append({"image_path": img['src']})
    return img_srcs

def contains_html(text):
    tags = ['div', 'ul', 'ol', 'a', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    soup = BeautifulSoup(text, "html.parser")
    for tag in tags:
        if soup.find(tag):
            return True
    return False


