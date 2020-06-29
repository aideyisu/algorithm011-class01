// 基于示范代码,使用官网给出的API进行修改

Deque<String> TestDeque = new LinkedList<String>();

// add first 或者 add last
TestDeque.addFirst("a");
TestDeque.addLast("b");
TestDeque.addLast("c");
System.out.println(TestDeque);

String str = TestDeque.peekFirst();
System.out.println(str);
System.out.println(TestDeque);

// 弹出所有元素
while (TestDeque.size() > 0) {
    System.out.println(TestDeque.removeFirst());
}

System.out.println(TestDeque);