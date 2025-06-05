-- Insert authors
INSERT INTO authors (author_id, first, last)
VALUES
('a1', 'George', 'Orwell'),
('a2', 'Jane', 'Austen'),
('a3', 'Harper', 'Lee');

-- Insert books
INSERT INTO books (book_id, title, year_published, author_id)
VALUES
('b1', '1984', 1949, 'a1'),
('b2', 'Pride and Prejudice', 1813, 'a2'),
('b3', 'To Kill a Mockingbird', 1960, 'a3');
