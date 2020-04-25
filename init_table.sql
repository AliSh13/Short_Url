USE short_link;

CREATE TABLE IF NOT EXISTS users
(
    id INT primary key AUTO_INCREMENT,
    username VARCHAR(30),
    email VARCHAR(30) UNIQUE,
    password_hash TEXT
);

CREATE TABLE IF NOT EXISTS urls
(
    id INT primary key AUTO_INCREMENT,
    url TEXT ,
    sh_url VARCHAR(30) UNIQUE,
    tag VARCHAR(50),
    user_id INT not null,
    constraint urls_user_id_fk
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS statistic
(
    id INT primary key AUTO_INCREMENT,
    url_id INT not null,
    user_id INT not null,
    counter INT ,
    chrome INT ,
    firefox INT ,
    yandex INT ,
    opera INT ,
    other_br INT ,
    android INT ,
    windows INT ,
    mac INT ,
    linux INT ,
    other_pl INT,
    date_use TIMESTAMP,
     constraint statistic_users_id_fk
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
     constraint statistic_urls_id_fk
            FOREIGN KEY (url_id) REFERENCES urls (id) ON DELETE CASCADE
);
