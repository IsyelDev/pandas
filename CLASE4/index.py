import yt_dlp

# URL del video
video_url = "https://ok.ru/video/7561029683759"

# Configuración de opciones para yt-dlp
ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',  # Nombre del archivo basado en el título del video
    'format': 'best',  # Descarga la mejor calidad disponible
}

# Descargar el video
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print("¡Video descargado exitosamente!")
except Exception as e:
    print(f"Error al descargar el video: {e}")