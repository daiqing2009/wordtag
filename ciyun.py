import matplotlib.pyplot as plt #数据可视化
import jieba #词语切割
import wordcloud #分词
from wordcloud import WordCloud,ImageColorGenerator #词云，颜色生成器，停止词
import numpy as np #科学计算
from PIL import Image #处理图片
import os

def read_stopword(fpath):
    # 读取中文停用词表
    with open(fpath, 'r', encoding='utf-8') as file:
        stopword = file.readlines()
    return [word.replace('\n', '') for word in stopword]
path='./stopwords'
name_list = ['baidu_stopwords.txt', 'cn_stopwords.txt', 'hit_stopwords.txt', 'scu_stopwords.txt']

stop_word = ["上帝","耶稣基督","耶稣","基督","事"]
for fname in name_list:
    stop_word += read_stopword(os.path.join(path, fname))
stop_word = set(stop_word)

def ciyun(): 
    # print(STOPWORDS)
    with open('data/腓利比书和合本2010.txt','r',encoding='utf-8') as f:  #打开新的文本转码为gbk
        textfile= f.read()  #读取文本内容
    wordlist = jieba.lcut(textfile)#切割词语
    space_list = ' '.join(wordlist) #空格链接词语
    # print(space_list)
    backgroud = np.array(Image.open('data\heart.png')) 
	
    wc = WordCloud(width=1400, height=2200,
			background_color='white',
	        mode='RGB', 
			mask=backgroud, #添加蒙版，生成指定形状的词云，并且词云图的颜色可从蒙版里提取
			max_words=500,
			stopwords=stop_word,#内置的屏蔽词,并添加自己设置的词语
			font_path='C:\Windows\Fonts\STZHONGS.ttf',
			max_font_size=150,
			relative_scaling=0.6, #设置字体大小与词频的关联程度为0.4
			random_state=50, 
			scale=2 
			).generate(space_list) 

    image_color = ImageColorGenerator(backgroud)#设置生成词云的颜色，如去掉这两行则字体为默认颜色
    wc.recolor(color_func=image_color)
	
    plt.imshow(wc) #显示词云
    plt.axis('off') #关闭x,y轴
    plt.show()#显示
    wc.to_file('target/test1_ciyun.jpg') #保存词云图

def main():
    ciyun()
 
if __name__ == '__main__':
    main()