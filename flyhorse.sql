PGDMP     &    /                w            flyhorse    11.1    11.1 �    E           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            F           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            G           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            H           1262    32796    flyhorse    DATABASE     �   CREATE DATABASE flyhorse WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Spanish_Venezuela.1252' LC_CTYPE = 'Spanish_Venezuela.1252';
    DROP DATABASE flyhorse;
             postgres    false            �            1259    33094    apuesta_apuesta    TABLE     ^  CREATE TABLE public.apuesta_apuesta (
    id integer NOT NULL,
    cuota double precision,
    "fechaAp" date NOT NULL,
    estatus character varying(1) NOT NULL,
    "idTrans_id" integer,
    "idTransGanada_id" integer,
    id_carr_id character varying(20),
    id_jorh_id character varying(20),
    "tApuesta_id" integer,
    usuario_id integer
);
 #   DROP TABLE public.apuesta_apuesta;
       public         postgres    false            �            1259    33092    apuesta_apuesta_id_seq    SEQUENCE     �   CREATE SEQUENCE public.apuesta_apuesta_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.apuesta_apuesta_id_seq;
       public       postgres    false    234            I           0    0    apuesta_apuesta_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.apuesta_apuesta_id_seq OWNED BY public.apuesta_apuesta.id;
            public       postgres    false    233            �            1259    33102    apuesta_detalleapuesta    TABLE     �   CREATE TABLE public.apuesta_detalleapuesta (
    id integer NOT NULL,
    posicion integer,
    "montoD" double precision,
    id_ap_id integer,
    id_cab_id integer
);
 *   DROP TABLE public.apuesta_detalleapuesta;
       public         postgres    false            �            1259    33100    apuesta_detalleapuesta_id_seq    SEQUENCE     �   CREATE SEQUENCE public.apuesta_detalleapuesta_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.apuesta_detalleapuesta_id_seq;
       public       postgres    false    236            J           0    0    apuesta_detalleapuesta_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.apuesta_detalleapuesta_id_seq OWNED BY public.apuesta_detalleapuesta.id;
            public       postgres    false    235            �            1259    33110    apuesta_tipoapuesta    TABLE     �   CREATE TABLE public.apuesta_tipoapuesta (
    id integer NOT NULL,
    nombre character varying(20) NOT NULL,
    descripcion character varying(70) NOT NULL,
    estatus character varying(1) NOT NULL
);
 '   DROP TABLE public.apuesta_tipoapuesta;
       public         postgres    false            �            1259    33108    apuesta_tipoapuesta_id_seq    SEQUENCE     �   CREATE SEQUENCE public.apuesta_tipoapuesta_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.apuesta_tipoapuesta_id_seq;
       public       postgres    false    238            K           0    0    apuesta_tipoapuesta_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.apuesta_tipoapuesta_id_seq OWNED BY public.apuesta_tipoapuesta.id;
            public       postgres    false    237            �            1259    32828 
   auth_group    TABLE     e   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);
    DROP TABLE public.auth_group;
       public         postgres    false            �            1259    32826    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public       postgres    false    203            L           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
            public       postgres    false    202            �            1259    32838    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         postgres    false            �            1259    32836    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public       postgres    false    205            M           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
            public       postgres    false    204            �            1259    32820    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         postgres    false            �            1259    32818    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public       postgres    false    201            N           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
            public       postgres    false    200            �            1259    33016    caballo_caballo    TABLE     V  CREATE TABLE public.caballo_caballo (
    id integer NOT NULL,
    nombre character varying(30),
    peso double precision,
    "fecha_Registro" date NOT NULL,
    fecha_nac date NOT NULL,
    foto character varying(100) NOT NULL,
    estatus character varying(1) NOT NULL,
    id_entre_id integer NOT NULL,
    id_hip_id integer NOT NULL
);
 #   DROP TABLE public.caballo_caballo;
       public         postgres    false            �            1259    33014    caballo_caballo_id_seq    SEQUENCE     �   CREATE SEQUENCE public.caballo_caballo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.caballo_caballo_id_seq;
       public       postgres    false    227            O           0    0    caballo_caballo_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.caballo_caballo_id_seq OWNED BY public.caballo_caballo.id;
            public       postgres    false    226            �            1259    32941    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         postgres    false            �            1259    32939    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public       postgres    false    214            P           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
            public       postgres    false    213            �            1259    32810    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         postgres    false            �            1259    32808    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public       postgres    false    199            Q           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
            public       postgres    false    198            �            1259    32799    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         postgres    false            �            1259    32797    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public       postgres    false    197            R           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
            public       postgres    false    196            �            1259    33178    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         postgres    false            �            1259    33008    entrenador_entrenador    TABLE     �   CREATE TABLE public.entrenador_entrenador (
    id integer NOT NULL,
    nombre character varying(30) NOT NULL,
    fecha_nac date NOT NULL,
    estatus character varying(1) NOT NULL,
    foto character varying(100) NOT NULL
);
 )   DROP TABLE public.entrenador_entrenador;
       public         postgres    false            �            1259    33006    entrenador_entrenador_id_seq    SEQUENCE     �   CREATE SEQUENCE public.entrenador_entrenador_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.entrenador_entrenador_id_seq;
       public       postgres    false    225            S           0    0    entrenador_entrenador_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.entrenador_entrenador_id_seq OWNED BY public.entrenador_entrenador.id;
            public       postgres    false    224            �            1259    33000    hipodromo_hipodromo    TABLE     �  CREATE TABLE public.hipodromo_hipodromo (
    id integer NOT NULL,
    nombre character varying(20) NOT NULL,
    rif character varying(20) NOT NULL,
    estado character varying(15) NOT NULL,
    ciudad character varying(15) NOT NULL,
    telefono character varying(20) NOT NULL,
    nombre_dueno character varying(20) NOT NULL,
    fecha_registro date NOT NULL,
    foto character varying(100) NOT NULL,
    estatus character varying(1) NOT NULL
);
 '   DROP TABLE public.hipodromo_hipodromo;
       public         postgres    false            �            1259    32998    hipodromo_hipodromo_id_seq    SEQUENCE     �   CREATE SEQUENCE public.hipodromo_hipodromo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.hipodromo_hipodromo_id_seq;
       public       postgres    false    223            T           0    0    hipodromo_hipodromo_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.hipodromo_hipodromo_id_seq OWNED BY public.hipodromo_hipodromo.id;
            public       postgres    false    222            �            1259    32992    jockey_jockey    TABLE        CREATE TABLE public.jockey_jockey (
    id integer NOT NULL,
    nombre character varying(30) NOT NULL,
    peso double precision NOT NULL,
    fecha_nac date NOT NULL,
    estatus character varying(1) NOT NULL,
    foto character varying(100) NOT NULL
);
 !   DROP TABLE public.jockey_jockey;
       public         postgres    false            �            1259    32990    jockey_jockey_id_seq    SEQUENCE     �   CREATE SEQUENCE public.jockey_jockey_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.jockey_jockey_id_seq;
       public       postgres    false    221            U           0    0    jockey_jockey_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.jockey_jockey_id_seq OWNED BY public.jockey_jockey.id;
            public       postgres    false    220            �            1259    33034    jornada_carrera    TABLE     -  CREATE TABLE public.jornada_carrera (
    id character varying(20) NOT NULL,
    hora time without time zone NOT NULL,
    cant_caballos integer,
    distancia double precision,
    estatus character varying(1) NOT NULL,
    publicable boolean NOT NULL,
    id_jh_id character varying(20) NOT NULL
);
 #   DROP TABLE public.jornada_carrera;
       public         postgres    false            �            1259    33039    jornada_detallescarrera    TABLE       CREATE TABLE public.jornada_detallescarrera (
    id character varying(20) NOT NULL,
    numero integer,
    posicion integer,
    estatus character varying(1) NOT NULL,
    id_caba_id integer NOT NULL,
    id_carr_id character varying(20) NOT NULL,
    id_jock_id integer NOT NULL
);
 +   DROP TABLE public.jornada_detallescarrera;
       public         postgres    false            �            1259    33046    jornada_job    TABLE     �   CREATE TABLE public.jornada_job (
    id integer NOT NULL,
    fecha date NOT NULL,
    hora time without time zone NOT NULL,
    estado character varying(1) NOT NULL
);
    DROP TABLE public.jornada_job;
       public         postgres    false            �            1259    33044    jornada_job_id_seq    SEQUENCE     �   CREATE SEQUENCE public.jornada_job_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.jornada_job_id_seq;
       public       postgres    false    231            V           0    0    jornada_job_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.jornada_job_id_seq OWNED BY public.jornada_job.id;
            public       postgres    false    230            �            1259    33052    jornada_jornadah    TABLE     �   CREATE TABLE public.jornada_jornadah (
    id character varying(20) NOT NULL,
    fecha date NOT NULL,
    cant_carr integer NOT NULL,
    fecha_reg date NOT NULL,
    estatus character varying(1) NOT NULL,
    id_hip_id integer NOT NULL
);
 $   DROP TABLE public.jornada_jornadah;
       public         postgres    false            �            1259    32965    monedavirtual_banco    TABLE       CREATE TABLE public.monedavirtual_banco (
    id integer NOT NULL,
    bco character varying(4) NOT NULL,
    numero character varying(20),
    tipo character varying(1) NOT NULL,
    ident character varying(20),
    names character varying(50),
    usua_id integer
);
 '   DROP TABLE public.monedavirtual_banco;
       public         postgres    false            �            1259    32963    monedavirtual_banco_id_seq    SEQUENCE     �   CREATE SEQUENCE public.monedavirtual_banco_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.monedavirtual_banco_id_seq;
       public       postgres    false    216            W           0    0    monedavirtual_banco_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.monedavirtual_banco_id_seq OWNED BY public.monedavirtual_banco.id;
            public       postgres    false    215            �            1259    32971    monedavirtual_monedavirtual    TABLE     �   CREATE TABLE public.monedavirtual_monedavirtual (
    fecha date NOT NULL,
    precio_bs double precision NOT NULL,
    precio_divisa double precision NOT NULL
);
 /   DROP TABLE public.monedavirtual_monedavirtual;
       public         postgres    false            �            1259    32978    monedavirtual_transaccion    TABLE     s  CREATE TABLE public.monedavirtual_transaccion (
    id integer NOT NULL,
    fecha date NOT NULL,
    monto double precision NOT NULL,
    tipo character varying(1) NOT NULL,
    estado character varying(1) NOT NULL,
    bco character varying(4) NOT NULL,
    ref character varying(20),
    descripcion integer NOT NULL,
    bco_retiro_id integer,
    usua_id integer
);
 -   DROP TABLE public.monedavirtual_transaccion;
       public         postgres    false            �            1259    32976     monedavirtual_transaccion_id_seq    SEQUENCE     �   CREATE SEQUENCE public.monedavirtual_transaccion_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.monedavirtual_transaccion_id_seq;
       public       postgres    false    219            X           0    0     monedavirtual_transaccion_id_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.monedavirtual_transaccion_id_seq OWNED BY public.monedavirtual_transaccion.id;
            public       postgres    false    218            �            1259    32888    usuario_type_user    TABLE     �   CREATE TABLE public.usuario_type_user (
    codigo character varying(8) NOT NULL,
    tipo_usuario integer NOT NULL,
    descripcion character varying(20) NOT NULL
);
 %   DROP TABLE public.usuario_type_user;
       public         postgres    false            �            1259    32869    usuario_user    TABLE     �  CREATE TABLE public.usuario_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    city text NOT NULL,
    location character varying(30) NOT NULL,
    birth_date date,
    phone character varying(20),
    balance double precision NOT NULL,
    last_access timestamp with time zone NOT NULL,
    type_u_id character varying(8)
);
     DROP TABLE public.usuario_user;
       public         postgres    false            �            1259    32882    usuario_user_groups    TABLE     �   CREATE TABLE public.usuario_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 '   DROP TABLE public.usuario_user_groups;
       public         postgres    false            �            1259    32880    usuario_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.usuario_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.usuario_user_groups_id_seq;
       public       postgres    false    209            Y           0    0    usuario_user_groups_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.usuario_user_groups_id_seq OWNED BY public.usuario_user_groups.id;
            public       postgres    false    208            �            1259    32867    usuario_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.usuario_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.usuario_user_id_seq;
       public       postgres    false    207            Z           0    0    usuario_user_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.usuario_user_id_seq OWNED BY public.usuario_user.id;
            public       postgres    false    206            �            1259    32896    usuario_user_user_permissions    TABLE     �   CREATE TABLE public.usuario_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 1   DROP TABLE public.usuario_user_user_permissions;
       public         postgres    false            �            1259    32894 $   usuario_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.usuario_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ;   DROP SEQUENCE public.usuario_user_user_permissions_id_seq;
       public       postgres    false    212            [           0    0 $   usuario_user_user_permissions_id_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE public.usuario_user_user_permissions_id_seq OWNED BY public.usuario_user_user_permissions.id;
            public       postgres    false    211                       2604    33097    apuesta_apuesta id    DEFAULT     x   ALTER TABLE ONLY public.apuesta_apuesta ALTER COLUMN id SET DEFAULT nextval('public.apuesta_apuesta_id_seq'::regclass);
 A   ALTER TABLE public.apuesta_apuesta ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    233    234    234                       2604    33105    apuesta_detalleapuesta id    DEFAULT     �   ALTER TABLE ONLY public.apuesta_detalleapuesta ALTER COLUMN id SET DEFAULT nextval('public.apuesta_detalleapuesta_id_seq'::regclass);
 H   ALTER TABLE public.apuesta_detalleapuesta ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    235    236    236                       2604    33113    apuesta_tipoapuesta id    DEFAULT     �   ALTER TABLE ONLY public.apuesta_tipoapuesta ALTER COLUMN id SET DEFAULT nextval('public.apuesta_tipoapuesta_id_seq'::regclass);
 E   ALTER TABLE public.apuesta_tipoapuesta ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    237    238    238                       2604    32831    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    202    203    203            	           2604    32841    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    204    205    205                       2604    32823    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    200    201    201                       2604    33019    caballo_caballo id    DEFAULT     x   ALTER TABLE ONLY public.caballo_caballo ALTER COLUMN id SET DEFAULT nextval('public.caballo_caballo_id_seq'::regclass);
 A   ALTER TABLE public.caballo_caballo ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    226    227    227                       2604    32944    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    213    214    214                       2604    32813    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    198    199    199                       2604    32802    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    196    197    197                       2604    33011    entrenador_entrenador id    DEFAULT     �   ALTER TABLE ONLY public.entrenador_entrenador ALTER COLUMN id SET DEFAULT nextval('public.entrenador_entrenador_id_seq'::regclass);
 G   ALTER TABLE public.entrenador_entrenador ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    225    224    225                       2604    33003    hipodromo_hipodromo id    DEFAULT     �   ALTER TABLE ONLY public.hipodromo_hipodromo ALTER COLUMN id SET DEFAULT nextval('public.hipodromo_hipodromo_id_seq'::regclass);
 E   ALTER TABLE public.hipodromo_hipodromo ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    222    223    223                       2604    32995    jockey_jockey id    DEFAULT     t   ALTER TABLE ONLY public.jockey_jockey ALTER COLUMN id SET DEFAULT nextval('public.jockey_jockey_id_seq'::regclass);
 ?   ALTER TABLE public.jockey_jockey ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    221    220    221                       2604    33049    jornada_job id    DEFAULT     p   ALTER TABLE ONLY public.jornada_job ALTER COLUMN id SET DEFAULT nextval('public.jornada_job_id_seq'::regclass);
 =   ALTER TABLE public.jornada_job ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    230    231    231                       2604    32968    monedavirtual_banco id    DEFAULT     �   ALTER TABLE ONLY public.monedavirtual_banco ALTER COLUMN id SET DEFAULT nextval('public.monedavirtual_banco_id_seq'::regclass);
 E   ALTER TABLE public.monedavirtual_banco ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    216    215    216                       2604    32981    monedavirtual_transaccion id    DEFAULT     �   ALTER TABLE ONLY public.monedavirtual_transaccion ALTER COLUMN id SET DEFAULT nextval('public.monedavirtual_transaccion_id_seq'::regclass);
 K   ALTER TABLE public.monedavirtual_transaccion ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    218    219    219            
           2604    32872    usuario_user id    DEFAULT     r   ALTER TABLE ONLY public.usuario_user ALTER COLUMN id SET DEFAULT nextval('public.usuario_user_id_seq'::regclass);
 >   ALTER TABLE public.usuario_user ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    206    207    207                       2604    32885    usuario_user_groups id    DEFAULT     �   ALTER TABLE ONLY public.usuario_user_groups ALTER COLUMN id SET DEFAULT nextval('public.usuario_user_groups_id_seq'::regclass);
 E   ALTER TABLE public.usuario_user_groups ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    209    208    209                       2604    32899     usuario_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.usuario_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.usuario_user_user_permissions_id_seq'::regclass);
 O   ALTER TABLE public.usuario_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    212    211    212            =          0    33094    apuesta_apuesta 
   TABLE DATA               �   COPY public.apuesta_apuesta (id, cuota, "fechaAp", estatus, "idTrans_id", "idTransGanada_id", id_carr_id, id_jorh_id, "tApuesta_id", usuario_id) FROM stdin;
    public       postgres    false    234   -=      ?          0    33102    apuesta_detalleapuesta 
   TABLE DATA               ]   COPY public.apuesta_detalleapuesta (id, posicion, "montoD", id_ap_id, id_cab_id) FROM stdin;
    public       postgres    false    236   J=      A          0    33110    apuesta_tipoapuesta 
   TABLE DATA               O   COPY public.apuesta_tipoapuesta (id, nombre, descripcion, estatus) FROM stdin;
    public       postgres    false    238   g=                0    32828 
   auth_group 
   TABLE DATA               .   COPY public.auth_group (id, name) FROM stdin;
    public       postgres    false    203   �=                 0    32838    auth_group_permissions 
   TABLE DATA               M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public       postgres    false    205   �=                0    32820    auth_permission 
   TABLE DATA               N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public       postgres    false    201   �=      6          0    33016    caballo_caballo 
   TABLE DATA                  COPY public.caballo_caballo (id, nombre, peso, "fecha_Registro", fecha_nac, foto, estatus, id_entre_id, id_hip_id) FROM stdin;
    public       postgres    false    227   �@      )          0    32941    django_admin_log 
   TABLE DATA               �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public       postgres    false    214   A                0    32810    django_content_type 
   TABLE DATA               C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public       postgres    false    199   )A                0    32799    django_migrations 
   TABLE DATA               C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public       postgres    false    197   B      B          0    33178    django_session 
   TABLE DATA               P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public       postgres    false    239   8D      4          0    33008    entrenador_entrenador 
   TABLE DATA               U   COPY public.entrenador_entrenador (id, nombre, fecha_nac, estatus, foto) FROM stdin;
    public       postgres    false    225   UD      2          0    33000    hipodromo_hipodromo 
   TABLE DATA               �   COPY public.hipodromo_hipodromo (id, nombre, rif, estado, ciudad, telefono, nombre_dueno, fecha_registro, foto, estatus) FROM stdin;
    public       postgres    false    223   rD      0          0    32992    jockey_jockey 
   TABLE DATA               S   COPY public.jockey_jockey (id, nombre, peso, fecha_nac, estatus, foto) FROM stdin;
    public       postgres    false    221   �D      7          0    33034    jornada_carrera 
   TABLE DATA               l   COPY public.jornada_carrera (id, hora, cant_caballos, distancia, estatus, publicable, id_jh_id) FROM stdin;
    public       postgres    false    228   �D      8          0    33039    jornada_detallescarrera 
   TABLE DATA               t   COPY public.jornada_detallescarrera (id, numero, posicion, estatus, id_caba_id, id_carr_id, id_jock_id) FROM stdin;
    public       postgres    false    229   �D      :          0    33046    jornada_job 
   TABLE DATA               >   COPY public.jornada_job (id, fecha, hora, estado) FROM stdin;
    public       postgres    false    231   �D      ;          0    33052    jornada_jornadah 
   TABLE DATA               _   COPY public.jornada_jornadah (id, fecha, cant_carr, fecha_reg, estatus, id_hip_id) FROM stdin;
    public       postgres    false    232   E      +          0    32965    monedavirtual_banco 
   TABLE DATA               [   COPY public.monedavirtual_banco (id, bco, numero, tipo, ident, names, usua_id) FROM stdin;
    public       postgres    false    216    E      ,          0    32971    monedavirtual_monedavirtual 
   TABLE DATA               V   COPY public.monedavirtual_monedavirtual (fecha, precio_bs, precio_divisa) FROM stdin;
    public       postgres    false    217   =E      .          0    32978    monedavirtual_transaccion 
   TABLE DATA               �   COPY public.monedavirtual_transaccion (id, fecha, monto, tipo, estado, bco, ref, descripcion, bco_retiro_id, usua_id) FROM stdin;
    public       postgres    false    219   ZE      %          0    32888    usuario_type_user 
   TABLE DATA               N   COPY public.usuario_type_user (codigo, tipo_usuario, descripcion) FROM stdin;
    public       postgres    false    210   wE      "          0    32869    usuario_user 
   TABLE DATA               �   COPY public.usuario_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, city, location, birth_date, phone, balance, last_access, type_u_id) FROM stdin;
    public       postgres    false    207   �E      $          0    32882    usuario_user_groups 
   TABLE DATA               D   COPY public.usuario_user_groups (id, user_id, group_id) FROM stdin;
    public       postgres    false    209   �F      '          0    32896    usuario_user_user_permissions 
   TABLE DATA               S   COPY public.usuario_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public       postgres    false    212   �F      \           0    0    apuesta_apuesta_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.apuesta_apuesta_id_seq', 1, false);
            public       postgres    false    233            ]           0    0    apuesta_detalleapuesta_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.apuesta_detalleapuesta_id_seq', 1, false);
            public       postgres    false    235            ^           0    0    apuesta_tipoapuesta_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.apuesta_tipoapuesta_id_seq', 1, false);
            public       postgres    false    237            _           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
            public       postgres    false    202            `           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
            public       postgres    false    204            a           0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 84, true);
            public       postgres    false    200            b           0    0    caballo_caballo_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.caballo_caballo_id_seq', 1, false);
            public       postgres    false    226            c           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);
            public       postgres    false    213            d           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 21, true);
            public       postgres    false    198            e           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 28, true);
            public       postgres    false    196            f           0    0    entrenador_entrenador_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.entrenador_entrenador_id_seq', 1, false);
            public       postgres    false    224            g           0    0    hipodromo_hipodromo_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.hipodromo_hipodromo_id_seq', 1, false);
            public       postgres    false    222            h           0    0    jockey_jockey_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.jockey_jockey_id_seq', 1, false);
            public       postgres    false    220            i           0    0    jornada_job_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.jornada_job_id_seq', 1, false);
            public       postgres    false    230            j           0    0    monedavirtual_banco_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.monedavirtual_banco_id_seq', 1, false);
            public       postgres    false    215            k           0    0     monedavirtual_transaccion_id_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public.monedavirtual_transaccion_id_seq', 1, false);
            public       postgres    false    218            l           0    0    usuario_user_groups_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.usuario_user_groups_id_seq', 1, false);
            public       postgres    false    208            m           0    0    usuario_user_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.usuario_user_id_seq', 2, true);
            public       postgres    false    206            n           0    0 $   usuario_user_user_permissions_id_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('public.usuario_user_user_permissions_id_seq', 1, false);
            public       postgres    false    211            u           2606    33099 $   apuesta_apuesta apuesta_apuesta_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.apuesta_apuesta
    ADD CONSTRAINT apuesta_apuesta_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.apuesta_apuesta DROP CONSTRAINT apuesta_apuesta_pkey;
       public         postgres    false    234            {           2606    33107 2   apuesta_detalleapuesta apuesta_detalleapuesta_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.apuesta_detalleapuesta
    ADD CONSTRAINT apuesta_detalleapuesta_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.apuesta_detalleapuesta DROP CONSTRAINT apuesta_detalleapuesta_pkey;
       public         postgres    false    236            }           2606    33115 ,   apuesta_tipoapuesta apuesta_tipoapuesta_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.apuesta_tipoapuesta
    ADD CONSTRAINT apuesta_tipoapuesta_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.apuesta_tipoapuesta DROP CONSTRAINT apuesta_tipoapuesta_pkey;
       public         postgres    false    238            &           2606    32835    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public         postgres    false    203            +           2606    32864 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public         postgres    false    205    205            .           2606    32843 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public         postgres    false    205            (           2606    32833    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public         postgres    false    203            !           2606    32850 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public         postgres    false    201    201            #           2606    32825 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public         postgres    false    201            [           2606    33021 $   caballo_caballo caballo_caballo_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.caballo_caballo
    ADD CONSTRAINT caballo_caballo_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.caballo_caballo DROP CONSTRAINT caballo_caballo_pkey;
       public         postgres    false    227            G           2606    32950 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public         postgres    false    214                       2606    32817 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public         postgres    false    199    199                       2606    32815 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public         postgres    false    199                       2606    32807 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public         postgres    false    197            �           2606    33185 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public         postgres    false    239            W           2606    33013 0   entrenador_entrenador entrenador_entrenador_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.entrenador_entrenador
    ADD CONSTRAINT entrenador_entrenador_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.entrenador_entrenador DROP CONSTRAINT entrenador_entrenador_pkey;
       public         postgres    false    225            U           2606    33005 ,   hipodromo_hipodromo hipodromo_hipodromo_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.hipodromo_hipodromo
    ADD CONSTRAINT hipodromo_hipodromo_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.hipodromo_hipodromo DROP CONSTRAINT hipodromo_hipodromo_pkey;
       public         postgres    false    223            S           2606    32997     jockey_jockey jockey_jockey_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.jockey_jockey
    ADD CONSTRAINT jockey_jockey_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.jockey_jockey DROP CONSTRAINT jockey_jockey_pkey;
       public         postgres    false    221            `           2606    33038 $   jornada_carrera jornada_carrera_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.jornada_carrera
    ADD CONSTRAINT jornada_carrera_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.jornada_carrera DROP CONSTRAINT jornada_carrera_pkey;
       public         postgres    false    228            g           2606    33043 4   jornada_detallescarrera jornada_detallescarrera_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.jornada_detallescarrera
    ADD CONSTRAINT jornada_detallescarrera_pkey PRIMARY KEY (id);
 ^   ALTER TABLE ONLY public.jornada_detallescarrera DROP CONSTRAINT jornada_detallescarrera_pkey;
       public         postgres    false    229            i           2606    33051    jornada_job jornada_job_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.jornada_job
    ADD CONSTRAINT jornada_job_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.jornada_job DROP CONSTRAINT jornada_job_pkey;
       public         postgres    false    231            m           2606    33056 &   jornada_jornadah jornada_jornadah_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.jornada_jornadah
    ADD CONSTRAINT jornada_jornadah_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.jornada_jornadah DROP CONSTRAINT jornada_jornadah_pkey;
       public         postgres    false    232            J           2606    32970 ,   monedavirtual_banco monedavirtual_banco_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.monedavirtual_banco
    ADD CONSTRAINT monedavirtual_banco_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.monedavirtual_banco DROP CONSTRAINT monedavirtual_banco_pkey;
       public         postgres    false    216            M           2606    32975 <   monedavirtual_monedavirtual monedavirtual_monedavirtual_pkey 
   CONSTRAINT     }   ALTER TABLE ONLY public.monedavirtual_monedavirtual
    ADD CONSTRAINT monedavirtual_monedavirtual_pkey PRIMARY KEY (fecha);
 f   ALTER TABLE ONLY public.monedavirtual_monedavirtual DROP CONSTRAINT monedavirtual_monedavirtual_pkey;
       public         postgres    false    217            P           2606    32983 8   monedavirtual_transaccion monedavirtual_transaccion_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.monedavirtual_transaccion
    ADD CONSTRAINT monedavirtual_transaccion_pkey PRIMARY KEY (id);
 b   ALTER TABLE ONLY public.monedavirtual_transaccion DROP CONSTRAINT monedavirtual_transaccion_pkey;
       public         postgres    false    219            >           2606    32892 (   usuario_type_user usuario_type_user_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.usuario_type_user
    ADD CONSTRAINT usuario_type_user_pkey PRIMARY KEY (codigo);
 R   ALTER TABLE ONLY public.usuario_type_user DROP CONSTRAINT usuario_type_user_pkey;
       public         postgres    false    210            8           2606    32887 ,   usuario_user_groups usuario_user_groups_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.usuario_user_groups
    ADD CONSTRAINT usuario_user_groups_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.usuario_user_groups DROP CONSTRAINT usuario_user_groups_pkey;
       public         postgres    false    209            ;           2606    32914 F   usuario_user_groups usuario_user_groups_user_id_group_id_1b0807de_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.usuario_user_groups
    ADD CONSTRAINT usuario_user_groups_user_id_group_id_1b0807de_uniq UNIQUE (user_id, group_id);
 p   ALTER TABLE ONLY public.usuario_user_groups DROP CONSTRAINT usuario_user_groups_user_id_group_id_1b0807de_uniq;
       public         postgres    false    209    209            0           2606    32877    usuario_user usuario_user_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.usuario_user
    ADD CONSTRAINT usuario_user_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.usuario_user DROP CONSTRAINT usuario_user_pkey;
       public         postgres    false    207            @           2606    32936 Z   usuario_user_user_permissions usuario_user_user_permis_user_id_permission_id_d74a6945_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.usuario_user_user_permissions
    ADD CONSTRAINT usuario_user_user_permis_user_id_permission_id_d74a6945_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.usuario_user_user_permissions DROP CONSTRAINT usuario_user_user_permis_user_id_permission_id_d74a6945_uniq;
       public         postgres    false    212    212            C           2606    32901 @   usuario_user_user_permissions usuario_user_user_permissions_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.usuario_user_user_permissions
    ADD CONSTRAINT usuario_user_user_permissions_pkey PRIMARY KEY (id);
 j   ALTER TABLE ONLY public.usuario_user_user_permissions DROP CONSTRAINT usuario_user_user_permissions_pkey;
       public         postgres    false    212            5           2606    32879 &   usuario_user usuario_user_username_key 
   CONSTRAINT     e   ALTER TABLE ONLY public.usuario_user
    ADD CONSTRAINT usuario_user_username_key UNIQUE (username);
 P   ALTER TABLE ONLY public.usuario_user DROP CONSTRAINT usuario_user_username_key;
       public         postgres    false    207            n           1259    33134 )   apuesta_apuesta_idTransGanada_id_676976ba    INDEX     u   CREATE INDEX "apuesta_apuesta_idTransGanada_id_676976ba" ON public.apuesta_apuesta USING btree ("idTransGanada_id");
 ?   DROP INDEX public."apuesta_apuesta_idTransGanada_id_676976ba";
       public         postgres    false    234            o           1259    33128 #   apuesta_apuesta_idTrans_id_f5603775    INDEX     i   CREATE INDEX "apuesta_apuesta_idTrans_id_f5603775" ON public.apuesta_apuesta USING btree ("idTrans_id");
 9   DROP INDEX public."apuesta_apuesta_idTrans_id_f5603775";
       public         postgres    false    234            p           1259    33140 #   apuesta_apuesta_id_carr_id_42bddbb7    INDEX     e   CREATE INDEX apuesta_apuesta_id_carr_id_42bddbb7 ON public.apuesta_apuesta USING btree (id_carr_id);
 7   DROP INDEX public.apuesta_apuesta_id_carr_id_42bddbb7;
       public         postgres    false    234            q           1259    33141 (   apuesta_apuesta_id_carr_id_42bddbb7_like    INDEX     ~   CREATE INDEX apuesta_apuesta_id_carr_id_42bddbb7_like ON public.apuesta_apuesta USING btree (id_carr_id varchar_pattern_ops);
 <   DROP INDEX public.apuesta_apuesta_id_carr_id_42bddbb7_like;
       public         postgres    false    234            r           1259    33147 #   apuesta_apuesta_id_jorh_id_509cf45a    INDEX     e   CREATE INDEX apuesta_apuesta_id_jorh_id_509cf45a ON public.apuesta_apuesta USING btree (id_jorh_id);
 7   DROP INDEX public.apuesta_apuesta_id_jorh_id_509cf45a;
       public         postgres    false    234            s           1259    33148 (   apuesta_apuesta_id_jorh_id_509cf45a_like    INDEX     ~   CREATE INDEX apuesta_apuesta_id_jorh_id_509cf45a_like ON public.apuesta_apuesta USING btree (id_jorh_id varchar_pattern_ops);
 <   DROP INDEX public.apuesta_apuesta_id_jorh_id_509cf45a_like;
       public         postgres    false    234            v           1259    33154 $   apuesta_apuesta_tApuesta_id_33fe5dc8    INDEX     k   CREATE INDEX "apuesta_apuesta_tApuesta_id_33fe5dc8" ON public.apuesta_apuesta USING btree ("tApuesta_id");
 :   DROP INDEX public."apuesta_apuesta_tApuesta_id_33fe5dc8";
       public         postgres    false    234            w           1259    33160 #   apuesta_apuesta_usuario_id_b32484da    INDEX     e   CREATE INDEX apuesta_apuesta_usuario_id_b32484da ON public.apuesta_apuesta USING btree (usuario_id);
 7   DROP INDEX public.apuesta_apuesta_usuario_id_b32484da;
       public         postgres    false    234            x           1259    33126 (   apuesta_detalleapuesta_id_ap_id_9b815e8f    INDEX     o   CREATE INDEX apuesta_detalleapuesta_id_ap_id_9b815e8f ON public.apuesta_detalleapuesta USING btree (id_ap_id);
 <   DROP INDEX public.apuesta_detalleapuesta_id_ap_id_9b815e8f;
       public         postgres    false    236            y           1259    33127 )   apuesta_detalleapuesta_id_cab_id_28626398    INDEX     q   CREATE INDEX apuesta_detalleapuesta_id_cab_id_28626398 ON public.apuesta_detalleapuesta USING btree (id_cab_id);
 =   DROP INDEX public.apuesta_detalleapuesta_id_cab_id_28626398;
       public         postgres    false    236            $           1259    32852    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public         postgres    false    203            )           1259    32865 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public         postgres    false    205            ,           1259    32866 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public         postgres    false    205                       1259    32851 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public         postgres    false    201            X           1259    33032 $   caballo_caballo_id_entre_id_ba9f9419    INDEX     g   CREATE INDEX caballo_caballo_id_entre_id_ba9f9419 ON public.caballo_caballo USING btree (id_entre_id);
 8   DROP INDEX public.caballo_caballo_id_entre_id_ba9f9419;
       public         postgres    false    227            Y           1259    33033 "   caballo_caballo_id_hip_id_2a75ba16    INDEX     c   CREATE INDEX caballo_caballo_id_hip_id_2a75ba16 ON public.caballo_caballo USING btree (id_hip_id);
 6   DROP INDEX public.caballo_caballo_id_hip_id_2a75ba16;
       public         postgres    false    227            E           1259    32961 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public         postgres    false    214            H           1259    32962 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public         postgres    false    214            ~           1259    33187 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public         postgres    false    239            �           1259    33186 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public         postgres    false    239            \           1259    33057     jornada_carrera_id_f4ae2333_like    INDEX     n   CREATE INDEX jornada_carrera_id_f4ae2333_like ON public.jornada_carrera USING btree (id varchar_pattern_ops);
 4   DROP INDEX public.jornada_carrera_id_f4ae2333_like;
       public         postgres    false    228            ]           1259    33085 !   jornada_carrera_id_jh_id_80f401d5    INDEX     a   CREATE INDEX jornada_carrera_id_jh_id_80f401d5 ON public.jornada_carrera USING btree (id_jh_id);
 5   DROP INDEX public.jornada_carrera_id_jh_id_80f401d5;
       public         postgres    false    228            ^           1259    33086 &   jornada_carrera_id_jh_id_80f401d5_like    INDEX     z   CREATE INDEX jornada_carrera_id_jh_id_80f401d5_like ON public.jornada_carrera USING btree (id_jh_id varchar_pattern_ops);
 :   DROP INDEX public.jornada_carrera_id_jh_id_80f401d5_like;
       public         postgres    false    228            a           1259    33073 (   jornada_detallescarrera_id_862a6587_like    INDEX     ~   CREATE INDEX jornada_detallescarrera_id_862a6587_like ON public.jornada_detallescarrera USING btree (id varchar_pattern_ops);
 <   DROP INDEX public.jornada_detallescarrera_id_862a6587_like;
       public         postgres    false    229            b           1259    33074 +   jornada_detallescarrera_id_caba_id_02e7bc0e    INDEX     u   CREATE INDEX jornada_detallescarrera_id_caba_id_02e7bc0e ON public.jornada_detallescarrera USING btree (id_caba_id);
 ?   DROP INDEX public.jornada_detallescarrera_id_caba_id_02e7bc0e;
       public         postgres    false    229            c           1259    33075 +   jornada_detallescarrera_id_carr_id_42d36e41    INDEX     u   CREATE INDEX jornada_detallescarrera_id_carr_id_42d36e41 ON public.jornada_detallescarrera USING btree (id_carr_id);
 ?   DROP INDEX public.jornada_detallescarrera_id_carr_id_42d36e41;
       public         postgres    false    229            d           1259    33076 0   jornada_detallescarrera_id_carr_id_42d36e41_like    INDEX     �   CREATE INDEX jornada_detallescarrera_id_carr_id_42d36e41_like ON public.jornada_detallescarrera USING btree (id_carr_id varchar_pattern_ops);
 D   DROP INDEX public.jornada_detallescarrera_id_carr_id_42d36e41_like;
       public         postgres    false    229            e           1259    33077 +   jornada_detallescarrera_id_jock_id_31e169aa    INDEX     u   CREATE INDEX jornada_detallescarrera_id_jock_id_31e169aa ON public.jornada_detallescarrera USING btree (id_jock_id);
 ?   DROP INDEX public.jornada_detallescarrera_id_jock_id_31e169aa;
       public         postgres    false    229            j           1259    33083 !   jornada_jornadah_id_1c87c4b0_like    INDEX     p   CREATE INDEX jornada_jornadah_id_1c87c4b0_like ON public.jornada_jornadah USING btree (id varchar_pattern_ops);
 5   DROP INDEX public.jornada_jornadah_id_1c87c4b0_like;
       public         postgres    false    232            k           1259    33084 #   jornada_jornadah_id_hip_id_0fbd51c6    INDEX     e   CREATE INDEX jornada_jornadah_id_hip_id_0fbd51c6 ON public.jornada_jornadah USING btree (id_hip_id);
 7   DROP INDEX public.jornada_jornadah_id_hip_id_0fbd51c6;
       public         postgres    false    232            K           1259    33172 $   monedavirtual_banco_usua_id_186f71e0    INDEX     g   CREATE INDEX monedavirtual_banco_usua_id_186f71e0 ON public.monedavirtual_banco USING btree (usua_id);
 8   DROP INDEX public.monedavirtual_banco_usua_id_186f71e0;
       public         postgres    false    216            N           1259    32989 0   monedavirtual_transaccion_bco_retiro_id_1b1de41e    INDEX        CREATE INDEX monedavirtual_transaccion_bco_retiro_id_1b1de41e ON public.monedavirtual_transaccion USING btree (bco_retiro_id);
 D   DROP INDEX public.monedavirtual_transaccion_bco_retiro_id_1b1de41e;
       public         postgres    false    219            Q           1259    33166 *   monedavirtual_transaccion_usua_id_22d2f0d3    INDEX     s   CREATE INDEX monedavirtual_transaccion_usua_id_22d2f0d3 ON public.monedavirtual_transaccion USING btree (usua_id);
 >   DROP INDEX public.monedavirtual_transaccion_usua_id_22d2f0d3;
       public         postgres    false    219            <           1259    32917 &   usuario_type_user_codigo_07b94284_like    INDEX     z   CREATE INDEX usuario_type_user_codigo_07b94284_like ON public.usuario_type_user USING btree (codigo varchar_pattern_ops);
 :   DROP INDEX public.usuario_type_user_codigo_07b94284_like;
       public         postgres    false    210            6           1259    32916 %   usuario_user_groups_group_id_e313e18d    INDEX     i   CREATE INDEX usuario_user_groups_group_id_e313e18d ON public.usuario_user_groups USING btree (group_id);
 9   DROP INDEX public.usuario_user_groups_group_id_e313e18d;
       public         postgres    false    209            9           1259    32915 $   usuario_user_groups_user_id_1df7a96d    INDEX     g   CREATE INDEX usuario_user_groups_user_id_1df7a96d ON public.usuario_user_groups USING btree (user_id);
 8   DROP INDEX public.usuario_user_groups_user_id_1df7a96d;
       public         postgres    false    209            1           1259    32918    usuario_user_type_u_id_d03bca52    INDEX     ]   CREATE INDEX usuario_user_type_u_id_d03bca52 ON public.usuario_user USING btree (type_u_id);
 3   DROP INDEX public.usuario_user_type_u_id_d03bca52;
       public         postgres    false    207            2           1259    32919 $   usuario_user_type_u_id_d03bca52_like    INDEX     v   CREATE INDEX usuario_user_type_u_id_d03bca52_like ON public.usuario_user USING btree (type_u_id varchar_pattern_ops);
 8   DROP INDEX public.usuario_user_type_u_id_d03bca52_like;
       public         postgres    false    207            A           1259    32938 4   usuario_user_user_permissions_permission_id_fae57acd    INDEX     �   CREATE INDEX usuario_user_user_permissions_permission_id_fae57acd ON public.usuario_user_user_permissions USING btree (permission_id);
 H   DROP INDEX public.usuario_user_user_permissions_permission_id_fae57acd;
       public         postgres    false    212            D           1259    32937 .   usuario_user_user_permissions_user_id_bfc8eb29    INDEX     {   CREATE INDEX usuario_user_user_permissions_user_id_bfc8eb29 ON public.usuario_user_user_permissions USING btree (user_id);
 B   DROP INDEX public.usuario_user_user_permissions_user_id_bfc8eb29;
       public         postgres    false    212            3           1259    32902 #   usuario_user_username_53514836_like    INDEX     t   CREATE INDEX usuario_user_username_53514836_like ON public.usuario_user USING btree (username varchar_pattern_ops);
 7   DROP INDEX public.usuario_user_username_53514836_like;
       public         postgres    false    207            �           2606    33135 F   apuesta_apuesta apuesta_apuesta_idTransGanada_id_676976ba_fk_monedavir    FK CONSTRAINT     �   ALTER TABLE ONLY public.apuesta_apuesta
    ADD CONSTRAINT "apuesta_apuesta_idTransGanada_id_676976ba_fk_monedavir" FOREIGN KEY ("idTransGanada_id") REFERENCES public.monedavirtual_transaccion(id) DEFERRABLE INITIALLY DEFERRED;
 r   ALTER TABLE ONLY public.apuesta_apuesta DROP CONSTRAINT "apuesta_apuesta_idTransGanada_id_676976ba_fk_monedavir";
       public       postgres    false    2896    219    234            �           2606    33129 @   apuesta_apuesta apuesta_apuesta_idTrans_id_f5603775_fk_monedavir    FK CONSTRAINT     �   ALTER TABLE ONLY public.apuesta_apuesta
    ADD CONSTRAINT "apuesta_apuesta_idTrans_id_f5603775_fk_monedavir" FOREIGN KEY ("idTrans_id") REFERENCES public.monedavirtual_transaccion(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.apuesta_apuesta DROP CONSTRAINT "apuesta_apuesta_idTrans_id_f5603775_fk_monedavir";
       public       postgres    false    2896    234    219            �           2606    33142 I   apuesta_apuesta apuesta_apuesta_id_carr_id_42bddbb7_fk_jornada_carrera_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.apuesta_apuesta
    ADD CONSTRAINT apuesta_apuesta_id_carr_id_42bddbb7_fk_jornada_carrera_id FOREIGN KEY (id_carr_id) REFERENCES public.jornada_carrera(id) DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public.apuesta_apuesta DROP CONSTRAINT apuesta_apuesta_id_carr_id_42bddbb7_fk_jornada_carrera_id;
       public       postgres    false    234    2912    228            �           2606    33149 J   apuesta_apuesta apuesta_apuesta_id_jorh_id_509cf45a_fk_jornada_jornadah_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.apuesta_apuesta
    ADD CONSTRAINT apuesta_apuesta_id_jorh_id_509cf45a_fk_jornada_jornadah_id FOREIGN KEY (id_jorh_id) REFERENCES public.jornada_jornadah(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.apuesta_apuesta DROP CONSTRAINT apuesta_apuesta_id_jorh_id_509cf45a_fk_jornada_jornadah_id;
       public       postgres    false    2925    232    234            �           2606    33155 N   apuesta_apuesta apuesta_apuesta_tApuesta_id_33fe5dc8_fk_apuesta_tipoapuesta_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.apuesta_apuesta
    ADD CONSTRAINT "apuesta_apuesta_tApuesta_id_33fe5dc8_fk_apuesta_tipoapuesta_id" FOREIGN KEY ("tApuesta_id") REFERENCES public.apuesta_tipoapuesta(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.apuesta_apuesta DROP CONSTRAINT "apuesta_apuesta_tApuesta_id_33fe5dc8_fk_apuesta_tipoapuesta_id";
       public       postgres    false    2941    234    238            �           2606    33161 F   apuesta_apuesta apuesta_apuesta_usuario_id_b32484da_fk_usuario_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.apuesta_apuesta
    ADD CONSTRAINT apuesta_apuesta_usuario_id_b32484da_fk_usuario_user_id FOREIGN KEY (usuario_id) REFERENCES public.usuario_user(id) DEFERRABLE INITIALLY DEFERRED;
 p   ALTER TABLE ONLY public.apuesta_apuesta DROP CONSTRAINT apuesta_apuesta_usuario_id_b32484da_fk_usuario_user_id;
       public       postgres    false    234    207    2864            �           2606    33116 U   apuesta_detalleapuesta apuesta_detalleapuesta_id_ap_id_9b815e8f_fk_apuesta_apuesta_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.apuesta_detalleapuesta
    ADD CONSTRAINT apuesta_detalleapuesta_id_ap_id_9b815e8f_fk_apuesta_apuesta_id FOREIGN KEY (id_ap_id) REFERENCES public.apuesta_apuesta(id) DEFERRABLE INITIALLY DEFERRED;
    ALTER TABLE ONLY public.apuesta_detalleapuesta DROP CONSTRAINT apuesta_detalleapuesta_id_ap_id_9b815e8f_fk_apuesta_apuesta_id;
       public       postgres    false    236    234    2933            �           2606    33121 V   apuesta_detalleapuesta apuesta_detalleapuesta_id_cab_id_28626398_fk_caballo_caballo_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.apuesta_detalleapuesta
    ADD CONSTRAINT apuesta_detalleapuesta_id_cab_id_28626398_fk_caballo_caballo_id FOREIGN KEY (id_cab_id) REFERENCES public.caballo_caballo(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.apuesta_detalleapuesta DROP CONSTRAINT apuesta_detalleapuesta_id_cab_id_28626398_fk_caballo_caballo_id;
       public       postgres    false    236    227    2907            �           2606    32858 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public       postgres    false    2851    201    205            �           2606    32853 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public       postgres    false    205    203    2856            �           2606    32844 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public       postgres    false    199    2846    201            �           2606    33022 A   caballo_caballo caballo_caballo_id_entre_id_ba9f9419_fk_entrenado    FK CONSTRAINT     �   ALTER TABLE ONLY public.caballo_caballo
    ADD CONSTRAINT caballo_caballo_id_entre_id_ba9f9419_fk_entrenado FOREIGN KEY (id_entre_id) REFERENCES public.entrenador_entrenador(id) DEFERRABLE INITIALLY DEFERRED;
 k   ALTER TABLE ONLY public.caballo_caballo DROP CONSTRAINT caballo_caballo_id_entre_id_ba9f9419_fk_entrenado;
       public       postgres    false    227    2903    225            �           2606    33027 L   caballo_caballo caballo_caballo_id_hip_id_2a75ba16_fk_hipodromo_hipodromo_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.caballo_caballo
    ADD CONSTRAINT caballo_caballo_id_hip_id_2a75ba16_fk_hipodromo_hipodromo_id FOREIGN KEY (id_hip_id) REFERENCES public.hipodromo_hipodromo(id) DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.caballo_caballo DROP CONSTRAINT caballo_caballo_id_hip_id_2a75ba16_fk_hipodromo_hipodromo_id;
       public       postgres    false    2901    227    223            �           2606    32951 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public       postgres    false    2846    214    199            �           2606    32956 E   django_admin_log django_admin_log_user_id_c564eba6_fk_usuario_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_usuario_user_id FOREIGN KEY (user_id) REFERENCES public.usuario_user(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_usuario_user_id;
       public       postgres    false    207    2864    214            �           2606    33087 H   jornada_carrera jornada_carrera_id_jh_id_80f401d5_fk_jornada_jornadah_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.jornada_carrera
    ADD CONSTRAINT jornada_carrera_id_jh_id_80f401d5_fk_jornada_jornadah_id FOREIGN KEY (id_jh_id) REFERENCES public.jornada_jornadah(id) DEFERRABLE INITIALLY DEFERRED;
 r   ALTER TABLE ONLY public.jornada_carrera DROP CONSTRAINT jornada_carrera_id_jh_id_80f401d5_fk_jornada_jornadah_id;
       public       postgres    false    2925    232    228            �           2606    33058 M   jornada_detallescarrera jornada_detallescarr_id_caba_id_02e7bc0e_fk_caballo_c    FK CONSTRAINT     �   ALTER TABLE ONLY public.jornada_detallescarrera
    ADD CONSTRAINT jornada_detallescarr_id_caba_id_02e7bc0e_fk_caballo_c FOREIGN KEY (id_caba_id) REFERENCES public.caballo_caballo(id) DEFERRABLE INITIALLY DEFERRED;
 w   ALTER TABLE ONLY public.jornada_detallescarrera DROP CONSTRAINT jornada_detallescarr_id_caba_id_02e7bc0e_fk_caballo_c;
       public       postgres    false    229    227    2907            �           2606    33063 M   jornada_detallescarrera jornada_detallescarr_id_carr_id_42d36e41_fk_jornada_c    FK CONSTRAINT     �   ALTER TABLE ONLY public.jornada_detallescarrera
    ADD CONSTRAINT jornada_detallescarr_id_carr_id_42d36e41_fk_jornada_c FOREIGN KEY (id_carr_id) REFERENCES public.jornada_carrera(id) DEFERRABLE INITIALLY DEFERRED;
 w   ALTER TABLE ONLY public.jornada_detallescarrera DROP CONSTRAINT jornada_detallescarr_id_carr_id_42d36e41_fk_jornada_c;
       public       postgres    false    2912    229    228            �           2606    33068 W   jornada_detallescarrera jornada_detallescarrera_id_jock_id_31e169aa_fk_jockey_jockey_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.jornada_detallescarrera
    ADD CONSTRAINT jornada_detallescarrera_id_jock_id_31e169aa_fk_jockey_jockey_id FOREIGN KEY (id_jock_id) REFERENCES public.jockey_jockey(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.jornada_detallescarrera DROP CONSTRAINT jornada_detallescarrera_id_jock_id_31e169aa_fk_jockey_jockey_id;
       public       postgres    false    229    221    2899            �           2606    33078 N   jornada_jornadah jornada_jornadah_id_hip_id_0fbd51c6_fk_hipodromo_hipodromo_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.jornada_jornadah
    ADD CONSTRAINT jornada_jornadah_id_hip_id_0fbd51c6_fk_hipodromo_hipodromo_id FOREIGN KEY (id_hip_id) REFERENCES public.hipodromo_hipodromo(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.jornada_jornadah DROP CONSTRAINT jornada_jornadah_id_hip_id_0fbd51c6_fk_hipodromo_hipodromo_id;
       public       postgres    false    232    2901    223            �           2606    33173 K   monedavirtual_banco monedavirtual_banco_usua_id_186f71e0_fk_usuario_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.monedavirtual_banco
    ADD CONSTRAINT monedavirtual_banco_usua_id_186f71e0_fk_usuario_user_id FOREIGN KEY (usua_id) REFERENCES public.usuario_user(id) DEFERRABLE INITIALLY DEFERRED;
 u   ALTER TABLE ONLY public.monedavirtual_banco DROP CONSTRAINT monedavirtual_banco_usua_id_186f71e0_fk_usuario_user_id;
       public       postgres    false    207    216    2864            �           2606    32984 R   monedavirtual_transaccion monedavirtual_transa_bco_retiro_id_1b1de41e_fk_monedavir    FK CONSTRAINT     �   ALTER TABLE ONLY public.monedavirtual_transaccion
    ADD CONSTRAINT monedavirtual_transa_bco_retiro_id_1b1de41e_fk_monedavir FOREIGN KEY (bco_retiro_id) REFERENCES public.monedavirtual_banco(id) DEFERRABLE INITIALLY DEFERRED;
 |   ALTER TABLE ONLY public.monedavirtual_transaccion DROP CONSTRAINT monedavirtual_transa_bco_retiro_id_1b1de41e_fk_monedavir;
       public       postgres    false    219    2890    216            �           2606    33167 W   monedavirtual_transaccion monedavirtual_transaccion_usua_id_22d2f0d3_fk_usuario_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.monedavirtual_transaccion
    ADD CONSTRAINT monedavirtual_transaccion_usua_id_22d2f0d3_fk_usuario_user_id FOREIGN KEY (usua_id) REFERENCES public.usuario_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.monedavirtual_transaccion DROP CONSTRAINT monedavirtual_transaccion_usua_id_22d2f0d3_fk_usuario_user_id;
       public       postgres    false    2864    207    219            �           2606    32908 J   usuario_user_groups usuario_user_groups_group_id_e313e18d_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.usuario_user_groups
    ADD CONSTRAINT usuario_user_groups_group_id_e313e18d_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.usuario_user_groups DROP CONSTRAINT usuario_user_groups_group_id_e313e18d_fk_auth_group_id;
       public       postgres    false    2856    209    203            �           2606    32903 K   usuario_user_groups usuario_user_groups_user_id_1df7a96d_fk_usuario_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.usuario_user_groups
    ADD CONSTRAINT usuario_user_groups_user_id_1df7a96d_fk_usuario_user_id FOREIGN KEY (user_id) REFERENCES public.usuario_user(id) DEFERRABLE INITIALLY DEFERRED;
 u   ALTER TABLE ONLY public.usuario_user_groups DROP CONSTRAINT usuario_user_groups_user_id_1df7a96d_fk_usuario_user_id;
       public       postgres    false    209    207    2864            �           2606    33194 H   usuario_user usuario_user_type_u_id_d03bca52_fk_usuario_type_user_codigo    FK CONSTRAINT     �   ALTER TABLE ONLY public.usuario_user
    ADD CONSTRAINT usuario_user_type_u_id_d03bca52_fk_usuario_type_user_codigo FOREIGN KEY (type_u_id) REFERENCES public.usuario_type_user(codigo) DEFERRABLE INITIALLY DEFERRED;
 r   ALTER TABLE ONLY public.usuario_user DROP CONSTRAINT usuario_user_type_u_id_d03bca52_fk_usuario_type_user_codigo;
       public       postgres    false    210    2878    207            �           2606    32930 V   usuario_user_user_permissions usuario_user_user_pe_permission_id_fae57acd_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.usuario_user_user_permissions
    ADD CONSTRAINT usuario_user_user_pe_permission_id_fae57acd_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.usuario_user_user_permissions DROP CONSTRAINT usuario_user_user_pe_permission_id_fae57acd_fk_auth_perm;
       public       postgres    false    201    2851    212            �           2606    32925 P   usuario_user_user_permissions usuario_user_user_pe_user_id_bfc8eb29_fk_usuario_u    FK CONSTRAINT     �   ALTER TABLE ONLY public.usuario_user_user_permissions
    ADD CONSTRAINT usuario_user_user_pe_user_id_bfc8eb29_fk_usuario_u FOREIGN KEY (user_id) REFERENCES public.usuario_user(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.usuario_user_user_permissions DROP CONSTRAINT usuario_user_user_pe_user_id_bfc8eb29_fk_usuario_u;
       public       postgres    false    2864    207    212            =      x������ � �      ?      x������ � �      A      x������ � �            x������ � �             x������ � �         !  x�m�A��0E��)8�'$��\��V �a�NPz��')���v��J�b����۴����mb7O�<���4�!�K�}E�RI���s��	�TRpG��5�l)(T��=��q���+HM��r ��a�,v��@���b�5�+I�~���ry��	�)#��H�* �.���wӼv��y�nG"\Z*>��
f+�+��Y�ZEW4�ۈ���V$�#�VV��`c��[US��	������zW�%L#_@��+�1H�by�2f2�PZ��h�DĮ=��kHJ�� �j� ̂6! �4-�)�\��y�{�'Q��`9�4(�¢,iP����4%����t�K_B4�`�Ab��B2h�9�8�n�'�A��/�x�����O�pr���ڣ&�5f����4�8*�ރ\��û.�}i���k�xi4�y�F_��T��?�P����M�I��y����y��y~o��fy�繃��Ü�vsq��M����(`8��h@��QF�e@�˘&��v�ޅ�b��WX�ȃ0�Ì��$��ﾋ���u��ͅ��*}�x�`�U�䵉���6�ym�/X5h������tZ^��S�5g� yY�,��Ɋ&o`5�1.��e��k�G�f�D@B2�J�0��$�f5%������*�5�$�z)IA8/��&+���RP���q��'� <�$�@l(��p,'�I���KM_{�[{iK��M^��	zӆvnۛ�i�׵��͏���Zj�b�Vt>�s�j�g�6� ��t>���{�Ts|�      6      x������ � �      )      x������ � �         �   x�]P�n�0}�?f���_&M&X%��I&��m�X����܍>��7	�fl�s�a}�^���4Ox �!��4O����W�'p��0�x�e���6/��I;�Q�^��[� �
���e��#Q�:Ie��55�k�����H5H�?�R�ZN��o�?�tz��q���r3�!��浠ҥ��M_O�
<e��W�fW��!5�������@�_ ��           x���ݮ� ���S����Y&!�2-3*=�����Zsj�7&��o��%�r]4]���	cL��l��A�Iy�p$�g
g�'����ޔ��i�ݨ��oT�[��*��,�(�}�ng�Iʳ��
P��ƫ����n��Z�O5����VQl*^�(:����ն٦I�L�3�-)�1��n1�#
*)�1#�%��!��]l�o>,��9Cxr㫷~�c�I�}`��(g�����::��ke�w^�&}1��r�	�3N��fkǂ�N2�ʷ�BI:� ���޺��q.&U
j��n[#@�I%쥁�cr�?����qy��*GGH��${���3���U]��>"X��`��3��[�4��4��L����y���&���\�]�cݒ�i��9M�k�w9wU��n��J̦���R$k��'���Tҷބ�CE��!]����,�@J����Qq�DN �����CM�^U��x���&�� �(������H2N��by�V�����9<
�@��7 ��S�����p8� ���      B      x������ � �      4      x������ � �      2      x������ � �      0      x������ � �      7      x������ � �      8      x������ � �      :      x������ � �      ;      x������ � �      +      x������ � �      ,      x������ � �      .      x������ � �      %   T   x�KL����4�tљ�%E�)�E\�yɉE�F��
ΉEE�E\@^^1�1�dH4���8��ӄ3��4�(3_�� ��ld� U�%�      "   �   x�����0D��W�`�!UHLX���	��P�
�~��'�;s��W����k`��(#&V�J�Ҡ=n�ē<ju���2��������a��� ��[^KN�[�<E��D ��-�~ ��]�j��ӆ��ل�ԛ�s���q����MF47����VO�;��5/      $      x������ � �      '      x������ � �     