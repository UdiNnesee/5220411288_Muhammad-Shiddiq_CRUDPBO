import mysql.connector
from datetime import datetime

class Posh_Coffe:
    def __init__(self) -> None:
        self.localhost = "localhost"
        self.root = "root"
        self.password = ""
        self.db_name = "5220411288"
        self.con = self.connection()
        self.cursor = self.db.cursor()

    def connection(self):
        db = mysql.connector.connect(
            host = self.localhost,
            user = self.root,
            password = self.password,
            database = self.db_name
        )
        self.db = db

class Karyawan(Posh_Coffe):
    def __init__(self) -> None:
        super().__init__()

    def tambah(self):
        header()
        nama_karyawan = input('Masukkan Nama Karyawan   : ')
        no_hp = int(input('Masukkan No HP    :'))
        query = "INSERT INTO tb_karyawan (nama_karyawan, no_hp) VALUES (%s, %s)"
        values = (nama_karyawan, no_hp)
        self.cursor.execute(query, values)
        self.db.commit()
        print(f"Karyawan {nama_karyawan} berhasil ditambahkan.")
        pilih = input('Ingin tambah karyawan lagi?(y/t)')
        if pilih == 'y':
            self.tambah()
        else:
            menu_karyawan()
    
    def read(self):
        header()
        query = f"SELECT * FROM tb_karyawan"
        self.cursor.execute(query)
        all_data = self.cursor.fetchall()
        if all_data:
            for row in all_data:
                print(f"ID Karyawan: {row[0]}")
                print(f"Nama Karyawan: {row[1]}")
                print(f"No HP: {row[2]}")
    
    def edit(self, id_karyawan):
        query = f"SELECT * FROM tb_karyawan"
        self.cursor.execute(query)
        all_data = self.cursor.fetchall()
        for row in all_data:
            if row[0] == id_karyawan :     
                new_nama_karyawan = input("Nama Karyawan   : ")
                new_no_hp = input("No HP        : ")
                query = "UPDATE tb_karyawan SET nama_karyawan = %s, no_hp = %s WHERE id_karyawan = %s"
                values = (new_nama_karyawan, new_no_hp, id_karyawan)
                self.cursor.execute(query, values)
                self.db.commit()
                print(f"Karyawan dengan ID {id_karyawan} berhasil diperbarui.")
                break
        if row[0] != id_karyawan:
            print('id Karyawan tidak ada')
            coba = input('Ingin pilih karyawan yang lain?(y/t)')
            if coba == 'y':
                id_karyawan = int(input('Pilih ID karyawan yang ingin di edit  : '))
                untuk_edit_karyawan(id_karyawan)
            else:
                menu_karyawan()
        coba = input('Ingin pilih karyawan yang lain?(y/t)')
        if coba == 'y':
            id_karyawan = int(input('Pilih ID karyawan yang ingin di edit  : '))
            untuk_edit_karyawan(id_karyawan)
        else:
            menu_karyawan()

