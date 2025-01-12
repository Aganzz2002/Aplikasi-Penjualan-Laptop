from .database import get_connection

def create_laptop(nama, brand, specs, harga, stok):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO laptops (nama, brand, specs, harga, stok) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nama, brand, specs, harga, stok))
    conn.commit()
    conn.close()

def read_laptops():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM laptops ORDER BY id ASC"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def update_laptop(laptop_id, nama, brand, specs, harga, stok):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    UPDATE laptops
    SET nama = %s, brand = %s, specs = %s, harga = %s, stok = %s
    WHERE id = %s
    """
    cursor.execute(query, (nama, brand, specs, harga, stok, laptop_id))
    conn.commit()
    conn.close()

def delete_laptop(laptop_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM laptops WHERE id = %s"
    cursor.execute(query, (laptop_id,))
    conn.commit()
    conn.close()
