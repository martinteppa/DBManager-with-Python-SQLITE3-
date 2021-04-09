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
         
        
         
        database.exxecute(query)
        
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

         
         
        query="INSERT INTO " + model.getClassName(self) + " VALUES (" + str(value)[1:-1] + " )"
         
        database.exxecute(query)

    def eliminar(self, id):

        try:
            query = "DELETE FROM " +   model.getClassName(self) + " WHERE rowid = " + str(id)
        except:
            print("no hay item con ese id")      

        database.exxecute(query)    

    def actualizar(self, id, **kwargs):
        
        query="SELECT * FROM " + model.getClassName(self) + " WHERE rowid = " + str(id)
        valor = database.buscar(query)
         
        cont = 0
        for elem in self.dic.keys():
            self.dic[elem]=valor[0][cont]
            cont+=1
        print(self.dic)

        cont = []
        for item in kwargs.keys():
            if item in self.dic.keys() :
                self.dic[item] = kwargs[item]

                if self.dic[item] == str(self.dic[item]):
                    cont.append(item + " = '" +  str(self.dic[item]) + "'" )
                else:
                    cont.append(item + " = " +  str(self.dic[item]) )
        print(cont)
        print(', '.join(cont))

        query="UPDATE " + model.getClassName(self) + " SET " + ', '.join(cont) + " WHERE rowid = " + str(id)
        database.exxecute(query) 
     