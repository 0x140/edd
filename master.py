#!bin/python3

'''
Created by @Edwin,on Sunday , Sept 29.

A class for teacher object.The class is initialized with four properties:name,identity number,contacts and the subjects taught.

'''

class teacher:
		
		attrsList = ['name' , '_id' , ' contacts' , 'subjects_taught' ]
		
		def __init__(self, name , _id , contacts , subject_taught):
				self.name = name
				self._id = _id
				self.contacts = contacts
				self.subject_taught = subject_taught
				
		def __repr__(self):
				return "teacher('{} ',' {}','{}','{}')".format(self.name , self._id,self.contacts,self.subject_taught)
				
		def __str__(self):
				return "Name : {}\nID No. - {}\nContact Details - {}\nSubject-taught : {}\n".format(self.name , self._id , self.contacts , self.subject_taught)
				
		def set_working_hours(self):
				pass
				
		def add_field_and_value(self, attr , value):
				self.attr = attr
				
				if self.attr in self.attrsList:
						print("{} is already there!".format(self.attr))
				else:
						self.attrsList.append('{}'.format(self.attr))
						return self.attr == value

		@classmethod		
		def update(cls,*args,**kwargs):
				
				pass
			


teacher_1 = teacher('Koimet','19/03006','0718207112','Physics')
print('The repr-dunder method is used for debugging and '
			'counterchecking errors. Mostly used by developers.')
print('###Results after using the __repr__')
print( )
print(repr(teacher_1))
print('=====================+++===================')
print('The str-dunder method is used for displaying user-friendly'
			' results for the end user. Used by end-users. ')
print('###Results after using the __str__')
print('=====================+++===================')
print(teacher_1)
print('=====================+++===================')

print(teacher_1.__dict__)
print( )
teacher_1.add_field_and_value('age','45')
print(teacher_1.__dict__)