class Produk(Posh_Coffe):
    def __init__(self) -> None:
        super().__init__()

    def tambah(self):
        header()
        nama_menu = input('Masukkan Nama Menu   : ')
        stok = input('Masukkan Stok     :')
        harga = input('Masukkan Harga(satuan)   : ')
        query = "INSERT INTO tb_produk (nama_menu, stok, harga) VALUES (%s, %s, %s)"
        values = (nama_menu, stok, harga)
        self.cursor.execute(query, values)
        self.db.commit()
        print(f"Menu {nama_menu} berhasil ditambahkan.")
        pilih = input('Ingin tambah menu lagi?(y/t)')
        if pilih == 'y':
            self.tambah()
        else:
            menu_produk()

    def read(self):
        header()
        query = f"SELECT * FROM tb_produk"
        self.cursor.execute(query)
        all_data = self.cursor.fetchall()
        if all_data:
            for row in all_data:
                print(f"ID Menu     : {row[0]}")
                print(f"Nama Produk : {row[1]}")
                print(f"Stok        : {row[2]}")
                print(f"Harga       : {row[3]}")
                garis()

    def read_by_index(self, id_menu):
        query = f"SELECT * FROM tb_produk WHERE id_menu = {id_menu}"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result
    
    def edit(self, id_menu):
        query = f"SELECT * FROM tb_produk"
        self.cursor.execute(query)
        all_data = self.cursor.fetchall()
        for row in all_data:
            if row[0] == id_menu :  
                new_nama_menu = input('Masukkan Nama Menu   : ')
                new_stok = input('Masukkan Stok     :')
                new_harga = input('Masukkan Harga(satuan)   : ')
                query = "UPDATE tb_produk SET nama_menu = %s, stok = %s, harga = %s WHERE id_menu = %s"
                values = (new_nama_menu, new_stok, new_harga, id_menu)
                self.cursor.execute(query, values)
                self.db.commit()
                print(f"Menu dengan ID {id_menu} berhasil diperbarui.")
                break
        if row[0] != id_menu:
            print('id menu tidak ada')
            print(garis())
            coba = input('Ingin pilih id menu yang lain?(y/t)')
            if coba == 'y':
                id_menu = int(input('Pilih ID produk yang ingin di edit  : '))
                untuk_edit_produk(id_menu)
            else:
                menu_produk()
        coba = input('Ingin pilih id menu yang lain?(y/t)')
        if coba == 'y':
            id_menu = int(input('Pilih ID produk yang ingin di edit  : '))
            untuk_edit_produk(id_menu)
        else:
            menu_produk()

    def hapus(self, id_menu):
        query = f"SELECT * FROM tb_produk"
        self.cursor.execute(query)
        all_data = self.cursor.fetchall()
        for row in all_data:
            if row[0] == id_menu :  
                query = "DELETE FROM tb_produk WHERE id_menu = %s"
                self.cursor.execute(query, (id_menu,))                
                self.db.commit()
                print(f"Menu dengan ID {id_menu} berhasil dihapus.")
                break
        else:
            print('id produk tidak ada')
            print(garis())
            coba = input('Ingin hapus produk yang lain?(y/t)')
            if coba == 'y':
                untuk_edit_produk()
            else:
                menu_produk()
        coba = input('Ingin hapus produk yang lain?(y/t)')
        if coba == 'y':
            untuk_hapus_produk()
        else:
            menu_produk()

class Transaksi(Posh_Coffe):
    def __init__(self) -> None:
        super().__init__()

    def tambah(self):
        header()
        menu_jumlah_list = []
        cur_harga = 0
        while True:
            produk.read()
            id_menu = int(input("Masukkan ID Produk yang dibeli : "))
            if id_menu == 0:
                break
            jumlah_beli = int(input("Masukkan Jumlah Beli: "))
            produk_info = produk.read_by_index(id_menu)
            menu, harga, stok = produk_info[1], produk_info[3], produk_info[2]
            if jumlah_beli > stok:
                return "Stok tidak mencukupi untuk melakukan pembelian."
            new_stok = stok - jumlah_beli
            total_harga = harga * jumlah_beli
            harga_for_struk = cur_harga + total_harga
            stok = new_stok
            query_edit_stok = "UPDATE tb_produk SET nama_menu=%s , stok=%s , harga = %s WHERE id_menu=%s"
            value = (menu, stok, harga, id_menu)
            self.cursor.execute(query_edit_stok,value)
            self.db.commit()
            menu_jumlah_list.append((id_menu, jumlah_beli))
            piliih = input("Tambah Produk yang di beli?y/t")
            cur_harga = total_harga
            if piliih == 't':
                break
        query_karyawan = "SELECT * FROM tb_karyawan LIMIT 1"
        self.cursor.execute(query_karyawan)
        karyawan_info = self.cursor.fetchone()
        id_karyawan, nama_karyawan = karyawan_info[0], karyawan_info[1]
        struk = f"===== Struk Pembelian =====\nKasir: {nama_karyawan}\n"
        query_transaksi = "INSERT INTO tb_transaksi (id_karyawan, tanggal) VALUES (%s, %s)"
        values_transaksi = (id_karyawan, datetime.now())
        self.cursor.execute(query_transaksi, values_transaksi)
        self.db.commit()
        id_transaksi = self.cursor.lastrowid
        for id_menu, jumlah_beli in menu_jumlah_list:
            query_detail_transaksi = "INSERT INTO tb_detail_transaksi (id_transaksi, id_menu, jumlah_beli, harga, total_harga) VALUES (%s, %s, %s, %s, %s)"
            values_detail_transaksi = (id_transaksi, id_menu, jumlah_beli, harga, harga_for_struk)
            self.cursor.execute(query_detail_transaksi, values_detail_transaksi)
            struk += f"\nMenu: {menu}\nJumlah Beli: {jumlah_beli}\nHarga Satuan: {harga}\n"
        struk += f"\nTotal Harga: {harga_for_struk}\n============================="
        self.db.commit()
        print(struk)
        pil = input('ingin lakukan transaksi lagi?(y/t) ')
        if pil == 'y':
            transaksi.tambah()
        else:
            menu_transaksi()
        
