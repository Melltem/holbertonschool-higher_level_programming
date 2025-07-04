-- Create table 'id_not_null' with 'id' defaulting to 1 and 'name' column, do not fail if table exists
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
