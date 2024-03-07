class KucingDewasa:
    def __init__(self, nama):
        self.nama = nama
        print(f"{self.nama} si kucing telah lahir!")

    def __del__(self):
        print(f"{self.nama} si kucing telah meninggal. Semoga tenang di sana, {self.nama}.")

def destructor_decorator(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)
            print(f"Sebuah {cls.__name__} baru telah lahir!")

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

        def __del__(self):
            print(f"{self.wrapped.nama} si {cls.__name__} telah meninggal. Semoga tenang di sana, {self.wrapped.nama}.")
            self.wrapped.__del__()

    return Wrapper

@destructor_decorator
class AnakKucing:
    def __init__(self, nama):
        self.nama = nama
        print(f"{self.nama} si anak kucing telah lahir!")

if __name__ == "__main__":
    kucing_dewasa = KucingDewasa("Meong")
    anak_kucing = AnakKucing("Muning")
