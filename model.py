import database

class model:

     
    dic = {}

    def getClassName(self):
        return self.__class__.__name__


    def charfield(self,char):
        self.dic[char]= str(char) + " text " 
           


    def intfield(self,num):  
        self.dic[num]= str(num) + " integer "
         

    def decimalfield(self,decimal): 
        self.dic[decimal]= str(decimal) + " decimal "
         


    def createTable(self):
        statement=[]
        for item in self.dic.values():
            statement.append(item)

         
        query = "CREATE TABLE IF NOT EXISTS " +  model.getClassName(self) + " ( " + ', '.join(statement) + ")"
         
        
         
        database.execute(query)
        
    def agregar(self ,**kwargs):

        for item in kwargs.keys():
            if not item in self.dic.keys():
                return print("no se puede realizar operacion, ha escrito mal alguna clave")
            else:
                self.dic[item]=kwargs[item]
        print(self.dic)
        value=[]
        for item in self.dic.values():
            value.append(item)

            
        x=model.getClassName(self)
         
        query="INSERT INTO " + x + " VALUES (" + str(value)[1:-1] + " )"
         
        database.execute(query)