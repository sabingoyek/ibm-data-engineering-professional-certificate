-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler version: 0.9.4
-- PostgreSQL version: 13.0
-- Project Site: pgmodeler.io
-- Model Author: ---

-- Database creation must be performed outside a multi lined SQL file. 
-- These commands were put in this file only as a convenience.
-- 
-- object: dw_design | type: DATABASE --
-- DROP DATABASE IF EXISTS dw_design;
CREATE DATABASE dw_design;
-- ddl-end --


-- object: public."DimDate" | type: TABLE --
-- DROP TABLE IF EXISTS public."DimDate" CASCADE;
CREATE TABLE public."DimDate" (
	dateid serial NOT NULL,
	day smallint,
	weekday smallint,
	weekdayname character varying(10),
	month smallint,
	monthname character varying(15),
	quarter smallint,
	quartername character(2),
	year smallint,
	date date,
	CONSTRAINT "MyDimDate_pk" PRIMARY KEY (dateid)
);
-- ddl-end --
ALTER TABLE public."DimDate" OWNER TO postgres;
-- ddl-end --

-- object: public."DimStation" | type: TABLE --
-- DROP TABLE IF EXISTS public."DimStation" CASCADE;
CREATE TABLE public."DimStation" (
	stationid serial NOT NULL,
	city character varying(50),
	CONSTRAINT "DimStation_pk" PRIMARY KEY (stationid)
);
-- ddl-end --
ALTER TABLE public."DimStation" OWNER TO postgres;
-- ddl-end --

-- object: public."DimTruck" | type: TABLE --
-- DROP TABLE IF EXISTS public."DimTruck" CASCADE;
CREATE TABLE public."DimTruck" (
	truckid serial NOT NULL,
	trucktype character varying(50),
	CONSTRAINT "DimTruck_pk" PRIMARY KEY (truckid)
);
-- ddl-end --
ALTER TABLE public."DimTruck" OWNER TO postgres;
-- ddl-end --

-- object: public."FactTrips" | type: TABLE --
-- DROP TABLE IF EXISTS public."FactTrips" CASCADE;
CREATE TABLE public."FactTrips" (
	tripid serial,
	"dateid_DimDate" integer NOT NULL,
	"stationid_DimStation" integer NOT NULL,
	"truckid_DimTruck" integer NOT NULL,
	wastecollected float

);
-- ddl-end --
ALTER TABLE public."FactTrips" OWNER TO postgres;
-- ddl-end --

-- object: "DimDate_fk" | type: CONSTRAINT --
-- ALTER TABLE public."FactTrips" DROP CONSTRAINT IF EXISTS "DimDate_fk" CASCADE;
ALTER TABLE public."FactTrips" ADD CONSTRAINT "DimDate_fk" FOREIGN KEY ("dateid_DimDate")
REFERENCES public."DimDate" (dateid) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: "DimStation_fk" | type: CONSTRAINT --
-- ALTER TABLE public."FactTrips" DROP CONSTRAINT IF EXISTS "DimStation_fk" CASCADE;
ALTER TABLE public."FactTrips" ADD CONSTRAINT "DimStation_fk" FOREIGN KEY ("stationid_DimStation")
REFERENCES public."DimStation" (stationid) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: "DimTruck_fk" | type: CONSTRAINT --
-- ALTER TABLE public."FactTrips" DROP CONSTRAINT IF EXISTS "DimTruck_fk" CASCADE;
ALTER TABLE public."FactTrips" ADD CONSTRAINT "DimTruck_fk" FOREIGN KEY ("truckid_DimTruck")
REFERENCES public."DimTruck" (truckid) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --


