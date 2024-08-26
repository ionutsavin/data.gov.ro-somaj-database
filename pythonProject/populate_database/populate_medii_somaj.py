import csv
import os
from connect_database import connect_to_database, get_judet_id, extract_month_year, map_judet_name


def traverse_and_insert_data(directory):
    conn, cursor = connect_to_database()

    for root, _, files in os.walk(directory):
        print("Current directory:", root)
        for file in files:
            if file.endswith("2.csv"):
                csv_file_path = os.path.join(root, file)
                month, year = extract_month_year(csv_file_path)

                with open(csv_file_path, 'r') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    next(csv_reader)
                    for row in csv_reader:
                        judet_name = map_judet_name(row[0].strip())

                        judet_id = get_judet_id(cursor, judet_name)
                        if judet_id is not None:
                            numar_total_someri_medii = int(row[1]) if row[1] else 0
                            numar_total_someri_femei = int(row[2]) if row[2] else 0
                            numar_total_someri_barbati = int(row[3]) if row[3] else 0
                            numar_total_someri_urban = int(row[4]) if row[4] else 0
                            numar_someri_femei_urban = int(row[5]) if row[5] else 0
                            numar_someri_barbati_urban = int(row[6]) if row[6] else 0
                            numar_total_someri_rural = int(row[7]) if row[7] else 0
                            numar_someri_femei_rural = int(row[8]) if row[8] else 0
                            numar_someri_barbati_rural = int(row[9]) if row[9] else 0
                            insert_query = '''
                                INSERT INTO medii_somaj (
                                    judet_id, year, month, 
                                    numar_total_someri, numar_total_someri_femei, numar_total_someri_barbati, 
                                    numar_total_someri_urban, numar_someri_femei_urban, numar_someri_barbati_urban, 
                                    numar_total_someri_rural, numar_someri_femei_rural, numar_someri_barbati_rural
                                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                            '''
                            cursor.execute(insert_query, (
                                judet_id, year, month,
                                numar_total_someri_medii, numar_total_someri_femei, numar_total_someri_barbati,
                                numar_total_someri_urban, numar_someri_femei_urban, numar_someri_barbati_urban,
                                numar_total_someri_rural, numar_someri_femei_rural, numar_someri_barbati_rural
                            ))

                            conn.commit()
                        else:
                            print(f"Judet '{judet_name}' not found in the judete table.")

    cursor.close()
    conn.close()

    print("Data inserted successfully into the medii_somaj table.")
