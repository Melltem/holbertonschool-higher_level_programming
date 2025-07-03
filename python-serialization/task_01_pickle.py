import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        # Print the attributes
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        # Save the object to a file using pickle
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception as e:
            print("Error during serialization:", e)

    @classmethod
    def deserialize(cls, filename):
        # Load the object from the file using pickle
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            print("Error during deserialization:", e)
            return None
