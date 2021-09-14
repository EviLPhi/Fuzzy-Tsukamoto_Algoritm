
import numpy as np
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file("Tsukamoto.kv")


class Data_Base(object):
    batas_harga = [400000, 600000, 900000, 1100000]
    batas_fasilitas = [3, 4, 6, 7]
    batas_kelas = [4, 6]


class Kelas_Kamar(object):
    def __init__(self, a=[4, 6]):
        self.batas = list(a)

    def sedikit(self, x):
        if x <= self.batas[0]:
            return 1
        elif x >= self.batas[1]:
            return 0
        else:
            return float((self.batas[1] - x)) / (self.batas[1] - self.batas[0])

    def banyak(self, x):
        if x <= self.batas[0]:
            return 0
        elif x >= self.batas[1]:
            return 1
        else:
            return float((x - self.batas[0])) / (self.batas[1] - self.batas[0])

    def ubah_batas(self, x):
        self.batas = x


class Fasilitas(object):
    def __init__(self, a=[3, 4, 6, 7]):
        self.batas = list(a)

    def tidak_lengkap(self, x):
        if x <= self.batas[0]:
            return 1
        elif x >= self.batas[1]:
            return 0
        else:
            return float(self.batas[1] - x) / (self.batas[1] - self.batas[0])

    def lengkap(self, x):
        if self.batas[1] <= x <= self.batas[2]:
            return 1
        elif self.batas[0] < x < self.batas[1]:
            return float(x - self.batas[0]) / (self.batas[1] - self.batas[0])
        elif self.batas[2] < x < self.batas[3]:
            return float(self.batas[3] - x) / (self.batas[3] - self.batas[2])
        else:
            return 0

    def sangat_lengkap(self, x):
        if x < self.batas[2]:
            return 0
        elif x > self.batas[3]:
            return 1
        else:
            return float(x - self.batas[2]) / (self.batas[3] - self.batas[2])

    def ubah_batas(self, x):
        self.batas = x


class Harga(object):
    def __init__(self, a=[400000, 600000, 900000, 1100000]):
        self.batas = list(a)

    def murah(self, x):
        return 1 if x <= self.batas[0] else 0 if x >= self.batas[1] else (
                float(self.batas[1] - x) / (self.batas[1] - self.batas[0]))

    def sedang(self, x):
        if self.batas[1] <= x <= self.batas[2]:
            return 1
        elif self.batas[0] < x < self.batas[1]:
            return float(x - self.batas[0]) / (self.batas[1] - self.batas[0])
        elif self.batas[2] < x < self.batas[3]:
            return float(self.batas[3] - x) / (self.batas[3] - self.batas[2])
        else:
            return 0

    def mahal(self, x):
        return 1 if x >= self.batas[3] else 0 if x <= self.batas[2] else (
                float(x - self.batas[2]) / (self.batas[3] - self.batas[2]))

    def ubah_batas(self, x):
        self.batas = x


class Bintang(object):
    def rendah(self, x):
        return 0 if x >= 5 else 1 if x <= 1 else (float(5 - x) / (5 - 1))

    def tinggi(self, x):
        return 0 if x <= 1 else 1 if x >= 5 else (float(x - 1) / (5 - 1))

    def cari_rendah(self, y):
        return 5 - float(y * (5 - 1))

    def cari_tinggi(self, y):
        return y * float(5 - 1) + 1


db = Data_Base()
B = Bintang()
F = Fasilitas()
K = Kelas_Kamar()
H = Harga()


class Main(ScreenManager):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)


class Home(Screen):
    def pindah_input(self):
        self.manager.current = "input"

    def pindah_batas(self):
        self.manager.current = "batas"


