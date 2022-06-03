class Student:

    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks 
        self.score = score
    def change.name(self, new_name):
        self.name = new_name
        print(f"change name to (new_name)")
        
    def change.name(self, new_age):
        try:
            new_age = int(new_age)
            except:
                Print("Failed to change age. Invalid data type")
                 raise Exception
     self.age = new_age
    print(f"changed to [new_age]")
    
    def add.tracks(self, new_track)
        self.tracks. append(new_track)
        print(f"added new track")
        
    def get_score(self):
        retrun self.score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

Bob.change_age("yes")

# Expected methods
Bob.change_name("Peter") 
Bob.change_age(34)
Bob.add_track("UI/UX")
Print(Bob.get_score())
