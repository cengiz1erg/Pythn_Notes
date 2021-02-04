def f1():
    print("f1 çağırıldı..")
    # default -> return None
f1()  # çıktı = f1 çağırıldı..
print(f1)  # çıktı = <function f1 at 0x00000230905BE040>
# f1() ifadesi f1 fonksiyonunu çağırırken, f1 ifadesi ise f1 fonksiyonunun bellekteki konumunu verir.
# Yani f1 kara kutusu bellekte hazır bir nesnedir ve çağırılıp, girdiye çıktı yaratmak istemektedir.
# --------------
a = f1
# print(id(a), id(f1)) # çıktı = 1375114616896 1375114616896
# Bu şunu söylüyor:
# 1375114616896 adresinde şu şu özelliklere sahip bir fonksiyon var ve a ile f1 değişkeni belleğin
# 1375114616896 adresindeki bu fonksiyonun dış dünyadaki bir temsilcisidir.
# -------
def f2(f):
    return f()
f2(f1)
# Burada ise bellekte hazır bekleyen bir f1 fonksiyonunu f2 fonksiyonuna parametre olarak giriyorum.
# --------------------------------------------------------------------------------------------------
# ------ Fonksiyonlar genel olarak bu şekilde. "Decorators"u kavramak için fonksiyonlara bu
# ------ açıdan bakmak önemliydi.
# Decorators,kısaca fonksiyonu modifiye eder.
def fa(function):
    import time

    def wrapper(*args,**kwargs):
        print("wrapper başladı")
        time.sleep(1)
        print(f'{function.__name__} fonksiyonu 2 sn sonra çalışacak')
        time.sleep(2)
        function(*args,**kwargs)
        time.sleep(1)
        print("fonksiyon çalıştırıldı.")
        time.sleep(1)
        print("wrapper kapanıyor..")
        time.sleep(2)
    return wrapper


def fx(a):
    print("Ben fx, Merhaba",a)


fx = fa(fx)  # fx, fa tarafından modifiye edildi.
# çıktı = wrapper/ Bu ne demek? Wrapper fonksiyonu çağırılmayı bekliyor demek.
print(fx.__name__)
# fx çağırılsa da aslında arka planda modifiye edilmiş fx, yani wrappper fonksiyonu çağırılıyor.
fx("cengiz")

# # ve fx = fa(fx) yazmanın kısayolu fx fonksiyonun üstüne @fa eklemektir.


@fa
def fx(a):
    print("Ben fx, Merhaba",a)