class Input(Screen):
    hasil = 0
    inputan = dict
    cek1 = StringProperty(" ")
    cek2 = StringProperty(" ")

    def rule(self):
        harga = int(self.ids["harga"].text)
        fasilitas = int(self.ids["fasilitas"].text)
        kelas = int(self.ids["kelas"].text)

        x = {"Kelas Kamar": kelas, "Fasilitas": fasilitas, "Harga": harga}
        self.inputan = x
        a = []
        z = []
        print("KELAS : ", K.sedikit(kelas), K.banyak(kelas))
        print("FASILITAS : ", F.tidak_lengkap(fasilitas), F.lengkap(fasilitas), F.sangat_lengkap(fasilitas))
        print("HARGA : ", H.murah(harga), H.sedang(harga), H.mahal(harga))
        a.append(min(K.sedikit(x["Kelas Kamar"]), F.tidak_lengkap(x["Fasilitas"]), H.murah(x["Harga"])))
        a.append(min(K.banyak(x["Kelas Kamar"]), F.tidak_lengkap(x["Fasilitas"]), H.murah(x["Harga"])))
        a.append(min(K.sedikit(x["Kelas Kamar"]), F.lengkap(x["Fasilitas"]), H.murah(x["Harga"])))
        a.append(min(K.banyak(x["Kelas Kamar"]), F.lengkap(x["Fasilitas"]), H.murah(x["Harga"])))
        a.append(min(K.sedikit(x["Kelas Kamar"]), F.sangat_lengkap(x["Fasilitas"]), H.murah(x["Harga"])))
        a.append(min(K.banyak(x["Kelas Kamar"]), F.sangat_lengkap(x["Fasilitas"]), H.murah(x["Harga"])))

        a.append(min(K.sedikit(x["Kelas Kamar"]), F.tidak_lengkap(x["Fasilitas"]), H.sedang(x["Harga"])))
        a.append(min(K.banyak(x["Kelas Kamar"]), F.tidak_lengkap(x["Fasilitas"]), H.sedang(x["Harga"])))
        a.append(min(K.sedikit(x["Kelas Kamar"]), F.lengkap(x["Fasilitas"]), H.sedang(x["Harga"])))
        a.append(min(K.banyak(x["Kelas Kamar"]), F.lengkap(x["Fasilitas"]), H.sedang(x["Harga"])))
        a.append(min(K.sedikit(x["Kelas Kamar"]), F.sangat_lengkap(x["Fasilitas"]), H.sedang(x["Harga"])))
        a.append(min(K.banyak(x["Kelas Kamar"]), F.sangat_lengkap(x["Fasilitas"]), H.sedang(x["Harga"])))

        a.append(min(K.sedikit(x["Kelas Kamar"]), F.tidak_lengkap(x["Fasilitas"]), H.mahal(x["Harga"])))
        a.append(min(K.banyak(x["Kelas Kamar"]), F.tidak_lengkap(x["Fasilitas"]), H.mahal(x["Harga"])))
        a.append(min(K.sedikit(x["Kelas Kamar"]), F.lengkap(x["Fasilitas"]), H.mahal(x["Harga"])))
        a.append(min(K.banyak(x["Kelas Kamar"]), F.lengkap(x["Fasilitas"]), H.mahal(x["Harga"])))
        a.append(min(K.sedikit(x["Kelas Kamar"]), F.sangat_lengkap(x["Fasilitas"]), H.mahal(x["Harga"])))
        a.append(min(K.banyak(x["Kelas Kamar"]), F.sangat_lengkap(x["Fasilitas"]), H.mahal(x["Harga"])))
        for i in range(len(a)):
            rendah = B.cari_rendah(a[i])
            tinggi = B.cari_tinggi(a[i])
            if i < len(a) / 2:
                z.append(rendah)
            else:
                z.append(tinggi)
        a = np.array(a)
        z = np.array(z)
        print(a)
        print(z)
        return sum(a * z) / sum(a)

    def cetak(self):
        self.hasil = int(self.rule())
        hotel = self.ids["nama"].text
        self.cek1 = "Kualitas " + hotel + " : "
        self.cek2 = "bintang " + str(self.hasil)

    def kembali(self):
        self.cek1 = ""
        self.cek2 = ""
        self.manager.current = "home"


class Batas(Screen):
    global F, K, H
    a, b, c, d, e, f, g, h, i, j = db.batas_kelas + db.batas_fasilitas + db.batas_harga
    a = StringProperty(str(a))
    b = StringProperty(str(b))
    c = StringProperty(str(c))
    d = StringProperty(str(d))
    e = StringProperty(str(e))
    f = StringProperty(str(f))
    g = StringProperty(str(g))
    h = StringProperty(str(h))
    i = StringProperty(str(i))
    j = StringProperty(str(j))

    def set(self):
        a, b, c, d, e, f, g, h, i, j = db.batas_kelas + db.batas_fasilitas + db.batas_harga
        self.a = str(a)
        self.b = str(b)
        self.c = str(c)
        self.d = str(d)
        self.e = str(e)
        self.f = str(f)
        self.g = str(g)
        self.h = str(h)
        self.i = str(i)
        self.j = str(j)

    def default(self):
        db.batas_harga = [400000, 600000, 900000, 1100000]
        db.batas_fasilitas = [3, 4, 6, 7]
        db.batas_kelas = [4, 6]
        self.set()
        self.ubah_batas()
        self.kembali()

    def ubah_batas(self):
        F.ubah_batas(db.batas_fasilitas)
        H.ubah_batas(db.batas_harga)
        K.ubah_batas(db.batas_kelas)
    def kembali(self):
        self.manager.current = "home"

    def to_int(self, list):
        temp = []
        for x in list:
            temp.append(int(x))
        return temp

    def save(self):
        list_kelas = [self.ids["kelas_1"].text,
                      self.ids["kelas_2"].text]
        list_fasilitas = [self.ids["fas_1"].text,
                          self.ids["fas_2"].text,
                          self.ids["fas_3"].text,
                          self.ids["fas_4"].text]
        list_harga = [self.ids["har_1"].text,
                      self.ids["har_2"].text,
                      self.ids["har_3"].text,
                      self.ids["har_4"].text]
        db.batas_harga = self.to_int(list_harga)
        db.batas_fasilitas = self.to_int(list_fasilitas)
        db.batas_kelas = self.to_int(list_kelas)
        self.set()
        self.ubah_batas()
        self.kembali()


Fuzzy = Main()
screens = [Home(name="home"), Input(name="input"), Batas(name="batas")]
for screen in screens:
    Fuzzy.add_widget(screen)


class Tsukamoto(App):
    def build(self):
        return Fuzzy

    def on_pause(self):
        return True


if __name__ in ('__main__', '__android__'):
    Tsukamoto().run()
