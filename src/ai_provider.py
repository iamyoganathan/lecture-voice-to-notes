"""
AI Provider abstraction layer for multiple LLM services
Supports: OpenAI, Groq, Ollama, and Hugging Face
"""

from typing import Optional, Dict, Any
import os


class AIProvider:
    """Abstract base for AI providers"""
    
    def __init__(self, provider_type: str, api_key: Optional[str] = None, **kwargs):
        """
        Initialize AI provider
        
        Args:
            provider_type: Type of provider (openai, groq, ollama, huggingface)
            api_key: API key for the provider (if required)
            **kwargs: Additional provider-specific parameters
        """
        self.provider_type = provider_type.lower()
        self.api_key = api_key
        self.client = None
        self.model = kwargs.get('model')
        self._initialize_client(**kwargs)
    
    def _initialize_client(self, **kwargs):
        """Initialize the specific provider client"""
        
        if self.provider_type == "openai":
            from openai import OpenAI
            self.client = OpenAI(api_key=self.api_key)
            self.model = self.model or "gpt-3.5-turbo"
            
        elif self.provider_type == "groq":
            from groq import Groq
            self.client = Groq(api_key=self.api_key)
            self.model = self.model or "llama-3.3-70b-versatile"
            
        else:
            raise ValueError(f"Unsupported provider type: {self.provider_type}. Supported: openai, groq")
    
    def generate_text(self, prompt: str, max_tokens: int = 1000, temperature: float = 0.7) -> str:
        """
        Generate text using the AI provider
        
        Args:
            prompt: The input prompt
            max_tokens: Maximum tokens to generate
            temperature: Generation temperature
            
        Returns:
            Generated text response
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content
                
        except Exception as e:
            raise Exception(f"Text generation error ({self.provider_type}): {str(e)}")
    
    def chat_completion(self, messages: list, max_tokens: int = 1000, temperature: float = 0.7) -> str:
        """
        Chat completion with conversation history
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            max_tokens: Maximum tokens to generate
            temperature: Generation temperature
            
        Returns:
            Generated response
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content
                
        except Exception as e:
            raise Exception(f"Chat completion error ({self.provider_type}): {str(e)}")


class TranscriptionProvider:
    """Handle audio transcription with multiple providers"""
    
    def __init__(self, provider_type: str, api_key: Optional[str] = None, **kwargs):
        """
        Initialize transcription provider
        
        Args:
            provider_type: Type of provider (openai, groq, local)
            api_key: API key for the provider (if required)
            **kwargs: Additional provider-specific parameters
        """
        self.provider_type = provider_type.lower()
        self.api_key = api_key
        self.client = None
        self.model = kwargs.get('model')
        self._initialize_client(**kwargs)
    
    def _initialize_client(self, **kwargs):
        """Initialize the specific transcription client"""
        
        if self.provider_type == "openai":
            from openai import OpenAI
            self.client = OpenAI(api_key=self.api_key)
            self.model = self.model or "whisper-1"
            
        elif self.provider_type == "groq":
            from groq import Groq
            self.client = Groq(api_key=self.api_key)
            self.model = self.model or "whisper-large-v3"
            
        else:
            raise ValueError(f"Unsupported transcription provider: {self.provider_type}. Supported: openai, groq")
    
    def transcribe(self, audio_path: str, language: str = None) -> str:
        """
        Transcribe audio file to text
        
        Args:
            audio_path: Path to audio file
            language: Language code (optional)
            
        Returns:
            Transcribed text
        """
        try:
            with open(audio_path, "rb") as audio_file:
                transcription = self.client.audio.transcriptions.create(
                    model=self.model,
                    file=audio_file,
                    language=language
                )
            return transcription.text
                
        except Exception as e:
            raise Exception(f"Transcription error ({self.provider_type}): {str(e)}")
    
    def transcribe_with_timestamps(self, audio_path: str, language: str = None) -> list:
        """
        Transcribe with timestamps
        
        Args:
            audio_path: Path to audio file
            language: Language code (optional)
            
        Returns:
            List of segments with timestamps and text
        """
        try:
            with open(audio_path, "rb") as audio_file:
                transcription = self.client.audio.transcriptions.create(
                    model=self.model,
                    file=audio_file,
                    language=language,
                    response_format="verbose_json",
                    timestamp_granularities=["segment"]
                )
            
            segments = []
            if hasattr(transcription, 'segments'):
                for seg in transcription.segments:
                    segments.append({
                        'start': seg.start,
                        'end': seg.end,
                        'text': seg.text
                    })
            return segments
                
        except Exception as e:
            raise Exception(f"Timestamp transcription error ({self.provider_type}): {str(e)}")


# Provider configurations and models
PROVIDER_CONFIGS = {
    "openai": {
        "name": "OpenAI",
        "requires_api_key": True,
        "llm_models": ["gpt-4", "gpt-3.5-turbo", "gpt-4-turbo"],
        "whisper_models": ["whisper-1"],
        "free": False
    },
    "groq": {
        "name": "Groq",
        "requires_api_key": True,
        "llm_models": ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "gemma2-9b-it"],
        "whisper_models": ["whisper-large-v3"],
        "free": True
    }
}


def get_available_providers():
    """Get list of available provider types"""
    return list(PROVIDER_CONFIGS.keys())


def get_provider_info(provider_type: str) -> Dict[str, Any]:
    """Get information about a specific provider"""
    return PROVIDER_CONFIGS.get(provider_type.lower(), {})
