import psycopg2

"""херня сверху будет жаловаться на линуксе и макосе, устанавливайте постгре через brew
код создает таблицу для хранения инфы о ресторанах
"""

def create_table():
    conn = psycopg2.connect(
        dbname="your_database_name",
        user="your_username",
        password="your_password",    #еще не поднял ее, подниму на компе. но по хорошему
        host="your_host",      #надо захостить на серваке
        port="your_port"
    )
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS restaurants (
                    location_id TEXT PRIMARY KEY,
                    name TEXT,
                    web_url TEXT,
                    street TEXT,
                    city TEXT,
                    country TEXT,
                    postalcode TEXT,
                    latitude TEXT,
                    longitude TEXT,
                    timezone TEXT,
                    email TEXT,
                    phone TEXT,
                    website TEXT,
                    write_review TEXT,
                    geo_location_id TEXT,
                    ranking_string TEXT,
                    geo_location_name TEXT,
                    ranking_out_of TEXT,
                    ranking TEXT,
                    rating TEXT,
                    rating_image_url TEXT,
                    num_reviews TEXT,
                    photo_count TEXT,
                    see_all_photos TEXT,
                    price_level TEXT,
                    monday TEXT,
                    tuesday TEXT,
                    wednesday TEXT,
                    thursday TEXT,
                    friday TEXT,
                    saturday TEXT,
                    sunday TEXT,
                    cuisine TEXT,
                    category TEXT,
                    subcategory TEXT,
                    address_obj JSONB,
                    ancestors JSONB,
                    review_rating_count JSONB,
                    subratings JSONB,
                    hours JSONB,
                    features TEXT,
                    neighborhood_info JSONB,
                    trip_types JSONB,
                    awards JSONB
                )''')
    conn.commit()
    conn.close()

def insert_data(data):
    conn = psycopg2.connect(
        dbname="your_database_name",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cursor = conn.cursor()
    values = tuple(data.values())
    cursor.execute('''INSERT INTO restaurants VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', values)
    conn.commit()
    conn.close()


#я панк
def backup_postgresql():
    conn = psycopg2.connect(
        dbname="your_database_name",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cursor = conn.cursor()
    with open('backup_file.sql', 'w') as f:
        cursor.copy_to(f, 'your_table_name', sep='\t')




#хз должно заработать

