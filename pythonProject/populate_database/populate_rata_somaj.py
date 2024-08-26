import csv
import os
from connect_database import connect_to_database, get_judet_id, extract_month_year, map_judet_name


def clean_and_convert_to_int(value):
    return int(''.join(filter(str.isdigit, value)))


def traverse_and_insert_data(directory):
    conn, cursor = connect_to_database()

    for root, _, files in os.walk(directory):
        print("Current directory:", root)
        for file in files:
            if file.endswith("1.csv"):
                csv_file_path = os.path.join(root, file)
                month, year = extract_month_year(csv_file_path)

                with open(csv_file_path, 'r') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    next(csv_reader)
                    for row in csv_reader:
                        judet_name = map_judet_name(row[0].strip())

                        judet_id = get_judet_id(cursor, judet_name)
                        if judet_id is not None:
                            numar_total_someri = clean_and_convert_to_int(row[1])
                            numar_total_someri_femei = clean_and_convert_to_int(row[2])
                            numar_total_someri_barbati = clean_and_convert_to_int(row[3])
                            numar_someri_indemnizati = clean_and_convert_to_int(row[4])
                            numar_someri_neindemnizati = clean_and_convert_to_int(row[5])
                            rata_somajului = float(row[6])
                            rata_somajului_feminina = float(row[7])
                            rata_somajului_masculina = float(row[8])

                            insert_query = '''
                            INSERT INTO rata_somaj (judet_id, year, month, numar_total_someri, numar_total_someri_femei,
                                                    numar_total_someri_barbati, numar_someri_indemnizati, 
                                                    numar_someri_neindemnizati, rata_somajului, rata_somajului_feminina,
                                                     rata_somajului_masculina)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                            '''
                            cursor.execute(insert_query, (judet_id, year, month, numar_total_someri,
                                                          numar_total_someri_femei, numar_total_someri_barbati,
                                                          numar_someri_indemnizati, numar_someri_neindemnizati,
                                                          rata_somajului, rata_somajului_feminina,
                                                          rata_somajului_masculina))
                            conn.commit()
                        else:
                            print(f"Judet '{judet_name}' not found in the judete table.")

    cursor.close()
    conn.close()

    print("Data inserted successfully into the rata_somaj table.")
