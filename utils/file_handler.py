"""
File handling utilities for uploading, saving, and managing files
"""

import os
import shutil
from pathlib import Path
from typing import BinaryIO
from config import TEMP_DIR, OUTPUT_DIR, MAX_FILE_SIZE_MB, SUPPORTED_FORMATS


class FileHandler:
    """Handle file operations for the application"""
    
    def __init__(self):
        self.temp_dir = TEMP_DIR
        self.output_dir = OUTPUT_DIR
        self.max_size_bytes = MAX_FILE_SIZE_MB * 1024 * 1024
        self.supported_formats = SUPPORTED_FORMATS
    
    def save_uploaded_file(self, uploaded_file) -> str:
        """
        Save an uploaded file to temp directory
        
        Args:
            uploaded_file: Streamlit uploaded file object
            
        Returns:
            Path to saved file
        """
        # Check file size
        file_size = uploaded_file.size
        if file_size > self.max_size_bytes:
            raise ValueError(
                f"File size ({file_size / (1024*1024):.2f} MB) exceeds "
                f"maximum allowed size ({MAX_FILE_SIZE_MB} MB)"
            )
        
        # Check file extension
        file_ext = Path(uploaded_file.name).suffix.lower()
        if file_ext not in self.supported_formats:
            raise ValueError(
                f"Unsupported file format: {file_ext}. "
                f"Supported formats: {', '.join(self.supported_formats)}"
            )
        
        # Save file
        file_path = self.temp_dir / uploaded_file.name
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        return str(file_path)
    
    def save_text(self, content: str, filename: str, output_dir: Path = None) -> str:
        """
        Save text content to file
        
        Args:
            content: Text content to save
            filename: Name of the output file
            output_dir: Directory to save to (default: OUTPUT_DIR)
            
        Returns:
            Path to saved file
        """
        output_dir = output_dir or self.output_dir
        file_path = output_dir / filename
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        return str(file_path)
    
    def cleanup(self, file_path: str):
        """
        Delete a temporary file
        
        Args:
            file_path: Path to file to delete
        """
        try:
            file_path = Path(file_path)
            if file_path.exists():
                file_path.unlink()
        except Exception as e:
            print(f"Warning: Could not delete {file_path}: {str(e)}")
    
    def cleanup_temp_dir(self):
        """Clean up all files in temp directory"""
        try:
            for file_path in self.temp_dir.glob("*"):
                if file_path.is_file():
                    file_path.unlink()
        except Exception as e:
            print(f"Warning: Could not clean temp directory: {str(e)}")
    
    def get_file_size(self, file_path: str) -> int:
        """
        Get file size in bytes
        
        Args:
            file_path: Path to file
            
        Returns:
            File size in bytes
        """
        return Path(file_path).stat().st_size
    
    def validate_audio_file(self, file_path: str) -> bool:
        """
        Validate that a file is a supported audio format
        
        Args:
            file_path: Path to file
            
        Returns:
            True if valid, False otherwise
        """
        file_path = Path(file_path)
        
        # Check if file exists
        if not file_path.exists():
            return False
        
        # Check extension
        if file_path.suffix.lower() not in self.supported_formats:
            return False
        
        # Check size
        if self.get_file_size(str(file_path)) > self.max_size_bytes:
            return False
        
        return True
