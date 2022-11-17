#for example you had completed your 10th class and you are applying for job.so, you need a resume. 
#so, first we will go with creating 10th class resume.
#here i am using multilevel inheritance concept.
class Resume_10th:
        #tpercent==10th percentage
        #tyop==10th_year_of_passedout
        #splace==school_place
    qualification="10"
    def __init__(self,name,phone_number,email,tpercent,tyop,tschool,splace):
        self.name=name
        self.phone_number=phone_number
        self.email=email
        self.tpercent=tpercent
        self.tyop=tyop
        self.tschool=tschool
        self.splace=splace

        #to display all details in 10th class details.
    def disp(self):
        print(self.name,self.phone_number,self.email,self.tpercent,self.tyop,self.tschool,self.splace)

        #in case to modify the phone number of the student.
    def change_phone_number(self,new_number):
        self.phone_number=new_number

        #in case to modify the email of the student.
    def change_email(self,new_email):
        self.email=new_email

        #remaining all properties are fixed, they can't be changed.
#so, upto here we created the 10th class resume.
#---------------------------------------------------------------------------------------------------------
#if you want to create a resume which includes intermediate details.  
class Resume_inter(Resume_10th):
    qualification="Intermediate"

    #iyop=intermediate_year_of_passedout
    #ipercent=intermediate_percentage
    #iplace=Intermediate_college_place
    def __init__(self,name,phone_number,email,tpercent,tyop,tschool,splace,ipercent,iyop,ischool,iplace):
        super().__init__(name,phone_number,email,tpercent,tyop,tschool,splace)
        self.ipercent=ipercent
        self.iyop=iyop
        self.iplace=iplace
        self.ischool=ischool

     #to display all details from 10th to intermediate.
    def disp(self):
        super().disp()
        print(self.ipercent,self.iyop,self.iplace,self.ischool)

#so, upto here we created resume which includes both 10th and intermediate details.
#---------------------------------------------------------------------------------------------------------
#if we want to create a resumme which includes graduation details for example BTech details.
class Resume_BE(Resume_inter):
    qualification='BTech'

    def __init__(self,name,phone_number,email,tpercent,tyop,tschool,splace,ipercent,iyop,ischool,iplace,bebranch,becollege,beplace,bepercent):
        super().__init__(name,phone_number,email,tpercent,tyop,tschool,splace,ipercent,iyop,ischool,iplace)
        self.bebranch=bebranch
        self.becollege=becollege
        self.beplace=beplace
        self.bepercent=bepercent

    def disp(self):
        super().disp()
        print(self.bebranch,self.becollege,self.beplace,self.bepercent)

#we are done with creating resume upto graduation 
#----------------------------------------------------------------------------------------------------------------------------------------------
#now enter details to print resume details by creating a student 

krishna=Resume_BE('krishna',9988774455,'k123@gmail.com',95,2016,'kkrschool','rajahmundry',97.9,2018,'sasi jr college','nidadavole','mechanical','VIT','vellore','79.4')
Resume_BE.disp(krishna)
#output: krishna 9988774455 k123@gmail.com 95 2016 kkrschool rajahmundry,97.9 2018 nidadavole sasi jr college,mechanical VIT vellore 79.4