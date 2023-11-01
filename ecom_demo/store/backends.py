from django.contrib.auth.models import User 
from store.models import user_info  # custom user authentication
 
class MyBackEnd(object): 
    """ 
    This is the custom backend to authenticate the user in the DB. 
    if this authentication fais then django default authentication  will get called 
    """ 
 
    def authenticate(self, email, password):   # get the user credentils
        """ :parameter email: email of the user  
            :parameter password: Password of the user 
            :return: 
        """ 
        #check is user is present in User DB. 
        existing_user = User.objects.get(email=email) # getting the info from db if the user is already exis or not  
        if not existing_user:       # condition for is the user is exis or not 
            #Checking the user UserData Custom DB. 
            user_data = user_info.objects.get(email=email,password=password) # quering the database if the user data from the db
            print("...%s...." % user_data) 
            if email == user_data.email and password == user_data.password: # to check the user name and password are correct or not 
                user =  User.objects.create_user(email=email,password=password) #if that credtntials are true create the user secction
                user.save()                 #save the user credentials
                return user                # return user cred to the frontend
            else: 
                print("user email or password is incorrect ")
                return None #if the user credential are wrong then return none 
        else: 
            return existing_user #
    
    def get_user(self, email,password): # this is get the user part not authenticating  if the user is exist the return user or return none
        try: 
            return User.objects.get(email=email,password=password) 
        except User.DoesNotExist: 
            print("get user gives error the user is not authenticated ")
            return None 