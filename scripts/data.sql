-- Insert data for User
INSERT INTO users (username, password) VALUES ('user', 'scrypt:32768:8:1$YbPK3ImaHTARze8L$2895b04bf4a253e2b35d1e56c9daa7f993779de128f1e6b9ebb9e03b8fb1c50daa2000993c86a074259d9e85b06f2b2553fda911d5dd977f53d0e18a7c271d54');

-- Insert data for Spaghetti Carbonara
INSERT INTO recipes (user_id, title, description, servings) VALUES 
(1, 'Spaghetti Carbonara', 'A classic Italian pasta dish made with eggs, cheese, pancetta, and pepper.', 4);

INSERT INTO ingredients (recipe_id, ingredient, quantity, units) VALUES 
(1, 'Spaghetti', '400', 'g'),
(1, 'Pancetta', '150', 'g'),
(1, 'Eggs', '4', ''),
(1, 'Parmesan cheese', '100', 'g'),
(1, 'Black pepper', '1', 'g'),
(1, 'Salt', '1', 'g');

INSERT INTO steps (recipe_id, step) VALUES 
(1, 'Cook the spaghetti according to the package instructions.'),
(1, 'Fry the pancetta in a pan until crispy.'),
(1, 'Beat the eggs in a bowl and mix in the grated Parmesan cheese.'),
(1, 'Drain the spaghetti and return it to the pot.'),
(1, 'Quickly mix in the egg and cheese mixture, along with the pancetta.'),
(1, 'Season with black pepper and salt, and serve immediately.');

INSERT INTO pictures (recipe_id, filename) VALUES 
(1, 'examples/carbonara.jpg');


-- Insert data for Chicken Tikka Masala
INSERT INTO recipes (user_id, title, description, servings) VALUES 
(1, 'Chicken Tikka Masala', 'A popular Indian curry dish made with marinated chicken cooked in a creamy tomato sauce.', 4);

INSERT INTO ingredients (recipe_id, ingredient, quantity, units) VALUES 
(2, 'Chicken breast', '500', 'g'),
(2, 'Yogurt', '200', 'g'),
(2, 'Garlic cloves', '3', ''),
(2, 'Ginger', '1', 'in'),
(2, 'Tomato puree', '200', 'g'),
(2, 'Cream', '100', 'ml'),
(2, 'Garam masala', '2' ,'tsp.'),
(2, 'Cumin', '1', 'tsp.'),
(2, 'Coriander', '1', 'tsp.'),
(2, 'Turmeric', '0.5', 'tsp.'),
(2, 'Salt', '1', 'g'),
(2, 'Cilantro (for garnish)', '1', 'tbsp.');

INSERT INTO steps (recipe_id, step) VALUES 
(2, 'Marinate the chicken with yogurt, minced garlic, minced ginger, and spices for at least 1 hour.'),
(2, 'Cook the marinated chicken in a pan until fully cooked.'),
(2, 'In another pan, cook the tomato puree with spices until fragrant.'),
(2, 'Add the cooked chicken and cream to the tomato sauce, and simmer for 10 minutes.'),
(2, 'Garnish with fresh cilantro and serve with rice or naan.');

INSERT INTO pictures (recipe_id, filename) VALUES 
(2, 'examples/masala.webp');


-- -- Insert data for Beef Tacos
INSERT INTO recipes (user_id, title, description, servings) VALUES 
(1, 'Beef Tacos', 'Mexican tacos filled with seasoned beef, lettuce, cheese, and salsa.', 3);

INSERT INTO ingredients (recipe_id, ingredient, quantity, units) VALUES 
(3, 'Ground beef', '500', 'g'),
(3, 'Taco seasoning', '2', 'tbsp.'),
(3, 'Taco shells', '8', ''),
(3, 'Lettuce', '1', 'cup'),
(3, 'Cheddar cheese', '1', 'cup'),
(3, 'Salsa', '1', 'cup'),
(3, 'Sour cream', '0.5', 'cup');

INSERT INTO steps (recipe_id, step) VALUES 
(3, 'Cook the ground beef in a pan until browned.'),
(3, 'Add the taco seasoning and a little water, and cook until the liquid is absorbed.'),
(3, 'Heat the taco shells according to the package instructions.'),
(3, 'Fill each taco shell with beef, lettuce, cheese, salsa, and sour cream.'),
(3, 'Serve immediately.');

INSERT INTO pictures (recipe_id, filename) VALUES 
(3, 'examples/tacos.jpg');

