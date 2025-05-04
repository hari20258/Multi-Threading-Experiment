import threading
import time
import requests

urls = [
    "https://cdn.britannica.com/07/234207-050-0037B589/English-bulldog-dog.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQEWw2ESX9PgwUKSa6H7Am1aYgjwSdbUG_nYA&s",
    "https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_16x9.jpg?w=1200"
]

def download_file(url, filename_prefix):
    try:
        response = requests.get(url)
        response.raise_for_status()
        ext = url.split('.')[-1].split('?')[0]
        filename = f"{filename_prefix}.{ext}"
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")


def sequential_download(urls):
    for i, url in enumerate(urls):
        download_file(url, f"sequential_file_{i}")


def threaded_download(urls):
    threads = []
    for i, url in enumerate(urls):
        t = threading.Thread(target=download_file, args=(url, f"threaded_file_{i}"))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

if __name__ == "__main__":
    print("Starting sequential download...")
    start_time = time.time()
    sequential_download(urls)
    print(f"Sequential download time: {time.time() - start_time:.2f} seconds\n")

    print("Starting threaded download...")
    start_time = time.time()
    threaded_download(urls)
    print(f"Threaded download time: {time.time() - start_time:.2f} seconds")
