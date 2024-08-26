CREATE TABLE IF NOT EXISTS rata_somaj (
    id SERIAL PRIMARY KEY,
    judet_id INTEGER REFERENCES judete(id),
    year INTEGER,
    month VARCHAR(50),
    numar_total_someri INTEGER,
    numar_total_someri_femei INTEGER,
    numar_total_someri_barbati INTEGER,
    numar_someri_indemnizati INTEGER,
    numar_someri_neindemnizati INTEGER,
    rata_somajului FLOAT,
    rata_somajului_feminina FLOAT,
    rata_somajului_masculina FLOAT
);

CREATE TABLE IF NOT EXISTS medii_somaj (
    id SERIAL PRIMARY KEY,
    judet_id INTEGER REFERENCES judete(id),
    year INTEGER,
    month VARCHAR(50),
    numar_total_someri INTEGER,
    numar_total_someri_femei INTEGER,
    numar_total_someri_barbati INTEGER,
    numar_total_someri_urban INTEGER,
    numar_someri_femei_urban INTEGER,
    numar_someri_barbati_urban INTEGER,
    numar_total_someri_rural INTEGER,
    numar_someri_femei_rural INTEGER,
    numar_someri_barbati_rural INTEGER
);

CREATE TABLE IF NOT EXISTS nivel_educatie_somaj (
    id SERIAL PRIMARY KEY,
    judet_id INTEGER REFERENCES judete(id),
    year INTEGER,
    month VARCHAR(50),
    numar_total_someri INTEGER,
    fara_studii INTEGER,
    invatamant_primar INTEGER,
    invatamant_gimnazial INTEGER,
    invatamant_liceal INTEGER,
    invatamant_postliceal INTEGER,
    invatamant_profesional_arte_si_meserii INTEGER,
    invatamant_universitar INTEGER
);

CREATE TABLE IF NOT EXISTS varste_somaj (
    id SERIAL PRIMARY KEY,
    judet_id INTEGER REFERENCES judete(id),
    year INTEGER,
    month VARCHAR(50),
    numar_total_someri INTEGER,
    sub_25 INTEGER,
    intre_25_si_29 INTEGER,
    intre_30_si_39 INTEGER,
    intre_40_si_49 INTEGER,
    intre_50_si_55 INTEGER,
    peste_55 INTEGER
);