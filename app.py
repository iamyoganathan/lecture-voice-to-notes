"""
Lecture Voice-to-Notes Generator
Main Streamlit Application
"""

import streamlit as st
import os
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Lecture Notes AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import modules
from src.audio_processor import AudioProcessor
from src.transcriber import Transcriber
from src.summarizer import NoteSummarizer
from src.quiz_generator import QuizGenerator
from src.flashcard_generator import FlashcardGenerator
from src.ai_provider import get_available_providers, get_provider_info, PROVIDER_CONFIGS
from utils.file_handler import FileHandler
import config

# Initialize session state
if 'transcription' not in st.session_state:
    st.session_state.transcription = None
if 'notes' not in st.session_state:
    st.session_state.notes = None
if 'quiz' not in st.session_state:
    st.session_state.quiz = None
if 'flashcards' not in st.session_state:
    st.session_state.flashcards = None

def main():
    """Main application function"""
    
    # Header
    st.title("🎓 Lecture Voice-to-Notes Generator")
    st.markdown("Transform your lecture recordings into structured notes, quizzes, and flashcards!")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # AI Provider Selection
        st.subheader("🤖 AI Provider")
        
        # Transcription provider
        transcription_providers = ["openai", "groq"]
        trans_provider_labels = {
            "openai": "OpenAI Whisper (Paid)",
            "groq": "Groq Whisper (FREE)"
        }
        
        transcription_provider = st.selectbox(
            "Transcription Provider",
            transcription_providers,
            index=1,  # Default to Groq
            format_func=lambda x: trans_provider_labels[x],
            help="Choose the provider for audio transcription"
        )
        
        # LLM provider
        llm_providers = ["openai", "groq"]
        llm_provider_labels = {
            "openai": "OpenAI GPT (Paid)",
            "groq": "Groq (FREE)"
        }
        
        llm_provider = st.selectbox(
            "Text Generation Provider",
            llm_providers,
            index=1,  # Default to Groq (free)
            format_func=lambda x: llm_provider_labels[x],
            help="Choose the provider for notes, quizzes, and flashcards"
        )
        
        # API Keys based on selected provider
        st.subheader("🔑 API Keys")
        
        api_key = None
        groq_api_key = None
        
        if transcription_provider == "openai" or llm_provider == "openai":
            api_key = st.text_input(
                "OpenAI API Key",
                value=config.OPENAI_API_KEY,
                type="password",
                help="Enter your OpenAI API key"
            )
        
        if transcription_provider == "groq" or llm_provider == "groq":
            groq_api_key = st.text_input(
                "Groq API Key (FREE)",
                value=config.GROQ_API_KEY,
                type="password",
                help="Get free API key from https://console.groq.com"
            )
            if not groq_api_key:
                st.warning("⚠️ Get your FREE Groq API key at https://console.groq.com")
        
        # Model selection based on provider
        st.subheader("🎯 Model Selection")
        
        if llm_provider in PROVIDER_CONFIGS:
            available_models = PROVIDER_CONFIGS[llm_provider]["llm_models"]
            if available_models:
                model_choice = st.selectbox(
                    "AI Model",
                    available_models,
                    help="Choose the model for note generation"
                )
            else:
                model_choice = None
        else:
            model_choice = "gpt-3.5-turbo"
        
        # Output preferences
        st.subheader("Output Options")
        generate_summary = st.checkbox("Generate Summary", value=True)
        generate_quiz = st.checkbox("Generate Quiz", value=True)
        generate_flashcards = st.checkbox("Generate Flashcards", value=True)
        
        # Quiz settings
        if generate_quiz:
            num_questions = st.slider("Number of Quiz Questions", 5, 20, 10)
        
        # Flashcard settings
        if generate_flashcards:
            num_flashcards = st.slider("Number of Flashcards", 5, 30, 15)
        
        st.divider()
        st.markdown("### 📚 About")
        st.info(
            "Upload a lecture audio file, and this app will:\n"
            "- Transcribe the audio\n"
            "- Generate structured notes\n"
            "- Create quiz questions\n"
            "- Make flashcards for study"
        )
    
    # Main content area
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📤 Upload", "📝 Transcription", "📋 Notes", "❓ Quiz", "🗂️ Flashcards"
    ])
    
    # Tab 1: Upload
    with tab1:
        st.header("Upload Lecture Audio")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            uploaded_file = st.file_uploader(
                "Choose an audio file",
                type=['mp3', 'wav', 'm4a', 'mp4', 'mpeg', 'mpga', 'webm'],
                help="Supported formats: MP3, WAV, M4A, MP4, MPEG, WEBM"
            )
            
            if uploaded_file:
                st.success(f"✅ File uploaded: {uploaded_file.name}")
                st.write(f"📊 File size: {uploaded_file.size / (1024*1024):.2f} MB")
                
                # Audio player
                st.audio(uploaded_file)
                
                # Process button
                if st.button("🚀 Start Processing", type="primary", use_container_width=True):
                    # Validate API keys based on selected providers
                    if transcription_provider == "openai" and not api_key:
                        st.error("❌ Please enter your OpenAI API key in the sidebar!")
                    elif transcription_provider == "groq" and not groq_api_key:
                        st.error("❌ Please enter your Groq API key in the sidebar! Get it FREE at https://console.groq.com")
                    elif llm_provider == "openai" and not api_key:
                        st.error("❌ Please enter your OpenAI API key for text generation!")
                    elif llm_provider == "groq" and not groq_api_key:
                        st.error("❌ Please enter your Groq API key for text generation!")
                    else:
                        # Determine which API key to use for each provider
                        trans_key = groq_api_key if transcription_provider == "groq" else api_key
                        llm_key = groq_api_key if llm_provider == "groq" else api_key
                        
                        process_audio(
                            uploaded_file, 
                            trans_key, llm_key,
                            transcription_provider, llm_provider,
                            model_choice, 
                            generate_summary, generate_quiz, generate_flashcards,
                            num_questions if generate_quiz else 0,
                            num_flashcards if generate_flashcards else 0
                        )
        
        with col2:
            st.markdown("### 💡 Tips")
            st.markdown("""
            - **Clear audio** works best
            - **Maximum 25 MB** file size
            - **Remove background noise** if possible
            - **Speaker close to mic** for accuracy
            """)
            
            st.markdown("### ⏱️ Processing Time")
            st.markdown("""
            - **Transcription**: ~1-2 min per 10 min audio
            - **Notes**: ~30 seconds
            - **Quiz & Flashcards**: ~1 minute
            """)
    
    # Tab 2: Transcription
    with tab2:
        st.header("📝 Lecture Transcription")
        
        if st.session_state.transcription:
            st.success("✅ Transcription completed!")
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.text_area(
                    "Full Transcription",
                    st.session_state.transcription,
                    height=400,
                    help="The complete transcription of your lecture"
                )
            
            with col2:
                st.metric("Word Count", len(st.session_state.transcription.split()))
                st.metric("Character Count", len(st.session_state.transcription))
                
                # Download button
                if st.download_button(
                    label="📥 Download Transcript",
                    data=st.session_state.transcription,
                    file_name="transcript.txt",
                    mime="text/plain"
                ):
                    st.success("Downloaded!")
        else:
            st.info("👆 Upload and process an audio file to see the transcription here.")
    
    # Tab 3: Notes
    with tab3:
        st.header("📋 Structured Notes")
        
        if st.session_state.notes:
            st.success("✅ Notes generated!")
            
            st.markdown(st.session_state.notes)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.download_button(
                    label="📥 Download as TXT",
                    data=st.session_state.notes,
                    file_name="lecture_notes.txt",
                    mime="text/plain"
                ):
                    st.success("Downloaded!")
            
            with col2:
                if st.download_button(
                    label="📥 Download as MD",
                    data=st.session_state.notes,
                    file_name="lecture_notes.md",
                    mime="text/markdown"
                ):
                    st.success("Downloaded!")
        else:
            st.info("👆 Upload and process an audio file to see the notes here.")
    
    # Tab 4: Quiz
    with tab4:
        st.header("❓ Practice Quiz")
        
        if st.session_state.quiz:
            st.success("✅ Quiz generated!")
            
            st.markdown(st.session_state.quiz)
            
            if st.download_button(
                label="📥 Download Quiz",
                data=st.session_state.quiz,
                file_name="lecture_quiz.txt",
                mime="text/plain"
            ):
                st.success("Downloaded!")
        else:
            st.info("👆 Upload and process an audio file to see the quiz here.")
    
    # Tab 5: Flashcards
    with tab5:
        st.header("🗂️ Study Flashcards")
        
        if st.session_state.flashcards:
            st.success("✅ Flashcards generated!")
            
            st.markdown(st.session_state.flashcards)
            
            if st.download_button(
                label="📥 Download Flashcards",
                data=st.session_state.flashcards,
                file_name="lecture_flashcards.txt",
                mime="text/plain"
            ):
                st.success("Downloaded!")
        else:
            st.info("👆 Upload and process an audio file to see the flashcards here.")

