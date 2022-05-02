from record import Record 
import operator

class Database(object):
    '''
    Database 
    --------------
    Organizes files from SSA year of birth 
    text files into a central database.

    '''
    
    rec_list = []

    # Creates our database object 
    def __init__(self, dir, start, end):
        
        for i in range(start, end + 1):
            file =  f'{dir}/yob{i}.txt'

            try:
                file_reader = open(file, "r")
                while True:
                    line = file_reader.readline()
                    if not line:
                        break;
                    
                    entry = line.split(',')
                    name = entry[0]
                    sex = entry[1]
                    num = int(entry[2])
                    year = i 
                    rec = Record(name, sex, num, year)
                    self.rec_list.append(rec)
                    
            except FileNotFoundError:
                print('Files not found. Please check that the file path is correct.')
              

    # Method to find all records for a give name and sex 
    def selectAllNameRecords(self, name, sex):
        name_list = []
        for rec in self.rec_list:
            if rec.name == name and rec.sex == sex:
                name_list.append(rec)
        return name_list 

    # Finds the top n names for a given year and sex 
    def top_ten(self, sex, year, n):
        name_list = [] 
        for rec in self.rec_list:
            if rec.year == year and rec.sex == sex:
                name_list.append(rec) 

        sorted_list = sorted(name_list, key=operator.attrgetter('num'), reverse=True)
        return sorted_list[0:n]
