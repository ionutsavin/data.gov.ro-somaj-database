import csv
import os
from connect_database import connect_to_database, get_judet_id, extract_month_year, map_judet_name


def traverse_and_insert_data(directory):
    conn, cursor = connect_to_database()

    for root, _, files in os.walk(directory):
        print("Current directory:", root)
        for file in files:
            if file.endswith("4.csv"):
                csv_file_path = os.path.join(root, file)
                month, year = extract_month_year(csv_file_path)

                with open(csv_file_path, 'r') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    next(csv_reader)
                    for row in csv_reader:
                        judet_name = map_judet_name(row[0].strip())

                        judet_id = get_judet_id(cursor, judet_name)
                        if judet_id is not None:
                            numar_total_someri_varste = int(row[1]) if row[1] else 0
                            sub_25 = int(row[2]) if row[2] else 0
                            intre_25_29 = int(row[3]) if row[3] else 0
                            intre_30_39 = int(row[4]) if row[4] else 0
                            intre_40_49 = int(row[5]) if row[5] else 0
                            intre_50_55 = int(row[6]) if row[6] else 0
                            peste_55 = int(row[7]) if row[7] else 0
                            insert_query = '''
                                INSERT INTO varste_somaj (
                                    judet_id, year, month, numar_total_someri, sub_25, intre_25_si_29, 
                                    intre_30_si_39, intre_40_si_49, intre_50_si_55, peste_55
                                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                            '''
                            cursor.execute(insert_query, (
                                judet_id, year, month, numar_total_someri_varste, sub_25, intre_25_29,
                                intre_30_39, intre_40_49, intre_50_55, peste_55
                            ))

                            conn.commit()
                        else:
                            print(f"Judet '{judet_name}' not found in the judete table.")

    cursor.close()
    conn.close()

    print("Data inserted successfully into the varste_somaj table.")
