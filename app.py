from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Function to get the transcript of the video by its ID
def get_transcript(video_id):
    try:
        # Get the transcript for the video
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Format the transcript as JSON
        formatter = JSONFormatter()
        formatted_transcript = formatter.format_transcript(transcript)
        
        return formatted_transcript
    except Exception as e:
        return str(e)

@app.route('/get_transcript', methods=['GET'])
def fetch_transcript():
    # Get video ID from the query parameter
    video_id = request.args.get('video_id')
    
    if video_id:
        # Fetch and return the transcript
        transcript = get_transcript(video_id)
        return jsonify({"transcript": transcript}), 200
    else:
        return jsonify({"error": "No video ID provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
