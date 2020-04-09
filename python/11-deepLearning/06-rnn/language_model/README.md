# language model


* https://github.com/pyliaorachel/resurrecting-the-dead-chinese.git

* [NLP 笔记 - Language models and smoothing](http://www.shuang0420.com/2017/02/24/NLP%20%E7%AC%94%E8%AE%B0%20-%20Language%20models%20and%20smoothing/)

Unknown word

对 unknown word 的处理，一般我们建一个固定大小的 lexicon(比如说语料库里 frequency>5 的单词)，再新建一个 token <UNK>，不在 lexicon 里的 token (也就是 frequency<5 的单词)都编译成 <UNK>，然后把 <UNK> 当做普通单词处理。