from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
<<<<<<< HEAD
from youtube_transcript_api.formatters import TextFormatter
=======
>>>>>>> 61764d41cb7af3db81965332d2f6602f0e512576

app = Flask(__name__)

@app.route('/get_transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
<<<<<<< HEAD
    
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
    app.run(debug=True)
=======
    if not video_id:
        return jsonify({'error': 'Missing video_id parameter'}), 400
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return jsonify({'transcript': transcript})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 61764d41cb7af3db81965332d2f6602f0e512576
