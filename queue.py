# -*- coding=utf-8 -*-
class Queue(object):
    """队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
#出队列及入队列操作总要有一个是O(n)一个是O(1)，所以根据出入的操作多少来选择
    def enqueue(self, item):
        """进队列"""
        #self.items.append(item)#O(1)
        self.items.insert(0,item)#O(n)头部添加

    def dequeue(self):
        """出队列"""
        #return self.items.pop(0)#O(n)
        return self.items.pop()#O(1)尾部删除

    def size(self):
        """返回大小"""
        return len(self.items)

if __name__ == "__main__":
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("itcast")
    print (q.size())
    print (q.dequeue())
    print (q.dequeue())
    print (q.dequeue())