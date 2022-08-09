class Transposition:
    def __fragment(self,message,length):
        n = 0
        p = len(message)
        fragList = []
        message = message+("~"*(length-(len(message)%length)))
        while n < p:
            fragList.append(message[n:n+length])
            n += length
        return fragList

    def __swap(self,msg,key):
        tempp = ""
        for i in key:
            tempp += msg[i-1]
        return tempp

    def __deswap(self,encMsg,key):
        decKey = [0]*len(key)
        for i,j in enumerate(key):
            decKey[j-1] = i+1
        return(self.__swap(encMsg,decKey))

    def encrypt(self,message,key):
        msgList = self.__fragment(message,len(key))
        encryptedMsg = ""
        for msg in msgList:
            encryptedMsg += self.__swap(msg,key)
        return encryptedMsg
    
    def decrypt(self,encMessage,key):
        encMsgList = self.__fragment(encMessage,len(key))
        decryptedMsg = ""
        for encMsg in encMsgList:
            decryptedMsg += self.__deswap(encMsg,key)
        for indx in range(len(decryptedMsg)-1,len(decryptedMsg)-len(key),-1):
            if decryptedMsg[indx] != "~":
                break
            else:
                decryptedMsg = decryptedMsg[:indx]
        return decryptedMsg



text = "hello world I dont know what i am doing so that means i am gonnna do all that stuff that you said that i am gonna do and well, Idk"
transposition = Transposition()
key = [2,1,3,6,7,5,4]
print(transposition.encrypt(text,key))
encrypted = transposition.encrypt(text,key)
print(transposition.decrypt(encrypted,key))
print(__name__)
