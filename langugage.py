from langdetect import detect_langs
while True:
    a=input('%:')
    print(detect_langs(a))