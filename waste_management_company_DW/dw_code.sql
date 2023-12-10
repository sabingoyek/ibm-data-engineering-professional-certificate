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


-- object: public."MyDimDate" | type: TABLE --
-- DROP TABLE IF EXISTS public."MyDimDate" CASCADE;
CREATE TABLE public."MyDimDate" (
	dateid serial NOT NULL,
	day smallint,
	weekday smallint,
	weekdayname character varying(10),
	month smallint,
	monthname character varying(15),
	quarter smallint,
	quartername character(2),
	year smallint,
	CONSTRAINT "MyDimDate_pk" PRIMARY KEY (dateid)
);
-- ddl-end --
ALTER TABLE public."MyDimDate" OWNER TO postgres;
-- ddl-end --

-- object: public."MyDimWaste" | type: TABLE --
-- DROP TABLE IF EXISTS public."MyDimWaste" CASCADE;
CREATE TABLE public."MyDimWaste" (
	wasteid serial NOT NULL,
	wastetype character varying(20),
	quantity smallint,
	CONSTRAINT "MyDimWaste_pk" PRIMARY KEY (wasteid)
);
-- ddl-end --
ALTER TABLE public."MyDimWaste" OWNER TO postgres;
-- ddl-end --

-- object: public."MyDimZone" | type: TABLE --
-- DROP TABLE IF EXISTS public."MyDimZone" CASCADE;
CREATE TABLE public."MyDimZone" (
	zoneid serial NOT NULL,
	zonename character varying(50),
	city character varying(50),
	CONSTRAINT "MyDimZone_pk" PRIMARY KEY (zoneid)
);
-- ddl-end --
ALTER TABLE public."MyDimZone" OWNER TO postgres;
-- ddl-end --

-- object: public."MyFactTrips" | type: TABLE --
-- DROP TABLE IF EXISTS public."MyFactTrips" CASCADE;
CREATE TABLE public."MyFactTrips" (
	tripid serial NOT NULL,
	truckid smallint,
	trucktype character varying(20),
	"dateid_MyDimDate" integer NOT NULL,
	"zoneid_MyDimZone" integer NOT NULL,
	"wasteid_MyDimWaste" integer NOT NULL,
	CONSTRAINT "MyFactTrips_pk" PRIMARY KEY (tripid)
);
-- ddl-end --
ALTER TABLE public."MyFactTrips" OWNER TO postgres;
-- ddl-end --

-- object: "MyDimDate_fk" | type: CONSTRAINT --
-- ALTER TABLE public."MyFactTrips" DROP CONSTRAINT IF EXISTS "MyDimDate_fk" CASCADE;
ALTER TABLE public."MyFactTrips" ADD CONSTRAINT "MyDimDate_fk" FOREIGN KEY ("dateid_MyDimDate")
REFERENCES public."MyDimDate" (dateid) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: "MyDimZone_fk" | type: CONSTRAINT --
-- ALTER TABLE public."MyFactTrips" DROP CONSTRAINT IF EXISTS "MyDimZone_fk" CASCADE;
ALTER TABLE public."MyFactTrips" ADD CONSTRAINT "MyDimZone_fk" FOREIGN KEY ("zoneid_MyDimZone")
REFERENCES public."MyDimZone" (zoneid) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --

-- object: "MyDimWaste_fk" | type: CONSTRAINT --
-- ALTER TABLE public."MyFactTrips" DROP CONSTRAINT IF EXISTS "MyDimWaste_fk" CASCADE;
ALTER TABLE public."MyFactTrips" ADD CONSTRAINT "MyDimWaste_fk" FOREIGN KEY ("wasteid_MyDimWaste")
REFERENCES public."MyDimWaste" (wasteid) MATCH FULL
ON DELETE RESTRICT ON UPDATE CASCADE;
-- ddl-end --


