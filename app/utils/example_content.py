

def addContent():
    from app.models.product_card import ProductCard
    from app.models.feedback import Feedback
    import app.services.registration as reg


    reg.register_buyer(email="example@gmail.com", phone_num="+7(926)123-45-67", user_name="Daetoya608", password="12345")
    reg.register_buyer(email="user1@gmail.com", phone_num="+7(926)111-22-33", user_name="Кира Йошикаге", password="12345")
    reg.register_buyer(email="user2@yahoo.com", phone_num="+7(916)222-33-44", user_name="Joestar", password="12345")
    reg.register_buyer(email="user3@hotmail.com", phone_num="+7(936)333-44-55", user_name="Higashikata", password="12345")
    reg.register_buyer(email="user4@outlook.com", phone_num="+7(926)444-55-66", user_name="Wukong", password="12345")
    reg.register_buyer(email="user5@mail.com", phone_num="+7(956)555-66-77", user_name="SSS-rang", password="12345")
    reg.register_buyer(email="user6@gmail.com", phone_num="+7(926)666-77-88", user_name="MC GJ{", password="12345")
    reg.register_buyer(email="user7@protonmail.com", phone_num="+7(976)777-88-99", user_name="McLovin", password="12345")
    reg.register_buyer(email="user8@yahoo.com", phone_num="+7(946)888-99-00", user_name="Stein", password="12345")
    reg.register_buyer(email="user9@gmail.com", phone_num="+7(926)999-00-11", user_name="Mao", password="12345")
    reg.register_buyer(email="user10@mail.com", phone_num="+7(986)123-45-67", user_name="Satoru JoJo", password="12345")


    reg.register_seller(email="lenovo@gmail.com", phone_num="+1(555)123-23-52", store_name="Lenovo",
                        password="lenovo123",
                        product_cards_list=[
                            ProductCard([
                                Feedback(0, 5, "норм"),
                                Feedback(3, 4, "qwerty")
                            ],
                                        name="Lenovo Legion 5", cost="1700$", buy_count=12411,
                                        sum_of_rating=57091,
                                        description='''Игровой ноутбук Legion 5i Pro (7th Gen, 16, Intel)
Процессоры Intel® Core 2-го поколения (в максимальной комплектации)
Видеокарты NVIDIA® GeForce RTX™
15,6-дюймовый дисплей стандарта WQHD+ с высочайшим качеством изображения (в максимальной комплектации)'''),
                            ProductCard([
                                Feedback(2, 5, "+вайб"),
                                Feedback(8, 3, "ну такое")
                            ],
                                        name="Lenovo Tab M11", cost="499$", buy_count=8589,
                                        sum_of_rating=37835,
                                        description='''Сертификат на потоковую передачу видео HD
Многозадачный режим с возможностью разделения экрана
Опциональный стилус''')
                        ])

    reg.register_seller(email="apple@gmail.com", phone_num="+1(555)456-78-90", store_name="Apple",
                        password="apple123",
                        product_cards_list=[
                            ProductCard([
                                Feedback(1, 5, "отлично"),
                                Feedback(4, 4, "понравилось"),
                                Feedback(9, 3, "неплохо")
                            ],
                                name="iPhone 13 Pro", cost="999$", buy_count=15689,
                                sum_of_rating=74234,
                                description='''Система камер профессионального уровня
    A15 Bionic чип для молниеносной производительности
    Сверхяркий дисплей Super Retina XDR с ProMotion'''),
                            ProductCard([
                                Feedback(2, 5, "полезный девайс"),
                                Feedback(7, 3, "дорого")
                            ],
                                name="Apple Watch Series 7", cost="399$", buy_count=13422,
                                sum_of_rating=59020,
                                description='''Большой дисплей и прочный корпус
    Поддержка экстренных вызовов и измерения уровня кислорода в крови
    Поддержка различных фитнес-приложений''')
                        ])

    reg.register_seller(email="samsung@gmail.com", phone_num="+1(555)987-65-43", store_name="Samsung",
                        password="samsung123",
                        product_cards_list=[
                            ProductCard([
                                Feedback(3, 5, "замечательно"),
                                Feedback(8, 4, "стоит своих денег")
                            ],
                                name="Samsung Galaxy S21", cost="799$", buy_count=18234,
                                sum_of_rating=80234,
                                description='''Сверхбыстрая зарядка и мощный процессор Exynos
    Камера с высоким разрешением и уникальными режимами съемки
    Совместимость с сетью 5G для скоростного интернета'''),
                            ProductCard([
                                Feedback(0, 5, "идеально для работы"),
                                Feedback(6, 3, "могло быть лучше")
                            ],
                                name="Samsung Galaxy Tab S7", cost="649$", buy_count=11234,
                                sum_of_rating=51000,
                                description='''Высококачественный экран с поддержкой S Pen
    Быстрая зарядка и производительность для многозадачности
    Поддержка DeX для удобного подключения к другим устройствам''')
                        ])

    reg.register_seller(email="dell@gmail.com", phone_num="+1(555)321-65-87", store_name="Dell",
                        password="dell123",
                        product_cards_list=[
                            ProductCard([
                                Feedback(5, 5, "мощный ноутбук"),
                                Feedback(2, 4, "доволен покупкой")
                            ],
                                name="Dell XPS 15", cost="1850$", buy_count=10245,
                                sum_of_rating=42001,
                                description='''Тонкий и легкий корпус с прочной конструкцией
    Дисплей InfinityEdge с высоким разрешением и яркостью
    Процессоры Intel Core i7 и i9, производительная графика'''),
                            ProductCard([
                                Feedback(4, 5, "компактный и удобный"),
                                Feedback(7, 3, "хороший выбор для бизнеса")
                            ],
                                name="Dell Latitude 7400", cost="1400$", buy_count=9834,
                                sum_of_rating=44210,
                                description='''Корпус из алюминиевого сплава и поддержка LTE
    Отличное время автономной работы и быстрый процессор
    Поддержка Windows Hello и камеры с ИК-датчиком''')
                        ])
