import concurrent.futures
import time

def sleeper(n, name):
    print("Hello, I am {}. Goint to sleep now.\n".format(name))
    time.sleep(n)
    return "Good morning. {} has woken up".format(name)

if __name__ == "__main__":

    # ThreadPoolExecutor daha kolay bir şekilde thread yönetimini sağlar bize
    # Context manager olarak kullanılması da threadlerin sonlandırılmasını otomatikleştirir
    # submit fonksiyonu future nesnesi dönderir ve bu nesneyle fonksiyon çıktısını yazdırabiliriz.
    # Ayrıca senkronizasyonu da context manager sağlıyor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(sleeper, 2, "thread1")
        print(f1.result())

    # 10 tane thread çalıştırmak istersek döngü oluşturabiliriz
    # with concurrent.futures.ThreadPoolExecutor() as executor2:
    #     futures_results = []
    #     for i in range(10):
    #         f = executor2.submit(sleeper, 1, "thread{}".format(i+2))
    #         futures_results.append(f.result())
    #     for result in futures_results:
    #         print(result)

    # list comprehension method used in this code block.
    with concurrent.futures.ThreadPoolExecutor() as executor2:
        results = [executor2.submit(sleeper, 2, "t{}".format(_+2)) for _ in range(10)]
        for f in concurrent.futures.as_completed(results):
            print(f.result())

