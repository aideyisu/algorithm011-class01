准备工作 & 计划
课件中直接给出了链接非常友好
QAQ从没看过java代码的我就这么上路了!

leetcode完成的话比较容易，先把这种分析类的作业搞定

#### 计划:

从比较简单的Queue开始，PriorityQueue随后看

## 正式开始

### Queue

#### 文档部分

首先看起来比较简单的样子，只有入队，出队，检查三种操作。以及这三种操作有两种形式，返回特殊值和失败引发异常

队列通常但不一定以FIFO(先进先出)的方式对元素进行排序。
例外情况时优先级队列 和 LIFO队列(或堆栈)，

可以知道Queue继承了Collection
最好不要把null插入到队列Queue中

#### 源码

源码非常简单暴力

只有6行方法的定义=。=好少的代码好多的模板化解释...Otz

### Priority Queue

#### 文档部分

基于优先级堆的无界限优先级队列=。=优先级队列中的元素根据自然顺序进行排序(基于权重)

所以优先级队列中不可以插入无法比较的对象

优先级队列也是无界限的，内部有容量来控制队列上存储元素数组的大小。总是和队列一样大，添加元素时，容量会自动增长。

#### 源码

源码版本为jdk8

一上来最奇怪的是有一个

```java
private static final long serialVersionUID = -7720805057305804111L;	
```

经过查询是继承自Serializable，用于java对象的序列化和反序列化

貌似是基于编译的产物，类的serialVersionUID的默认值完全依赖于Java编译器的实现，对于同一个类，用不同的Java编译器编译，也有可能会导致不同的serialVersionUID。所以 ide 才会提示声明 serialVersionUID 的值。

在初始化的时候默认存储容量会设定为11

```java
private static final int DEFAULT_INITIAL_CAPACITY = 11;	
```

优先级队列被平衡的二进制堆实现

甚至还有一个modCount用于基于被修改过的次数

```java
transient int modCount = 0;
```

此外还有存储元素的队列

```java
transient Object[] queue;
```

元素个数

```java
/**
* The number of elements in the priority queue.
*/
private int size = 0;
```

随后逐一定义各种情况下的构造函数，

没想到add 会 直接 return offer 的结果=。=

同样offer先判断元素是不是空，不为空就插入队列中

第二个是peek，取出首元素

```java
    @SuppressWarnings("unchecked")
    public E peek() {
        return (size == 0) ? null : (E) queue[0];
    }
```

好久没有见过这种 ? : 表达式了！不容易不容易，自己几乎就没这么写过Otz，端午节假期趁机好好研究一下

第三个出现的使用函数是出队 remove

逻辑为先判断是否存在于队列中，若存在移除并返回true，否则返回false

第四个是contains

```java
public boolean contains(Object o) {
    return indexOf(o) != -1;
}
```

这就是功能最小化的优势么！直接一行解决了问题

第四个 toArray 主功能调用了Arrays.copyOf(queue, size);

第五个这里还有一个独单的迭代器～

```java
    public Iterator<E> iterator() {
        return new Itr();
    }
```

第六位是 clear 清空队列

```java
/**
* Removes all of the elements from this priority queue.
* The queue will be empty after this call returns.
*/
public void clear() {
    modCount++;
    for (int i = 0; i < size; i++)
        queue[i] = null;
    size = 0;
}
```

第一次这么仔细阅读源码！

没想到还有这么朴实无华的函数QAQ！ 要是我可能都不好意思这么写=。=面子信息作祟，真的是朴实无华，学习了

第六个 is 比较器

```java
public Comparator<? super E> comparator() {
    return comparator;
}
```

朴实无华

最后一个是分离器

```java
public final Spliterator<E> spliterator() {
    return new PriorityQueueSpliterator<E>(this, 0, -1, 0);
}
```

貌似是一个公共接口，用于便利和划分源元素的对象=。= 可以单独遍历元素也可以顺序遍历元素

第一次慢慢看了大部分源码，开心