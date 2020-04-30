# 語言處理

## jieba1.py

```
PS D:\ccc\ai\python\07-nlp> python jieba1.py 
Building prefix dict from the default dictionary ...
Dumping model to file cache C:\Users\Tim\AppData\Local\Temp\jieba.cache      
Loading model cost 2.671 seconds.
Prefix dict has been built successfully.
Default Mode: 我/ 来到/ 北京/ 清华大学
```

## e2c.py

```
PS D:\ccc\ai\python\07-nlp> python e2c.py a dog chase a cat
['一隻', '狗', '追', '一隻', '貓']
```

## gen_english

```
PS D:\ccc\ai\python\07-nlp> python gen_english1.py
a cat eat a cat
PS D:\ccc\ai\python\07-nlp> python gen_english1.py
the dog chase the dog
```

## gen_exp1.py

```
PS D:\ccc\ai\python\07-nlp> python gen_exp1.py    
7 = 7
PS D:\ccc\ai\python\07-nlp> python gen_exp1.py
6-7/2 = 2.5
PS D:\ccc\ai\python\07-nlp> python gen_exp1.py
3 = 3
PS D:\ccc\ai\python\07-nlp> python gen_exp1.py
7-2+8+6+2/1-6-7+8+5/9/4+3+6 = 25.13888888888889
PS D:\ccc\ai\python\07-nlp> python gen_exp1.py
4/2 = 2.0
```

## pgen_english.py

```
PS D:\ccc\ai\python\07-nlp> python pgen_english.py
['the', 'cat', 'eat', 'the', 'cat'] 0.049000
['a', 'cat', 'chase', 'the', 'dog'] 0.031500
['the', 'dog', 'chase', 'the', 'cat'] 0.031500
['the', 'cat', 'chase', 'a', 'dog'] 0.031500
['the', 'cat', 'eat', 'the', 'dog'] 0.021000
['a', 'dog', 'chase', 'the', 'dog'] 0.013500
['a', 'cat', 'chase', 'a', 'cat'] 0.073500
['a', 'cat', 'eat', 'a', 'dog'] 0.021000
['a', 'cat', 'chase', 'a', 'dog'] 0.031500
['the', 'cat', 'eat', 'a', 'dog'] 0.021000
```

## eliza.py

```
PS D:\ccc\ai\python\07-nlp> python eliza.py
你好，我是 Eliza ! 
> 你是誰
你認為我是誰?
> 我不知道
為何不知道?
> 你很有名嗎?
你真的是在說我嗎?
> 對阿
我了解!
> 了解甚麼?
我能理解
> 理解甚麼?
接下來呢? 
> 你有聽懂嗎?
不要再說我了，談談你吧!
> 我?
再來呢? 可以多說一些嗎
> 我不想說了
為何不想說了?
> 因為你說話很奇怪
不要再說我了，談談你吧!
> bye
```

## 自然語言

* http://www.nltk.org/
* https://pypi.org/project/gensim/

## 文章


* http://zake7749.github.io/
    * https://github.com/zake7749
    * [以 gensim 訓練中文詞向量](http://zake7749.github.io/2016/08/28/word2vec-with-gensim/)
    * [聊天機器人的開發思路](http://zake7749.github.io/2016/12/17/how-to-develop-chatbot/)
    * [基於詞向量的主題匹配](http://zake7749.github.io/2016/08/30/chatterbot-with-word2vec/)
    * [從零開始的 Sequence to Sequence](http://zake7749.github.io/2017/09/28/Sequence-to-Sequence-tutorial/)

* [word2vec词向量中文语料处理(python gensim word2vec总结）](https://blog.csdn.net/shuihupo/article/details/85162237)

## 專案

* https://github.com/LasseRegin/gensim-word2vec-model
* https://github.com/MiguelSteph/word2vec-with-gensim
    * http://migsena.com/build-and-visualize-word2vec-model-on-amazon-reviews/