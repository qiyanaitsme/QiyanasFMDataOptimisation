import openpyxl
from concurrent.futures import ThreadPoolExecutor

def process_line(line):
    email, password = line.strip().split(':')
    login = email.split('@')[0]
    full_info = f"{login}:{password}:{email}:{password}"
    return [login, password, email, password, full_info]

def process_data(input_file, output_file):
    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()[1:]

    with ThreadPoolExecutor() as executor:
        processed_data = list(executor.map(process_line, lines))

    wb = openpyxl.Workbook()
    ws = wb.active

    ws.append(['LOGIN', 'PASSWORD', 'EMAIL', 'PASSWORD', 'Full Info'])

    for idx, data in enumerate(processed_data, start=2):
        ws.append(data)

    ws['F1'] = 'login:password:email:password'

    wb.save(output_file)

input_file = "steam.txt"
output_file = "steam.xlsx"
process_data(input_file, output_file)