"""
Audio processing module for handling and preprocessing audio files
"""

import os
from pathlib import Path
from pydub import AudioSegment
from pydub.effects import normalize
import librosa
import soundfile as sf
import numpy as np
from config import AUDIO_SAMPLE_RATE, TEMP_DIR


class AudioProcessor:
    """Process and prepare audio files for transcription"""
    
    def __init__(self):
        self.sample_rate = AUDIO_SAMPLE_RATE
        self.temp_dir = TEMP_DIR
    
    def process(self, audio_path: str) -> str:
        """
        Process audio file: convert format, normalize, and prepare for transcription
        
        Args:
            audio_path: Path to the audio file
            
        Returns:
            Path to the processed audio file
        """
        audio_path = Path(audio_path)
        
        # Check if file exists
        if not audio_path.exists():
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
        
        # For now, return the original path
        # In future, add noise reduction, normalization, etc.
        return str(audio_path)
    
    def convert_to_wav(self, audio_path: str) -> str:
        """
        Convert audio file to WAV format
        
        Args:
            audio_path: Path to the audio file
            
        Returns:
            Path to the converted WAV file
        """
        audio_path = Path(audio_path)
        output_path = self.temp_dir / f"{audio_path.stem}_converted.wav"
        
        try:
            # Load audio file
            audio = AudioSegment.from_file(str(audio_path))
            
            # Convert to mono and set sample rate
            audio = audio.set_channels(1)
            audio = audio.set_frame_rate(self.sample_rate)
            
            # Export as WAV
            audio.export(str(output_path), format='wav')
            
            return str(output_path)
            
        except Exception as e:
            raise Exception(f"Error converting audio: {str(e)}")
    
    def normalize_audio(self, audio_path: str) -> str:
        """
        Normalize audio levels
        
        Args:
            audio_path: Path to the audio file
            
        Returns:
            Path to the normalized audio file
        """
        audio_path = Path(audio_path)
        output_path = self.temp_dir / f"{audio_path.stem}_normalized.wav"
        
        try:
            # Load audio
            audio = AudioSegment.from_file(str(audio_path))
            
            # Normalize
            normalized_audio = normalize(audio)
            
            # Export
            normalized_audio.export(str(output_path), format='wav')
            
            return str(output_path)
            
        except Exception as e:
            raise Exception(f"Error normalizing audio: {str(e)}")
    
    def reduce_noise(self, audio_path: str) -> str:
        """
        Apply basic noise reduction
        
        Args:
            audio_path: Path to the audio file
            
        Returns:
            Path to the processed audio file
        """
        audio_path = Path(audio_path)
        output_path = self.temp_dir / f"{audio_path.stem}_denoised.wav"
        
        try:
            # Load audio using librosa
            y, sr = librosa.load(str(audio_path), sr=self.sample_rate)
            
            # Apply basic noise gate (simple threshold)
            threshold = np.percentile(np.abs(y), 5)  # 5th percentile as noise floor
            y_denoised = np.where(np.abs(y) > threshold, y, 0)
            
            # Save processed audio
            sf.write(str(output_path), y_denoised, sr)
            
            return str(output_path)
            
        except Exception as e:
            raise Exception(f"Error reducing noise: {str(e)}")
    
    def get_duration(self, audio_path: str) -> float:
        """
        Get audio duration in seconds
        
        Args:
            audio_path: Path to the audio file
            
        Returns:
            Duration in seconds
        """
        try:
            audio = AudioSegment.from_file(str(audio_path))
            return len(audio) / 1000.0  # Convert milliseconds to seconds
        except Exception as e:
            raise Exception(f"Error getting audio duration: {str(e)}")
    
    def split_audio(self, audio_path: str, chunk_length_ms: int = 600000) -> list:
        """
        Split long audio into chunks (for processing very long lectures)
        
        Args:
            audio_path: Path to the audio file
            chunk_length_ms: Length of each chunk in milliseconds (default 10 minutes)
            
        Returns:
            List of paths to audio chunks
        """
        audio_path = Path(audio_path)
        
        try:
            audio = AudioSegment.from_file(str(audio_path))
            chunks = []
            
            # Split audio into chunks
            for i, chunk_start in enumerate(range(0, len(audio), chunk_length_ms)):
                chunk = audio[chunk_start:chunk_start + chunk_length_ms]
                chunk_path = self.temp_dir / f"{audio_path.stem}_chunk_{i}.wav"
                chunk.export(str(chunk_path), format='wav')
                chunks.append(str(chunk_path))
            
            return chunks
            
        except Exception as e:
            raise Exception(f"Error splitting audio: {str(e)}")
