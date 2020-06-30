def aadhar(file):

    import pytesseract
    from PIL import Image
    from pytesseract import image_to_string
    import datetime
    import cv2
    import sys
    import os
    import os.path
    import re
    import numpy as np
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HP\Desktop\ONE-PERSON-ONE-PORTAL\Tesseract-OCR\tesseract'
    TESSDATA_PREFIX = r'C:\Users\HP\Desktop\ONE-PERSON-ONE-PORTAL\Tesseract-OCR'
    class Text_Extractor():
        #Constructor
        def __init__(self,image_file):
            self.image_file=image_file
            if self is None:
                return 0
            
    #Function to extract the text from image as string 
        def extract_text(self): 

            #img=Image.open(self.image_file)
            img = cv2.imread(self.image_file)
            #resize the image
            img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
            #convert the image to gray
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            text=pytesseract.image_to_string(img) 
            return text
        
    #class to validate if  an image is a adhar card where the text is passed as an argument
    class Aadhar_Card_Validator():
        #Constructor
        def __init__(self,text):
            self.text=text
            #print(self.text)
    #Function to validate if an image contains text showing its an aadhar card
        def is_aadhar_card(self):
            res=self.text.split()
            #print(res)
            dates={}  
            aadhar_number=''
            print('Aadhar card details:')
            for word in res:
                
                if len(word) ==12 and word.isdigit():
                    aadhar_number=aadhar_number  + word + ''
                    
                    
            if len(aadhar_number)>=12: 
                #print("It is an aadhar card and the details are:")
                
                    
                for i in range(len(res)):
                    if(res[i]=='Name'):
                        print('Name:',res[i+2]+' '+res[i+3])
                        adfname=res[i+2]
                        adlname=res[i+3]

        

                    
                for i in range(len(res)):
                    if(res[i]=='DOB'):
                        print("DOB:",res[i+2])
                        addob=res[i+2]
                

                print("Aadhar number:"+ aadhar_number)
                return aadhar_number,adfname,adlname,addob
               


                            
            
   
        
        
    image_file_name =file
    te= Text_Extractor(image_file_name)
    text=te.extract_text()
    acv=Aadhar_Card_Validator(text)
    aadhar_number,adfname,adlname,addob= acv.is_aadhar_card()
    return aadhar_number,adfname,adlname,addob




   