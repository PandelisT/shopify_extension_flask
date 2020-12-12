--
-- PostgreSQL database dump
--

-- Dumped from database version 12.5 (Ubuntu 12.5-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.5 (Ubuntu 12.5-0ubuntu0.20.04.1)

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
-- Name: addresses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.addresses (
    id integer NOT NULL,
    created_on timestamp without time zone NOT NULL,
    number integer NOT NULL,
    postcode integer NOT NULL,
    street character varying NOT NULL,
    suburb character varying NOT NULL,
    state character varying NOT NULL,
    user_id integer NOT NULL,
    customer_id integer
);


ALTER TABLE public.addresses OWNER TO postgres;

--
-- Name: addresses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.addresses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.addresses_id_seq OWNER TO postgres;

--
-- Name: addresses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.addresses_id_seq OWNED BY public.addresses.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: articles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.articles (
    id integer NOT NULL,
    created_on timestamp without time zone NOT NULL,
    body_html character varying NOT NULL,
    summary character varying NOT NULL,
    title character varying NOT NULL,
    user_id integer NOT NULL,
    allow_comments boolean,
    custom_post_type character varying,
    show_date_and_author boolean,
    show_summary boolean
);


ALTER TABLE public.articles OWNER TO postgres;

--
-- Name: articles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.articles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.articles_id_seq OWNER TO postgres;

--
-- Name: articles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.articles_id_seq OWNED BY public.articles.id;


--
-- Name: customers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customers (
    id integer NOT NULL,
    fname character varying NOT NULL,
    lname character varying NOT NULL,
    created_on timestamp without time zone NOT NULL,
    is_active boolean,
    email character varying NOT NULL,
    customer_of integer NOT NULL
);


ALTER TABLE public.customers OWNER TO postgres;

--
-- Name: customers_habits; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customers_habits (
    customer_id integer,
    habit_id integer
);


ALTER TABLE public.customers_habits OWNER TO postgres;

--
-- Name: customers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.customers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.customers_id_seq OWNER TO postgres;

--
-- Name: customers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.customers_id_seq OWNED BY public.customers.id;


--
-- Name: customers_tags; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customers_tags (
    customer_id integer,
    tag_id integer
);


ALTER TABLE public.customers_tags OWNER TO postgres;

--
-- Name: habits; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.habits (
    id integer NOT NULL,
    habit character varying NOT NULL,
    created_at timestamp without time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.habits OWNER TO postgres;

--
-- Name: habits_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.habits_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.habits_id_seq OWNER TO postgres;

--
-- Name: habits_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.habits_id_seq OWNED BY public.habits.id;


--
-- Name: notes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.notes (
    id integer NOT NULL,
    comms_type character varying NOT NULL,
    note character varying NOT NULL,
    customer_id integer NOT NULL,
    created_at timestamp without time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.notes OWNER TO postgres;

--
-- Name: notes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.notes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.notes_id_seq OWNER TO postgres;

--
-- Name: notes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.notes_id_seq OWNED BY public.notes.id;


--
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    id integer NOT NULL,
    created_on timestamp without time zone NOT NULL,
    customer_of integer NOT NULL,
    customer_id integer NOT NULL
);


ALTER TABLE public.orders OWNER TO postgres;

--
-- Name: orders_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.orders_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders_id_seq OWNER TO postgres;

--
-- Name: orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.orders_id_seq OWNED BY public.orders.id;


--
-- Name: orders_products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders_products (
    order_id integer,
    product_id integer
);


ALTER TABLE public.orders_products OWNER TO postgres;

--
-- Name: products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products (
    id integer NOT NULL,
    title character varying NOT NULL,
    description character varying NOT NULL,
    quantity integer,
    price integer NOT NULL,
    created_on timestamp without time zone NOT NULL,
    user_id integer NOT NULL,
    no_of_articles integer
);


ALTER TABLE public.products OWNER TO postgres;

--
-- Name: products_articles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products_articles (
    product_id integer,
    article_id integer
);


ALTER TABLE public.products_articles OWNER TO postgres;

--
-- Name: products_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_id_seq OWNER TO postgres;

--
-- Name: products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;


--
-- Name: tags; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tags (
    id integer NOT NULL,
    tag character varying NOT NULL,
    created_at timestamp without time zone NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.tags OWNER TO postgres;

--
-- Name: tags_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tags_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tags_id_seq OWNER TO postgres;

--
-- Name: tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tags_id_seq OWNED BY public.tags.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying NOT NULL,
    password character varying NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: addresses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.addresses ALTER COLUMN id SET DEFAULT nextval('public.addresses_id_seq'::regclass);


--
-- Name: articles id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.articles ALTER COLUMN id SET DEFAULT nextval('public.articles_id_seq'::regclass);


--
-- Name: customers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customers ALTER COLUMN id SET DEFAULT nextval('public.customers_id_seq'::regclass);


--
-- Name: habits id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.habits ALTER COLUMN id SET DEFAULT nextval('public.habits_id_seq'::regclass);


--
-- Name: notes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notes ALTER COLUMN id SET DEFAULT nextval('public.notes_id_seq'::regclass);


--
-- Name: orders id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders ALTER COLUMN id SET DEFAULT nextval('public.orders_id_seq'::regclass);


--
-- Name: products id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);


--
-- Name: tags id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tags ALTER COLUMN id SET DEFAULT nextval('public.tags_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: addresses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.addresses (id, created_on, number, postcode, street, suburb, state, user_id, customer_id) FROM stdin;
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
7263a9a85ae5
\.


--
-- Data for Name: articles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.articles (id, created_on, body_html, summary, title, user_id, allow_comments, custom_post_type, show_date_and_author, show_summary) FROM stdin;
1	2020-12-12 10:32:20.719586	Body text1	Summary1	title1	5	t	Custom Post Type1	t	t
2	2020-12-12 10:32:20.721432	Body text2	Summary2	title2	2	t	Custom Post Type2	t	t
3	2020-12-12 10:32:20.722461	Body text3	Summary3	title3	1	t	Custom Post Type3	t	t
4	2020-12-12 10:32:20.723358	Body text4	Summary4	title4	3	t	Custom Post Type4	t	t
5	2020-12-12 10:32:20.724368	Body text5	Summary5	title5	3	t	Custom Post Type5	t	t
6	2020-12-12 10:32:20.725476	Body text6	Summary6	title6	5	t	Custom Post Type6	t	t
7	2020-12-12 10:32:20.726563	Body text7	Summary7	title7	3	t	Custom Post Type7	t	t
8	2020-12-12 10:32:20.727534	Body text8	Summary8	title8	1	t	Custom Post Type8	t	t
9	2020-12-12 10:32:20.728421	Body text9	Summary9	title9	5	t	Custom Post Type9	t	t
10	2020-12-12 10:32:20.72935	Body text10	Summary10	title10	2	t	Custom Post Type10	t	t
11	2020-12-12 10:32:20.730261	Body text11	Summary11	title11	2	t	Custom Post Type11	t	t
12	2020-12-12 10:32:20.731326	Body text12	Summary12	title12	2	t	Custom Post Type12	t	t
13	2020-12-12 10:32:20.732365	Body text13	Summary13	title13	4	t	Custom Post Type13	t	t
14	2020-12-12 10:32:20.733432	Body text14	Summary14	title14	2	t	Custom Post Type14	t	t
15	2020-12-12 10:32:20.734346	Body text15	Summary15	title15	1	t	Custom Post Type15	t	t
16	2020-12-12 10:32:20.735259	Body text16	Summary16	title16	1	t	Custom Post Type16	t	t
17	2020-12-12 10:32:20.736626	Body text17	Summary17	title17	2	t	Custom Post Type17	t	t
18	2020-12-12 10:32:20.738071	Body text18	Summary18	title18	2	t	Custom Post Type18	t	t
19	2020-12-12 10:32:20.739254	Body text19	Summary19	title19	5	t	Custom Post Type19	t	t
20	2020-12-12 10:32:20.740141	Body text20	Summary20	title20	1	t	Custom Post Type20	t	t
\.


--
-- Data for Name: customers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customers (id, fname, lname, created_on, is_active, email, customer_of) FROM stdin;
1	firstname1	lastname1	2020-12-12 10:32:20.648924	t	name1@email.com	3
2	firstname2	lastname2	2020-12-12 10:32:20.650938	t	name2@email.com	2
3	firstname3	lastname3	2020-12-12 10:32:20.65208	t	name3@email.com	2
4	firstname4	lastname4	2020-12-12 10:32:20.653227	t	name4@email.com	5
5	firstname5	lastname5	2020-12-12 10:32:20.654225	t	name5@email.com	4
6	firstname6	lastname6	2020-12-12 10:32:20.655125	t	name6@email.com	4
7	firstname7	lastname7	2020-12-12 10:32:20.656321	t	name7@email.com	5
8	firstname8	lastname8	2020-12-12 10:32:20.657219	t	name8@email.com	2
9	firstname9	lastname9	2020-12-12 10:32:20.658511	t	name9@email.com	3
10	firstname10	lastname10	2020-12-12 10:32:20.659546	t	name10@email.com	2
\.


--
-- Data for Name: customers_habits; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customers_habits (customer_id, habit_id) FROM stdin;
\.


--
-- Data for Name: customers_tags; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customers_tags (customer_id, tag_id) FROM stdin;
\.


--
-- Data for Name: habits; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.habits (id, habit, created_at, user_id) FROM stdin;
1	Habit number 1	2020-12-12 10:32:20.805125	2
2	Habit number 2	2020-12-12 10:32:20.807079	5
3	Habit number 3	2020-12-12 10:32:20.808154	5
4	Habit number 4	2020-12-12 10:32:20.809156	2
5	Habit number 5	2020-12-12 10:32:20.8101	4
6	Habit number 6	2020-12-12 10:32:20.811032	2
7	Habit number 7	2020-12-12 10:32:20.812454	2
8	Habit number 8	2020-12-12 10:32:20.813402	5
9	Habit number 9	2020-12-12 10:32:20.814331	3
10	Habit number 10	2020-12-12 10:32:20.815198	5
\.


--
-- Data for Name: notes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.notes (id, comms_type, note, customer_id, created_at, user_id) FROM stdin;
1	Email	Note number 1	6	2020-12-12 10:32:20.867846	5
2	Email	Note number 2	8	2020-12-12 10:32:20.869817	1
3	Email	Note number 3	9	2020-12-12 10:32:20.870993	4
4	Email	Note number 4	9	2020-12-12 10:32:20.872068	1
5	Email	Note number 5	8	2020-12-12 10:32:20.873214	4
6	Email	Note number 6	7	2020-12-12 10:32:20.874348	2
7	Email	Note number 7	8	2020-12-12 10:32:20.875417	1
8	Email	Note number 8	5	2020-12-12 10:32:20.876314	1
9	Email	Note number 9	8	2020-12-12 10:32:20.877154	4
10	Email	Note number 10	9	2020-12-12 10:32:20.878299	2
\.


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders (id, created_on, customer_of, customer_id) FROM stdin;
1	2020-12-12 10:32:20.77824	4	7
2	2020-12-12 10:32:20.780197	2	10
3	2020-12-12 10:32:20.781388	1	10
4	2020-12-12 10:32:20.782361	3	7
5	2020-12-12 10:32:20.783364	1	2
6	2020-12-12 10:32:20.784426	2	6
7	2020-12-12 10:32:20.785506	1	4
8	2020-12-12 10:32:20.786449	4	5
9	2020-12-12 10:32:20.787289	5	9
10	2020-12-12 10:32:20.78815	2	3
\.


--
-- Data for Name: orders_products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders_products (order_id, product_id) FROM stdin;
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products (id, title, description, quantity, price, created_on, user_id, no_of_articles) FROM stdin;
1	title1	description1	1	10	2020-12-12 10:32:20.679756	3	0
2	title2	description2	1	10	2020-12-12 10:32:20.681751	3	0
3	title3	description3	1	10	2020-12-12 10:32:20.682867	5	0
4	title4	description4	1	10	2020-12-12 10:32:20.683839	4	0
5	title5	description5	1	10	2020-12-12 10:32:20.684834	5	0
6	title6	description6	1	10	2020-12-12 10:32:20.685845	4	0
7	title7	description7	1	10	2020-12-12 10:32:20.687176	1	0
8	title8	description8	1	10	2020-12-12 10:32:20.688101	5	0
9	title9	description9	1	10	2020-12-12 10:32:20.688946	3	0
10	title10	description10	1	10	2020-12-12 10:32:20.690017	2	0
11	title11	description11	1	10	2020-12-12 10:32:20.690885	4	0
12	title12	description12	1	10	2020-12-12 10:32:20.691794	2	0
13	title13	description13	1	10	2020-12-12 10:32:20.692791	5	0
14	title14	description14	1	10	2020-12-12 10:32:20.693834	5	0
15	title15	description15	1	10	2020-12-12 10:32:20.694647	2	0
16	title16	description16	1	10	2020-12-12 10:32:20.695525	2	0
17	title17	description17	1	10	2020-12-12 10:32:20.696633	3	0
18	title18	description18	1	10	2020-12-12 10:32:20.697727	5	0
19	title19	description19	1	10	2020-12-12 10:32:20.69862	3	0
20	title20	description20	1	10	2020-12-12 10:32:20.699614	1	0
\.


--
-- Data for Name: products_articles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.products_articles (product_id, article_id) FROM stdin;
\.


--
-- Data for Name: tags; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tags (id, tag, created_at, user_id) FROM stdin;
1	Tag number 1	2020-12-12 10:32:20.828844	2
2	Tag number 2	2020-12-12 10:32:20.830764	5
3	Tag number 3	2020-12-12 10:32:20.832383	5
4	Tag number 4	2020-12-12 10:32:20.833386	2
5	Tag number 5	2020-12-12 10:32:20.83434	5
6	Tag number 6	2020-12-12 10:32:20.83525	5
7	Tag number 7	2020-12-12 10:32:20.836237	2
8	Tag number 8	2020-12-12 10:32:20.837165	2
9	Tag number 9	2020-12-12 10:32:20.838028	4
10	Tag number 10	2020-12-12 10:32:20.838794	5
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, email, password) FROM stdin;
1	test1@test.com	$2b$12$Im9JOXo5ePTr2iSJvyYjoO5/awvo8quR2pcA.ktAgo6xjzD0RoVAK
2	test2@test.com	$2b$12$dnhTqGwKMP8I/xSLz.Eujub8ikUJ/ZSO26E9Pw1A8fazzCcr95RSi
3	test3@test.com	$2b$12$d5IQxfzvtCJRA4tIMaJjH.Gbx/sKRHlAI2fJVTISkXmk/8BxY/32y
4	test4@test.com	$2b$12$o0cgQMoJ/KBGNpntCpN7EuYvoftCnH7IiJbEyVGmwKfT3p9bNg/Wi
5	test5@test.com	$2b$12$sE1XUS4S6KfpXD/Jwo3OAeuYtfl1ZTYU48jAms5NREeHPBBC6qnBW
\.


--
-- Name: addresses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.addresses_id_seq', 1, false);


--
-- Name: articles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.articles_id_seq', 20, true);


--
-- Name: customers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.customers_id_seq', 10, true);


--
-- Name: habits_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.habits_id_seq', 10, true);


--
-- Name: notes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.notes_id_seq', 10, true);


--
-- Name: orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_id_seq', 10, true);


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_id_seq', 20, true);


--
-- Name: tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tags_id_seq', 10, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 5, true);


--
-- Name: addresses addresses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.addresses
    ADD CONSTRAINT addresses_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: articles articles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.articles
    ADD CONSTRAINT articles_pkey PRIMARY KEY (id);


--
-- Name: customers customers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (id);


--
-- Name: habits habits_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.habits
    ADD CONSTRAINT habits_pkey PRIMARY KEY (id);


--
-- Name: notes notes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notes
    ADD CONSTRAINT notes_pkey PRIMARY KEY (id);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (id);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);


--
-- Name: tags tags_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: addresses addresses_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.addresses
    ADD CONSTRAINT addresses_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(id);


--
-- Name: addresses addresses_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.addresses
    ADD CONSTRAINT addresses_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: articles articles_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.articles
    ADD CONSTRAINT articles_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: customers customers_customer_of_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customers
    ADD CONSTRAINT customers_customer_of_fkey FOREIGN KEY (customer_of) REFERENCES public.users(id);


--
-- Name: customers_habits customers_habits_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customers_habits
    ADD CONSTRAINT customers_habits_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(id);


--
-- Name: customers_habits customers_habits_habit_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customers_habits
    ADD CONSTRAINT customers_habits_habit_id_fkey FOREIGN KEY (habit_id) REFERENCES public.habits(id);


--
-- Name: customers_tags customers_tags_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customers_tags
    ADD CONSTRAINT customers_tags_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(id);


--
-- Name: customers_tags customers_tags_tag_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customers_tags
    ADD CONSTRAINT customers_tags_tag_id_fkey FOREIGN KEY (tag_id) REFERENCES public.tags(id);


--
-- Name: habits habits_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.habits
    ADD CONSTRAINT habits_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: notes notes_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notes
    ADD CONSTRAINT notes_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(id);


--
-- Name: notes notes_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notes
    ADD CONSTRAINT notes_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: orders orders_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customers(id);


--
-- Name: orders orders_customer_of_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_customer_of_fkey FOREIGN KEY (customer_of) REFERENCES public.users(id);


--
-- Name: orders_products orders_products_order_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders_products
    ADD CONSTRAINT orders_products_order_id_fkey FOREIGN KEY (order_id) REFERENCES public.orders(id);


--
-- Name: orders_products orders_products_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders_products
    ADD CONSTRAINT orders_products_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(id);


--
-- Name: products_articles products_articles_article_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products_articles
    ADD CONSTRAINT products_articles_article_id_fkey FOREIGN KEY (article_id) REFERENCES public.articles(id);


--
-- Name: products_articles products_articles_product_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products_articles
    ADD CONSTRAINT products_articles_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(id);


--
-- Name: products products_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: tags tags_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

