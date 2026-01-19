<div align="center">

# 🎓 Lecture Voice-to-Notes Generator

### Transform Your Lecture Recordings into Comprehensive Study Materials

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30.0-FF4B4B.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Live Demo](https://img.shields.io/badge/Live-Demo-success.svg)](https://lecture-voice-to-notes-3smm9xbpjnqzkcotfuejba.streamlit.app/)

*An AI-powered application that automatically converts lecture audio into structured notes, interactive quizzes, and study flashcards using advanced speech-to-text and generative AI technology.*

[🚀 Live Demo](https://lecture-voice-to-notes-3smm9xbpjnqzkcotfuejba.streamlit.app/) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API Providers](#-api-providers) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Providers](#-api-providers)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Cost Estimates](#-cost-estimates)
- [Troubleshooting](#-troubleshooting)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🌟 Features

### Core Capabilities

- **🎙️ Audio Transcription** - Convert lecture recordings to accurate text transcripts
- **📝 Smart Note Generation** - Automatically create structured, comprehensive study notes
- **❓ Quiz Generation** - Generate practice questions (Multiple Choice, True/False, Short Answer)
- **💭 Flashcard Creation** - Build effective flashcards for active recall studying
- **📥 Multiple Export Formats** - Download content as TXT, Markdown, PDF, or DOCX

### Flexible AI Provider Options

- **Groq** - FREE, fast, and high-quality AI (⚡ Recommended)
- **OpenAI** - Industry-leading models with premium quality

### User-Friendly Interface

- Clean, intuitive Streamlit web interface
- Real-time processing status updates
- Interactive content preview and editing
- Organized multi-tab layout

---

## 🎬 Demo

### 🌐 Live Demo
**Try it now:** [https://lecture-voice-to-notes-3smm9xbpjnqzkcotfuejba.streamlit.app/](https://lecture-voice-to-notes-3smm9xbpjnqzkcotfuejba.streamlit.app/)

> **FREE AI-powered transcription using Groq!** No installation required - just upload your audio and get instant results.

### Features Demo
- Upload lecture audio (MP3, WAV, M4A, etc.)
- Get accurate transcriptions with timestamps
- Generate structured study notes automatically
- Create practice quizzes and flashcards
- Export in multiple formats (TXT, MD, PDF, DOCX)

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- 100MB free disk space

### Quick Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/lecture-voice-to-notes.git
   cd lecture-voice-to-notes
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   # Groq (FREE - Recommended)
   GROQ_API_KEY=your_groq_api_key_here
   
   # OpenAI (Optional - Premium)
   OPENAI_API_KEY=your_openai_api_key_here
   
   # Default Settings
   DEFAULT_PROVIDER=groq
   DEFAULT_TRANSCRIPTION_PROVIDER=groq
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   
   Navigate to `http://localhost:8501`

---

## ⚙️ Configuration

### Getting API Keys

#### Groq (FREE - Recommended) ⚡

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up for a free account (no credit card required)
3. Navigate to API Keys section
4. Create and copy your API key
5. Paste into `.env` file

**Why Groq?**
- ✅ Completely free with generous limits
- ✅ Lightning-fast processing
- ✅ High-quality results
- ✅ No credit card required

#### OpenAI (Premium Option)

1. Visit [platform.openai.com](https://platform.openai.com)
2. Create an account and add payment method
3. Generate an API key
4. Paste into `.env` file

### Configuration Options

Edit [config.py](config.py) to customize:

```python
# Audio Processing
MAX_FILE_SIZE_MB = 25
SAMPLE_RATE = 16000

# AI Models
PROVIDER_MODELS = {
    'groq': {
        'transcription': ['whisper-large-v3'],
        'text': ['llama-3.3-70b-versatile', 'mixtral-8x7b-32768']
    },
    'openai': {
        'transcription': ['whisper-1'],
        'text': ['gpt-3.5-turbo', 'gpt-4']
    }
}

# Generation Defaults
DEFAULT_NUM_QUESTIONS = 10
DEFAULT_NUM_FLASHCARDS = 15
```

---

## 📖 Usage

### Step-by-Step Guide

1. **Launch the Application**
   ```bash
   streamlit run app.py
   ```

2. **Configure Provider Settings** (Sidebar)
   - Select your AI provider (Groq recommended)
   - Choose transcription provider
   - Enter API key if not in `.env`
   - Select AI models

3. **Upload Audio File**
   - Click the "Upload Audio" section
   - Select your lecture recording (MP3, WAV, M4A, FLAC, OGG)
   - Supported formats: Most common audio formats
   - Maximum file size: 25MB (configurable)

4. **Configure Generation Options**
   - ✅ Generate comprehensive notes
   - ✅ Create practice quiz
   - ✅ Build study flashcards
   - Set number of quiz questions (5-50)
   - Set number of flashcards (5-50)

5. **Start Processing**
   - Click "🚀 Start Processing"
   - Watch real-time progress updates
   - Processing time: ~1-3 minutes per hour of audio

6. **Review Results**
   - **Transcription Tab**: Full audio transcript with timestamps
   - **Notes Tab**: Structured study notes with key concepts
   - **Quiz Tab**: Interactive practice questions with answers
   - **Flashcards Tab**: Question-answer pairs for studying

7. **Export Your Content**
   - Choose format: TXT, Markdown, PDF, or DOCX
   - Click download button
   - Files saved to `output/` directory

### Tips for Best Results

- **Audio Quality**: Use clear recordings with minimal background noise
- **File Length**: Split very long lectures (>2 hours) into parts
- **Topic Clarity**: Recordings with clear structure produce better notes
- **Language**: Currently optimized for English content

---

## 🔌 API Providers

### Supported Providers

| Provider | Transcription | Text Generation | Cost | Speed | Quality |
|----------|--------------|-----------------|------|-------|---------|
| **Groq** | ✅ whisper-large-v3 | ✅ llama-3.3-70b | FREE | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ |
| **OpenAI** | ✅ whisper-1 | ✅ gpt-3.5/gpt-4 | Paid | ⚡⚡ | ⭐⭐⭐⭐⭐ |

### Provider Details

#### Groq (Recommended)
```python
# Models Used
Transcription: whisper-large-v3
Text Generation: llama-3.3-70b-versatile

# Features
- Free tier with generous limits
- Ultra-fast inference
- Excellent quality for notes and quizzes
- No credit card required
```

#### OpenAI
```python
# Models Used
Transcription: whisper-1
Text Generation: gpt-3.5-turbo / gpt-4

# Features
- Industry-leading quality
- Highly consistent results
- Pay-as-you-go pricing
- Advanced customization options
```

---

## 🛠️ Technology Stack

### Frontend & UI
- **Streamlit** `1.30.0` - Web application framework
- **Python** `3.8+` - Core programming language

### AI & Machine Learning
- **OpenAI API** - Whisper speech-to-text, GPT models
- **Groq API** - Fast inference for Llama and Whisper models

### Audio Processing
- **PyDub** `0.25.1` - Audio file manipulation
- **Librosa** `0.10.1` - Audio analysis
- **soundfile** `0.12.1` - Audio I/O

### Document Generation
- **FPDF** `1.7.2` - PDF export
- **python-docx** `1.1.0` - DOCX export
- **markdown** `3.5.2` - Markdown formatting

### Utilities
- **python-dotenv** - Environment variable management
- **requests** - HTTP library

---

## 📁 Project Structure

```
lecture-voice-to-notes/
│
├── 📄 app.py                      # Main Streamlit application
├── 📄 config.py                   # Configuration and settings
├── 📄 requirements.txt            # Python dependencies
├── 📄 .env                        # Environment variables (create this)
├── 📄 .gitignore                  # Git ignore rules
├── 📄 README.md                   # This file
│
├── 📁 src/                        # Core application modules
│   ├── 📄 __init__.py
│   ├── 📄 ai_provider.py          # AI provider abstraction layer
│   ├── 📄 audio_processor.py      # Audio preprocessing and handling
│   ├── 📄 transcriber.py          # Speech-to-text transcription
│   ├── 📄 summarizer.py           # Intelligent note generation
│   ├── 📄 quiz_generator.py       # Quiz creation logic
│   └── 📄 flashcard_generator.py  # Flashcard generation
│
├── 📁 utils/                      # Utility functions
│   ├── 📄 __init__.py
│   ├── 📄 file_handler.py         # File I/O operations
│   └── 📄 export.py               # Export to multiple formats
│
├── 📁 temp/                       # Temporary files (auto-created)
├── 📁 output/                     # Generated files (auto-created)
└── 📁 screenshots/                # Demo images (optional)
```

### Key Components

- **app.py** - Main application entry point with Streamlit UI
- **src/ai_provider.py** - Unified interface for AI providers (Groq/OpenAI)
- **src/transcriber.py** - Handles audio-to-text conversion
- **src/summarizer.py** - Generates structured notes from transcripts
- **src/quiz_generator.py** - Creates educational quizzes
- **src/flashcard_generator.py** - Builds study flashcards
- **utils/export.py** - Exports content to various formats

---

## 💰 Cost Estimates

### Groq (FREE) ⚡
```
Transcription: $0.00
Text Generation: $0.00
Total: $0.00 per hour of lecture
```

### OpenAI (Premium)
```
Based on OpenAI pricing (January 2026):

Whisper Transcription:  $0.006/minute → $0.36/hour
GPT-3.5-turbo:          $0.50/1M tokens → ~$0.05-0.10/hour
GPT-4:                  $10/1M tokens → ~$0.50-1.00/hour

Typical costs per lecture hour:
- With GPT-3.5: ~$0.40-0.50
- With GPT-4: ~$0.85-1.35
```

**Recommendation**: Use Groq for unlimited free processing!

---

## 🐛 Troubleshooting

### Common Issues

#### Installation Issues

**Problem**: `ModuleNotFoundError: No module named 'streamlit'`
```bash
# Solution
pip install -r requirements.txt
```

**Problem**: `Python version too old`
```bash
# Solution: Upgrade Python
# Visit https://www.python.org/downloads/
# Install Python 3.8 or higher
```

#### API Key Issues

**Problem**: `Invalid API key` or `Authentication failed`
```bash
# Solution 1: Check .env file
cat .env  # Linux/Mac
type .env  # Windows

# Solution 2: Verify key format
# Groq keys start with: gsk_
# OpenAI keys start with: sk-

# Solution 3: Re-enter key in app sidebar
```

**Problem**: `Rate limit exceeded` (OpenAI)
```bash
# Solution: Switch to Groq (FREE)
# Or wait and retry with OpenAI
# Or upgrade OpenAI plan
```

#### Audio Processing Issues

**Problem**: `Audio file too large`
```bash
# Solution 1: Compress audio
# Use Audacity or online tools to reduce file size

# Solution 2: Split long lectures
# Process in parts (e.g., 1-hour segments)

# Solution 3: Increase limit in config.py
MAX_FILE_SIZE_MB = 50  # Increase if needed
```

**Problem**: `Poor transcription quality`
```bash
# Solutions:
# ✓ Use clear audio with minimal background noise
# ✓ Ensure speaker is close to microphone
# ✓ Remove music/sound effects from recording
# ✓ Try different AI model (Groq whisper-large-v3 is excellent)
```

#### FFmpeg Warning

**Warning**: `Couldn't find ffmpeg or avconv`
```bash
# This is optional - app works without FFmpeg
# To install (optional):

# Windows: 
# Download from https://ffmpeg.org/download.html

# Mac:
brew install ffmpeg

# Linux:
sudo apt-get install ffmpeg
```

### Getting Help

1. Check the [Issues](https://github.com/yourusername/lecture-voice-to-notes/issues) page
2. Search for similar problems
3. Create a new issue with:
   - Error message
   - Steps to reproduce
   - Your environment (OS, Python version)

---

## 🔮 Future Enhancements

### Planned Features

- [ ] **Real-time Recording** - Record and transcribe lectures live
- [ ] **Speaker Diarization** - Identify and label different speakers
- [ ] **Multi-language Support** - Process lectures in multiple languages
- [ ] **Integration with Note Apps** - Sync with Notion, Evernote, OneNote
- [ ] **Mobile Application** - iOS and Android versions
- [ ] **Collaborative Features** - Share and collaborate on notes
- [ ] **Visual Diagrams** - Auto-generate diagrams from descriptions
- [ ] **Video Support** - Extract audio from video lectures
- [ ] **Advanced Search** - Search across all processed lectures
- [ ] **Study Analytics** - Track learning progress and quiz performance

### Contributions Welcome!

Have an idea? [Open an issue](https://github.com/yourusername/lecture-voice-to-notes/issues/new) or submit a pull request!

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute

1. **Report Bugs** - Found an issue? [Report it](https://github.com/yourusername/lecture-voice-to-notes/issues)
2. **Suggest Features** - Have an idea? Share it in discussions
3. **Improve Documentation** - Help make docs clearer
4. **Submit Code** - Fix bugs or add features

### Contribution Process

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/lecture-voice-to-notes.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**
   - Write clean, documented code
   - Follow existing code style
   - Add tests if applicable

4. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**
   - Describe your changes
   - Reference any related issues

### Code Style Guidelines

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Comment complex logic
- Keep functions focused and concise

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 Lecture Voice-to-Notes Generator Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

### Technologies & Services

- **[OpenAI](https://openai.com)** - For Whisper and GPT models that pioneered this space
- **[Groq](https://groq.com)** - For providing FREE, lightning-fast AI inference
- **[Streamlit](https://streamlit.io)** - For the amazing web framework
- **[Python Community](https://www.python.org)** - For excellent libraries and tools

### Inspiration

- Students worldwide struggling with lecture note-taking
- The need for accessible AI-powered educational tools
- Open-source community and collaborative development

### Special Thanks

- All contributors who have helped improve this project
- Beta testers who provided valuable feedback
- The open-source community for continuous inspiration

---

## 📞 Contact & Support

### Get Help

- **Documentation**: You're reading it!
- **Issues**: [GitHub Issues](https://github.com/yourusername/lecture-voice-to-notes/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/lecture-voice-to-notes/discussions)

### Stay Updated

- ⭐ **Star this repo** to stay updated with new features
- 👁️ **Watch** for notifications on updates
- 🍴 **Fork** to create your own version

---

<div align="center">

### ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/lecture-voice-to-notes&type=Date)](https://star-history.com/#yourusername/lecture-voice-to-notes&Date)

---

**Made with ❤️ by developers, for students**

**Happy Learning! 📚✨**

[Back to Top](#-lecture-voice-to-notes-generator)

</div>
