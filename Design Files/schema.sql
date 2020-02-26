--
-- File generated with SQLiteStudio v3.2.1 on Tue Feb 25 19:04:23 2020
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Competitors
DROP TABLE IF EXISTS Competitors;

CREATE TABLE Competitors (
    c_id INTEGER PRIMARY KEY ASC AUTOINCREMENT
                 NOT NULL,
    name STRING  DEFAULT [New Division]
);


-- Table: CompList
DROP TABLE IF EXISTS CompList;

CREATE TABLE CompList (
    r_id        INTEGER REFERENCES Rounds (r_id),
    c_id        INTEGER REFERENCES Competitors (c_id),
    comp_flag   BOOLEAN NOT NULL
                        DEFAULT (false),
    round_order INT,
    PRIMARY KEY (
        r_id ASC,
        c_id ASC
    )
);


-- Table: DivisionInfo
DROP TABLE IF EXISTS DivisionInfo;

CREATE TABLE DivisionInfo (
    d_id INTEGER PRIMARY KEY
               NOT NULL
               UNIQUE
               CONSTRAINT ValidId CHECK (d_id = 0) 
);


-- Table: Rounds
DROP TABLE IF EXISTS Rounds;

CREATE TABLE Rounds (
    r_id      INT     PRIMARY KEY ASC
                      NOT NULL,
    comp_flag BOOLEAN DEFAULT (0) 
                      NOT NULL
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
