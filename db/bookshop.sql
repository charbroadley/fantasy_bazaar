DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    status BOOLEAN
);

CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_id INT NOT NULL REFERENCES authors(id),
    genre VARCHAR(255),
    description TEXT,
    stock_quantity INT,
    buying_cost INT,
    selling_price INT
);