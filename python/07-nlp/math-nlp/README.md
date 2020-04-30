# 小學數學問題 -- 生成、Parse 與逐字翻譯

## 生成

```
PS D:\ccc\ai\python\07-nlp\math-nlp> python gen_math.py
問題:   小華有11個番茄
        給了小莉2個
        又給了小明5個
        請問小華還有幾個番茄?

答案:   4個
```

## Parse

```
PS D:\ccc\ai\python\07-nlp\math-nlp> python parse_math.py
['小明', '有', '5', '個', '蘋果', '，', '給', '了', '小華', '3', '個', '蘋果', '，', '請問', '他', '還', '剩', '幾', '個', '蘋果', '？']
tag=N word=小明
tag=V word=有
tag=D word=5
tag=d word=個
tag=N word=蘋果
tag=. word=，
tag=V word=給
tag=v word=了
tag=N word=小華
tag=D word=3
tag=d word=個
tag=N word=蘋果
tag=. word=，
tag=Q word=請問
tag=N word=他
tag=v word=還
tag=V word=剩
tag=D word=幾
tag=d word=個
tag=N word=蘋果
tag=. word=？
```

## 逐字翻譯

```
PS D:\ccc\ai\python\07-nlp\math-nlp> python mt_math.py   
中文: ['小明', '有', '5', '個', '蘋果', '，', '給', '了', '小華', '3', '個', 
'蘋果', '，', '請問', '他', '還', '剩', '幾', '個', '蘋果', '？']
tag=N word=小明
tag=V word=有
tag=D word=5
tag=d word=個
tag=N word=蘋果
tag=. word=，
tag=V word=給
tag=v word=了
tag=N word=小華
tag=D word=3
tag=d word=個
tag=N word=蘋果
tag=. word=，
tag=Q word=請問
tag=N word=他
tag=v word=還
tag=V word=剩
tag=D word=幾
tag=d word=個
tag=N word=蘋果
tag=. word=？
英文： ['ShaoMin', 'have', '5', '_', 'apple', '，', 'give', '_', 'ShaoHua', '3', '_', 'apple', '，', 'Q', 'he', 'still', 'own', 'n?', '_', 'apple', '_.'] 
```

