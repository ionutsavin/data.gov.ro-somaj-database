import csv
import os
from connect_database import connect_to_database, get_judet_id, extract_month_year, map_judet_name


def traverse_and_insert_data(directory):
    conn, cursor = connect_to_database()

    for root, _, files in os.walk(directory):
        print("Current directory:", root)
        for file in files:
            if file.endswith("3.csv") and "ianuarie_2023" not in file:
                csv_file_path = os.path.join(root, file)
                month, year = extract_month_year(csv_file_path)

                with open(csv_file_path, 'r') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    next(csv_reader)
                    for row in csv_reader:
                        judet_name = map_judet_name(row[0].strip())

                        judet_id = get_judet_id(cursor, judet_name)
                        if judet_id is not None:
                            numar_total_someri_educatie = int(row[1]) if row[1] else 0
                            fara_studii = int(row[2]) if row[2] else 0
                            invatamant_primar = int(row[3]) if row[3] else 0
                            invatamant_gimnazial = int(row[4]) if row[4] else 0
                            invatamant_liceal = int(row[5]) if row[5] else 0
                            invatamant_postliceal = int(row[6]) if row[6] else 0
                            invatamant_profesional_arte_si_meserii = int(row[7]) if row[7] else 0
                            invatamant_universitar = int(row[8]) if row[8] else 0
                            insert_query = '''
                                INSERT INTO nivel_educatie_somaj (
                                    judet_id, year, month, 
                                    numar_total_someri, fara_studii, invatamant_primar, 
                                    invatamant_gimnazial, invatamant_liceal, invatamant_postliceal, 
                                    invatamant_profesional_arte_si_meserii, invatamant_universitar
                                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                            '''
                            cursor.execute(insert_query, (
                                judet_id, year, month, numar_total_someri_educatie,
                                fara_studii, invatamant_primar, invatamant_gimnazial,
                                invatamant_liceal, invatamant_postliceal,
                                invatamant_profesional_arte_si_meserii, invatamant_universitar
                            ))

                            conn.commit()
                        else:
                            print(f"Judet '{judet_name}' not found in the judete table.")

    cursor.close()
    conn.close()

    print("Data inserted successfully into the nivel_educatie_somaj table.")
