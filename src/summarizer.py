"""
Note summarization module using multiple AI providers
"""

from typing import Optional
from pathlib import Path
from config import DEFAULT_MODEL, MAX_TOKENS, TEMPERATURE, PROMPTS_DIR
from src.ai_provider import AIProvider


class NoteSummarizer:
    """Generate structured notes from lecture transcriptions"""
    
    def __init__(self, api_key: Optional[str] = None, provider: str = "openai", model: str = None):
        """
        Initialize summarizer with provider
        
        Args:
            api_key: API key for the provider (if required)
            provider: Provider type (openai, groq, ollama, huggingface)
            model: Model to use (optional, uses default)
        """
        self.provider = AIProvider(
            provider_type=provider,
            api_key=api_key,
            model=model or DEFAULT_MODEL
        )
        self.max_tokens = MAX_TOKENS
        self.temperature = TEMPERATURE
    
    def generate_notes(self, transcription: str) -> str:
        """
        Generate structured notes from transcription
        
        Args:
            transcription: Lecture transcription text
            
        Returns:
            Structured notes in markdown format
        """
        prompt = self._get_notes_prompt()
        
        try:
            response = self.provider.chat_completion(
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": f"Please create structured notes from this lecture:\n\n{transcription}"}
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            return response
            
        except Exception as e:
            raise Exception(f"Note generation error: {str(e)}")
    
    def generate_summary(self, transcription: str, max_length: int = 300) -> str:
        """
        Generate a brief summary of the lecture
        
        Args:
            transcription: Lecture transcription text
            max_length: Maximum word count for summary
            
        Returns:
            Brief summary
        """
        prompt = f"""You are an expert at summarizing academic lectures.
Create a concise summary (maximum {max_length} words) that captures the key points and main ideas.
Focus on the most important concepts, definitions, and takeaways."""
        
        try:
            response = self.provider.chat_completion(
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": transcription}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            return response
            
        except Exception as e:
            raise Exception(f"Summary generation error: {str(e)}")
    
    def extract_key_points(self, transcription: str, num_points: int = 10) -> str:
        """
        Extract key points as bullet points
        
        Args:
            transcription: Lecture transcription text
            num_points: Number of key points to extract
            
        Returns:
            Key points as formatted text
        """
        prompt = f"""You are an expert at identifying key points in lectures.
Extract the {num_points} most important points from this lecture.
Format them as a numbered list with clear, concise statements."""
        
        try:
            response = self.provider.chat_completion(
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": transcription}
                ],
                max_tokens=800,
                temperature=0.7
            )
            
            return response
            
        except Exception as e:
            raise Exception(f"Key point extraction error: {str(e)}")
    
    def _get_notes_prompt(self) -> str:
        """
        Load or create the notes generation prompt
        
        Returns:
            System prompt for note generation
        """
        prompt_file = PROMPTS_DIR / "summarize.txt"
        
        if prompt_file.exists():
            return prompt_file.read_text()
        
        # Default prompt
        default_prompt = """You are an expert note-taker for students. Your task is to transform lecture transcriptions into well-structured, comprehensive study notes.

Follow these guidelines:
1. Create a clear hierarchy with main topics and subtopics
2. Use markdown formatting (headers, bullets, bold, italic)
3. Identify and highlight key concepts, definitions, and terminology
4. Organize information logically by theme or chronology
5. Include important examples, case studies, or demonstrations mentioned
6. Note any formulas, equations, or technical details
7. Summarize complex explanations in clear, concise language
8. Preserve important numbers, dates, names, and references
9. Use bullet points for lists and related items
10. Add section summaries for long topics

Format:
# [Main Topic/Lecture Title]

## Overview
[Brief 2-3 sentence summary of the lecture]

## Key Concepts
- [Important terms and definitions]

## Main Topics

### [Topic 1]
[Detailed notes with sub-points]

### [Topic 2]
[Detailed notes with sub-points]

## Important Points to Remember
- [Critical takeaways]

## Study Questions
- [2-3 questions for review]

Make the notes clear, comprehensive, and easy to study from."""
        
        # Save default prompt
        prompt_file.write_text(default_prompt)
        
        return default_prompt
