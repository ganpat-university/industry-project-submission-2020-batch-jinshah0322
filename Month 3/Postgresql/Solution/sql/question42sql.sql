INSERT INTO employee (name, city_id, join_date) VALUES
('John Doe', 1, '2023-01-01'),
('Alice Smith', 2, '2023-02-01'),
('Bob Johnson', 3, '2023-03-01'),
('Emma Watson', 4, '2023-04-01'),
('Michael Davis', 5, '2023-05-01'),
('Sarah Lee', 6, '2023-06-01'),
('David Brown', 7, '2023-07-01'),
('Olivia Wilson', 8, '2023-08-01'),
('James Taylor', 9, '2023-09-01'),
('Sophia Martinez', 10, '2023-10-01'),
('Matthew Clark', 1, '2023-11-01'),
('Emily Rodriguez', 2, '2023-12-01'),
('Daniel Garcia', 3, '2024-01-01'),
('Madison Martinez', 4, '2024-02-01'),
('Ethan Wilson', 5, '2024-03-01');


update employee set join_date=current_date where city_id=(select city_id from city where name='Mumbai')