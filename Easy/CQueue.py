'''
    剑指 09. 用两个栈实现队列
'''

class CQueue:
    """
        用两个栈实现队列

        Attributes:
            stack1: 第一个栈用于存储元素（栈顺序）
            stack2: 第二个栈用于输出元素（队列顺序）
    """

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail(self, value: int) -> None:
        self.stack1.append(value)


    def deleteHead(self) -> int:
        """
            输出队首元素

            如果stack2有元素，就输出最后的元素
            否则将stack1的元素压入stack2再输出

            Returns:
                队首元素，int
                如果无元素，则输出-1
        """
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return -1
        return self.stack2.pop()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()