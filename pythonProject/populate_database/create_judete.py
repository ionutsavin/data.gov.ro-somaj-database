from connect_database import connect_to_database


conn, cursor = connect_to_database()


def create_judete_table():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS judete (
        id SERIAL PRIMARY KEY,
        judet VARCHAR(50) NOT NULL
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()


def insert_judete():
    judete = [
        'ALBA', 'ARAD', 'ARGES', 'BACAU', 'BIHOR', 'BISTRITA-NASAUD', 'BOTOSANI', 'BRAILA', 'BRASOV', 'BUZAU',
        'CALARASI', 'CARAS-SEVERIN', 'CLUJ', 'CONSTANTA', 'COVASNA', 'DAMBOVITA', 'DOLJ', 'GALATI', 'GIURGIU', 'GORJ',
        'HARGHITA', 'HUNEDOARA', 'IALOMITA', 'IASI', 'ILFOV', 'MARAMURES', 'MEHEDINTI', 'BUCURESTI', 'MURES', 'NEAMT',
        'OLT', 'PRAHOVA', 'SALAJ', 'SATU-MARE', 'SIBIU', 'SUCEAVA', 'TELEORMAN', 'TIMIS', 'TULCEA', 'VALCEA', 'VASLUI',
        'VRANCEA', 'TOTAL'
    ]

    for judet in judete:
        insert_query = '''
        INSERT INTO judete (judet) VALUES (%s)
        '''
        cursor.execute(insert_query, (judet,))
    conn.commit()
