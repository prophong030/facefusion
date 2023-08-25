import os
from deepspeech import Model
import numpy as np

def extract_audio_to_srt(audio_file, output_srt):
    ds = Model("deepspeech-0.9.3-models-zh-CN.pbmm")
    
    # Đọc tệp âm thanh
    audio = np.fromfile(audio_file, dtype=np.int16)
    
    # Trích xuất văn bản từ âm thanh bằng DeepSpeech
    text = ds.stt(audio)
    
    # In văn bản đã trích xuất lên dòng lệnh
    print("Văn bản trích xuất:", text)
    
    # Tạo nội dung file phụ đề SRT
    subtitle_content = "1\n00:00:00,000 --> 00:00:01,000\n" + text

    # Ghi nội dung vào file phụ đề
    with open(output_srt, "w") as subtitle:
        subtitle.write(subtitle_content)

if __name__ == "__main__":
    downloaded_file = "video.mp3"  # Tên tệp audio đã có sẵn (định dạng MP3)
    output_srt_path = "subtitle.srt"

    extract_audio_to_srt(downloaded_file, output_srt_path)
    print("Trích xuất và tạo file SRT thành công!")
