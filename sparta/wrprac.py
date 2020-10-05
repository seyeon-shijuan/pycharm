#파일 쓰기
f = open("test.txt", "w", encoding="utf-8")
for i in [1,2,3,4,5]:
    f.write(f"{i}번째 줄이에요\n")

f.close()

#파일 읽기
text=''
with open("lloyd.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[4:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('카카오톡 봇','').replace('이모티콘','').replace('있는','')
print(text)

import matplotlib.font_manager as fm

# 이용 가능한 폰트 중 '고딕'만 선별
for font in fm.fontManager.ttflist:
    if 'Gothic' in font.name:
        print(font.name, font.fname)

#C:\WINDOWS\Fonts\NanumGothicExtraBold.ttf

from wordcloud import WordCloud

wc = WordCloud(font_path='C:/WINDOWS/Fonts/NanumGothicExtraBold.ttf', background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")

from PIL import Image
import numpy as np

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/WINDOWS/Fonts/NanumGothicExtraBold.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")