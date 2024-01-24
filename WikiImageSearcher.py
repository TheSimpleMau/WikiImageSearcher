import requests
import lxml.html as html
import os
from googlesearch import search





class WikiImageSearcher:
    def __init__(self, to_search:str,language:str) -> None:
        if to_search.__contains__("Wikipedia"):
            self.to_search = to_search
        else:
            self.to_search = to_search + " Wikipedia"
        self.language = language

    def get_links(self):
        links = []
        for link in search(self.to_search,lang=self.language,num_results=5):
            links.append(link)
        return links

    def trys_on_images(self,parsed)->str:
        xpaths = [".//table[@class='infobox vcard']//img/@src",".//table[@class='infobox']//img/@src"]
        image = ''
        for xpath in xpaths:
            try:
                image = parsed.xpath(xpath)[0]
            except:
                continue
        return image

    def get_images(self,links:list) -> list:
        images = []
        for link in links:
            response = requests.get(link)
            if response.status_code == 200:
                parsed = html.fromstring(response.content.decode('utf-8'))
                image = self.trys_on_images(parsed)
                image = image[2::]
                if image != '':
                    images.append(image)
        print(f"Found {len(images)} images, downloading...")
        return images
    
    def download_images(self,images:list) -> None:
        
        def get_extension(image:str)->str:
            return image.split(".")[-1]

        len_images = len(images)
        for idx, image in enumerate(images):
            print(f"\r\tObtaingn image {idx+1}/{len_images}", end="")
            extension = get_extension(image)
            command = f"wget -q -O {self.to_search.replace(" Wikipedia","")}_{idx+1}.{extension} {image}"
            os.system(command)