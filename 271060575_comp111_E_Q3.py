from abc import ABC,abstractmethod
class Document(ABC):
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def save_file(self):
        pass
class Word_doc(Document):
    def __init__(self,file_name,file_size,content):
        self.file_name = file_name
        self.file_size = file_size
        self.content = content
    def open(self):
        print(f"file {self.file_name} has been opened as word document")
    def read(self):
        print(f"the content of the file is : ")
        print(f"{self.content}")
    def save_file(self):
        print(f"file of size {self.file_size} has been saved as word document ")           
class Pdf_doc(Document):
    def __init__(self,file_name,file_size,content):
        self.file_name = file_name
        self.file_size = file_size
        self.content = content
    def open(self):
        print(f"file {self.file_name} has been opened as pdf document")
    def read(self):
        print(f"the content of the file is : ")
        print(f"{self.content}")
    def save_file(self):
        print(f"file of size {self.file_size} has been saved as pdf document ")   
class Excel_doc(Document):
    def __init__(self,file_name,file_size,content):
        self.file_name = file_name
        self.file_size = file_size
        self.content = content
    def open(self):
        print(f"file {self.file_name} has been opened as Excel document")
    def read(self):
        print(f"the content of the file is : ")
        print(f"{self.content}")
    def save_file(self):
        print(f"file of size {self.file_size} has been saved as Excel document ")     
class Document_factory(ABC):
    @abstractmethod
    def create_doc(self):
        pass
class Word_doc_factory(Document_factory):
    def create_doc(self):
        name_input = str(input("enter the name of the word file : "))
        content_input = str(input("enter the content of the  word file :"))
        size_input = str(input("enter the size of the word file : "))
        return Word_doc(name_input,size_input,content_input)              
class Pdf_doc_factory(Document_factory):
    def create_doc(self):
        name_input = str(input("enter the name of the pdf file : "))
        content_input = str(input("enter the content of the  pdf file :"))
        size_input = str(input("enter the size of the pdf file : "))
        return Pdf_doc(name_input,size_input,content_input)     
class Excel_doc_factory(Document_factory):
    def create_doc(self):
        name_input = str(input("enter the name of the excel file : "))
        content_input = str(input("enter the content of the  excel file :"))
        size_input = str(input("enter the size of the excel file : "))
        return Excel_doc(name_input,size_input,content_input)  
def read_factory():
    doc_dict = {
        "word" : Word_doc_factory(),
        "pdf" : Pdf_doc_factory(),
        "excel": Excel_doc_factory()
    }
    print("the following docs are available: ")
    print("word,excel and pdf")
    while True:
        doc_decided = str(input("which doc do you want: "))
        if doc_decided in doc_dict:
            return doc_dict[doc_decided]
        else:
            print("invalid doc type.please try again ")
if __name__ == "__main__":
    doc_var = read_factory()
    new_var = doc_var.create_doc()
    new_var.open()
    new_var.read()
    new_var.save_file()


            