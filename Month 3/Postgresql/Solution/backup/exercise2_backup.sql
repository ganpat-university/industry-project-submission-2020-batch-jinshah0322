--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: city; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.city (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    code character varying(10),
    company_id integer
);


ALTER TABLE public.city OWNER TO postgres;

--
-- Name: city_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.city_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.city_id_seq OWNER TO postgres;

--
-- Name: city_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.city_id_seq OWNED BY public.city.id;


--
-- Name: company; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.company (
    id integer NOT NULL
);


ALTER TABLE public.company OWNER TO postgres;

--
-- Name: company_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.company_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.company_id_seq OWNER TO postgres;

--
-- Name: company_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.company_id_seq OWNED BY public.company.id;


--
-- Name: employee; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employee (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    city_id integer NOT NULL,
    join_date date,
    CONSTRAINT check_date CHECK ((join_date >= '2010-01-01'::date))
);


ALTER TABLE public.employee OWNER TO postgres;

--
-- Name: employee_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.employee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.employee_id_seq OWNER TO postgres;

--
-- Name: employee_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.employee_id_seq OWNED BY public.employee.id;


--
-- Name: new_table; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.new_table (
    id integer NOT NULL
);


ALTER TABLE public.new_table OWNER TO postgres;

--
-- Name: start1000; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.start1000
    START WITH 1000
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.start1000 OWNER TO postgres;

--
-- Name: new_table1; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.new_table1 (
    id integer DEFAULT nextval('public.start1000'::regclass) NOT NULL
);


ALTER TABLE public.new_table1 OWNER TO postgres;

--
-- Name: start500; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.start500
    START WITH 500
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.start500 OWNER TO postgres;

--
-- Name: new_table2; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.new_table2 (
    id integer DEFAULT nextval('public.start500'::regclass) NOT NULL
);


ALTER TABLE public.new_table2 OWNER TO postgres;

--
-- Name: new_table_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.new_table_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.new_table_id_seq OWNER TO postgres;

--
-- Name: new_table_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.new_table_id_seq OWNED BY public.new_table.id;


--
-- Name: city id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.city ALTER COLUMN id SET DEFAULT nextval('public.city_id_seq'::regclass);


--
-- Name: company id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.company ALTER COLUMN id SET DEFAULT nextval('public.company_id_seq'::regclass);


--
-- Name: employee id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee ALTER COLUMN id SET DEFAULT nextval('public.employee_id_seq'::regclass);


--
-- Name: new_table id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.new_table ALTER COLUMN id SET DEFAULT nextval('public.new_table_id_seq'::regclass);


--
-- Data for Name: city; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.city (id, name, code, company_id) FROM stdin;
1	Mumbai	C1	1
2	Delhi	C2	2
3	Bangalore	C3	3
4	Hyderabad	C4	4
5	Chennai	C5	5
6	Kolkata	C6	6
7	Ahmedabad	C7	7
8	Pune	C8	8
9	Surat	C9	9
10	Jaipur	C10	10
\.


--
-- Data for Name: company; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.company (id) FROM stdin;
1
2
3
4
5
6
7
8
9
10
11
\.


--
-- Data for Name: employee; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employee (id, name, city_id, join_date) FROM stdin;
1	John Doe	1	2024-03-15
2	Alice Smith	2	2024-03-15
3	Bob Johnson	3	2024-03-15
4	Emma Watson	4	2024-03-15
5	Michael Davis	5	2024-03-15
6	Sarah Lee	6	2024-03-15
7	David Brown	7	2024-03-15
8	Olivia Wilson	8	2024-03-15
9	James Taylor	9	2024-03-15
10	Sophia Martinez	10	2024-03-15
11	John Doe	1	2024-03-15
12	Alice Smith	2	2024-03-15
13	Bob Johnson	3	2024-03-15
14	Emma Watson	4	2024-03-15
15	Michael Davis	5	2024-03-15
16	Sarah Lee	6	2024-03-15
17	David Brown	7	2024-03-15
18	Olivia Wilson	8	2024-03-15
19	James Taylor	9	2024-03-15
20	Sophia Martinez	10	2024-03-15
21	Matthew Clark	1	2024-03-15
22	Emily Rodriguez	2	2024-03-15
23	Daniel Garcia	3	2024-03-15
24	Madison Martinez	4	2024-03-15
25	Ethan Wilson	5	2024-03-15
\.


--
-- Data for Name: new_table; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.new_table (id) FROM stdin;
\.


--
-- Data for Name: new_table1; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.new_table1 (id) FROM stdin;
1000
1001
\.


--
-- Data for Name: new_table2; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.new_table2 (id) FROM stdin;
\.


--
-- Name: city_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.city_id_seq', 10, true);


--
-- Name: company_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.company_id_seq', 11, true);


--
-- Name: employee_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.employee_id_seq', 25, true);


--
-- Name: new_table_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.new_table_id_seq', 1, false);


--
-- Name: start1000; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.start1000', 1001, true);


--
-- Name: start500; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.start500', 500, false);


--
-- Name: city city_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.city
    ADD CONSTRAINT city_pkey PRIMARY KEY (id);


--
-- Name: company company_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_pkey PRIMARY KEY (id);


--
-- Name: employee employee_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (id);


--
-- Name: new_table1 new_table1_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.new_table1
    ADD CONSTRAINT new_table1_pkey PRIMARY KEY (id);


--
-- Name: new_table2 new_table2_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.new_table2
    ADD CONSTRAINT new_table2_pkey PRIMARY KEY (id);


--
-- Name: new_table new_table_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.new_table
    ADD CONSTRAINT new_table_pkey PRIMARY KEY (id);


--
-- Name: city unique_cmp_code; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.city
    ADD CONSTRAINT unique_cmp_code UNIQUE (company_id, code);


--
-- Name: emp_index; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX emp_index ON public.employee USING btree (city_id, join_date);


--
-- Name: emp_nameindex; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX emp_nameindex ON public.employee USING btree (name);


--
-- Name: index_name; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX index_name ON public.city USING btree (name);


--
-- Name: employee employee_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.city(id);


--
-- Name: city fk_company; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.city
    ADD CONSTRAINT fk_company FOREIGN KEY (company_id) REFERENCES public.company(id);


--
-- PostgreSQL database dump complete
--

