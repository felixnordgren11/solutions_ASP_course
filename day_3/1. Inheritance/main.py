from classroom import Person, Student, Teacher





def main():
    me = Student("Felix", "Nordgren", "Materials Chemistry")
    print(me.printNameSubject()) # prints name and subject for inherited class Student
    


if __name__ == "__main__":
    main()