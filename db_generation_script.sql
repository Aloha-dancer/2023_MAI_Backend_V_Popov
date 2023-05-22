begin;
create table if not exists public.product(
	product_id serial primary key,
	product_name varchar(100) unique not null,
	price int not null,	
	country_id int,
	is_discounted bool,
	discont_start timestamp,
	discont_end timestamp,
	date_added timestamp not null
);

create table if not exists users(
	user_id serial primary key,
	login varchar(30) not null,
	password varchar(30) not null,
	age smallint not null,
	country_id int unique,
	user_name varchar(30),
	first_name varchar(30)
);

create table if not exists company(
	company_id serial primary key,
	company_name varchar(30) not null,
	country_id int unique,
	location varchar(100),
	manager varchar(150) not null
);
savepoint first;
create table if not exists country(
	country_id serial primary key,
	country_name varchar(100) not null,
	constraint fk_country_user foreign key (country_id) references users(country_id),
	constraint fk_country_company foreign key (country_id) references company(country_id)
);

create table if not exists product_company_rel(
	product_id int references product(product_id) on update cascade on delete cascade,
	company_id int references company(company_id) on update cascade on delete cascade,
	sell_percent real,
	constraint product_company_pkey primary key (product_id, company_id)
);

create table if not exists sales(
	user_id int not null,
	product_list text[] not null,
	total_price bigint not null
);

create table if not exists user_product_rel(
	user_id int references users(user_id) on update cascade on delete cascade,
	product_id int references product(product_id) on update cascade on delete cascade,
	constraint product_user_pkey primary key (user_id, product_id)
);
commit;
end;

begin;
alter table sales add constraint fk_sale_user foreign key (user_id) references users(user_id);
commit;
end;