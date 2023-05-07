CREATE TABLE IF NOT EXISTS card_shop (
    id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
    shop_name VARCHAR(255) NOT NULL,
    shop_address VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS activity_type (
    id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
    type_name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS activity (
    id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
    activity_type_id INTEGER NOT NULL,
    card_shop_id INTEGER NOT NULL,
    activity_date DATE NOT NULL,
    activity_time TIME NOT NULL,
    FOREIGN KEY (activity_type_id) REFERENCES activity_type(id),
    FOREIGN KEY (activity_shop_id) REFERENCES card_shop(id)
);

INSERT INTO card_shop (shop_name, shop_address) VALUES 
('DD 異次元卓遊社TCG', '香港天后清風街6-8號凱豐商業大廈2樓B'),
('Home-run FABulous card shop', '香港太子彌敦道749A號愛都婚紗中心 10/F'),
('TCG Express', '香港旺角彌敦道608號總統商業大廈20樓01室'),
('My Card', '香港長沙灣元州街162號天悅廣場1樓 113/ 133.138店'),
('金豐遊玩王', '香港長沙灣元州街162號天悅廣場1樓136,151,165號'),
('卡之里', '香港長沙灣元州街162號天悅廣場1樓163a, 163及187號舖'),
('Combo TCG (天悅店)', '香港長沙灣元州街162號天悅廣場1樓129號店'),
('Combo TCG (步陞店)', '香港長沙灣元州街165號步陞工商業大樓7樓A'),
('Nova', '香港長沙灣元州街165號步陞工商業大樓 1樓A室'),
('TOP 3', '香港荔枝角489-491號香港工業中心C座2樓19A室'),
('Battleground', '香港荔枝角長順街11號 長城工廠大廈10樓A03室'),
('Battle Phase', '香港葵芳葵豐街53號福業大廈10樓03室'),
('Ark Black Cat', '香港觀塘官塘工業中心第四期 CD 座 地庫層 3 號室'),
('皇巢', '香港觀塘觀塘道404號時運工業大廈1樓A室'),
('新手村 TCG Village', '新蒲崗大有街29號宏基中心一期4樓408室'),
('球琪桌遊', '澳門炮兵街8A號地下');

INSERT INTO activity_type (type_name) VALUES ('新手試玩會'), ('Party'), ('Ceremony'), ('Tournament');