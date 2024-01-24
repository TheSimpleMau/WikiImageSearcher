from WikiImageSearcher import WikiImageSearcher


def main():
    to_search = input("Image to search: ")
    language = input("In which language want to search?: ")
    # language = "en"
    searcher = WikiImageSearcher(to_search,language)
    links = searcher.get_links()
    images = searcher.get_images(links)
    if len(links) == 0:
        print("exit...")
        exit()
    searcher.download_images(images)


if __name__ == '__main__':
    main()