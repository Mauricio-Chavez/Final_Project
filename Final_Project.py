import datetime


# 1 para perro #0 Para gato
class Animal:
    def __init__(self, name, age, breed, date, species):
        self.name = name
        self.age = age
        self.breed = breed
        self.date = date
        self.next = None
        self.species = species

class Animal_Queue:
    def __init__(self):
        self.first = None
        self.length = 0
        self.last = None

    def animal_enqueue(self, name, age, breed, species):
        date = datetime.datetime.now()
        new_node = Animal(name, age, breed, date, species)
        if self.first == None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1
        return

    def print_queue(self):
        tem = self.first
        while tem is not None:
            print("-----------------------------------------")
            print(f"Name: {tem.name} Age: {tem.age} Breed: {tem.breed} Date: {tem.date}")
            print("-----------------------------------------")
            tem = tem.next

    def animal_dequeue(self):
        tem = self.first
        if self.first == None:

            return False
        else:
            if self.first == self.last:
                self.first = None
                self.last = None
            else:
                self.first = tem.next
                tem.next = None
            self.length -= 1
        return tem

my_queue_cat = Animal_Queue()
my_queue_dog = Animal_Queue()
selection = 0
des = 0
while True:
    print("\n")
    print("1.-Ingresar un Animalito")
    print("2.-Imprimir los animalitos disponibles")
    print("3.-Adoptar un Animalito")
    print("4.-Salir")
    selection = int(input())
    match selection:
        case 1:
            print("1.-Ingresar un Perrito al sistema")
            print("2.-Ingresar un Gatito al sistema")
            des = int(input())
            match des:
                case 1:
                    name = str(input("Ingresa el nombre del Perrito: \n"))
                    age = int(input("Ingresa la edad del Perrito: \n"))
                    breed = str(input("Ingresa la raza del Perrito: \n"))
                    species = "Perro"
                    my_queue_dog.animal_enqueue(name, age, breed, species)
                case 2:
                    name = str(input("Ingresa el nombre del Gatito: \n"))
                    age = int(input("Ingresa la edad del Gatito: \n"))
                    breed = str(input("Ingresa la raza del Gatito: \n"))
                    species = "Gato"
                    my_queue_cat.animal_enqueue(name, age, breed, species)
        case 2:
            print("1.- Imprimir la lista de Perritos disponibles:")
            print("2.- Imprimir la lista de Gatitos disponibles:")
            print("3.- Imprimir ambas listas:")
            des = int(input())
            match des:
                case 1:
                    if my_queue_dog.first is None:
                        print("No hay Perritos en Adopcion de Momento")
                    else:
                        print("Lista de Perros: ")
                        my_queue_dog.print_queue()
                case 2:
                    if my_queue_cat.first is None:
                        print("No hay Gatitos en Adopcion de Momento")
                    else:
                        print("Lista de Gatos")
                        my_queue_cat.print_queue()
                case 3:
                    if my_queue_dog.first is None and my_queue_cat.first is None:
                        print("1")
                        print("No hay Perritos ni Gatitos en Adopcion de Momento")
                    elif my_queue_dog.first is None:
                        print("2")
                        print("Lista de Gatos")
                        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                        my_queue_cat.print_queue()
                        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                    elif my_queue_cat.first is None:
                        print("3")
                        print("Lista de Perros")
                        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                        my_queue_dog.print_queue()
                        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                    else:
                        print("4")
                        print("Lista de Gatos")
                        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                        my_queue_cat.print_queue()
                        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                        print("\n")
                        print("Lista de Perros")
                        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                        my_queue_dog.print_queue()
                        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        case 3:
            print("\n")
            print("1.-Adoptar un Perrito")
            print("2.-Adoptar un Gatito")
            print("3.-Me es indiferente solo quiero adoptar")
            des = int(input())
            match des:
                case 1:
                    r = my_queue_dog.animal_dequeue()
                    if r == False:
                        print("De momento ya no tenemos mas Perritos en adopcion")
                    else:
                        print("------------------------------------------")
                        print(f"Name: {r.name} Age: {r.age} Breed: {r.breed} Date: {r.date}")
                        print("------------------------------------------")
                case 2:
                    r = my_queue_cat.animal_dequeue()
                    if r == False:
                        print("De momento ya no tenemos mas Gatitos en adopcion")
                    else:
                        print("------------------------------------------")
                        print(f"Name: {r.name} Age: {r.age} Breed: {r.breed} Date: {r.date}")
                        print("------------------------------------------")
                case 3:
                    if my_queue_dog.first is not None and my_queue_cat.first is not None:
                        if my_queue_dog.first.date < my_queue_cat.first.date:
                            r = my_queue_dog.animal_dequeue()
                            print("------------------------------------------")
                            print(f"Name: {r.name} Age: {r.age} Breed: {r.breed} Date: {r.date}")
                            print("------------------------------------------")
                        elif my_queue_dog.first.date > my_queue_cat.first.date:
                            r = my_queue_cat.animal_dequeue()
                            print("------------------------------------------")
                            print(f"Name: {r.name} Age: {r.age} Breed: {r.breed} Date: {r.date}")
                            print("------------------------------------------")
                        else:
                            print("El perro y el gato tienen la misma fecha de adopción")
                    elif my_queue_dog.first is None and my_queue_cat.first is None:
                        print("Ya no contamos con Perritos ni Gatitos para adoptar")
                    elif my_queue_dog.first is None:
                        r = my_queue_cat.animal_dequeue()
                        print("------------------------------------------")
                        print(f"Name: {r.name} Age: {r.age} Breed: {r.breed} Date: {r.date}")
                        print("------------------------------------------")
                    else:
                        r = my_queue_dog.animal_dequeue()
                        print("------------------------------------------")
                        print(f"Name: {r.name} Age: {r.age} Breed: {r.breed} Date: {r.date}")
                        print("------------------------------------------")
        case 4:
            print("Saliendo...")
            exit()
