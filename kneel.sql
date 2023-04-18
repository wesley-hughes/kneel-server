CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(7,2) NOT NULL
);
CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carats` NUMERIC(5,2) NOT NULL,
    `price` NUMERIC(7,2) NOT NULL
);
CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(7,2) NOT NULL
);
CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    [metal_id] INTEGER NOT NULL,
    [size_id] INTEGER NOT NULL,
    [style_id] INTEGER NOT NULL,
    `timestamp` NVARCHAR(160) NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`)
);



INSERT INTO 'Metals' VALUES (null , "Sterling Silver", 12.42);
INSERT INTO 'Metals' VALUES (null , "14K Gold", 736.4);
INSERT INTO 'Metals' VALUES (null , "24K Gold", 1258.9);
INSERT INTO 'Metals' VALUES (null , "Platinum", 795.45);
INSERT INTO 'Metals' VALUES (null , "Palladium", 1241.0);

INSERT INTO 'Sizes' VALUES (null, 0.5, 405 );
INSERT INTO 'Sizes' VALUES (null, 0.75, 782 );
INSERT INTO 'Sizes' VALUES (null, 1, 1470 );
INSERT INTO 'Sizes' VALUES (null, 1.5, 1997 );
INSERT INTO 'Sizes' VALUES (null, 2, 3638 );

INSERT INTO 'Styles' VALUES (null, "Classic", 500 );
INSERT INTO 'Styles' VALUES (null, "Modern", 710 );
INSERT INTO 'Styles' VALUES (null, "Vintage", 965 );

INSERT INTO 'Orders' VALUES (null, 1, 2, 3, "1623659931693");
INSERT INTO 'Orders' VALUES (null, 4, 3, 2, "1615659931693");
INSERT INTO 'Orders' VALUES (null, 5, 1, 1, "1614659932693");
INSERT INTO 'Orders' VALUES (null, 1, 4, 3, "1614659831693");
INSERT INTO 'Orders' VALUES (null, 3, 5, 2, "1614659931695");

SELECT * FROM Orders;