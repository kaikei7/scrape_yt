import scrapetube
import requests

def save_channel_videos_to_file(channel_username):
    try:
        # Ambil data video dari channel menggunakan scrapetube
        videos = list(scrapetube.get_channel(channel_username=channel_username))
        
        # Siapkan list untuk menyimpan hasil
        video_info_list = []
        
        # Iterasi terbalik dan ambil informasi dari setiap video
        for i in range(len(videos) - 1, -1, -1):
            video_title = videos[i]['title']['runs'][0]['text']
            video_url = f"https://www.youtube.com/watch?v={videos[i]['videoId']}"
            video_info_list.append(f"{len(videos) - i}. {video_title} : {video_url}")
        
        # Simpan ke file teks
        filename = f"{channel_username}_videos.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n\n".join(video_info_list))
        
        print(f"Berhasil menyimpan daftar video dari channel '{channel_username}' ke file {filename}.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error dalam melakukan request: {e}")
    except (KeyError, IndexError) as e:
        print(f"Error dalam parsing data: {e}")

# Gunakan fungsi untuk menyimpan video dari channel tertentu
if __name__ == "__main__":
    channel_username = input("Masukkan username channel YouTube: ").strip()
    save_channel_videos_to_file(channel_username)
