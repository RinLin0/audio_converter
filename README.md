# 简易音频转换器 (Simple Audio Converter)

一个基于 Pydub 和 FFmpeg 的简单 Python 脚本，用于将单个音频文件批量转换为多种主流音频格式（MP3, WAV, OGG, FLAC, AAC 等）。

## 🚀 功能

* 读取任意 FFmpeg 支持的音频文件（如 .mp3, .wav, .m4a, .flac 等）。
* 一次性将其转换为 9 种常见的音频格式。
* 通过简单的命令行界面 (CLI) 运行。
* 允许用户指定自定义的输出目录。

## 🛠️ 依赖要求 (Requirements)

本项目依赖 Python 3 和两个核心组件：

1.  **Pydub (Python 库):**
    你需要通过 pip 安装 `pydub` 库。

    ```bash
    pip install pydub
    ```
    (或者，使用 `pip install -r requirements.txt`)

2.  **FFmpeg (核心编解码器):**
    `pydub` 在后台依赖 FFmpeg 来处理所有音频编解码工作。你必须在你的系统上安装它，并确保它在系统的 PATH 环境变量中。

    * **Windows:**
        1.  从 [FFmpeg 官网](https://ffmpeg.org/download.html) 下载预编译的二进制文件 (builds)。
        2.  解压文件（例如到 `C:\ffmpeg`）。
        3.  将其 `bin` 目录 (例如 `C:\ffmpeg\bin`) 添加到系统的 `PATH` 环境变量中。

    * **macOS (使用 Homebrew):**
        ```bash
        brew install ffmpeg
        ```

    * **Linux (使用 apt, 适用于 Ubuntu/Debian):**
        ```bash
        sudo apt update
        sudo apt install ffmpeg
        ```

## ⌨️ 如何使用

1.  克隆或下载本项目。
2.  确保已安装上述所有**依赖要求**。
3.  打开您的终端或命令提示符。
4.  运行 `audio_converter.py` 脚本，并传入您要转换的音频文件路径。

---

### 命令行示例:

**基本用法 (转换并保存到默认文件夹):**

将 `my_song.wav` 转换为所有格式，并存入默认的 `./converted_audio` 文件夹中。

```bash
python audio_converter.py "my_song.wav"
```
**指定一个不同的输出文件夹:**
```bash
python audio_converter.py "song.m4a" -o "my_output_folder"
```
**查看帮助:**
```bash
python audio_converter.py -h
```