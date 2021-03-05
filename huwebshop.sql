-- MySQL Script generated by MySQL Workbench
-- Wed Mar  3 15:14:06 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

-- -----------------------------------------------------
-- Schema HUWebshop
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema HUWebshop
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Table HUWebshop.Products
-- -----------------------------------------------------
DROP TABLE IF EXISTS Products ;

create type targets as enum ('Man', 'Vrouw', 'Unisex', 'Baby', 'Gezin', 'B2B', 'Senior', 'Kinderen');
CREATE TABLE IF NOT EXISTS Products (
  idProducts SERIAL NOT NULL,
  name VARCHAR(255) NULL,
  brand VARCHAR(255) NULL,
  category VARCHAR(255) NULL,
  deeplink VARCHAR(255) NULL,
  fastmover BOOLEAN NULL,
  target targets NULL,
  herhaalaankopen BOOLEAN NULL,
  price DECIMAL NULL,
  stocklevel INT NULL,
  PRIMARY KEY (idProducts))
;


-- -----------------------------------------------------
-- Table HUWebshop.Visitors
-- -----------------------------------------------------
DROP TABLE IF EXISTS Visitors ;

CREATE TABLE IF NOT EXISTS Visitors (
  idVisitors SERIAL NOT NULL,
  previously_recommended VARCHAR(255) NULL,
  latest_activity timestamp NULL,
  PRIMARY KEY (idVisitors))
;


-- -----------------------------------------------------
-- Table HUWebshop.Buids
-- -----------------------------------------------------
DROP TABLE IF EXISTS Buids ;

CREATE TABLE IF NOT EXISTS Buids (
  buids SERIAL NOT NULL,
  Visitors_idVisitors INT NOT NULL,
  Device VARCHAR(255) NULL,
  PRIMARY KEY (buids),
  CONSTRAINT fk_Buids_Visitors
    FOREIGN KEY (Visitors_idVisitors)
    REFERENCES Visitors (idVisitors))
;


-- -----------------------------------------------------
-- Table HUWebshop.Sessions
-- -----------------------------------------------------
DROP TABLE IF EXISTS Sessions ;

CREATE TABLE IF NOT EXISTS Sessions (
  idSessions SERIAL NOT NULL,
  Buids_buids int NOT NULL,
  Device VARCHAR(255) NULL,
  sessie_start TIME NULL,
  sessie_end TIME NULL,
  PRIMARY KEY (idSessions),
  CONSTRAINT fk_Sessions_Buids1
    FOREIGN KEY (Buids_buids)
    REFERENCES Buids (buids))
;


-- -----------------------------------------------------
-- Table `HUWebshop`.`events`
-- -----------------------------------------------------
DROP TABLE IF EXISTS events ;

CREATE TABLE IF NOT EXISTS events (
  Products_idProducts SERIAL NOT NULL,
  Sessions_idSessions SERIAL NOT NULL,
  Event VARCHAR(255) NULL,
  CONSTRAINT fk_events_Products1
    FOREIGN KEY (Products_idProducts)
    REFERENCES Products (idProducts),
  CONSTRAINT fk_events_Sessions1
    FOREIGN KEY (Sessions_idSessions)
    REFERENCES Sessions (idSessions))
;


-- -----------------------------------------------------
-- Table `HUWebshop`.`order`
-- -----------------------------------------------------
DROP TABLE IF EXISTS orders ;

CREATE TABLE IF NOT EXISTS orders (
  Products_idProducts SERIAL NOT NULL,
  Sessions_idSessions INT NOT NULL,
  Amount INT NOT NULL,
  CONSTRAINT fk_orders_Products1
    FOREIGN KEY (Products_idProducts)
    REFERENCES Products (idProducts),
  CONSTRAINT fk_orders_Sessions1
    FOREIGN KEY (Sessions_idSessions)
    REFERENCES Sessions (idSessions))
;


-- -----------------------------------------------------
-- Table `HUWebshop`.`viewed_before`
-- -----------------------------------------------------
DROP TABLE IF EXISTS viewed_before ;

CREATE TABLE IF NOT EXISTS viewed_before (
  Visitors_idVisitors SERIAL NOT NULL,
  Products_idProducts SERIAL NOT NULL,
  Timedate timestamp NULL,
  CONSTRAINT fk_viewed_before_Products1
    FOREIGN KEY (Products_idProducts)
    REFERENCES Products (idProducts),
  CONSTRAINT fk_viewed_before_Visitors1
    FOREIGN KEY (Visitors_idVisitors)
    REFERENCES Visitors (idVisitors))
;


-- -----------------------------------------------------
-- Table `HUWebshop`.`Category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS Category ;

CREATE TABLE IF NOT EXISTS Category (
  idCategory SERIAL NOT NULL,
  Products_idProducts SERIAL NOT NULL,
  _name VARCHAR(255) NULL,
  PRIMARY KEY (idCategory),
  CONSTRAINT fk_Category_Products1
    FOREIGN KEY (Products_idProducts)
    REFERENCES Products (idProducts))
;


-- -----------------------------------------------------
-- Table `HUWebshop`.`Subcategory`
-- -----------------------------------------------------
DROP TABLE IF EXISTS Subcategory ;

CREATE TABLE IF NOT EXISTS Subcategory (
  idSubcategory SERIAL NOT NULL,
  Category_idCategory SERIAL NOT NULL,
  name VARCHAR(255) NULL,
  leveldepth INT NULL,
  PRIMARY KEY (idSubcategory),
  CONSTRAINT fk_Subcategory_Category1
    FOREIGN KEY (Category_idCategory)
    REFERENCES Category (idCategory))
;


-- -----------------------------------------------------
-- Table `HUWebshop`.`Similars`
-- -----------------------------------------------------
DROP TABLE IF EXISTS Similars ;

CREATE TABLE IF NOT EXISTS Similars (
  Visitors_idVisitors SERIAL NOT NULL,
  Products_idProducts SERIAL NOT NULL,
  CONSTRAINT fk_Similars_Visitors1
    FOREIGN KEY (Visitors_idVisitors)
    REFERENCES Visitors (idVisitors),
  CONSTRAINT fk_Similars_Products1
    FOREIGN KEY (Products_idProducts)
    REFERENCES Products (idProducts))
;


-- -----------------------------------------------------
-- Table `HUWebshop`.`Has_sale`
-- -----------------------------------------------------
DROP TABLE IF EXISTS Has_sale ;

create type TypeSales as enum ('Korting', '1Plus1');
CREATE TABLE IF NOT EXISTS Has_sale (
  Sessions_idSessions SERIAL NOT NULL,
  Products_idProducts SERIAL NOT NULL,
  TypeSale TypeSales NULL,
  AmountKorting INT NULL,
  CONSTRAINT fk_Has_sale_Sessions1
    FOREIGN KEY (Sessions_idSessions)
    REFERENCES Sessions (idSessions),
  CONSTRAINT fk_Has_sale_Products1
    FOREIGN KEY (Products_idProducts)
    REFERENCES Products (idProducts))
;


-- -----------------------------------------------------
-- Table `HUWebshop`.`Properties`
-- -----------------------------------------------------
DROP TABLE IF EXISTS Properties ;

CREATE TABLE IF NOT EXISTS Properties (
  Products_idProducts SERIAL NOT NULL,
  Properties VARCHAR(255) NOT NULL,
  CONSTRAINT fk_Properties_Products1
    FOREIGN KEY (Products_idProducts)
    REFERENCES Products (idProducts))
;
