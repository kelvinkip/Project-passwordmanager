class Credentials:
   
    
    credentials_list = [] #empty credentials list
    
    def __init__(self,account,username,pass_word):
       
        
        self.account = account
        self.username = username
        self.pass_word = pass_word
        
    def save_credential(self):
       
        
        Credentials.credentials_list.append(self)
        
    def delete_credential(self):
        
        Credentials.credentials_list.remove(self)
        
    @classmethod
    def find_user_by_account(cls, account):
      
        
        for Credentials in cls.credentials_list:
            if Credentials.account == account:
                return Credentials
            
    @classmethod
    def find_credential_exist(cls,account):
      
        
        for Credentials in cls.credentials_list:
            if Credentials.account == account:
                return True
            
        return False
    
    @classmethod
    def display_credentials(cls):
      
        return cls.credentials_list
    