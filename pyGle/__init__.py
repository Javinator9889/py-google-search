#
#                py-google-search  Copyright (C) 2018  Javinator9889                
#   This program comes with ABSOLUTELY NO WARRANTY; for details add the "-h" option.
#           This is free software, and you are welcome to redistribute it
#                 under certain conditions; type "-L" for details.
#


def main():
    import requests as rq
    import ujson as json

    from bs4 import BeautifulSoup
    import pprint
    import time

    from url import GoogleSearch, URLBuilder
    from values import Countries, TimeLimit, Languages, GooglePages, GoogleImages
    from extractor import ImageExtractor, SearchExtractor, NewsExtractor

    pp = pprint.PrettyPrinter(indent=4)
    country = Countries()
    country.setCountry("Spain")

    lang = Languages()
    lang.setLanguage("Spanish")

    limit = TimeLimit()
    limit.setDay()

    page = GooglePages()
    page.searchImage()

    image = GoogleImages()
    image.setImageFormat("jpg")
    image.setImageSize(">400*300")

    news = GooglePages()
    news.searchNews()

    prepared_query = GoogleSearch() \
        .withQuery("test") \
        .withContainingTwoTerms("psico", "analysis") \
        .withExcludedWords(["press"]) \
        .withNumberOfResults(20) \
        .withResultBetweenTwoNumbers(10, 20) \
        .withResultsAtCountry(country) \
        .withResultsLanguage(lang) \
        .withTimeLimit(limit)
    s_extractor = SearchExtractor(must_use_session=True, with_history_enabled=True)
    # print(URLBuilder(prepared_query).build())
    # sbu = URLBuilder(prepared_query)
    # nr = s_extractor.extract_url(sbu)
    # pp.pprint(nr)

    # npq = GoogleSearch().withQuery("cursos hablar en público en madrid").withNumberOfResults(10)\
    #     .withResultsLanguage(lang)
    # url = URLBuilder(npq).build()
    # for i in range(10):
    #     # print(url)
    #     nr1 = s_extractor.extract_url(URLBuilder(npq))
    #     # print("Waiting for values...")
    #     result = nr1.result(10)
    #     ex = nr1.exception()
    #     if ex:
    #         print(ex)
    #     pp.pprint(result)

    # start_time = time.time()
    # data = rq.get(url)
    # end_time = time.time()
    # print("Data time: " + str((end_time - start_time)) + " s")
    # start_time = time.time()
    # content = data.content
    # end_time = time.time()
    # print("Content time: " + str((end_time - start_time)) + " s")
    '''
    build_url = URLBuilder(prepared_query).build()
    print(build_url)
    data = rq.get(build_url).content
    soup = BeautifulSoup(data, 'html.parser')
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134"
                      " Safari/537.36"}

    print(soup.prettify())'''
    # extractor = ImageExtractor(must_use_session=True, with_history_enabled=True)
    # for m in range(10):
    #     n_p_q = GoogleSearch().withQuery("cursos hablar en público madrid").withNumberOfResults(
    #         10).withSortByUpdateTime().withSearchingAtDifferentGooglePages(page).withImageParams(image)
    #     nbu = URLBuilder(n_p_q)
    #     # print(nbu.build())
    #     result = extractor.extract_url(nbu)
    #     # pprint(result)
    #     pp.pprint(result.result())
    # s_extractor.printOverallTime()
    # extractor.printOverallTime()

    npqa = GoogleSearch().withQuery("tailandia").withResultsLanguage(lang).withTimeLimit(limit)\
        .withSearchingAtDifferentGooglePages(news)
    print(URLBuilder(npqa).build())
    news_ex = NewsExtractor(with_history_enabled=True, must_use_session=False)
    rs = news_ex.extract_url(URLBuilder(npqa))
    pp.pprint(rs.result())
    '''print(nbu)
    ndata = rq.get(nbu, headers=header).content
    ns = BeautifulSoup(ndata, 'html.parser')
    actual_images = []
    for a in ns.find_all("div", {"class": "rg_meta"}):
        link, image_type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
        if not image_type:
            image_type = "unknown format"
        actual_images.append((link, image_type))
    print(ns.prettify())
    print("There are total: " + str(len(actual_images)) + " images")
    for i, (img_link, img_type) in enumerate(actual_images):
        print("\t- Image link [" + str(i) + "]: " + img_link + "\n\t\t- Image type [" + str(i) + "]: " + img_type)'''


if __name__ == '__main__':
    main()
