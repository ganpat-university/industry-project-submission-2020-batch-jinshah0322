import asyncio

async def download_file(url, filename):
    print(f"Downloading {url} to {filename}")
    await asyncio.sleep(2)
    print(f"Download complete for {url}")

async def main():
    tasks = [
        download_file("http://example.com/file1.txt", "file1.txt"),
        download_file("http://example.com/file2.txt", "file2.txt"),
        download_file("http://example.com/file3.txt", "file3.txt"),
    ]

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
