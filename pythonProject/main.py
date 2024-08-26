from archive_download.data_2019_2024 import download_files as download_files_2019_2024
from archive_download.data_2018 import download_files as download_files_2018
from populate_database.populate_medii_somaj import traverse_and_insert_data as traverse_and_insert_medii_somaj
from populate_database.populate_nivel_educatie_somaj import \
    traverse_and_insert_data as traverse_and_insert_nivel_educatie_somaj
from populate_database.populate_rata_somaj import traverse_and_insert_data as traverse_and_insert_rata_somaj
from populate_database.populate_varste_somaj import traverse_and_insert_data as traverse_and_insert_varste_somaj
from populate_database.create_judete import create_judete_table


def main():
    print("Creating the 'judete' table...")
    create_judete_table()

    print("Starting download from 2018 data script...")
    url = "https://data.gov.ro/dataset/somajul-inregistrat"
    year = 2018
    romanian_months = ["August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie"]
    download_files_2018(url, year, romanian_months)

    print("Starting download from 2019-2024 data script...")
    download_files_2019_2024()

    print("Download completed. Starting data population...")
    archive = "arhiva_somaj"

    print("Populating database with 'medii' data...")
    traverse_and_insert_medii_somaj(archive)

    print("Populating database with 'nivel educatie' data...")
    traverse_and_insert_nivel_educatie_somaj(archive)

    print("Populating database with 'rata' data...")
    traverse_and_insert_rata_somaj(archive)

    print("Populating database with 'varste' data...")
    traverse_and_insert_varste_somaj(archive)

    print("Data population completed.")


if __name__ == "__main__":
    main()
