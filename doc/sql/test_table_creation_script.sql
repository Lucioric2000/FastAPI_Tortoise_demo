create table test_table
(
    item_name  varchar,
    item_value integer,
    id         integer not null
        constraint test_table_pk
            primary key
);