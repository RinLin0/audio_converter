import os
import argparse
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError


def convert_audio(input_file_path, output_dir):
    """
    读取一个音频文件，并将其转换为多种常见的音频格式。

    参数:
    input_file_path (str): 输入音频文件的路径。
    output_dir (str): 存放转换后文件的目录。
    """
    # 检查输入文件是否存在
    if not os.path.exists(input_file_path):
        print(f"错误：文件 '{input_file_path}' 不存在。")
        return

    try:
        # 从文件加载音频
        print(f"正在读取文件: {input_file_path}")
        audio = AudioSegment.from_file(input_file_path)
    except CouldntDecodeError:
        print(f"错误：无法解码文件 '{input_file_path}'。")
        print("请确保您已正确安装 FFmpeg 并且文件格式受支持。")
        return
    except Exception as e:
        print(f"读取文件时发生未知错误: {e}")
        return

    # 获取不带扩展名的文件名
    base_name = os.path.splitext(os.path.basename(input_file_path))[0]

    # 创建输出目录（如果不存在）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"已创建输出目录: {output_dir}")

    # 定义目标封装格式
    # pydub 会根据格式扩展名自动选择合适的默认编码器
    output_formats = {
        'mp3': {'format': 'mp3'},
        'wav': {'format': 'wav'},
        'ogg': {'format': 'ogg'},
        'flac': {'format': 'flac'},
        'aac': {'format': 'mp4'},  # AAC 编码通常存储在 .mp4 容器中
        'm4a': {'format': 'ipod'},  # m4a 容器
        'wma': {'format': 'asf'},  # WMA 编码存储在 .asf 容器中
        'opus': {'format': 'opus'},
        'webm': {'format': 'webm'},  # WebM (通常是 Vorbis 或 Opus)
    }

    print("\n开始转换音频...")
    # 遍历所有目标格式并导出文件
    for format_ext, parameters in output_formats.items():
        output_file_path = os.path.join(output_dir, f"{base_name}.{format_ext}")

        try:
            print(f"  -> 正在导出为 {format_ext.upper()} 格式...")
            audio.export(output_file_path, **parameters)
            print(f"     成功保存到: {output_file_path}")
        except Exception as e:
            print(f"     导出为 {format_ext.upper()} 失败: {e}")
            print(f"     请检查您的 FFmpeg 是否支持该格式/编码器。")

    print("\n所有转换任务已完成！")


def main():
    # --- 设置命令行参数解析 ---
    parser = argparse.ArgumentParser(
        description="一个简单的音频转换工具，可将单个音频文件转换为多种主流格式。",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "input_file",
        type=str,
        help="要转换的输入音频文件的路径。\n例如: my_song.mp3 或 C:/Music/test.wav"
    )

    parser.add_argument(
        "-o", "--output_dir",
        type=str,
        default="converted_audio",
        help="用于存放转换后文件的输出目录。\n(默认: 'converted_audio')"
    )

    args = parser.parse_args()

    # 执行转换
    convert_audio(args.input_file, args.output_dir)


if __name__ == "__main__":
    main()