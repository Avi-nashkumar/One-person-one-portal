def ab(file):




    import pytesseract
    from PIL import Image
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
    class Pan_Card_Validator():
        #Constructor
        def __init__(self,text):
            self.text=text
            #print(self.text)
    #Function to validate if an image contains text showing its an aadhar card
        def is_pan_card(self):
            res=self.text.split()
            #print(res)
            dates={}  
            pan_number=''
            print('Pan card details:')
        
                
            for i in range(len(res)):
                if(res[i]=='Number'):
                    print('Pan Number:',res[i+1])
                    panno=res[i+1]
                
        #if len(aadhar_number)>=12: 
            #print("It is an aadhar card and the details are:")
            
                
            for i in range(len(res)):
                if(res[i]=='Name'):
                    print('Name:',res[i+1]+' '+res[i+2])
                    panfname=res[i+1]
                    panlname=res[i+2]


                
            for i in range(len(res)):
                if(res[i]=='DOB'):
                    print("DOB:",res[i+1])
                    pandob=res[i+1]

            
            return panno,panfname,panlname,pandob
        
                
                





    
        
    '''if len(sys.argv) != 2:
        print ("Wrong number of arguments")
        sys.exit(1)'''
    image_file_name =file
    
    te= Text_Extractor(image_file_name)
    text=te.extract_text()
    acv=Pan_Card_Validator(text)
    panno,panfname,panlname,pandob=acv.is_pan_card()
    return panno,panfname,panlname,pandob
        
  
