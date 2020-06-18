# -*- coding=utf-8 -*-
#二叉树

class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild
class Tree(object):
    """树类"""
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        #如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            #对已有的节点进行层次遍历
            while queue:
                #弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    #如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)
    
    def breadth_travel(self):
        """利用队列实现树的层次遍历"""
        if self.root == None:
            return
        queue = []
        queue.append(self.root)
        while queue:
            node = queue.pop(0)
            print (node.elem)
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)

    #递归实现先序遍历
    def preorder(self, node):
        #根节点为空或者叶节点，直接return
        if node is None:
            return
        print (node.elem)
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    #"""递归实现中序遍历"""
    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.lchild)
        print (node.elem)
        self.inorder(node.rchild)

    #"""递归实现后续遍历"""
    def postorder(self, node):
        if node == None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print (node.elem)

if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.breadth_travel()
    tree.preorder(tree.root)
    tree.inorder(tree.root)
    tree.postorder(tree.root)
