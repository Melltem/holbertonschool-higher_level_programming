-- Create table 'unique_id' with 'id' defaulting to 1 and unique, and 'name' column, do not fail if table exists
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
