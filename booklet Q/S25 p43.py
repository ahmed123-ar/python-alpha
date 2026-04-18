class Node :

    # PRIVATE TheData : INTEGER
    # PRIVATE NextNode : Node


    def __init__(self , data):
        self.__TheData  = data
        self.__NextNode = None

    def GetData(self) :
        return self.__TheData

    def GetNextNode(self) :
        return self.__NextNode    
    
    def SetNextNode(self , obj) :
        self.__NextNode = obj

class LinkedList :

    # PRIVATE HeadNode : Node

    def __init__(self):
        self.__HeadNode = None

    def InsertNode(self , integer) :
        New_Node = Node(integer) 
        New_Node.SetNextNode(self.__HeadNode)
        self.__HeadNode = New_Node

    def Traverse(self) :  
        string = ""
        start = self.__HeadNode
        while start != None :
            data = start.GetData()
            string = string + "  "  + str( data)
            start = start.GetNextNode()
        return string    

    def RemoveNode(self , integer) : 
        found = False       
        if self.__HeadNode == None :
            return False
        elif integer == self.__HeadNode.GetData() :
            return True
        currentNode = self.__HeadNode
        while currentNode != None and found == False :
            if currentNode.GetNextNode().GetData() == integer :
                currentNode.SetNextNode(currentNode.GetNextNode().GetNextNode())
                found = True
            else :
                currentNode = currentNode.GetNextNode()    


new = LinkedList()
new.InsertNode(10)
new.InsertNode(20)
new.InsertNode(30)
new.InsertNode(40)
new.InsertNode(50)
print(new.Traverse())
new.RemoveNode(30)
print(new.Traverse())


        