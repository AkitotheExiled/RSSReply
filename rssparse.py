from bs4 import BeautifulSoup


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
            count2 += 1
        return data
    except Exception as e:
        print(e)



