-- AB-Cloud unified package: data schema (SQLite/Postgres compatible DDL)
-- The consolidated register of the programme's numbers.

CREATE TABLE levels (
    id TEXT PRIMARY KEY,          -- I, I+, II, III, IV, V
    name TEXT NOT NULL,
    name_ru TEXT,
    campaigns TEXT,               -- e.g. 'V01-V19'
    theorems TEXT,
    essence TEXT
);

CREATE TABLE flagship_results (
    id INTEGER PRIMARY KEY,
    result TEXT NOT NULL,
    numbers TEXT NOT NULL,        -- verbatim from source verdict files
    level TEXT NOT NULL           -- campaign id: V/E/D/C/heritage
);

CREATE TABLE verdicts (
    id TEXT PRIMARY KEY,          -- G1..G5, RH
    claim_en TEXT,
    claim_ru TEXT,
    verdict TEXT NOT NULL CHECK (verdict IN ('YES','NO','BLOCKED')),
    basis TEXT NOT NULL
);

CREATE TABLE numbers_registry (
    n INTEGER PRIMARY KEY,
    metric_en TEXT, metric_ru TEXT,
    value TEXT NOT NULL,          -- numbers are stored as text, verbatim
    campaign TEXT NOT NULL
);

CREATE TABLE provenance (
    rowid INTEGER PRIMARY KEY,
    ts TEXT, action TEXT, source TEXT, destination TEXT, transform TEXT
);
