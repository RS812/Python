f=open("file1.txt","r")
def counter(fname):
 
    num_words = 0
     
    num_digits = 0
    
    num_charc = 0
  
    num_symbols = 0
    
    with open(fname, 'r') as f:
   
        for i  in range(len (string)):
         
            num_digits += 1
            word = 'Y'
             
            for letter in line:
              
                if (letter != ' ' and word == 'Y'):
                    
                    num_words += 1
                    
                    word = 'N'
              
                elif (letter == ' '):
                    
                    num_symbols += 1
                    
                    word = 'Y'
                 
                for i in letter:
                     
                    if(i !=" " and i !="\n"):
                         
                        num_charc += 1
   
    print("Number of words in text file: ",
          num_words)
    
    print("Number of digits in text file: ",
          num_digits)
     
    print('Number of characters in text file: ',
          num_charc)
     
    print('Number of symbols in text file: ',
          num_symbols)

if __name__ == '__main__':
    fname = 'file1.txt'
    try:
        counter(fname)
    except:
        print('File not found')
