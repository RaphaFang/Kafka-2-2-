CREATE DATABASE pc_db;
-- ---------------------------------------------------
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------------------------------------
CREATE TABLE Products (
    product_id VARCHAR(100) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    commerce VARCHAR(100) NOT NULL,
    original_id VARCHAR(50) NOT NULL,
    current_price NUMERIC(10, 2) NOT NULL,
    sold INT DEFAULT 0,
    info TEXT NOT NULL,
    info_url VARCHAR(255) NOT NULL,
    rating NUMERIC(3, 2) DEFAULT 0.0,
    rating_times INT DEFAULT 0,
    product_url VARCHAR(255) NOT NULL,
    img_list TEXT[] NOT NULL
);
-- ---------------------------------------------------

CREATE TABLE Watch_list (
    watch_list_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,  
    product_id VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,   -- 這邊是一個自動偵測刪除機制
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE
);

-- ---------------------------------------------------

CREATE TABLE Price_history (
    history_id SERIAL PRIMARY KEY,
    product_id VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE
);