class Node:
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.prev,self.next=None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity

        self.least,self.most=Node(0,0),Node(0,0)
        self.least.next,self.most.prev=self.most,self.least

    def remove(self,node):
        prev,next=node.prev,node.next
        prev.next,next.prev=next,prev


    def insert(self,node):
        prev,next=self.most.prev,self.most
        prev.next=next.prev=node
        node.prev,node.next=prev,next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node=Node(key,value)
        self.insert(node)
        self.cache[key]=node
        if len(self.cache)> self.capacity:
            remove=self.least.next
            next=remove.next
            self.least.next=next
            next.prev=self.least
            del self.cache[remove.key]

                



        
