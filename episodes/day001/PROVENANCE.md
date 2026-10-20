# Day 1 素材与复现

- 文案、网页、排版与渲染代码：本项目自主创作，GPT 辅助。无第三方影视、音乐或付费素材。
- 原型内容：本仓库 f8c5a01 的公开 README、STATE、DECISIONS、LOG；完整固定提交及源文件在 prototype/snapshot.json。四页摘要由制作时编排，非网页自动推理。
- 演示图片：本次实际操作自制原型的浏览器截图，原件在 evidence/。视频仅剪裁卡片/弹窗区域以便阅读并加入字幕，保留截图剪辑标识；不是连续录屏。
- 旁白：本机 macOS `say`，Tingting 中文合成声音，语速 210。分句合成并测量实际音频时长；无配乐。
- 字体：macOS 黑体，脚本使用系统字体绘制；不在仓库分发字体文件。可用 CJK_FONT 指定有权使用的本地中文字体。
- 封面：Pillow 几何图形与文字原创排版；未使用新的生成图或外部图片。

## 复现

需要 Python 3 + Pillow、FFmpeg/FFprobe，以及 macOS `say` 的 Tingting 语音。

在仓库根目录运行：

```sh
python3 scripts/build_memory_machine.py
python3 scripts/render_day1.py
```

第二步使用已保存的实际截图，不需网络。临时音频及检查图片写入被忽略的 tmp/day001。输出成片、封面、逐字稿、SRT 和逐句时间线到 episodes/day001。

不同 macOS 语音版本可能改变读音或时长；重建时脚本会重新测量并计算字幕。当前发布候选的检查记录见 QA.md。
