# --------------------------------------------------------------------------------------------------
# Scraping HTML Data with BeautifulSoup
# --------------------------------------------------------------------------------------------------

# from typing import Collection
# import urllib.request, urllib.parse, urllib.error, urllib.response
# from bs4 import BeautifulSoup

# import collections
# collections.Callable = collections.abc.Callable

# # Ignore SSL certificate errors

# # ctx = ssl.create_default_context()
# # ctx.check_hostname = False
# # ctx.verify_mode = ssl.CERT_NONE

# urlInput = input("Enter url: ")

# url = urllib.request.urlopen(urlInput).read()
# soup = BeautifulSoup(url, "html.parser")

# tags = soup('span')

# veces = int()
# suma = int()

# for tag in tags:
#     suma += int(tag.string)
#     veces += 1

# print("Enter - " + str(urlInput))
# print("Count", veces)
# print("Sum", suma)

# --------------------------------------------------------------------------------------------------
# Following Links in HTML using BeautifulSoup
# --------------------------------------------------------------------------------------------------

# import urllib.request, urllib.parse, urllib.error, urllib.response
# from bs4 import BeautifulSoup
# import collections
# collections.Callable = collections.abc.Callable

# inputURL = input("Enter URL: ")
# count = input("Enter count: ")
# pos = int(input("Enter position: ")) - 1

# newURL = str()

# for veces in range(int(count)):
#     if veces <1:
#         url = urllib.request.urlopen(inputURL).read()
#         soup = BeautifulSoup(url, "html.parser")
#     else:
#         try:
#             url = urllib.request.urlopen(newURL).read()
#             soup = BeautifulSoup(url, "html.parser")
#         except:
#             continue
   
#     tags = soup("a")
#     temporalCount = 0

#     for tag in tags:
#         if temporalCount == pos:
#             if veces == 0:
#                 print("Retrieving:", inputURL)
#             newURL = tag.get("href")
#             print("Retrieving:",tag.get("href"))
#         temporalCount += 1
#     veces += 1

# --------------------------------------------------------------------------------------------------
# Following Links in HTML using BeautifulSoup
# --------------------------------------------------------------------------------------------------

