# CIDR Calculator

Tugas kecil untuk menyelesaikan mata kuliah IF3130 Jaringan Komputer
Program Studi Teknik Informatika
Institut Teknologi
Bandung

Created by Ray Andrew - 13515073

---

### Prerequisites

Things you need to install

* [Makefile](https://www.gnu.org/software/make/)
* [Python 2.7](https://www.python.org/download/releases/2.7/)

---

### Installing

No need to install, because python is interpreter

---

## Running

```
make run
```

---

## Process each phase

**1.  Phase 1 (fungsi getValidSubnet)**
```
Cukup menambahkan host + "/32" di setiap host
Kenapa seperti itu?
Hal ini dikarenakan subnet dengan "ip address + /32" valid untuk host "ip address"
```

**2.  Phase 2 (fungsi countHosts)**
```
Cara menghitung banyaknya host dalam subnet adalah 2**(32 - mask)
```

**3.  Phase 3 (fungsi isSubnetValid)**
```
Cara cek host valid dalam subnet adalah dengan mengubah menjadi binary keduanya.
Kemudian binary dari host di "and" kan dengan mask, sebut saja B1.
Selanjutnya binary dari subnet di "and" kan juga dengan mask, sebut saja B2.
Hasil binary yaitu B1 dan B2 disamakan
├── jika sama berarti host valid dalam subnet
└── jika tidak berarti host tidak valid dalam subnet
```

---

## Authors

* [Ray Andrew](https://github.com/rayandrews)

## LICENSE
Do whatever you want dude, this is open, feel free to use!