import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_PATH = "C:/Users/Surya/Desktop/ghj/exak.csv"

def load_data():
    if os.path.exists(FILE_PATH):
        data = pd.read_csv(FILE_PATH)
        print("Data loaded successfully.")
        print(data.head())  # Debug: print first few rows of the DataFrame
    else:
        print("File not found. Creating a new DataFrame.")
        columns = ["rollno", "name", "father_name", "adharrid", "age", "attempt", "lastattemptscore", "dateofbirth", "address", "phonenumber", "email"]
        data = pd.DataFrame(columns=columns)
    return data

def save_data(data):
    data.to_csv(FILE_PATH, index=False)
    print("Data saved successfully.")

def display_main_menu():
    print('*' * 80) 
    print('                                  WELCOME TO EXAMINATION MANAGEMENT MENU    ')
    print('*' * 80)
    print('1. Show Examination Details\n')
    print('2. Show Data Columns \n')
    print('3. Display Top Records\n')
    print('4. Display Bottom Records\n')
    print('5. Display Specific Column\n')
    print('6. Add a New Record\n')
    print('7. Add a New Column\n')
    print('8. Delete a Column\n')
    print('9. Delete a Record\n')
    print('10. Update a Record\n')
    print('11. Move to Graph Menu\n')
    print('12. Exit\n')

def handle_main_choice(data, choice):
    if choice == 1:
        print(data)
    elif choice == 2:
        print(data.columns)
    elif choice == 3:
        n = int(input('Enter number of top records to display: '))
        print(data.head(n))
    elif choice == 4:
        n = int(input('Enter number of bottom records to display: '))
        print(data.tail(n))
    elif choice == 5:
        col_name = input('Enter column name to display: ')
        if col_name in data.columns:
            print(data[col_name])
        else:
            print(f'Column "{col_name}" does not exist.')
    elif choice == 6:
        new_record = {
            "rollno": input('Enter Roll Number: '),
            "name": input('Enter Name: '),
            "father_name": input('Enter Father Name: '),
            "adharrid": input('Enter Aadhar ID: '),
            "age": int(input('Enter Age: ')),
            "attempt": int(input('Enter Attempt Number: ')),
            "lastattemptscore": float(input('Enter Last Attempt Score: ')),
            "dateofbirth": input('Enter Date of Birth (YYYY-MM-DD): '),
            "address": input('Enter Address: '),
            "phonenumber": input('Enter Phone Number: '),
            "email": input('Enter Email: ')
        }
        new_df = pd.DataFrame([new_record])
        data = pd.concat([data, new_df], ignore_index=True)
        save_data(data)
        load_data()
    elif choice == 7:
        col_name = input('Enter new column name: ')
        default_value = input('Enter default value for the new column: ')
        if col_name not in data.columns:
            data[col_name] = default_value
            save_data(data)
        else:
            print(f'Column "{col_name}" already exists.')
    elif choice == 8:
        col_name = input('Enter column name to delete: ')
        if col_name in data.columns:
            data = data.drop(columns=[col_name])
            save_data(data)
        else:
            print(f'Column "{col_name}" does not exist.')
    elif choice == 9:
        index_no = int(input('Enter the index number of the record to delete: '))
        if index_no in data.index:
            data = data.drop(index_no)
            save_data(data)
        else:
            print(f'Index {index_no} does not exist.')
    elif choice == 10:
        index_no = int(input('Enter the index number of the record to update: '))
        if index_no in data.index:
            updated_record = {
                "rollno": input('Enter Roll Number: '),
                "name": input('Enter Name: '),
                "father_name": input('Enter Father Name: '),
                "adharrid": input('Enter Aadhar ID: '),
                "age": int(input('Enter Age: ')),
                "attempt": int(input('Enter Attempt Number: ')),
                "lastattemptscore": float(input('Enter Last Attempt Score: ')),
                "dateofbirth": input('Enter Date of Birth (YYYY-MM-DD): '),
                "address": input('Enter Address: '),
                "phonenumber": input('Enter Phone Number: '),
                "email": input('Enter Email: ')
            }
            data.loc[index_no] = updated_record
            save_data(data)
        else:
            print(f'Index {index_no} does not exist.')
    elif choice == 11:
        graph_menu(data)
    elif choice == 12:
        print("Exiting the system. Thank you!")
        return False
    return True

def display_graph_menu():
    print('*' * 80)
    print('                          GRAPH MENU                             ')
    print('*' * 80)
    print('1. Age Distribution Histogram\n')
    print('2. Attempt Distribution Bar Graph\n')
    print('3. Last Attempt Score Scatter Plot\n')
    print('4. Exit to Main Menu\n')

def handle_graph_choice(data, choice):
    if choice == 1:
        plt.hist(data['age'].dropna(), bins=10, edgecolor='black')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.title('Age Distribution')
        plt.show()
    elif choice == 2:
        attempt_counts = data['attempt'].value_counts().sort_index()
        attempt_counts.plot(kind='bar')
        plt.xlabel('Attempt Number')
        plt.ylabel('Number of Records')
        plt.title('Attempt Distribution')
        plt.show()
    elif choice == 3:
        plt.scatter(data['attempt'], data['lastattemptscore'])
        plt.xlabel('Attempt Number')
        plt.ylabel('Last Attempt Score')
        plt.title('Last Attempt Score vs Attempt Number')
        plt.show()
    elif choice == 4:
        return False
    return True

def main():
    data = load_data()
    while True:
        display_main_menu()
        try:
            choice = int(input('Enter your choice: '))
            if not handle_main_choice(data, choice):
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    while True:
        display_graph_menu()
        try:
            choice = int(input('Enter your choice: '))
            if not handle_graph_choice(data, choice):
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
