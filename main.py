from WikiImageSearcher import WikiImageSearcher


def main():

    searcher = WikiImageSearcher("Goolge","en")
    links = searcher.get_links()
    images = searcher.get_images(links)
    searcher.download_images(images)



if __name__ == '__main__':
    main()