def process_audio(file, trans_api_key, llm_api_key, trans_provider, llm_provider, 
                 model, gen_summary, gen_quiz, gen_flashcards, num_q, num_f):
    """Process the uploaded audio file"""
    
    try:
        # Step 1: Save uploaded file temporarily
        with st.spinner("💾 Saving audio file..."):
            file_handler = FileHandler()
            audio_path = file_handler.save_uploaded_file(file)
            st.success("✅ File saved!")
        
        # Step 2: Process audio (if needed)
        with st.spinner("🎵 Processing audio..."):
            processor = AudioProcessor()
            processed_path = processor.process(audio_path)
            st.success("✅ Audio processed!")
        
        # Step 3: Transcribe
        provider_name = trans_provider.upper() if trans_provider != "local" else "Faster-Whisper (Local)"
        with st.spinner(f"🎤 Transcribing audio with {provider_name} (this may take a few minutes)..."):
            transcriber = Transcriber(
                api_key=trans_api_key,
                provider=trans_provider
            )
            transcription = transcriber.transcribe(processed_path)
            st.session_state.transcription = transcription
            st.success(f"✅ Transcription complete using {provider_name}!")
        
        # Step 4: Generate notes
        if gen_summary:
            provider_name = llm_provider.upper()
            with st.spinner(f"📝 Generating structured notes with {provider_name}..."):
                summarizer = NoteSummarizer(
                    api_key=llm_api_key,
                    provider=llm_provider,
                    model=model
                )
                notes = summarizer.generate_notes(transcription)
                st.session_state.notes = notes
                st.success(f"✅ Notes generated using {provider_name}!")
        
        # Step 5: Generate quiz
        if gen_quiz:
            provider_name = llm_provider.upper()
            with st.spinner(f"❓ Creating quiz questions with {provider_name}..."):
                quiz_gen = QuizGenerator(
                    api_key=llm_api_key,
                    provider=llm_provider,
                    model=model
                )
                quiz = quiz_gen.generate_quiz(transcription, num_q)
                st.session_state.quiz = quiz
                st.success(f"✅ Quiz created using {provider_name}!")
        
        # Step 6: Generate flashcards
        if gen_flashcards:
            provider_name = llm_provider.upper()
            with st.spinner(f"🗂️ Making flashcards with {provider_name}..."):
                flashcard_gen = FlashcardGenerator(
                    api_key=llm_api_key,
                    provider=llm_provider,
                    model=model
                )
                flashcards = flashcard_gen.generate_flashcards(transcription, num_f)
                st.session_state.flashcards = flashcards
                st.success(f"✅ Flashcards ready using {provider_name}!")
        
        # Clean up temporary files
        file_handler.cleanup(audio_path)
        if processed_path != audio_path:
            file_handler.cleanup(processed_path)
        
        st.balloons()
        st.success("🎉 All done! Check the tabs above for your results.")
        
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        st.exception(e)

if __name__ == "__main__":
    main()
