-- Create table 'force_name' with 'id' and 'name' (NOT NULL), do not fail if table already exists
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
