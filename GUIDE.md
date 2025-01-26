# AI Recruitment Platform Guide

## Introduction
This guide provides instructions for setting up, testing, and deploying the AI Recruitment Platform.

## Prerequisites
- Python 3.x
- Node.js and npm
- OpenAI API key
- Firebase or Supabase account (for backend hosting)
- Vercel or Netlify account (for frontend hosting)

## Setup

### Backend
1. Clone the repository:
   ```bash
   git clone https://github.com/nitish0shr/AI-Recruitment-Platform.git
   ```

2. Navigate to the `backend` directory:
   ```bash
   cd AI-Recruitment-Platform/backend
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the `backend` directory.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

5. Run the Flask application:
   ```bash
   python app.py
   ```

### Frontend
1. Navigate to the `frontend` directory:
   ```bash
   cd ../frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

## Testing
- Access the frontend at `http://localhost:3000`.
- Upload job descriptions and resumes to test the platform's functionality.
- View the results on the dashboard.

## Deployment

### Backend
1. Deploy to Firebase or Supabase:
   - Follow the hosting provider's instructions to deploy the `backend` directory.

### Frontend
1. Deploy to Vercel or Netlify:
   - Follow the hosting provider's instructions to deploy the `frontend` directory.

## Conclusion
The AI Recruitment Platform is now ready for use. You can customize and extend the platform as needed.
