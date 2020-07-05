学习笔记

HashMap 一个很常见的概念,在学习
中有很多别名,散列,哈希,杂凑...说的都是一种东西=。=

Python中dict字典就是由HashMap来实现的,在py3.6以后字典有序切速度提高了25%

cpython/Objects/dict-common.h

typedef struct {
    /* Cached hash code of me_key. */
    Py_hash_t me_hash;
    PyObject *me_key;
    PyObject *me_value; /* This field is only meaningful for combined tables */
    这里是核心结构体,dict存储来每一对key-value
    
#### 字典类型

字典分为联合字典和分离字典

分离字典用来保存object的__dict__属性时才会创建联合字典

联合字典,使用dict内建函数和 {} 生产的字典统称,模块和大部分其他字典都是联合字典

#### 字典容量

python-dict最佳容量在1/2到2/3之间，超过限度会自动扩容

看到一篇文章写的不错:

https://blog.csdn.net/qq_33339479/article/details/90446988

一行java都没写过哭...看了看python


心得体会:

这周事情也不少,周末的leetcode又没打,上周因为调休,第二周因为女朋友有事情

刷题在超哥第一次直播以后开始拿出小本子开始进行leetcode五毒神掌的练习

感觉五遍有一点少,打算7遍先试试,如果有余力尝试一下九遍

现在平均每天2-3个新题...但愿新题目不会太少


