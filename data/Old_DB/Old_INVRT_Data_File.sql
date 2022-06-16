SELECT * FROM users;
SELECT * FROM cart;
SELECT * FROM orders;
SELECT * FROM products;
SELECT * FROM products_in_orders;

INSERT INTO products (name, color, description, price, drop_num, soldout, design, patch, front_img, back_img) VALUES ("INVRT Colosseum Tee", "Black", "This design contains a Roman Colosseum graphic with a sculptured hand reaching through the Colosseum. The front of the shirt has an embroidered INVRT logo patch on the left chest.", 30, 1, 1, "static/all_imgs/drop-1/colosseum_design.jpg", "static/all_imgs/INVRT_patch.jpeg", "static/all_imgs/drop-1/colosseum_black_front.jpeg", "static/all_imgs/drop-1/colosseum_black_back.jpeg");
INSERT INTO products (name, color, description, price, drop_num, soldout, design, patch, front_img, back_img) VALUES ("INVRT Ctrl+Eye Tee", "Creme", 'When you press both "Ctrl" and "I" at the same time on photoshop, it INVERTS the colors on the layer. Pretty smart, huh? The design contains a double headed snake wrapped across a red eye ball, surrounded by text. The front of the shirt has an embroidered INVRT logo patch on the left chest.', 30, 2, 0, "static/all_imgs/drop-2/ctrleye_design.jpeg", "static/all_imgs/INVRT_patch.jpeg", "static/all_imgs/drop-2/ctrleye_creme_front.jpg", "static/all_imgs/drop-2/ctrleye_creme_back.jpg");
INSERT INTO products (name, color, description, price, drop_num, soldout, design, patch, front_img, back_img) VALUES ("INVRT Ctrl+Eye Tee", "Brown", 'When you press both "Ctrl" and "I" at the same time on photoshop, it INVERTS the colors on the layer. Pretty smart, huh? The design contains a double headed snake wrapped across a red eye ball, surrounded by text. The front of the shirt has an embroidered INVRT logo patch on the left chest.', 30, 2, 0, "static/all_imgs/drop-2/ctrleye_design.jpeg", "static/all_imgs/INVRT_patch.jpeg", "static/all_imgs/drop-2/ctrleye_brown_front.jpg", "static/all_imgs/drop-2/ctrleye_brown_back.jpg");
INSERT INTO products (name, color, description, price, drop_num, soldout, design, patch, front_img, back_img) VALUES ("INVRT Astronaut Tee", "Blue", "What you know about rollin' down in the deep? When your brain goes numb, you can call that mental freeze When these people talk too much, put that shit in slow motion, yeah I feel like an astronaut in the ocean", 30, 2, 0, "static/all_imgs/drop-2/astronaut_design.jpeg", "static/all_imgs/INVRT_patch.jpeg", "static/all_imgs/drop-2/astronaut_blue_front.jpg", "static/all_imgs/drop-2/astronaut_blue_back.jpg");
INSERT INTO products (name, color, description, price, drop_num, soldout, design, patch, front_img, back_img) VALUES ("INVRT Astronaut Tee", "Gray", "What you know about rollin' down in the deep? When your brain goes numb, you can call that mental freeze When these people talk too much, put that shit in slow motion, yeah I feel like an astronaut in the ocean", 30, 2, 0, "static/all_imgs/drop-2/astronaut_design.jpeg", "static/all_imgs/INVRT_patch.jpeg", "static/all_imgs/drop-2/astronaut_gray_front.jpg", "static/all_imgs/drop-2/astronaut_gray_back.jpg");

INSERT INTO cart (size, quantity, user_id, product_id) VALUES ("XL", 1, 1, 4);

SELECT * FROM users LEFT JOIN cart ON users.id = cart.user_id LEFT JOIN products ON cart.product_id = products.id WHERE users.id=1;

DELETE FROM cart WHERE id=1;

SELECT * FROM cart WHERE id = 3;

UPDATE cart SET quantity=2 WHERE id=4;