karyawan = Karyawan()
produk = Produk()
transaksi = Transaksi()

def header():
    garis()
    print(''*5,'Posh Coffe')
    garis()
    print('\n')

def garis():
    return print('='*20)

def menu():
    header()
    print('1. Produk')
    print('2. Karyawan')
    print('3. Transaksi')
    print('\n')
    garis()
    pilih = int(input('Pilihan  : '))
    garis()
    if pilih == 1:
        menu_produk()
    elif pilih == 2:
        menu_karyawan()
    elif pilih == 3:
        menu_transaksi()

def menu_produk():
    header()
    print('1. Tambah Data Produk')
    print('2. Lihat Data Produk')
    print('3. Edit Data Produk')
    print('4. Hapus Data Produk')
    print('5. Kembali ke menu utama')
    print('\n')
    garis()
    pilih = int(input('Pilihan  : '))
    garis()
    if pilih == 1:
        produk.tambah()
    elif pilih == 2:
        produk.read()
        coba = input('Kembali ke menu sebelumnya?(y/t)')
        if coba == 'y':
            menu_produk()
    elif pilih == 3:
        produk.read()
        id_menu = int(input('Pilih ID menu yang ingin di edit  : '))
        untuk_edit_produk(id_menu)
    elif pilih == 4:
        produk.read()
        id_menu = int(input('Pilih ID menu yang ingin di hapus  : '))
        untuk_hapus_produk(id_menu)
    else:
        menu()

def menu_karyawan():
    header()
    print('1. Tambah Data Karyawan')
    print('2. Lihat Data Karyawan')
    print('3. Edit Data Karyawan')
    print('4. Kembali ke menu utama')
    print('\n')
    garis()
    pilih = int(input('Pilihan  : '))
    garis()
    if pilih == 1:
        karyawan.tambah()
    elif pilih == 2:
        karyawan.read()
        coba = input('Kembali ke menu sebelumnya?(y/t)')
        if coba == 'y':
            menu_karyawan()
    elif pilih == 3:
        karyawan.read()
        id_karyawan = int(input('Pilih ID karyawan yang ingin di edit  : '))
        untuk_edit_karyawan(id_karyawan)
    else:
        menu()

def menu_transaksi():
    header()
    print('1. Tambah Transaksi')
    print('2. Kembali ke menu utama')
    print('\n')
    garis()
    pilih = int(input('Pilihan  : '))
    garis()
    if pilih == 1:
        transaksi.tambah()
    else:
        menu()

def untuk_edit_produk(id_menu):
    produk.edit(id_menu)

def untuk_edit_karyawan(id_karyawan):
    karyawan.edit(id_karyawan)

def untuk_hapus_produk(id_menu):
    produk.hapus(id_menu)

def main():
    menu()

main()