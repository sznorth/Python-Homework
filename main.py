import loader


if __name__=="__main__":
    url         = "https://index.hu"
    level       = "h2"  # SEO miatt H1-et cikk címek/contentek címzésére már nem szokás használni.
    filename    = "szabo_bence_istvan_index.txt"


    response = loader.webmapper(url)
    loader.printFiltered(response, level)
    loader.fileWrite(response, level, filename)
