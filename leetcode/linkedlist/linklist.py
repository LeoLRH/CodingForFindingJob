"""
linklist.py
功能: 实现单链表的构建和操作
重点代码
"""

# 创建节点类
class Node(object):
    """
    链表的节点
    思路 : *自定义类视为节点类,类中的属性为数据内容
          *写一个next属性,用来和下一个 节点建立关系
    """
    def __init__(self, elem):
        """
             val: 有用数据
                next: 下一个节点引用
        """
        self.elem = elem
        self.next = None

class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None

class SingleLinkList(object):
    """
        单链表
        通过实例化的对象就代表一个链表,可以调用具体的操作方法完成各种功能
    """
    def __init__(self):
        self._head = None

    def is_empty(self):
        """
        判断链表是否为空
        :return:True/False
        """
        return self._head == None

    def length(self):
        """
        链表的长度
        :return:链表的长度
        """
        # cur初始时指向头节点
        cur = self._head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """
        遍历链表
        :return: 整个链表按照顺序输出
        """
        cur = self._head
        while cur != None:
            print (cur.item,)
            cur = cur.next
        print ("")

    def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self._head
        # 将链表的头_head指向新节点
        self._head = node

    def append(self, item):
        """
            链表的尾部添加元素，尾插法
            :param item: 要添加的元素
            :return:
        """
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """
            指定位置添加元素
            :param pos:指定的位置
            :param item:要添加的元素
            return:
        """
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(item)
        # 找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def search(self, item):
        """
              在链表查找节点是否存在，并返回True或者False
              :param item:查找的节点值
              :return:True/False
        """
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def remove(self,item):
        """
            删除节点
            :param item:要删除的元素
            :return:
        """
        cur = self._head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    print ("length:",ll.length())
    ll.travel()
    print (ll.search(3))
    print (ll.search(5))
    ll.remove(1)
    print ("length:",ll.length())
    ll.travel()









if __name__ == '__main__':

    # 实例化链表
    ll = SingleLinkList()

    # 判断链表是否为空
    print(ll.is_empty())

    # 链表的长度
    print(ll.length())

    # 在链表的尾部添加节点 1
    ll.append(1)
    ll.travel()

    # 在链表的头添加节点 0
    ll.add(0)
    ll.travel()

    # 链表添加节点
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travel()
    print(ll.length())

    # 插入的位置为-1 因此使用头插法
    ll.insert(-1, 999)  # 999 0 1 2 3 4 5 6
    ll.travel()

    # 在位置2插入100
    ll.insert(2, 100)  # 999 0 1 100 2 3 4 5 6
    ll.travel()

    # 插入的位置为10 因此使用尾插法
    ll.insert(10, 200)  # 999 0 1 100 2 3 4 5 6 200
    ll.travel()

    # 移除第一个200的元素
    ll.remove(200)
    ll.travel()

    # 移除第一个999的元素
    ll.remove(999)
    ll.travel()



