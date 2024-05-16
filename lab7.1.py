class Ajilchin:
    def __init__(self, f_name, l_name, id, gender, age, worked_year, still_working, salary, role):
        self.Нэр = f_name
        self.Овог = l_name
        self.id = id
        self.Хүйс = gender
        self.нас = age
        self.АжилсанЖил = worked_year
        self.АжиллажБайгаа = still_working
        self.Цалин = salary
        self.АлбанТушаал = role
        
    def __str__(self):
        return f"{self.Нэр} -ийн {self.Овог} нь {self.АжилсанЖил} жил ажилласан. (Ажиллаж байгаа эсэх: {self.АжиллажБайгаа} нас: {self.нас} Хүйс: {self.Хүйс} Цалин: {self.Цалин} Албан тушаал: {self.АлбанТушаал})"

def read_workers_from_file(filename):
    workers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip().split(',')
            workers.append(Ajilchin(*data))
    return workers

def main():
    while True:
        choice = input("| 2 gj bcvl - read>filter>saveToAnother': | 1 gj bcvl - read> save > filter > save | ")

        if choice == '2':
            filename = 'UbA.txt'
            workers = read_workers_from_file(filename)
            filter(workers)
            break
        elif choice == '1':
            filename = 'UbA.txt'
            workers = read_workers_from_file(filename)
            filter2(workers)
            break
        else:
            print("Invalid choice. Please choose either '1' or '2'.")

def filter2(workers):
    with open('dar.txt', 'w', encoding='utf-8') as f:
        for worker in workers:
            f.write(str(worker) + '\n')
    print("Amjilttai hadgalsan")
    
    with open('dar.txt', 'r', encoding='utf-8') as f:
        print(f.read())
        
    result = workers
    while True:
        filter_value = input("Filter hiih ugee biceerei ('exit' - biceed garah esvel'save' - biceed hadgalj bln): ")
        if filter_value.lower() == 'exit':
            break
        elif filter_value.lower() == 'save':
            with open('dar.txt', 'w', encoding='utf-8') as f:
                for worker in result:
                    f.write(str(worker) + '\n')
            print("Amjilttai")
            break

        new_result = []
        for worker in result:
            if filter_value.lower() in [str(value).lower() for value in vars(worker).values()]:
                new_result.append(worker)

        result = new_result

        i = 0
        for worker in result:
            i += 1
            print(f"{i}. {vars(worker)}\n")

    return result
    

def filter(workers):
    result = workers
    while True:
        i = 0
        for worker in result:
            i += 1
            print(f"{i}. {vars(worker)}\n")

        filter_value = input("Filter hiih ugee biceerei ('exit' - biceed garah esvel'save' - biceed hadgalj bln): ")
        if filter_value.lower() == 'exit':
            break
        elif filter_value.lower() == 'save':
            with open('darkhanB.txt', 'w', encoding='utf-8') as f:
                for worker in result:
                    f.write(str(worker) + '\n')
            print("Amjilttai hadgallaa!!!")
            break

        new_result = []
        for worker in result:
            if filter_value.lower() in [str(value).lower() for value in vars(worker).values()]:
                new_result.append(worker)

        result = new_result

    return result

if __name__ == "__main__":
    main()