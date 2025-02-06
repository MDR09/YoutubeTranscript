from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

app = Flask(__name__)

@app.route('/get_transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
    
    if not video_id:
        return jsonify({"error": "video_id is required"}), 400

    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Format it to text
        formatter = TextFormatter()
        formatted_transcript = formatter.format_transcript(transcript)
        
        return jsonify({"transcript": formatted_transcript})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
