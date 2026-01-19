# Streamlit Deployment Guide

## 🚀 Deploy to Streamlit Community Cloud (FREE)

### Prerequisites
- GitHub account with your project repository
- Groq API key (FREE at https://console.groq.com)

### Step-by-Step Deployment

#### 1. Push to GitHub (Already Done ✅)
Your code is already on GitHub!

#### 2. Go to Streamlit Community Cloud
Visit: https://share.streamlit.io/

#### 3. Sign In with GitHub
- Click "Sign in with GitHub"
- Authorize Streamlit Community Cloud

#### 4. Deploy New App
- Click "New app" button
- Select your repository: `[yourusername]/lecture-voice-to-notes`
- Main file path: `app.py`
- Branch: `main`

#### 5. Configure Secrets (IMPORTANT)
Before deploying, add your API keys:

1. Click "Advanced settings"
2. In "Secrets" section, paste:

```toml
# Groq API Key (FREE)
GROQ_API_KEY = "your_groq_api_key_here"

# OpenAI API Key (Optional)
OPENAI_API_KEY = "your_openai_api_key_here"

# Default Settings
DEFAULT_PROVIDER = "groq"
DEFAULT_TRANSCRIPTION_PROVIDER = "groq"
```

3. Replace `your_groq_api_key_here` with your actual Groq API key

#### 6. Deploy!
Click "Deploy!" button and wait 2-3 minutes

#### 7. Get Your Public URL
After deployment, you'll get a public URL like:
```
https://yourusername-lecture-voice-to-notes-app-abc123.streamlit.app
```

Share this URL with anyone! 🌐

---

## 🔒 Security Notes

✅ **Safe**: API keys stored in Streamlit Secrets (encrypted)
✅ **Safe**: .env file NOT pushed to GitHub (in .gitignore)
❌ **Never**: Commit API keys to GitHub

---

## 📝 App Settings

### Resource Limits (Free Tier)
- **RAM**: 1 GB
- **CPU**: 1 vCPU
- **Concurrent Users**: Unlimited
- **Uptime**: Always available
- **Cost**: FREE forever

### Recommendations
- Audio file size limit: Keep at 25MB for free tier
- For larger files, consider upgrading or compressing audio

---

## 🛠️ Troubleshooting

### App Not Starting?
1. Check logs in Streamlit dashboard
2. Verify requirements.txt is correct
3. Ensure secrets are properly configured

### FFmpeg Warning?
This is normal! The app works without FFmpeg on Streamlit Cloud.

### API Key Error?
Double-check:
1. Secrets are spelled correctly (GROQ_API_KEY)
2. No extra spaces or quotes
3. API key is valid and active

---

## 🔄 Updating Your Deployed App

Just push changes to GitHub:
```bash
git add .
git commit -m "Update app"
git push
```

Streamlit will automatically redeploy! ✨

---

## 📊 Monitor Your App

Visit: https://share.streamlit.io/

- View logs in real-time
- See usage analytics
- Manage settings
- Restart app if needed

---

## 🌟 Features Available After Deployment

✅ Share your app URL with anyone worldwide
✅ No installation required for users
✅ Professional public URL
✅ Automatic HTTPS security
✅ Built-in analytics
✅ Free custom domain possible

---

## 💡 Tips for Better Performance

1. **Optimize Audio Files**: Recommend users compress audio before upload
2. **Clear Cache**: Add st.cache decorators for frequently used functions
3. **Monitor Usage**: Check analytics to understand user patterns
4. **Update Dependencies**: Keep requirements.txt updated

---

## 🎯 Next Steps After Deployment

1. ✅ Test your deployed app thoroughly
2. ✅ Update README with live demo link
3. ✅ Share on social media
4. ✅ Add custom domain (optional)
5. ✅ Monitor usage and feedback

---

**Your app will be live at:**
`https://[yourusername]-lecture-voice-to-notes-app-[id].streamlit.app`

**Happy Deploying! 🚀**
