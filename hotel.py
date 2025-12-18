sapaan = "Selamat datang di Aplikasi BOOKING HOTEL PM 🏨"
print("="*50)
print(sapaan.center(50))
print("="*50)

data_dummy = [
    {
      "nama_hotel": "Hotel PM",
      "kota": "Malang",
      "list_kamar": [
          {"tipe": "Standard", "harga": 450000, "sisa": 5},
            {"tipe": "Deluxe", "harga": 600000, "sisa": 2},
            {"tipe": "Suite", "harga": 1200000, "sisa": 1},
      ]  
    },
    {
      "nama_hotel": "Hotel PH",
      "kota": "Malang",
      "list_kamar": [
          {"tipe": "Standard", "harga": 450000, "sisa": 5},
            {"tipe": "Deluxe", "harga": 600000, "sisa": 2},
            {"tipe": "Suite", "harga": 1200000, "sisa": 1},
      ]  
    },
    {
      "nama_hotel": "Hotel KM",
      "kota": "Bandung",
      "list_kamar": [
            {"tipe": "Standard", "harga": 450000, "sisa": 5},
            {"tipe": "Deluxe", "harga": 600000, "sisa": 2},
            {"tipe": "Suite", "harga": 1200000, "sisa": 1},
      ]
    },
    {
      "nama_hotel": "Hotel HR",
      "kota": "Bandung",
      "list_kamar": [
            {"tipe": "Standard", "harga": 450000, "sisa": 5},
            {"tipe": "Deluxe", "harga": 600000, "sisa": 2},
            {"tipe": "Suite", "harga": 1200000, "sisa": 1},
      ]
    },
    {
      "nama_hotel": "Hotel MJ",
      "kota": "Bandung",
      "list_kamar": [
            {"tipe": "Standard", "harga": 450000, "sisa": 5},
            {"tipe": "Deluxe", "harga": 600000, "sisa": 2},
            {"tipe": "Suite", "harga": 1200000, "sisa": 0},
      ]
    },
    {
      "nama_hotel": "Hotel DN",
      "kota": "Yogyakarta",
      "list_kamar": [
            {"tipe": "Standard", "harga": 450000, "sisa": 5},
            {"tipe": "Deluxe", "harga": 600000, "sisa": 2},
            {"tipe": "Suite", "harga": 1200000, "sisa": 1},
      ]
    },
]

# contoh duplikat
# for kota in list_hotel:
#     print(kota['kota'])

def pilihan_kota(data_hotel):
    cities = list({kota["kota"].lower() for kota in data_hotel}) #list comprehension versi SET -> "Loop semua data hotel → ambil nilai kota → simpan ke SET → otomatis hilangkan duplikat."
    print("🏢 Silahkan pilih kota tujuan anda :")
    for idx, city in enumerate(cities, start=1):
        print(f"{idx}. {city}")
        
    pilihan = input("Silahkan masukan nomor kota tujuan anda : ")
    
    while not pilihan or pilihan not in cities:
        print("⚠️ Kota tidak tersedia. Silahkan masukan nomor kota yang tersedia. ⚠️")
        pilihan = input("Silahkan masukan nomor kota tujuan anda : ")
        
    print("pilihan anda : ", pilihan)
    return pilihan
        

def display_hotel(kota):
    list_hotel = []
    print(f"\n🏩 Berikut list hotel di kota {kota} :")
    for index, hotel in enumerate(data_dummy, start=1):
        if hotel['kota'].lower() == kota.lower():
            list_hotel.append(hotel["nama_hotel"].lower())
            print(f"{index}. {hotel['nama_hotel']}")
            
    print("list_hotel", list_hotel)
    pilihan_hotel = input("\nSilahkan masukan nama hotel tujuan anda atau ketik '0' untuk kembali : ").lower()
    while pilihan_hotel not in list_hotel and pilihan_hotel != "0":
        print("⚠️ Hotel tidak tersedia. Silahkan masukan nama hotel yang tersedia. ⚠️")
        pilihan_hotel = input("\nSilahkan masukan nama hotel tujuan anda atau ketik '0' untuk kembali : ")
        
    
    if pilihan_hotel == "0":
        return
    
    print(f"Pilihan tersedia ✅")
    return pilihan_hotel

def list_kamar(pilihan_hotel):
  print(f"🛏️  Berikut list kamar yang tersedia di {pilihan_hotel} :")
  print("=" * 50)
  print(f"{'No':<10}{'Tipe Kamar':<15} {'Harga/malam':<15} {'Sisa Kamar':<15}")

  list_kamar = []
  for kamar in data_dummy:
    if kamar['nama_hotel'].lower() == pilihan_hotel.lower():
      for idx, list in enumerate(kamar['list_kamar'], start=1):
        if list['sisa'] >= 1:
          list_kamar.append(list)
          print(f"{idx:<10} {list['tipe']:<15} {list['harga']:<15} {list['sisa']:<15}")
        # print("list kamar", list)
  print("=" * 50)
  print("list_kamar", list_kamar)
  print("list_kamar index ", list_kamar[0])
  
  pilihan_kamar = input("Silahkan masukan nomor kamar yang ingin anda booking atau ketik '0' untuk kembali : ")
    
  while not pilihan_kamar and pilihan_kamar != "0":
    print("⚠️ Nomor kamar tidak tersedia. Silahkan masukan nomor kamar yang tersedia. ⚠️")
    pilihan_kamar = input("Silahkan masukan nomor kamar yang ingin anda booking : ")
  
  if pilihan_kamar == "0":
    return
  
  # kamar_dipilih = 
  # validsi
  validasi = input(f"Apakah anda yakin ingin booking kamar dengan tipe {list_kamar[int(pilihan_kamar)-1]['tipe']} ? (y/n) : ").lower()
  
  while validasi not in ["y", "n"]:
    print("⚠️ Input tidak valid. Silahkan masukan 'y' atau 'n'. ⚠️")
    validasi = input(f"Apakah anda yakin ingin booking kamar {list_kamar[int(pilihan_kamar)-1]['tipe']} ? (y/n) : ").lower()
  
  if validasi == "n":
    return validasi
  
  return pilihan_kamar
  
def nota_hooking():
    nota= "💲 Nota Booking Hotel💲"
    print("\n" + "=" * 50)
    print(nota.center(50))
    print("=" * 50)
    
while True:
  pilihan = pilihan_kota(data_hotel=data_dummy)
    
  pilihan_hotel = display_hotel(kota=pilihan)
    
  if not pilihan_hotel:
      continue
    
  while True:
    list_kmr = list_kamar(pilihan_hotel=pilihan_hotel)
    print(list_kmr)
      
    if list_kmr == "n":
      continue
        
    if not list_kmr:
      break
  
  continue
  
  # break
