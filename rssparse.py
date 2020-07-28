from bs4 import BeautifulSoup


def get_links_titles_guuids(text):
    soup = BeautifulSoup(text, "lxml-xml")
    data = {"data": []}
    count = 0
    count2 = 0
    titles = soup.find_all("title")
    links = soup.find_all("link")
    guids =  soup.find_all("guid")
    for (guid, title, link) in zip(guids, titles, links):
        data["data"].append({"id": guid.text})
        data["data"][count]["title"] = titles[count].text
        data["data"][count]["link"] = links[count].text
        count += 1
    return data



