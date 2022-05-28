#class for student
class Student:
    

        
    def __init__(self,name,age,tracks,score):
        
        #instance variable
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)


    def change_name(self,new_name):
        self.name =new_name
        #return self.name
        print(new_name)
    
    def change_age(self, new_age):
        self.age = int(new_age)
       #return self.age
        print(new_age)
        
    def add_track(self,new_tracks):
        self.track = new_tracks
        #return self.track
        print(new_tracks)

    def get_score(self,score):
        #return self.score
        print(score)
    


#objects for student class
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

print('Student details:')  
print('Name', Bob.name)
print('Age', Bob.age)
print('Tracks: ', Bob.tracks)
print('Score: ', Bob.score)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score("2.5")

